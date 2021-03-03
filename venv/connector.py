import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
mycursor=mydb.cursor()
mycursor.execute("create database crud_project")
mycursor.execute("use crud_project")
mycursor.execute("CREATE TABLE employee_details ( id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(45) NOT NULL, last_name VARCHAR(45) NOT NULL, designation VARCHAR(45) NULL, total_experiance INT(11) NULL, created_on DATETIME NULL DEFAULT CURRENT_TIMESTAMP, email VARCHAR(200) NOT NULL, active TINYINT(1) NULL DEFAULT '1', PRIMARY KEY (id));")