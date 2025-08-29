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

ventana_principal.mainloop()