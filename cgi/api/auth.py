#!D:/Python3/python.exe
import api_controller
import hashlib
import mysql.connector
import sys

sys.path.append('../../')
import dao

class AuthController(api_controller.ApiController):
    def do_get(self):
        login, password = self.get_basic_credentials_or_exit()

        try:
            user_data = dao.Auth.get_user(login, password)

            if user_data == None:
                self.send_response(
                    401, 
                    "Unauthorized", 
                    meta={'service': 'auth', 'count': 0, 'status': 401},
                    data={'message': 'Credentials rejected'})

            self.send_response(200, 'OK', meta={'service': 'auth', 'count': 1, 'status': 200}, data={'auth': 'success', 'token': str(user_data['id'])})
        except mysql.connector.Error as err:
            self.send_response(
                503, 
                "Service Unavailable", 
                meta={'service': 'auth', 'count': 0, 'status': 503}, 
                data={'message': 'Server error, see logs for details'}
            )

    def do_post(self):
        auth_token = self.get_bearer_token_or_exit()
        self.send_response(200, 'OK', meta={'service': 'auth', 'count': 1, 'status': 200}, data=auth_token)

AuthController().serve()