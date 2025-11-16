"""
init_db.py

Creates three MongoDB logical databases (branch_espoo, branch_london, branch_toronto).
Each DB will have 5 collections: students, agents, applications, documents, communications.
Each collection gets 10 documents: 5 replicated (same _id in every DB) and 5 fragmented (unique per DB).

If a local MongoDB server is available at mongodb://localhost:27017/ the script will use it;
otherwise it falls back to mongomock for an offline demo.

It also saves a JSON snapshot 'edu_snapshot.json' under the current working directory
so you can restore to this initial state with 'restore_db.py'.
"""
import datetime, json, os
from pymongo import MongoClient

# connecting to MongoDB; fall back to mongomock if not
USE_MOCK = False
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=200)
    client.server_info()  # raises if cannot connect
    print("Connected to MongoDB at mongodb://localhost:27017/")
except Exception as e:
    print("Cannot connect to local MongoDB (or none present). Using mongomock for demo.")
    USE_MOCK = True

if USE_MOCK:
    import mongomock
    client = mongomock.MongoClient()

db_names = ["branch_espoo", "branch_london", "branch_toronto"]
collections = ["students", "agents", "applications", "documents", "communications"]

def make_docs(coll_name, branch_code, n_repl=5, n_frag=5):
    docs = []
    # replicated docs (same _id across all DBs)
    for i in range(1, n_repl+1):
        _id = f"R-{coll_name}-{i:02d}"
        docs.append({
            "_id": _id,
            "type": "replicated",
            "coll": coll_name,
            "title": f"{coll_name}_common_{i}",
            "created_at": datetime.datetime.utcnow().isoformat()
        })
    # fragmented docs (local to branch)
    for i in range(1, n_frag+1):
        _id = f"F-{branch_code}-{i:02d}"
        docs.append({
            "_id": _id,
            "type": "fragmented",
            "coll": coll_name,
            "title": f"{branch_code}_unique_{i}",
            "created_at": datetime.datetime.utcnow().isoformat()
        })
    return docs

snapshot = {}

for dbname in db_names:
    db = client[dbname]
    snapshot[dbname] = {}
    branch_code = dbname.split("_")[-1]
    for coll in collections:
        # clear collection if exists
        db[coll].delete_many({})
        docs = make_docs(coll, branch_code)
        db[coll].insert_many(docs)
        # store snapshot for restore
        snapshot[dbname][coll] = docs

# Save snapshot
snapshot_file = os.path.join(os.getcwd(), "edu_snapshot.json")
with open(snapshot_file, "w") as f:
    json.dump(snapshot, f, indent=2)

print("Initialization complete.")
print("Databases created:", ", ".join(db_names))
print("Snapshot saved to:", snapshot_file)
