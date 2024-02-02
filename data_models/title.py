from data_models.user import User
class Title():
    def __init__(self,id:int,titleName:str,user:User):
        self.id=id
        self.titleName=titleName
        self.user=user
        
        
print("title")