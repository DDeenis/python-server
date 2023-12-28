from starter import MainHandler
import sys
import json

sys.path.append('../Python')
import dao

class ShopController():
    def __init__(self, handler: MainHandler):
        self.handler = handler

    def index(self):
        products = dao.Products().get_all()
        self.view_data = {
            '@initial_products': json.dumps(products).replace('"', "'")
        }
        self.handler.send_view()
    
    def cart(self):
        self.handler.send_view()