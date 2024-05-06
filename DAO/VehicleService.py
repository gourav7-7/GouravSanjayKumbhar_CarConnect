from DAO.IVheicleService import IVehicleService
from Entity.Vehicle import Vehicle
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil

conn_str = DBProprtyUtil.getConnectionString('CarConnect')
conn = DBconnutil.getConnection(conn_str)
stmt = conn.cursor()

class VehicleService(IVehicleService):
    def GetVehicleById(self, vehicleId):
       self.vehicleid = vehicleId
       stmt.execute(f"select * from Vehicle where VehicleID = {self.vehicleid}")
       row = stmt.fetchall()
       print(row)
       stmt.close()
    
    def GetAvailableVehicles():
        stmt.execute(f"select * from vehicle where Availability = 1")
        row = stmt.fetchall()
        print(row)
        stmt.close()

    def AddVehicle(self,vehicleData):
        self.vehicleData = vehicleData
        stmt.execute(f"insert into vehicle values({self.vehicleData.getVehicleID()},'{self.vehicleData.getModel()}','{self.vehicleData.getMake()}',{self.vehicleData.getYear()},'{self.vehicleData.getColor()}','{self.vehicleData.getRegistrationNumber()}',{self.vehicleData.getAvailability()},{self.vehicleData.getDailyRate()})") 
        conn.commit()
        print("Vehicle Added Successfully")
        stmt.close()

    def UpdateVehicle(self, vehicleData):
        self.vehicleData = vehicleData
        stmt.execute(f"UPDATE vehicle SET Model='{self.vehicleData.getModel()}', Make='{self.vehicleData.getMake()}', Year={self.vehicleData.getYear()}, Color='{self.vehicleData.getColor()}', RegistrationNumber='{self.vehicleData.getRegistrationNumber()}', Availability={self.vehicleData.getAvailability()}, DailyRate={self.vehicleData.getDailyRate()} WHERE VehicleID={self.vehicleData.getVehicleID()}")
        conn.commit()
        print("Vehicle Updated Successfully")
        stmt.close()

    def RemoveVehicle(self,vehicleID):
        self.vehicleid = vehicleID
        stmt.execute(f"delete from vehicle where VehicleID = {self.vehicleid}")
        conn.commit()
        print("Vehicle removed")
        stmt.close()