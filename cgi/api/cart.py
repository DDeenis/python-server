#!D:/Python3/python.exe
import api_controller
import json
import sys
import os

sys.path.append('../../')
import dao

class CartController(api_controller.ApiController):
    def do_post(self):
        user_id = dao.Auth().get_user_id(self.get_bearer_token_or_exit())
        request_body = sys.stdin.read().encode(sys.stdin.encoding).decode("utf-8")

        if not dao.Auth().get_user_id(user_id):
            self.send_response(
                401, 
                "Unauthorized", 
                meta={'service': 'cart', 'count': 0, 'status': 401},
                data={'message': 'Token is invalid'}
            )

        try:
            body_data = json.loads(request_body)
        except:
            self.send_response(
                400, 
                "Bad request", 
                meta={'service': 'cart', 'count': 0, 'status': 400}, 
                data={'message': 'Body must be valid json'}
            )

        if not ('productId' in body_data and 'count' in body_data):
            self.send_response(
                400, 
                "Bad request", 
                meta={'service': 'cart', 'count': 0, 'status': 400}, 
                data={'message': "Must include parameters: 'productId', 'count'"}
            )
        
        if not dao.Cart().add_to_cart(user_id, body_data['productId'], body_data['count']):
            self.send_response(
                500, 
                "Internal server error", 
                meta={'service': 'cart', 'count': 0, 'status': 500}, 
                data={'message': 'Server error, see logs for details'}
            )

        self.send_response(201, 'Created', meta={'service': 'cart', 'count': 1, 'status': 200}, data={'status': 'created'})
    

CartController().serve()