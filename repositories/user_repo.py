from data_models.user import User
from repositories.generic_repo import GenericRepo
class UserRepo(GenericRepo):
    
    def __init__(self):
        super().__init__()
           
    def addData(self,user:User):
       query="insert into Shop_User values ({0},{1},{2},{3},{4})".format(user.userName,user.userPass,user.fullName,user.userAddress,user.roleId)
       self.cursor.execute(query)
       self.conn.commit()
   
    def updateData(self,user:User):
        query="update Shop_User set userName={0},userPass={1},fullName={2},userAddress={3},roleId={4} where id={5}".format(user.userName,
                                                        user.userPass,user.fullName,user.userAddress,user.roleId,user.id)
        self.cursor.execute(query)
        self.conn.commit()
    
    def deleteData(self,id:int):
        query="delete from Shop_User where id={0}".format(id)
        self.cursor.execute(query)
        self.conn.commit()
        
    def getData(self,id:int):
        query="select * from Shop_User where id={0}".format(id)
        self.cursor.execute(query)
        data=self.cursor.fetchone()
        return data
    
    def getAllData(self):
        query="select * from Shop_User"
        self.cursor.execute(query)
        data=self.cursor.fetchall()
        return data