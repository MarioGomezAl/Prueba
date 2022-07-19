from tkinter import*

root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, pady=2.5, padx=10)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, pady=2.5, padx=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2, column=1, padx=10, pady=2.5)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=3, column=1, pady=2.5, padx=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=3, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLable=Label(miFrame, text="Nombre:")
nombreLable.grid(row=0, column=0, sticky="e", padx=10, pady=2.5)

apellidoLable=Label(miFrame, text="Apellido:")
apellidoLable.grid(row=1, column=0, sticky="e", padx=10, pady=2.5)

passwordLable=Label(miFrame, text="Password:")
passwordLable.grid(row=2, column=0, sticky="e", padx=10, pady=2.5)

comentariosLable=Label(miFrame, text="Comentarios:")
comentariosLable.grid(row=3, column=0, sticky="e", pady=2.5, padx=10)

def codigoBoton():
    
    minombre.set("Juan")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()