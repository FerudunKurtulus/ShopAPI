from typing import List
from data_models.product import Product

class Product_Type():
    def __init__(self,id:int,typeName:str,products:List[Product]):
        self.id=id
        self.typeName=typeName
        self.products=products