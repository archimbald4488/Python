This project implements a simplified distributed database system using three MongoDB databases:

branch_espoo

branch_london

branch_toronto

Each database contains five collections (students, agents, applications, documents, communications) with ten documents each.
Half of these documents are replicated (same _id across all databases) while the other half are fragmented (unique per branch).

A simple python app allows the user to:

-Select which database to connect to

-Print collection contents

-Update individual documents

#### Installation:
1. Create a virtual environment
python -m venv venv
source venv/bin/activate      Linux & macOS
venv\Scripts\activate         Windows

2. Install dependencies
pip install -r requirements.txt

3. Initialize databases by running init_db.py

Run the app with app.py and restore the database with restore_db.py
