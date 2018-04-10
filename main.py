#Ricardo Ugalde 2016165753
LCarreras=[]
LCursos=[]
LGrupos=[]
LEstuCurso=[]
LEstudiantes=[]
LProfesores=[]

import sys

#Abrir archivos
OpenCarreras = open("Archivos/carreras.txt",'r')
OpenCursos = open("Archivos/cursos.txt",'r')
OpenGrupos = open("Archivos/grupos.txt",'r')
OpenEstuCurso = open("Archivos/estudiante-curso.txt",'r')
Openestudiantes = open("Archivos/estudiantes.txt",'r')
OpenProfesores = open("Archivos/profesores.txt",'r')

#Reportes = open("REPORTE.TXT",'a')

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
def reportCarreras(Reportes):
  Reportes.write("codCarrera,Nombre\n")
  for strings in LCarreras:
      cod_carrera=strings[0]
      nombre=strings[1]
##      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
##                "Nombre: "+nombre+"\n")
      reporte=cod_carrera+","+nombre
##      Reportes.write("Carreras") 
      Reportes.write(reporte)
def reportCursos(Reportes):
  Reportes.write("CodCarrera,CodCurso,Nombre\n")
  for strings in LCursos:    
      cod_carrera=strings[0]
      cod_curso=strings[1]
      nombre = strings[2]
##      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Nombre: "+nombre+"\n")
      reporte=cod_carrera+","+cod_curso+","+nombre
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
#cursos dentro de una carrera:
def reportCursosporCarrera(Reportes,carrid):
  Reportes.write("CodCarrera,CodCurso,Nombre\n")
  for strings in LCursos:    
      cod_carrera=strings[0]
      cod_curso=strings[1]
      nombre = strings[2]
      if cod_carrera==carrid:
##      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Nombre: "+nombre+"\n")
        reporte=cod_carrera+","+cod_curso+","+nombre
      #Reportes.write("Profesores")  
        Reportes.write(reporte)
def reportGrupos(Reportes):
 Reportes.write("CodCarrera,CodCurso,CodGrupo,CodProfesor, CupoTotal, CupoMatriculado, CuposCongelados\n")
 for strings in LGrupos:   
     cod_carrera=strings[0]
     cod_curso=strings[1]
     cod_grupo=strings[2]
     cod_prof=strings[3]
     cupototal = strings[4]
     cupomatriculado=strings[5]
     cupocongelado= strings[6]
##      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Codigo de grupo: "+cod_grupo+"\n"+
##                "Codigo de profesor: "+cod_prof+"\n"+
##                "Cupo Total: "+cupototal+"\n"+
##                "Cupo Matriculado: "+cupomatriculado+"\n"+
##                "Cupo Congelado: "+cupocongelado+"\n")
     reporte= cod_carrera+","+cod_curso+","+cod_grupo+","+cod_prof+","+cupototal+","+cupomatriculado+","+cupocongelado
     #Reportes.write("Profesores")  
     Reportes.write(reporte)
def reportGruposProfs(Reportes,codcurs):
 Reportes.write("CodCarrera,CodCurso,CodGrupo,CodProfesor, CupoTotal, CupoMatriculado, CuposCongelados\n")
 for strings in LGrupos:   
     cod_carrera=strings[0]
     cod_curso=strings[1]
     cod_grupo=strings[2]
     cod_prof=strings[3]
     cupototal = strings[4]
     cupomatriculado=strings[5]
     cupocongelado= strings[6]
     if codcurs== cod_curso:
##      reporte = ("Codigo de carrera: "+cod_carrera+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Codigo de grupo: "+cod_grupo+"\n"+
##                "Codigo de profesor: "+cod_prof+"\n"+
##                "Cupo Total: "+cupototal+"\n"+
##                "Cupo Matriculado: "+cupomatriculado+"\n"+
##                "Cupo Congelado: "+cupocongelado+"\n")
        reporte= cod_carrera+","+cod_curso+","+cod_grupo+","+cod_prof+","+cupototal+","+cupomatriculado+","+cupocongelado
     #Reportes.write("Profesores")  
        Reportes.write(reporte)
def reportEstuCurso(Reportes):
  Reportes.write("Ident-Estudiante,CodCurso,CodGrupo,Estado\n")
  for strings in LEstuCurso:    
      ident_estu=strings[0]
      cod_curso=strings[1]
      cod_grupo = strings[2]
      category = ""
      if strings[3]=="1\n" :
        category= "Matriculado"
      if strings[3]=="2\n" :
        category= "Desmatriculado"
      if strings[3]=="3\n" :
        category= "Congelado"
