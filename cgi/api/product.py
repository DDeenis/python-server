#!D:/Python3/python.exe
import api_controller
import json
import sys

sys.path.append('../../')
import dao

class ProductController(api_controller.ApiController):
    def do_get(self):
        try:
            res = dao.Products.get_all()
        except:
            self.send_response(
                500, 
                "Internal server error", 
                meta={'service': 'product', 'count': 0, 'status': 500}, 
                data={'message': 'Server error, see logs for details'}
            )

        res = list(map(self.transform_product, res))

        self.send_response(200, 'OK', meta={'service': 'product', 'count': len(res), 'status': 200}, data=res)

    def do_post(self):
        auth_token = self.get_bearer_token_or_exit()
        request_body = sys.stdin.read().encode(sys.stdin.encoding).decode("utf-8")
        
        try:
            body_data = json.loads(request_body)
        except:
            self.send_response(
                400, 
                "Bad request", 
                meta={'service': 'product', 'count': 0, 'status': 400}, 
                data={'message': 'Body must be valid json'}
            )

        if not ('name' in body_data and 'price' in body_data):
            self.send_response(
                400, 
                "Bad request", 
                meta={'service': 'product', 'count': 0, 'status': 400}, 
                data={'message': "Must include parameters: 'name', 'price'"}
            )

        try:
            dao.Products.create(body_data)
        except:
            self.send_response(
                500, 
                "Internal server error", 
                meta={'service': 'product', 'count': 0, 'status': 500}, 
                data={'message': 'Server error, see logs for details'}
            )

        self.send_response(201, 'Created', meta={'service': 'product', 'count': 1, 'status': 201}, data={'message': 'Created'})
    
    def transform_product(self, product: dict):
        product['id'] = str(product['id'])
        return product
    

ProductController().serve()