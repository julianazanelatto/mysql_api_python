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
            '[POST] Creation of a instance in the current table':'http://127.0.0.1:8000/create/{table_name}',
            '[PUT] Updating the Customers contact in table by id':'http://127.0.0.1:8000/update/customers/{id}',
            '[PUT] Removing (delete) a instance by some condition':'http://127.0.0.1:8000/delete/{table_name}'
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

@router.post('/create/{table_name}')
async def creating_table_instance(attr: dict, table_name: str):
    # attr será enviado via payload
    status = db.create_line(attr, table_name)
    if status is True:
        return 'Inserted successfully'

    return HTTPException(status_code=404, detail=f'Error during the insertion. Message: {status}')

@router.put('/update/customers/{id}')
async def update_customers_contact_by_id(id, data: dict):
    # o dict será enviado via payload
    status = db.update_customers_contact_by_id(id, data)
    if status is True:
        return 'Updated successfully'

    return HTTPException(status_code=404, detail=f'Error during the update. Message:{status}')

@router.put('/delete/{table_name}')
async def deleting_instance(table_name: str, data: dict):
    # dict com os valores condition: str, value recebidos via post

    status = db.delete_instance( table_name, data['condition'], [data['value']])
    if status is True:
        return 'Instance removed successfully'

    return HTTPException(status_code=404, detail=f'Error in removal. Message:{status}')