##      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Codigo de grupo: "+cod_grupo+"\n"+
##                "Estado: "+category+"\n")
      reporte=ident_estu+","+cod_curso+","+cod_grupo+","+category
      #Reportes.write("Profesores")
      #print(type(strings[3]))
      Reportes.write(reporte)
def reportEstudeGrupo(Reportes,curs,grup):
  Reportes.write("Ident-Estudiante,CodCurso,CodGrupo,Estado\n")
  for strings in LEstuCurso:    
      ident_estu=strings[0]
      cod_curso=strings[1]
      cod_grupo = strings[2]
      category = ""
      if strings[3]=="1\n" :
        category= "Matriculado"
      if strings[3]=="2\n" :
        category= "Desmatriculado"
      if strings[3]=="3\n" :
        category= "Congelado"
      if cod_curso==curs:
        if cod_grupo==grup:
          reporte=ident_estu+","+cod_curso+","+cod_grupo+","+category
          Reportes.write(reporte)
##      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
##                "Codigo de curso: "+cod_curso+"\n"+
##                "Codigo de grupo: "+cod_grupo+"\n"+
##                "Estado: "+category+"\n")
          
      #Reportes.write("Profesores")
      #print(type(strings[3]))
          
def reportEstudiantes(Reportes):
  Reportes.write("Ident-Estudiante,CodCarrera,Nombre,Direccion,Telefono\n")
  for strings in LEstudiantes:    
      ident_estu=strings[0]
      cod_carrera=strings[1]
      nombre = strings[2]
      direccion=strings[3]
      telefono=strings[4]
##      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
##                "Codigo de carrera: "+cod_carrera+"\n"+
##                "Nombre: "+nombre+"\n"+
##                "Direccion: "+direccion+"\n"+
##                "telefono: "+telefono+"\n")
      reporte= ident_estu+","+cod_carrera+","+nombre+","+direccion+","+telefono
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportEstudiantesdeCarrerra(Reportes,codcar):
  Reportes.write("Ident-Estudiante,CodCarrera,Nombre,Direccion,Telefono\n")
  for strings in LEstudiantes:    
      ident_estu=strings[0]
      cod_carrera=strings[1]
      nombre = strings[2]
      direccion=strings[3]
      telefono=strings[4]
      if codcar== cod_carrera:
##      reporte = ("Identificacion de estudiante: "+ident_estu+"\n"+
##                "Codigo de carrera: "+cod_carrera+"\n"+
##                "Nombre: "+nombre+"\n"+
##                "Direccion: "+direccion+"\n"+
##                "telefono: "+telefono+"\n")
        reporte= ident_estu+","+cod_carrera+","+nombre+","+direccion+","+telefono
      #Reportes.write("Profesores")  
        Reportes.write(reporte)
def reportProfesores(Reportes):
  Reportes.write("CodProfesor, CodCarrera,Categoría,Nombre\n")
  for strings in LProfesores:
      
      cod_prof=strings[0]
      cod_carrera=strings[1]
      category = "Servicio" if strings[2]=="1" else "Carrera"
      nombre = strings[3]
##      reporte = ("Codigo de profesor: "+cod_prof+"\n"+
##                "Codigo de carrera: "+cod_carrera+"\n"+
##                "Categoria: "+category+"\n"+
##                "Nombre: "+nombre+"\n")
      reporte= cod_prof+","+cod_carrera+","+category+","+nombre
      #Reportes.write("Profesores")  
      Reportes.write(reporte)
def reportProfesoresServ(Reportes):
  Reportes.write("CodProfesor, CodCarrera,Categoría,Nombre\n")
  for strings in LProfesores:      
      cod_prof=strings[0]
      cod_carrera=strings[1]
      category = "Servicio" if strings[2]=="1" else "Carrera"
      if category== "Servicio":       
        nombre = strings[3]
##        reporte = ("Codigo de profesor: "+cod_prof+"\n"+
##                  "Codigo de carrera: "+cod_carrera+"\n"+
##                  "Categoria: "+category+"\n"+
##                  "Nombre: "+nombre+"\n")
        reporte= cod_prof+","+cod_carrera+","+category+","+nombre
        #Reportes.write("Profesores")  
        Reportes.write(reporte)
