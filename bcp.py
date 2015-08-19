#!/usr/bin/python
import proveedores, time
import Empleados, sys,os

def leer():
	efl="\n"
	
	msj="""		Programa de creacion de archivos para 
				importar data en el BCP"""
	msj2= "Precione:"+efl+"1.- Para crear archivo de proveedores"+efl
	msj2+="2.- Para crear archivo de Empleados"+efl
	msj2+="3.- Para salir del programa"
	while True:
		os.system('clear')
		print "*"*(len(msj)+2)
		print "*"+msj+'*'
		print "*"*(len(msj)+2)
		print efl
		print msj2

		
		c=sys.stdin.read(1)		
		if c=='1':		
					proveedores.leer_proveedores()

					for i in xrange(5):
						print i
						time.sleep(0.5)
						
		elif c=='2':	Empleados.leer_empleados()
		elif c=='3':
			print "Saliendo del programa..."+efl
			time.sleep(1)
			break

		c=sys.stdin.read(1)		

leer()	
