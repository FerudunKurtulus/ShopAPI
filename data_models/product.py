from data_models.product_type import Product_Type
class Product():
    def __init__(self,id:int,productName:str,productId:int,stock:int,price:int,imageUrl:str,productType:Product_Type):
        self.id=id
        self.productName=productName
        self.productId=productId
        self.stock=stock
        self.price=price
        self.imageUrl=imageUrl
        self.productType=productType