def reportProfesoresCarrera(Reportes,carrid):
  Reportes.write("CodProfesor, CodCarrera,Categoría,Nombre\n")
  for strings in LProfesores:
      
      cod_prof=strings[0]
      cod_carrera=strings[1]
      category = "Servicio" if strings[2]=="1" else "Carrera"
      if cod_carrera== carrid:
        nombre = strings[3]
##        reporte = ("Codigo de profesor: "+cod_prof+"\n"+
##                  "Codigo de carrera: "+cod_carrera+"\n"+
##                  "Categoria: "+category+"\n"+
##                  "Nombre: "+nombre+"\n")
        reporte= cod_prof+","+cod_carrera+","+category+","+nombre
        #Reportes.write("Profesores")  
        Reportes.write(reporte)
  # print(LProfesores)
###################### BOOTS  ############################     
loadcarreras()
loadcursos()
loadgrupos()
loadestucurso()
loadestudiantes()
loadprofesores()

##reportCarreras()
##reportCursos()
##reportGrupos()
##reportEstuCurso()
##reportEstudiantes()
##reportProfesores()
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
##def loopMatricular():
##
##def loopDesmatricular():
##
##def loopCongelar():

def loopReportes():
  while True:
      print("Que reporte desea hacer:")
      print("1) Carreras")
      print("2) Cursos de una carrera")
      print("3) Profesores")    
      print("4) Profesores de un curso")
      print("5) Estudiantes de un grupo")
      print("6) Estudiantes de una carrera")
      print("7) Profesores de Servicio")
      print("8) Profesores de una carrera")
      print("9) Cantidad de personas atendidas por mostrador")
      print("S) Salir")
      respuesta=input(": ")
      filename=input("Digite el nombre del archivo: ")
      filename="Reports/"+filename
      
      if respuesta == "1":
        Reportes = open(filename+".csv",'a')
        reportCarreras(Reportes)
        Reportes.close()
        print("Las carreras han sigo agregadas al archivo "+filename)
        print("")
      if respuesta == "2":
        codcar=input("Digite el codigo de la carrera: ")
        Reportes = open(filename+".csv",'a')
        reportCursosporCarrera(Reportes,codcar)
        Reportes.close()
        print("Los cursos de esa carrera han sigo agregados al archivo "+filename)
        print("")
        
      if respuesta == "3":
        Reportes = open(filename+".csv",'a')
        reportProfesores(Reportes)
        Reportes.close()
        print("Los profesores han sido agregados al archivo "+filename)
        print("")
      if respuesta == "4":
        codcur=input("Digite el codigo del curso: ")
        Reportes = open(filename+".csv",'a')
        reportGruposProfs(Reportes,codcur)
        Reportes.close()
        print("Los profesores de ese curso han sido agregados al archivo "+filename)
        print("")


      if respuesta == "5":
        curs=input("Difite el curso: ")
        grup=input("Digite el grupo: ")
        Reportes = open(filename+".csv",'a')
        reportEstudeGrupo(Reportes,curs,grup)
        Reportes.close()
        print("Los estudiantes de ese curso y grupo han sido agregados al archivo "+filename)
        print("")

      if respuesta == "6":
        codcar=input("Digite la carrera: ")
        Reportes = open(filename+".csv",'a')
        reportEstudiantesdeCarrerra(Reportes,codcar)
        Reportes.close()
        print("Los estudiantes de esa carrera han sido agregados al archivo "+filename)
        print("")


      if respuesta == "7":
        Reportes = open(filename+".csv",'a')
        reportProfesoresServ(Reportes)
        Reportes.close()
        print("Los profesores de Servicio han sido agregados al archivo "+filename)
        print("")
        
      if respuesta == "8":
        codcarr=input("Digite el codigo de la carrera: ")
        Reportes = open(filename+".csv",'a')
        reportProfesoresCarrera(Reportes,codcarr)
        Reportes.close()
        print("Las carreras han sigo agregadas al archivo "+filename)
        print("")

##      if respuesta == "9":
##        Reportes = open(filename+".csv",'a')
##        reportGrupos(Reportes)
##        Reportes.close()
##        print("Las carreras han sigo agregadas al archivo "+filename)
##        print("")  


      if respuesta == "s" or respuesta == "S":
          break





main()



OpenCarreras.close()
OpenCursos.close()
OpenGrupos.close()
OpenEstuCurso.close()
Openestudiantes.close()
OpenProfesores.close()

Reportes.close()
