from app import app, db
from sqlalchemy import MetaData, Table

def view_tables():
    with app.app_context():
        meta = MetaData()
        meta.reflect(bind=db.engine)
        for table in meta.tables.values():
            print(f"Table: {table.name}")
            print(f"Columns: {[col.name for col in table.columns]}")
            for row in db.session.query(table).all():
                row_dict = {column.name: getattr(row, column.name) for column in table.columns}
                print(row_dict)
        print("\n")

if __name__ == "__main__":
    view_tables()
