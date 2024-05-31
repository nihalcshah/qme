from app import db, User, app
from werkzeug.security import generate_password_hash
import sys
from sqlalchemy import text

def add_user(username, password): # python dbedit.py add_user alice secret_password
    with app.app_context():
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print(f"User {username} added successfully.")

def create_table(table_name, columns): # python dbedit.py create_table new_table name:TEXT age:INTEGER
    with app.app_context():
        query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, "
        query += ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        query += ");"
        with db.engine.connect() as connection:
            connection.execute(text(query))
        print(f"Table {table_name} created successfully.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python dbedit.py add_user <username> <password>")
        print("       python dbedit.py create_table <table_name> <column1:type> <column2:type> ...")
    elif sys.argv[1] == "add_user" and len(sys.argv) == 4:
        add_user(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "create_table" and len(sys.argv) > 3:
        table_name = sys.argv[2]
        columns = {}
        for col in sys.argv[3:]:
            col_name, col_type = col.split(":")
            columns[col_name] = col_type
        create_table(table_name, columns)
    else:
        print("Invalid command or number of arguments.")

