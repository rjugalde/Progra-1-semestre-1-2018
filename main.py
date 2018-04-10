L=[]
import sys


f = open("profesores.txt",'r')
f2 = open("REPORTE.TXT",'w')

for line in f:
    strings = line.split(';')
    L.append(strings)

##QUITAR ULTIMO CARACTER x[:len(x)-1]
    
for strings in L:
    
    cod_prof=strings[0]
    cod_carrera=strings[1]
    category = "Servicio" if strings[2]=="1" else "Carrera"
    nombre = strings[3]
    reporte = ("Codigo de profesor: "+cod_prof+"\n"+
              "Codigo de carrera: "+cod_carrera+"\n"+
              "Categoria: "+category+"\n"+
              "Nombre: "+nombre+"\n")
              
    
    f2.write(reporte)

print(reporte)

f.close()
f2.close()
