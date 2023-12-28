import logging
import sys
import mysql.connector
import hashlib

sys.path.append('../')
import db_ini

def get_db_or_exit():
    return mysql.connector.connect(**db_ini.connection_params)
    # except mysql.connector.Error as err:
    #     self.send_response(503, "Service Unavailable", err)

class Products():
    def get_all(self = None):
        db = get_db_or_exit()
        sql = "select * from py201_products"
        res = []
        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                for row in cursor:
                    res.append(dict(zip(cursor.column_names, row)))
        except mysql.connector.Error as err:
            logging.error('Failed to get products', {'query': sql, 'err': str(err)})
            raise RuntimeError()
        else:
            return res
        
    def create(body_data: object):
        sql = "insert into py201_products (`name`, `price`, `image_url`) values (%(name)s, %(price)s, %(image)s)"
        db = get_db_or_exit()
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, body_data)
                db.commit()
        except mysql.connector.Error as err:
            logging.error('Failed to create product', {'query': sql, 'err': str(err)})
            raise RuntimeError()

class Auth():
    def get_user_id(self, token: str):
        db = get_db_or_exit()
        sql = "select count(id) from py201_users where id=%s";
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, (token,))
                count = cursor.fetchone()[0]
                return token if count == 1 else None
        except mysql.connector.Error as err:
            logging.error('Failed to get user id', {'query': sql, 'err': str(err)})
            raise RuntimeError()
        except Exception as err:
            logging.error('Unknown error', {'err': str(err)})
            raise RuntimeError()

    def get_user(login: str, password: str):
        db = get_db_or_exit()
        sql = "select * from py201_users u where u.`login`=%s and u.`password`=%s"
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, (
                    login, 
                    hashlib.md5(password.encode()).hexdigest()
                ))

                row = cursor.fetchone()
                if row == None:
                    logging.warning('No response was returned from database call', {'query': sql})
                    return None

                user_data = dict(zip(cursor.column_names, row))
                return user_data
        except mysql.connector.Error as err:
            logging.error('Failed to get user', {'query': sql, 'err': str(err)})
            raise RuntimeError()
        
class Cart():
    def get_cart_item(self, user_id: int, product_id: int):
        db = get_db_or_exit()
        sql = "select * from py201_cart where `userId`=%s and `productId`=%s";
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, (user_id, product_id))
                row = cursor.fetchone()
                if row == None:
                    logging.warning('No response was returned from database call', {'query': sql})
                    return None

                item_data = dict(zip(cursor.column_names, row))
                return item_data
        except mysql.connector.Error as err:
            logging.error('Failed to get cart item', {'query': sql, 'err': str(err)})
            raise RuntimeError()


    def add_to_cart(self, user_id: int, product_id: int, count: int = 1):
        existing_item = Cart().get_cart_item(user_id, product_id)
        is_insert = existing_item == None
        sql_insert = "insert into py201_cart (`userId`, `productId`, `count`) values (%s, %s, %s)"
        sql_update = "update py201_cart set `count` = `count` + %s where `userId`=%s and `productId`=%s"

        db = get_db_or_exit()
        sql = sql_insert if is_insert else sql_update

        try:
            with db.cursor() as cursor:
                cursor.execute(sql, (user_id, product_id, count) if is_insert else (count, user_id, product_id))
                db.commit()
                return True
        except mysql.connector.Error as err:
            logging.error('Failed to get cart item', {'query': sql, 'err': str(err)})
            raise RuntimeError()