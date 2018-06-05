import sqlite3
import time
from flask_restful import Resource, reqparse



class Computer(Resource):
    backup_status_parser = reqparse.RequestParser()
    backup_status_parser.add_argument('backup_status',
        required=True,
        help="This field cannot be left blank!" 
    )
    backup_time_parser = reqparse.RequestParser()
    backup_time_parser.add_argument('backup_time',
        required=True,
        help="This field cannot be left blank!" 
    )

    computer_number_parser = reqparse.RequestParser()
    computer_number_parser.add_argument('computer_number',
        required=True,
        help="This field cannot be left blank!" 
    )

   


  #backup_status,backup_time,input_name,computer_number


    def get(self, input_name): 
        computer = self.find_by_name(input_name)
        if computer:
            return computer    
        return {'message': 'Computer not found'}, 404


    @classmethod
    def find_by_name(cls, input_name):
        connection = sqlite3.connect('../db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * FROM computermonitor_computerbackup WHERE input_name=?"
        result = cursor.execute(query, (input_name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'computer': {'id': row[0],'backup_status': row[2],'backup_time': row[3],'computer_number': row[5],'input_name': row[6]}}
       
    
    
    def post(self, name):
        backup_status = Computer.backup_status_parser.parse_args()
        backup_time = Computer.backup_time_parser.parse_args()
        computer_number = Computer.computer_number_parser.parse_args() 
        computer = {'input_name': name, 'backup_status': backup_status['backup_status'],'backup_time': backup_time['backup_time'],'computer_number': computer_number['computer_number']} 
        try:
          self.insert(computer)
        except: 
           return {"message": "An error occurred inserting the item."}, 500 
        return computer, 201
    

    @classmethod
    def insert(cls, computer):
        connection = sqlite3.connect('../db.sqlite3')
        cursor = connection.cursor()
        query = "INSERT INTO computermonitor_computerbackup (input_name,backup_status,backup_time,computer_number_id) VALUES (?,?,?,?)"
        cursor.execute(query, (computer['input_name'], computer['backup_status'],computer['backup_time'],computer['computer_number'])) 
        connection.commit()  
        connection.close()



    def delete(self, input_name):
        connection = sqlite3.connect('../db.sqlite3')
        cursor = connection.cursor()
        query = "DELETE FROM computermonitor_computerbackup WHERE id=?"
        cursor.execute(query,(input_name,)) 
        connection.commit()  
        connection.close()
        return {'message': 'Computer deleted'}



class ComputerList(Resource):
  def get(self): 
      connection = sqlite3.connect('../db.sqlite3')
      cursor = connection.cursor()
      query = "SELECT * FROM computermonitor_computerbackup"
      result = cursor.execute(query) 
      computers = []
      for row in result:
          computers.append({'id': row[0], 'backup_status': row[1],'backup_time': row[2],'input_name': row[3],'computer_number_id': row[4]})
      connection.close()
      return {'computers': computers}



