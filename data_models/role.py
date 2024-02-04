from data_models.user import User
from typing import List
class Role():
    def __init__(self,id:int,roleName:str,users:List[User]):
        self.id=id
        self.roleName=roleName
        self.users=users
        