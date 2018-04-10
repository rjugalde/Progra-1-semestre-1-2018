LCarreras=[]
LCursos=[]
LGrupos=[]
LEstuCurso=[]
LEstudiantes=[]
LProfesores=[]

import sys

#Abrir archivos
OpenCarreras = open("carreras.txt",'r')
OpenCursos = open("cursos.txt",'r')
OpenGrupos = open("grupos.txt",'r')
OpenEstuCurso = open("estudiante-curso.txt",'r')
Openestudiantes = open("estudiantes.txt",'r')
OpenProfesores = open("profesores.txt",'r')

Reportes = open("REPORTE.TXT",'w')

def loadcarreras():
  for line in OpenCarreras:
      strings = line.split(';')
      LCarreras.append(strings)
      #print(strings)
  #print(LCarreras)
def loadcursos():
  for line in OpenCursos:
      strings = line.split(';')
      LCursos.append(strings)
      #print(strings)
  #print(LCursos)
def loadgrupos():
  for line in OpenGrupos:
      strings = line.split(';')
      LGrupos.append(strings)
      #print(strings)
  #print(LGrupos)
def loadestucurso():
  for line in OpenEstuCurso:
      strings = line.split(';')
      LEstuCurso.append(strings)
      #print(strings)
  #print(LEstuCurso)
def loadestudiantes():
  for line in Openestudiantes:
      strings = line.split(';')
      LEstudiantes.append(strings)
      #print(strings)
  #print(LEstudiantes)
def loadprofesores():
  for line in OpenProfesores:
      strings = line.split(';')
      LProfesores.append(strings)
      #print(strings)
  #print(LProfesores)


  ##QUITAR ULTIMO CARACTER x[:len(x)-1] ]
########## loops de reportes   #################
def reportCarreras():
  for strings in LCarreras:
      cod_carrera=strings[0]
      nombre=strings[1]
      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
                "Nombre: "+nombre+"\n") 
      Reportes.write("Carreras") 
      Reportes.write(reporte)
def reportCursos():
  for strings in LCursos:    
      cod_carrera=strings[0]
      cod_curso=strings[1]
      nombre = strings[2]
      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
                "Codigo de curso: "+cod_curso+"\n"+
                "Nombre: "+nombre+"\n")
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportGrupos():
  for strings in LGrupos:   
      cod_carrera=strings[0]
      cod_curso=strings[1]
      cod_grupo=strings[2]
      cod_prof=strings[3]
      cupototal = strings[4]
      cupomatriculado=strings[5]
      cupocongelado= strings[6]
      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
                "Codigo de curso: "+cod_curso+"\n"+
                "Codigo de grupo: "+cod_grupo+"\n"+
                "Codigo de profesor: "+cod_prof+"\n"+
                "Cupo Total: "+cupototal+"\n"+
                "Cupo Matriculado: "+cupomatriculado+"\n"+
                "Cupo Congelado: "+cupocongelado+"\n")
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportEstuCurso():
  for strings in LEstuCurso:    
      ident_estu=strings[0]
      cod_curso=strings[1]
      cod_grupo = strings[2]
      category = ""
      if strings[3]=="1" :
        category= "Matriculado"
      if strings[3]=="2" :
        category= "Desmatriculado"
      if strings[3]=="3" :
        category= "Congelado"
      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
                "Codigo de curso: "+cod_curso+"\n"+
                "Codigo de grupo: "+cod_grupo+"\n"+
                "Estado: "+category+"\n")
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportEstudiantes():
  for strings in LEstudiantes:    
      ident_estu=strings[0]
      cod_carrera=strings[1]
      nombre = strings[2]
      direccion=[3]
      telefono=[4]
      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
                "Codigo de carrera: "+cod_carrera+"\n"+
                "Nombre: "+nombre+"\n"+
                "Direccion: "+direccion+"\n"+
                "telefono: "+telefono+"\n")
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportProfesores():
  for strings in LProfesores:
      
      cod_prof=strings[0]
      cod_carrera=strings[1]
      category = "Servicio" if strings[2]=="1" else "Carrera"
      nombre = strings[3]
      reporte = ("Codigo de profesor: "+cod_prof+"\n"+
                "Codigo de carrera: "+cod_carrera+"\n"+
                "Categoria: "+category+"\n"+
                "Nombre: "+nombre+"\n")
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
  # print(LProfesores)
###################### BOOTS  ############################     
loadcarreras()
loadcursos()
loadestucurso()
loadestudiantes()
loadprofesores()

reportCarreras()
reportCursos()
reportGrupos()
reportProfesores()
############ MAIIIN   ##########################################
def main():
  while True:
      
      print("Que desea hacer:")
      print("1) Matricular") 
      print("2) Desmatricular")
      print("3) Congelar")
      print("4) Reportes")
      print("S) Salir del sistema")
      
      respuesta=input(": ")
      print("")
      if respuesta == "1":
        loopMatricular()

      if respuesta == "2":
        loopDesmatricular()

      if respuesta == "3":
        loopCongelar()

      if respuesta == "4":
        loopReportes()
      if respuesta == "s" or respuesta == "S":
        break
def loopMatricular():

def loopDesmatricular():

def loopCongelar():

def loopREportes():

OpenCarreras.close()
OpenCursos.close()
OpenGrupos.close()
OpenEstuCurso.close()
Openestudiantes.close()
OpenProfesores.close()

Reportes.close()
