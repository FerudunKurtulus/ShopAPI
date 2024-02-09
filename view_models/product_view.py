class ProductView():
    def __init__(self,id:int,productName:str,typeName:str,stock:int,price:int,imageUrl:str):
        self.id=id
        self.productName=productName
        self.typeName=typeName
        self.stock=stock
        self.price=price
        self.imageUrl=imageUrl