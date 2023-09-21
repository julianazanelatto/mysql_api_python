import pprint

from Database import MySQLDatabase

if __name__ == '__main__':
    print('Running')

    try:
        db = MySQLDatabase()
        print(f"Starting the connection...\nStatus: {db.conn.is_connected()}")
    except ConnectionError as err:
        raise f"Error during the connection. Message: {err}"

    tables = db.get_database_tables()

    print("\n-> Sample of the database table")
    db.get_lines_from_table('customers', limit=True, number_of_lines=1)
    description = db.desc_table('customers')
    pprint.pprint(description)

    new_instance = {"customerNumber": 105,
                    "customerName": "Atelier",
                    "contactLastName": "Schmitt",
                    "contactFirstName": "Carine",
                    "phone": "40322555",
                    "addressLine1": "54 rue Royale",
                    "city": "Nantes",
                    "postalCode": "44000",
                    "country": "France",
                    "salesRepEmployeeNumber": 1370,
                    "creditLimit": 21000.00}

    #if db.create_line(new_instance, 'customers'):
    #    print("Inserção bem sucedida")


    db.delete_instance('customers', 'customerNumber', [105])