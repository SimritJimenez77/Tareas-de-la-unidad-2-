import tkinter as tk
from tkinter import messagebox
import mysql.connector


def conectar_db():
    conexion = mysql.connector.connect(user = 'root', password = '123456789', host = 'localhost' , database = 'base_prueba' , port = '3306')
    sql = ("""CREATE TABLE IF NOT EXISTS Alumnos 
                (id int primary key AUTO_INCREMENT , 
                nombre VARCHAR (20) , edad int(3), 
                telefono VARCHAR(30), carrera VARCHAR(50))""")
    
    conexion.execute(sql)
    conexion.close()


def guardar_alumno():
    conexion = mysql.connector.connect(user = 'root', password = '123456789', host = 'localhost' , database = 'escuela' , port = '3306')
    if name.get() == "" or age.get() == "" or telefono.get() == "" or carrera.get() == "":
        messagebox.showerror("Error en los datos", "Debe completar los datos del alumno")
        return
    int_age = int(age.get())
    print(int_age)
    print(name.get())
    conexion.execute("INSERT INTO alumnos(nombre, edad, telefono, carrera) VALUES(?,?,?,?)", (name.get(), int_age))
    conexion.commit()
    conexion.close()
    ventana_nuevo.destroy()
    actualiza_listado()


def get_alumnos():
    conexion = mysql.connect("escuela.db")
    cursor = conexion.cursor()
    registros_raw = cursor.execute("SELECT * FROM alumnos")
    registros_fetch = registros_raw.fetchall()
    print(registros_fetch)
    global registros
    registros = registros_fetch
    cursor.close()


def actualiza_listado():
    registros_lb.delete(0, tk.END)
    get_alumnos()
    for registro in registros:
        registros_lb.insert(tk.END, registro)



def nuevo_alumno(event=None):
    ventana_nuevo_alumno = tk.Toplevel(ventana)
    ventana_nuevo_alumno.title("Agregar Alumno")
    # Crear la etiqueta y el campo de entrada para el nombre
    name_label = tk.Label(ventana_nuevo_alumno, text="Nombre:")
    name_label.grid(row=0, column=0, padx=(10, 0))

    name_entry = tk.Entry(ventana_nuevo_alumno)
    name_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

    # Crear la etiqueta y el campo de entrada para la edad
    age_label = tk.Label(ventana_nuevo_alumno, text="Edad:")
    age_label.grid(row=1, column=0, padx=(10,0))

    age_entry = tk.Entry(ventana_nuevo_alumno)
    age_entry.grid(row=1, column=1, padx=(0, 10))
    
    # Crear la etiqueta y el campo de entrada para el telefono
    telefono_label = tk.Label(ventana_nuevo_alumno, text="Telefono:")
    telefono_label.grid(row=1, column=0, padx=(10,0))

    telefono_entry = tk.Entry(ventana_nuevo_alumno)
    telefono_entry.grid(row=1, column=1, padx=(0, 10))

    # Crear la etiqueta y el campo de entrada para la carrera
    carrera_label = tk.Label(ventana_nuevo_alumno, text="Carrera:")
    carrera_label.grid(row=1, column=0, padx=(10,0))

    carrera_entry = tk.Entry(ventana_nuevo_alumno)
    carrera_entry.grid(row=1, column=1, padx=(0, 10))

    #
    global name
    name = name_entry
    #
    global age
    age = age_entry
    #
    global telefono
    telefono = telefono_entry
    #
    global carrera
    carrera = carrera_entry
    #
    global ventana_nuevo
    ventana_nuevo = ventana_nuevo_alumno

    # Crear el botón para enviar los datos
    submit_button = tk.Button(ventana_nuevo_alumno, text="Guardar", command=guardar_alumno)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)


conectar_db()
get_alumnos()
ventana = tk.Tk()
ventana.title("Control de Alumnos")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
# Crear el primer menú.
menu_alumnos = tk.Menu(barra_menus, tearoff=False)
# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_alumnos, label="Alumnos")
menu_alumnos.add_command(label="Agregar Alumno", accelerator="Ctrl+N", command=nuevo_alumno)
ventana.config(menu=barra_menus)
registros_lb = tk.Listbox(ventana)
for registro in registros:
    registros_lb.insert(tk.END, registro)

registros_lb.pack(pady=20, padx=20)
ventana.bind_all("<Control-n>", nuevo_alumno)
ventana.mainloop()
