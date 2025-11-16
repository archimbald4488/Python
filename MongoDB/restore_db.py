"""
restore_db.py

Reads edu_snapshot.json and restores data to branch DBs.
This will wipe existing collections and re-insert the snapshot data.
"""
import json, os
from pymongo import MongoClient

# Connect or fallback to mongomock (same logic as init)
USE_MOCK = False
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=200)
    client.server_info()
    print("Connected to local MongoDB")
except Exception:
    print("Using mongomock (no real MongoDB detected).")
    import mongomock
    client = mongomock.MongoClient()

snapshot_file = os.path.join(os.getcwd(), "edu_snapshot.json")
if not os.path.exists(snapshot_file):
    print("Snapshot file not found:", snapshot_file)
    raise SystemExit(1)

with open(snapshot_file, "r") as f:
    snapshot = json.load(f)

for dbname, colmap in snapshot.items():
    db = client[dbname]
    for coll, docs in colmap.items():
        db[coll].delete_many({})
        # convert created_at back to datetime if needed, but leave as string is okay
        db[coll].insert_many(docs)

print("Restore complete from", snapshot_file)
