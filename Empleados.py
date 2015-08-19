import csv, time



def completa(aux,x,longitud,tipo):
	
	if len(aux)>longitud : aux=aux[:longitud]
	
	if tipo==1:
		while (len(aux)<longitud): aux=x + aux
	else:
		while (len(aux)<longitud): aux= aux +x
	return aux

def cabecera(x,dato, fila):

	if x ==1 :	return str(10)
	elif x==2:	return completa(str(fila),'0',6,1)
	elif x==3:	return completa(dato,'',3,1)
	elif x==4:	return completa(str(dato),' ',12,2)#DNI
	elif x==5:	return completa(str(dato),' ',3,2)
	elif x==6:	return completa(str(dato),' ',25,2) #paterno
	elif x==7:	return completa(str(dato),' ',25,2) #materno
	elif x==8:	return completa(str(dato),' ',25,2) #nombre
	elif x==9:	return completa(str(dato),' ',60,2) #correo
	elif x==10:	return completa(" ",' ',92,2)+'\n' #filler

	#cuentas
	elif x==11:	return completa("20",' ',2,2)
	elif x==12:	return completa(str(fila),'0',6,1)
	elif x==13:	return completa(str(dato),'',1,2)
	elif x==14:	return completa(str(dato),' ',20,2)
	elif x==15:	return completa("RUC"," ",3,2)
	elif x==16:	return completa("20507795642",' ',12,2)
	elif x==17:	return completa('',' ',2,2)
	elif x==18:	return completa("  ",' ',207,2)+'\n'
 

def leer_empleados():
	print "Creando archivo de empleados..."
	print "Utilizando archivofuente: ppersonal.csv"
	print "archivo de salida empleados.txt"
	time.sleep(1)

	archivo1=open("personal.csv","r")
	destino=open("empleados.txt","w")
	proveedores_csv=csv.DictReader(archivo1)
	
	EOL='\n'
	filas=1
	linea=""

	for row in proveedores_csv:	
		x=1
		campo=1
		if (filas %2)!=0:
			while campo<19:
				linea=cabecera(campo,row[str(x)],filas)

				if campo==12:	x=8
				elif campo >2:	
					if campo > 14: x=1
					else:x+=1
				
				destino.write(linea)										
				campo+=1
		else:
			campo=11
			x=8
			while campo<19:
				linea=cabecera(campo,row[str(x)],filas-1)

				if campo==12:	x=8
				elif campo >2:	
					if campo > 14: x=1
					else:x+=1
				
				destino.write(linea)										
				campo+=1
				
			#break
		filas+=1
		#break
	#filler
	destino.write("99")	
	
	destino.write(completa(str(filas+1),'0',6,1))#numero
	
	destino.write(completa(str(filas/2),'0',6,1))#proveedores
	destino.write(completa(str(filas),'0',6,1))#cuentas
	destino.write(completa(" ",' ',233,1))#filler
		#break
		#destino.write(EOL)			

	archivo1.close() 
	destino.close()
	print "Archivo de empleados completado..."