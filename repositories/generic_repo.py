import pyodbc as sql

class GenericRepo():
    def __init__(self):
        self.conn=sql.connect("DRIVER=SQL Server;SERVER=LENOVO-FERIDUN\SQLEXPRESS01;DATABASE=Shop")
        self.cursor=self.conn.cursor()    