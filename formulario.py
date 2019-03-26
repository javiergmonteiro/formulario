#!/usr/bin/python

from Tkinter import *
import sqlite3

def main():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	 
	window = Tk()
	 
	window.title("Formulario")
	 
	window.geometry('350x200')
	 
	lblnombre = Label(window, text="Nombre")
	lblprofesion = Label(window, text="Profesion")
	lbledad = Label(window, text="Edad")
	 
	lblnombre.grid(column=0, row=0)
	lblprofesion.grid(column=0, row=1)
	lbledad.grid(column=0, row=2)
	 
	txt = Entry(window,width=30)
	txt1 = Entry(window,width=30)
	txt2 = Entry(window,width=30)
	 
	txt.grid(column=1, row=0)
	txt1.grid(column=1, row=1)
	txt2.grid(column=1, row=2)
	
	def popupmsg(msg):
		popup = Tk()
		popup.wm_title("!")
		label = Label(popup, text=msg)
		label.pack(side="top", fill="x", pady=10)
		B1 = Button(popup, text="Okay", command = popup.destroy)
		B1.pack()
		popup.mainloop()
	
	def almacenados(lista):
		count = 1
		ventana = Tk ()
		ventana.title("Datos Almacenados")
		ventana.geometry('350x500')
		for i in lista:
			
			lbltabla = Label(ventana, text="Entrada " + str(count) + ":")
			lbltabla.pack(side="top", fill="x", pady=5)
			lblnombre = Label(ventana, text="Nombre: " + i[0])
			lblnombre.pack(side="top", fill="x", pady=5)
			lblprofesion = Label(ventana, text="Profesion: " + i[1])
			lblprofesion.pack(side="top", fill="x", pady=5)
			lbledad = Label(ventana, text="Edad: " + str(i[2]))
			lbledad.pack(side="top", fill="x", pady=2)
			
			count = count +1
		
		B2 = Button(ventana, text="Okay", command = ventana.destroy)
		B2.pack()
		ventana.mainloop()
		
	def clicked():
		list = [str(txt.get()),str(txt1.get()),int(txt2.get())]
		c.execute('insert into data(Nombre,Profesion,edad) values (?,?,?)', list)
		conn.commit()
		popupmsg("Datos Guardados")
		
		
	def ver():
		cur = conn.cursor()
		cur.execute("SELECT * FROM data")
		
		resultado = cur.fetchall()
		
		almacenados(resultado)
		
	
    
	btn1 = Button(window, text="Guardar", command=clicked)
	btn2= Button(window, text="Ver datos", command=ver)

	btn1.grid(column=0, row=4)
	btn2.grid(column=1, row=4)
	
	 
	window.mainloop()

if __name__ == '__main__':
	main()

