import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '123456789', host = 'localhost' , database = 'base_prueba' , port = '3306')

cursor = conexion.cursor()

sql = """CREATE TABLE IF NOT EXISTS Alumnos 
                (id int primary key AUTO_INCREMENT , 
                nombre VARCHAR (20) , edad int(3), 
                telefono VARCHAR(30), carrera VARCHAR(50))"""

cursor.execute(sql)
conexion.commit()                

conexion.close()

conexion = mysql.connector.connect(user = 'root', password = '123456789', host = 'localhost' , database = 'base_prueba' , port = '3306')

conexion.execute("INSERT INTO Alumnos(nombre, edad, telefono, carrera) VALUES(?,?,?,?)" , ("Simrit" , 20, 9971132716, "Ing. Sistemas Computacionales"))
conexion.execute("INSERT INTO Alumnos(nombre, edad, telefono, carrera) VALUES(?,?,?,?)" , ("Noe" , 20, 9971388970, "Ing. Sistemas Computacionales"))
conexion.execute("INSERT INTO Alumnos(nombre, edad, telefono, carrera) VALUES(?,?,?,?)" , ("Jesus" , 21, 9971407557, "Ing. Sistemas Computacionales"))
conexion.execute("INSERT INTO Alumnos(nombre, edad, telefono, carrera) VALUES(?,?,?,?)" , ("Berenice" , 19, 9971140200, "Ing. Sistemas Computacionales"))

conexion.commit()

Alumnos = conexion.execute("SELECT * FROM Alumnos WHERE nombre = 'Simrit'")
fila = Alumnos.fetchone()
print(fila)
conexion.close()


