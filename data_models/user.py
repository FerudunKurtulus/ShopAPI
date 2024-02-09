
class User():   
    def __init__(self,id:int,userName:str,userPass:str,fullName:str,userAddress:str,roleId:int):
        self.id=id
        self.userName=userName.encode('utf-8').decode('unicode-escape') if isinstance(userName, str) else userName
        self.userPass=userPass
        self.fullName=fullName.encode('utf-8').decode('unicode-escape') if isinstance(fullName, str) else fullName
        self.userAddress=userAddress.encode('utf-8').decode('unicode-escape') if isinstance(userAddress, str) else userAddress
        self.roleId=roleId
    def __str__(self):
        return f"User({self.id}, {self.userName}, {self.userPass}, {self.fullName}, {self.userAddress}, {self.roleId})"

