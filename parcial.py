import os

personas=[]
universidades=[]
ciudades=[]

def validar(id, lista, atributo):
    esta=False
    for val in lista:
        if(val[atributo]==id):
            esta=True
            break
    return esta




class Ciudad:
    
    def crearciudad():
        nombre=input("digite el nombre: ")
        pais=input("digite el pais: ")
        while(True):
            codigo=input("digite el codigo postal: ")
            if(validar(codigo,ciudades,"codigo")==False):
                break
            else:
                print("el codigo postal ya existe")
        
        
        diccionario_ciudad={"nombre": nombre,"pais":pais,"codigo":codigo}
        ciudades.append(diccionario_ciudad)
        print(diccionario_ciudad)

    def eliminarciudad():
        
        id=input("digite el codigo postal de la ciudad a eliminar: ")
        
        for codigo in ciudades:
            if(codigo["codigo"]==id):
                print(codigo)
                confirmar=input("seguro desea eliminar?  1)Si  2)No : " )
                if(confirmar=="1"):
                    ciudades.remove(codigo)
                    print("ciudad eliminada correctamente")
                
         

class Universidad:
    
    def crearuniversidad():
        nombre=input("digite el nombre: ")
        ciudad=input("digite la ciudad: ")
        while(True):
            codigo=input("digite el codigo: ")
            if(validar(codigo,universidades,"codigo")==False):
                break
            else:
                print("el codigo ya existe")
        
        diccionario_uni={"nombre": nombre,"ciudad":ciudad,"codigo":codigo}
        universidades.append(diccionario_uni)
        print(diccionario_uni)

    def eliminaruniversidad():
        
        id=input("digite el codigo de la universidad a eliminar: ")
        
        for codigo in universidades:
            if(codigo["codigo"]==id):
                print(codigo)
                confirmar=input("seguro desea eliminar?  1)Si  2)No : " )
                if(confirmar=="1"):
                    universidades.remove(codigo)
                    print("universidad eliminada correctamente")
                
          


class Persona:
    
    def crearpersona():
        nombre=input("digite el nombre: ")
        apellido=input("digite el apellido: ")
        while(True):
            cedula=input("digite la cedula: ")
            if(validar(cedula,personas,"id")==False):
                break
            else:
                print("la cedula ya existe")
        
        diccionario_persona={"nombre": nombre,"apellido":apellido,"id":cedula}
        personas.append(diccionario_persona)
        print(diccionario_persona)

    def eliminarpersona():
        
        id=input("digite cedula de persona a eliminar: ")
        
        for cedula in personas:
            if(cedula["id"]==id):
                print(cedula)
                confirmar=input("seguro desea eliminar?  1)Si  2)No : " )
                if(confirmar=="1"):
                    personas.remove(cedula)
                    print("persona eliminada correctamente")
                
                    
        
        
opcion=0      
while(opcion!=4):
    os.system('cls')
    os.system('clear')
    print("Menu\n1)personas\n2)universidades\n3)ciudades\n4)salir")
    
    opcion=int(input("ingrese una opcion: "))
    
    if(opcion==1):
        opc=0
        while(opc!=4):
            
            os.system('cls')
            os.system('clear')
            print("PERSONAS \n1)crear\n2)listar\n3)eliminar\n4)atras")
            opc=int(input("ingrese una opcion: "))
            
            if(opc==1):
                
                Persona.crearpersona()
            if(opc==2):
                print(personas)
                
            if(opc==3):
                Persona.eliminarpersona()
                
            
            input("Presione enter para continuar...")
            
    if(opcion==2):
            opc=0
            while(opc!=4):
                
                os.system('cls')
                os.system('clear')
                print("UNIVERSIDADES \n1)crear\n2)listar\n3)eliminar\n4)atras")
                opc=int(input("ingrese una opcion: "))
                
                if(opc==1):
                    
                    Universidad.crearuniversidad()
                if(opc==2):
                    print(universidades)
                    
                if(opc==3):
                    Universidad.eliminaruniversidad()
                    
                
                input("Presione enter para continuar...")
        
    if(opcion==3):
            opc=0
            while(opc!=4):
                
                os.system('cls')
                os.system('clear')
                print("CIUDADES \n1)crear\n2)listar\n3)eliminar\n4)atras")
                opc=int(input("ingrese una opcion: "))
                
                if(opc==1):
                    
                    Ciudad.crearciudad()
                if(opc==2):
                    print(ciudades)
                    
                if(opc==3):
                    Ciudad.eliminarciudad()
                    
                
                input("Presione enter para continuar...")
        
    