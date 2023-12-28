import mysql.connector
import hashlib

db_init = {
    'host': 'aws.connect.psdb.cloud',
    'database': 'maindb',
    'user': '9smxynsgmtbkhjqzzjgs',
    'password': 'pscale_pw_cS7ptw8jdGVQI6fy2VkI7Efhtt7E5sllRw1u0fWZQPQ',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}
db_connection = None

def add_product(name: str, price: float, img_url: str | None = None):
    sql = f"insert into py201_products (`name`, `price`, `image_url`) values ('{name}', {price}, '{img_url}')"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            db_connection.commit()
        print("Insert product OK")
    except mysql.connector.Error as err:
        print(err)

def add_user(login: str, password: str, avatar: str | None = None):
    password = hashlib.md5(password.encode()).hexdigest()
    sql = f"insert into py201_users (`login`, `password`, `avatar`) values ('{login}', '{password}', '{avatar}')"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            db_connection.commit()
        print("Insert user OK")
    except mysql.connector.Error as err:
        print(err)

def add_cart_item(userId: str, productId: str):
    sql = f"insert into py201_cart (`userId`, `productId`) values ('{userId}', '{productId}')"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            db_connection.commit()
        print("Insert cart item OK")
    except mysql.connector.Error as err:
        print(err)

def create_users():
    sql = '''create table if not exists py201_users (
        `id` bigint unsigned primary key default (uuid_short()),
        `password` varchar(32) not null,
        `login` varchar(32) not null,
        `avatar` varchar(256) null
    ) engine = InnoDB, default charset = utf8mb4 collate utf8mb4_unicode_ci'''

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
        print("Create users OK")
    except mysql.connector.Error as err:
        print(err)

def create_products():
    sql = '''create table if not exists py201_products (
        `id` bigint unsigned primary key default (uuid_short()),
        `name` varchar(64) not null,
        `price` float not null,
        `image_url` varchar(256) null
    ) engine = InnoDB, default charset = utf8mb4 collate utf8mb4_unicode_ci'''

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
        print("Create products OK")
    except mysql.connector.Error as err:
        print(err)

def create_cart():
    sql = '''create table if not exists py201_cart (
        `id` bigint unsigned primary key default (uuid_short()),
        `userId` bigint not null,
        `productId` bigint not null
    ) engine = InnoDB, default charset = utf8mb4 collate utf8mb4_unicode_ci'''

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
        print("Create cart OK")
    except mysql.connector.Error as err:
        print(err)

def main():
    global db_connection
    try:
        db_connection = mysql.connector.connect(**db_init)
        print("OK")
    except mysql.connector.Error as err:
        print(err)
        return
    
    sql = "show databases"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    print(cursor.column_names)
    for row in cursor:
        print(row)

    # product = {
    #     'name': 'Коробка',
    #     "price": 30,
    #     "img_url": 'box1.png'
    # }
    # add_product(**product)

    # create_users()
        
    # user = {
    #     'login': 'user',
    #     'password': 'password',
    #     'avatar': 'user.png'
    # }
    # add_user(**user)
        
    create_cart()
    add_cart_item('3127039489931739138', '3127039489931739137')

if __name__ == "__main__": 
    main()