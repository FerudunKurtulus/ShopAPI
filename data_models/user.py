from data_models.title import Title
from typing import List
class User():   
    def __init__(self,id:int,userName:str,password:str,fullName:str,address:str,titleId:int,titles:List[Title]):
        self.id=id
        self.userName=userName
        self.password=password
        self.fullName=fullName
        self.address=address
        self.titleId=titleId
        self.titles=titles

