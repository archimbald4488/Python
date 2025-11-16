"""
app.py - simple CLI for interacting with the demo DBs.

Features:
- List available databases
- Select a database to use
- List collections
- Print documents from a collection (with optional limit)
- Update a document by _id (set field=value)

"""
import argparse, json, sys, os
from pymongo import MongoClient

# Connect or fallback
USE_MOCK = False
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=200)
    client.server_info()
except Exception:
    import mongomock
    client = mongomock.MongoClient()

def list_dbs():
    all_dbs = client.list_database_names()
    return [d for d in all_dbs if d.startswith("branch_")]

def list_collections(dbname):
    db = client[dbname]
    return db.list_collection_names()

def print_collection(dbname, coll, limit=10):
    db = client[dbname]
    col = db[coll]
    docs = list(col.find().limit(limit))
    for d in docs:
        print(json.dumps(d, default=str, indent=2))

def update_doc(dbname, coll, doc_id, updates: dict):
    db = client[dbname]
    res = db[coll].update_one({"_id": doc_id}, {"$set": updates})
    return res.matched_count, res.modified_count

def main():
    print("EduBridge DB CLI\n")
    while True:
        print("Using mock:", USE_MOCK)
        print("\nCommands:")
        print("  1) list-dbs")
        print("  2) use-db <dbname>")
        print("  3) list-colls")
        print("  4) print-coll <collection> [limit]")
        print("  5) update <collection> <_id> <field>=<value>")
        print("  6) exit")
        cmd = input("\nEnter command: ").strip()
        if cmd == "list-dbs" or cmd == "1":
            print("Databases:", list_dbs())
        elif cmd.startswith("use-db") or cmd.startswith("2"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Usage: use-db <dbname>")
                continue
            dbname = parts[1]
            if dbname not in list_dbs():
                print("DB not found. Available:", list_dbs())
                continue
            print("Using database:", dbname)
            # start subloop for db
            while True:
                sub = input(f"[{dbname}]> ").strip()
                if sub in ("back", "exit", "quit"):
                    break
                if sub in ("list-colls", "3"):
                    print("Collections:", list_collections(dbname))
                    continue
                if sub.startswith("print-coll") or sub.startswith("4"):
                    sp = sub.split()
                    if len(sp) < 2:
                        print("Usage: print-coll <collection> [limit]")
                        continue
                    coll = sp[1]
                    limit = int(sp[2]) if len(sp) > 2 else 10
                    print_collection(dbname, coll, limit)
                    continue
                if sub.startswith("update") or sub.startswith("5"):
                    sp = sub.split()
                    if len(sp) < 4:
                        print("Usage: update <collection> <_id> <field>=<value>")
                        continue
                    _, coll, docid, fv = sp[0], sp[1], sp[2], sp[3]
                    if "=" not in fv:
                        print("Field must be field=value")
                        continue
                    field, value = fv.split("=", 1)
                    # naive type handling: try int
                    if value.isdigit():
                        value = int(value)
                    matched, modified = update_doc(dbname, coll, docid, {field: value})
                    print("Matched:", matched, "Modified:", modified)
                    continue
                if sub in ("help", "?"):
                    print("Commands: list-colls, print-coll <collection> [limit], update <collection> <_id> <field>=<value>, back")
                    continue
                print("Unknown command. Type 'back' to return to main menu.")
        elif cmd in ("exit", "6", "quit"):
            print("Bye.")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
