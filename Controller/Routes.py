from Database import MySQLDatabase
from fastapi import APIRouter, HTTPException


db = MySQLDatabase()
router = APIRouter()

# rotas para chamadas dos métodos

@router.get('/')
async def read_root():
    return {
        'Message': 'Welcome to the MySQL API',
        'Endpoints':{
            '[GET] Database info': 'http://127.0.0.1:8000/db_info',
            '[GET] Database tables':'http://127.0.0.1:8000/db_tables',
            '[GET] Reading some instances of a table': 'http://127.0.0.1:8000/reading/{tables}',
            '[GET] Reading table instances defining the limit': 'http://127.0.0.1:8000/reading/{table}/{instances}',
            '[POST] Creation of a instance in the current table':'http://127.0.0.1:8000/{table}',
            '[PUT] Updating the Customers table by id':'http://127.0.0.1:8000/update/{table}/{id}',
            '[PUT] Removing (delete) a instance by some condition':'http://127.0.0.1:8000/delete/{table}'
        }
    }

@router.get('/db_info')
async def get_bd_info():
    return {
        'Database info': {
            'Database': db.get_database_name(),
            'Number of tables': len(db.get_database_tables())
            }
        }

@router.get('/db_tables')
async def get_db_tables():
    return db.get_database_tables()

@router.get('/reading/{table}')
async def read_db_table(table: str):
    return db.read_table(table)

@router.get('/reading/{table}/{instances}')
async def read_db_table(table: str, instances):
    return db.get_lines_from_table(table, limit=True, number_of_lines=instances)

@router.post('/{table}')
async def creating_table_instance(attr: dict, table_name: str):
    # attr será enviado via payload
    status = db.create_line(attr, table_name)
    if status:
        return 'Inserted successfully'

    return HTTPException(status_code=404, detail='Error during the insertion')

@router.put('/update/{table}/{id}')
async def update_customers_contact_by_id(id, data: dict):
    # o dict será enviado via payload
    if db.update_users_by_id(id, data):
        return 'Updated successfully'

    return HTTPException(status_code=404, detail='Error during the update')

@router.put('/delete/{table}')
async def deleting_instance(table_name: str, data: dict):
    # dict com os valores condition: str, value recebidos via post
    if db.delete_instance( table_name, data['condition'], data['value']):
        return 'Instance removed successfully'

    return HTTPException(status_code=404, detail='Error in removal')
