from data_models.role import Role
class User():   
    def __init__(self,id:int,userName:str,userPass:str,fullName:str,userAddress:str,roleId:int,role:Role):
        self.id=id
        self.userName=userName
        self.userPass=userPass
        self.fullName=fullName
        self.userAddress=userAddress
        self.roleId=roleId
        self.role=role

