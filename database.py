import mysql.connector

def save_db(data):
        # from run_tracker import program_name, start_time, end_time, duration
        program_name, start_time, end_time, duration = data
        myBD = mysql.connector.connect(
                host="localhost",
                user="root",
                password="iarowosola9876#+",
                database="vstracker_db",
                auth_plugin='mysql_native_password'
        )


        myCursor = myBD.cursor()
        # print("connected")

        # create database 
        # myCursor.execute("CREATE DATABASE vstracker_db")

        # create table 
        # program_name,start_time,end_time,duration
        # myCursor.execute("CREATE TABLE USAGE_Table (id INT(4) PRIMARY KEY AUTO_INCREMENT, program_name VARCHAR(100), start_time VARCHAR(50), end_time VARCHAR(50), duration VARCHAR(50)) ")

        # insert data Values 
        values = "INSERT INTO USAGE_Table (program_name, start_time, end_time, duration) VALUES (%s, %s, %s, %s)"

        data_values = (program_name, start_time, end_time, duration)

        myCursor.executemany(values, data_values)

        myBD.commit()


