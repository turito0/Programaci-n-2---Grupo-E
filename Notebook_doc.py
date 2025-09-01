#importación de librerías
import tkinter as tk
from tkinter import ttk
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#Crear frames (uno por pestaña)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
frame_doctores=ttk.Notebook(ventana_principal)
#Agregar pestañas al Notebook
pestañas.add(frame_pacientes,text="Pacientes")
pestañas.add(frame_doctores,text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre:")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
entryNombre=tk.Entry(frame_pacientes)
entryNombre.grid(row=0,column=1,sticky="w",padx=5,pady=5)

#Fecha de Nacimiento
labelFecha=tk.Label(frame_pacientes,text="Fecha de Nacimiento:")
labelFecha.grid(row=1,column=0,sticky="w",padx=5,pady=5)
entryFecha=tk.Entry(frame_pacientes)
entryFecha.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad 
labelEdadP=tk.Label(frame_pacientes,text="Edad:")
labelEdadP.grid(row=2,column=0,sticky="w",padx=5,pady=5)
EdadEntryP=tk.Entry(frame_pacientes,state="readonly")
EdadEntryP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Genero
labelGenero=tk.Label(frame_pacientes,text="Genero")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)
 
#Grupo Sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguíneo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", padx=5, pady=5)
GrupoSanguineoEntry=tk.Entry(frame_pacientes)
GrupoSanguineoEntry.grid(row=4, column=1, sticky="w", pady=5, padx=5)
 
#Tipo de Seguro
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipoSeguro=tk.StringVar()
tipoSeguro.set("Público")
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)
 
#Centro Medico
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centroMedico)
comboCentroMedico.grid(row=6, column=1, sticky="w", pady=5, padx=5)

#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2, pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command="")
btn_registrar.grid(row=0,column=0,padx=5)

#Botón Eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=0,column=1,padx=5)

#Crear Treeview para mostrar pacientes
Treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")

#Definir encabezados
Treeview.heading("Nombre",text="Nombre Completo")
Treeview.heading("FechaN",text="Fecha Nacimiento")
Treeview.heading("Edad",text="Edad")
Treeview.heading("Genero",text="Género")
Treeview.heading("GrupoS",text="Grupo Sanguíneo")
Treeview.heading("TipoS",text="Tipo Seguro")
Treeview.heading("CentroM",text="Centro Médico")

#Definir anchos de columnas
Treeview.column("Nombre",width=120)
Treeview.column("FechaN",width=120)
Treeview.column("Edad",width=50,anchor="center")
Treeview.column("Genero",width=60,anchor="center")
Treeview.column("GrupoS",width=100,anchor="center")
Treeview.column("TipoS",width=100,anchor="center")
Treeview.column("CentroM",width=120)

#Ubicar el TreeView en la cuadricula
Treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=Treeview.yview)
Treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7,column=2,sticky="ns")

#Nombre DOC
label_nombreD = tk.Label(frame_doctores, text="Nombre:")
label_nombreD.grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_nombreD = tk.Entry(frame_doctores)
entry_nombreD.grid(row=0, column=1, sticky="w", pady=5, padx=5)
 
#Especialidad (Combobox) DOC
label_especialidad = tk.Label(frame_doctores, text="Especialidad:")
label_especialidad.grid(row=1, column=0, sticky="w", pady=5, padx=5)
especialidad_var = tk.StringVar()
especialidad_var.set("Neurología") 
combo_especialidad = ttk.Combobox(frame_doctores,textvariable=especialidad_var, values=["Neurología", "Cardiología", "Pediatría", "Traumatología"])
combo_especialidad.grid(row=1, column=1, sticky="w", pady=5, padx=5)
 
#Edad con Spinbox DOC
label_edadD = tk.Label(frame_doctores, text="Edad:")
label_edadD.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edad_varD = tk.StringVar()
spinbox_edadD = tk.Spinbox(frame_doctores, from_=18, to=100, textvariable=edad_varD, width=5)
spinbox_edadD.grid(row=2, column=1, sticky="w", pady=5, padx=5)
 
#Teléfono DOC
label_telefono = tk.Label(frame_doctores, text="Teléfono:")
label_telefono.grid(row=3, column=0, sticky="w", pady=5, padx=5)
entry_telefono = tk.Entry(frame_doctores)
entry_telefono.grid(row=3, column=1, sticky="w", pady=5, padx=5)
 
#Botones Registrar y Eliminar DOC
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")
 
btn_registrarD = tk.Button(btn_frameD, text="Registrar", bg="green", fg="white")
btn_registrarD.grid(row=0, column=0, padx=5)
 
btn_eliminarD = tk.Button(btn_frameD, text="Eliminar", bg="red", fg="white")
btn_eliminarD.grid(row=0, column=1, padx=5)
 
# Tabla Treeview para mostrar doctores DOC
treeviewD = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Telefono", text="Teléfono")
 
treeviewD.column("Nombre", width=150)
treeviewD.column("Especialidad", width=150)
treeviewD.column("Edad", width=50, anchor="center")
treeviewD.column("Telefono", width=100)
 
treeviewD.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
 
# Scrollbar vertical DOC
scroll_yD = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yD.set)
scroll_yD.grid(row=5, column=2, sticky="ns")


ventana_principal.mainloop()