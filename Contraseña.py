import tkinter as tk

def  iniciar_sesion ():
    usuario  =  nombre_usuario.get()
    contrasena  =  contrasena_usuario.get()
    if usuario == "Simrit" and contrasena == "12345" :
        resultado.config(text = "Inicio de sesión exitosa" )
    else:
        resultado.config(text = "Nombre de usuario o contraseña incorrectas" )

ventana = tk.Tk ()
ventana.title( "Iniciar sesión" )
ventana.configure(padx = 100)
ventana.config(bg = 'silver')

# Crear campos de entrada para el nombre de usuario y la contraseña

User = tk.Label(ventana, text = "Usuario: ")
User.pack(pady = 0)
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady = 5)

Password = tk.Label(ventana, text = "Contraseña: ")
Password.pack(padx = 1, pady = 5)
contrasena_usuario = tk.Entry(ventana, show= "*" )
contrasena_usuario.pack(padx = 0, pady = 0)

# Crear botones para iniciar sesión y salir
iniciar_sesion  =  tk.Button(ventana , text = "Iniciar sesión" , command = iniciar_sesion)
iniciar_sesion.pack( padx = 10 , pady = 10 )
salir = tk.Button(ventana , text = "Salir" , command= ventana.quit)
salir.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado  =  tk.Label( ventana , text = "" )
resultado.pack(pady = 10)

ventana.mainloop()
