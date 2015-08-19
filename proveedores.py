import csv, time



def completa(aux,x,longitud,tipo):
	
	if len(aux)>longitud : aux=aux[:longitud]
	
	if tipo==1:
		while (len(aux)<longitud): aux=x + aux
	else:
		while (len(aux)<longitud): aux= aux +x
	return aux

def cabecera(x,dato):

	if x ==1 :	return str(dato)
	elif x==2:	return completa(str(dato),'0',6,1)
	elif x==3:	return completa(dato,'',3,1)
	elif x==4:	
		aux=str(dato)
		
		if len(aux)>11: aux=aux[:11]		
		return completa(aux,' ',12,2)
	elif x==5:	return completa(str(dato),' ',3,2)
	elif x==6:	return completa(str(dato),' ',75,2) #razon social
	elif x==7:	return completa(str(dato),' ',75,2) #contacto
	elif x==8:	return completa(str(dato),'0',15,2) #numero
	elif x==9:	return completa(str(dato),' ',60,2) #correo
	elif x==10:	return completa(str(dato),'N',1,2) #cheque gerencia
	elif x==11:	return completa(str(dato),'N',1,2) #datos bancarios
	#cuentas
	elif x==12:	return completa(str(dato),'99',2,2)
	elif x==13:	return completa(str(dato),'',6,2)
	elif x==14:	return completa(str(dato),'',1,2)
	elif x==15:	return completa(str(dato),' ',20,2)
	elif x==16:	return completa(str(dato),' ',3,2)
	elif x==17:	return completa(str(dato),' ',12,2)
	elif x==18:	return completa(str(dato),' ',2,2)
	elif x==19:	return completa(str(dato),' ',207,2)
 

def leer_proveedores():

	print "Creando archivo de proveedores..."
	print "Utilizando archivofuente: proveedores.csv"
	print "archivo de salida proveedores.txt"
	time.sleep(1)

	archivo1=open("proveedores.csv","r")
	destino=open("proveedores.txt","w")
	#proveedores_csv=csv.reader(archivo1)
	proveedores_csv=csv.DictReader(archivo1)
	#proveedores_csv = csv.reader(archivo1, delimiter=',')

	
	EOL='\n'
	filas=0
	for row in proveedores_csv:	
		x=1
		#proveedor
		while x <12: 
			destino.write(cabecera(x,row[str(x)]))			
			x=x+1
		destino.write(EOL)			
		#cuentas
		while x <20: 
			if x==13:destino.write(cabecera(x-11,row[str(x-11)]))
			else: destino.write(cabecera(x,row[str(x)]))			
			x=x+1			
		filas=1+filas
		destino.write(EOL)			
		#break
	#filler
	destino.write("99")	
	ultimo=row[str(x-18)]
	destino.write(completa(str(int(ultimo)+1),'0',6,1))#numero
	
	destino.write(completa(str(filas),'0',6,1))#proveedores
	destino.write(completa(str(filas),'0',6,1))#cuentas
	destino.write(completa(" ",' ',233,1))#filler
		#break
		#destino.write(EOL)			

	archivo1.close() 
	destino.close()
	print "Archivo de proveedores completado..."