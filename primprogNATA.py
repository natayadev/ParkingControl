import os
import datetime
import time
os.system('cls')

#Cabecera
print("\n\nBIENVENIDO A MI PRIMER PROGRAMA EN PYTHON :)")
print("Servicio de estacionamiento 24hs de Nataya")

#Listas
lista1=[]
lista2=[]
precio=115
x = datetime.datetime.now()
class p:
    Patente=()
class h:
    Hora=()

#Objetos
def IngresoDetectado():
    if len(lista1)==100:
        print("NO HAY LUGARES DISPONIBLES.")
    else:
        a=p()
        a=input("\nIngrese la patente del vehiculo:")
        lista1.append (a)
        print(x.strftime("%c"))
        
def EgresoDetectado():
    a=p()
    a=input("\nIngrese la patente del vehiculo:")
    lista1.remove (a)
    print(x.strftime("%c"))
    
    b=h()
    b=int(input("\nIngrese la hora que estuvo estacionado:"))
    lista2.append (b)
    
    print("\nA cobrar:")
    print(b*precio)

def DatosObtenidos():
    print(lista1)

    print("\nLugares ocupados: ")
    print(len(lista1))
    print("Lugares disponibles: ")
    print(100 - len(lista1))

def TotalFacturado():
    print("Precio actual por hora:")
    print(precio)
    print("\nTOTAL:")
    print(sum(lista2)*precio)

#Menu    
def menu():
    print ("\n----------------------------------------------\nOpciones:")
    print ("\t1 - Ingreso de vehiculos.")
    print ("\t2 - Egreso de vehiculos.")
    print ("\t3 - Lugares disponibles.")
    print ("\t4 - Total facturado.")
    print ("\t5 - Cerrar programa.")

while True:
    menu()
    op=input("----------------------------------------------\nIngresa una opción:")

    if op=="1":
        print ("\n\n-------------Ingreso de vehiculos-------------")
        IngresoDetectado()
        input ("Pulse una tecla para continuar:")
        
    elif op=="2":
        print ("\n\n-------------Egreso de vehiculos--------------")
        EgresoDetectado()
        input ("Pulse una tecla para continuar:")

    elif op=="3":
        print ("\n\n--------------Lista de patentes---------------")
        DatosObtenidos()
        input ("Pulse una tecla para continuar:")

    elif op=="4":
        print ("\n\n---------------Total facturado----------------")
        TotalFacturado()
        input ("Pulse una tecla para continuar:")
        
    elif op=="5":
        print ("\nQue tengas un lindo dia, bye :)")
        break
        
    else:
        print ("\n:( Error 404 - Opción incorrecta")
        input ("Pulsa una tecla para continuar:")
