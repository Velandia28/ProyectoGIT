import os
import json
import pathlib
from main import *
menu_principal1 = ("1. TARJETAS ", "2. REPORTES", "3. SALIR")

# def mostrar_menu(menu):
#     for i in menu:
#         print(i)

def menu_principal():
    clear_screen()
    while True:
        try:
            print("***********************************************")
            print("BIENVENIDO A HOY NO FIO, MAÑANA TAMPOCO ")
            print("************************************************")
            print("Con qué rol va a ingresar al sistema ")
            print("***********************************************")
            for i in menu_principal1:
                print(i)
            opcion = int(input("Ingrese el número del menú al que desea ingresar: "))
            if opcion == 3:
                print("*****************************")
                print("SALIENDO.....")
                print("*****************************")
                break
            elif opcion == 1:
                menu_tarjetas1()
            elif opcion == 2:
                menu_reportes1()
            else :
                print("Opción no válida, por favor intente nuevamente.")
                continue
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue
        
        
        
menu_tarjetas = ("1.  Modificar informacion ","2. Eliminar Tarjetas ","3. Añadir tarjetas","4. Volver al menu anterior")

def menu_tarjetas1():
    clear_screen()
    while True:
        try:
            print("****************************")
            print("BIENVENIDO A TARJETAS ")
            print ("***************************")
            print("Escoja la opción que va a realizar")
            print("******************************")
            for u in menu_tarjetas:
                print(u)
            opci = int(input("Ingrese el número del menú al que desea ingresar: "))
            if opci==1:
                print("Vamos a modificar la informacion de una tarjeta ")
                #modificar_tarjeta()
            elif opci==2:
                print("Vamos a Eliminar una tarjeta del sistema ")
                #eliminar_tarjeta()
            elif opci==3:
                print("Vamos a añadir una nueva tarjeta al sistema")
                #crear_tarjeta()
            elif opci==4:
                print("VOLVIENDO AL MENU ANTERIOR")
                return
            
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue    

menu_reportes=("1. Mostrar tarjetas del cliente","2. Mostrar datos por numero de tarjeta","3. Mostrar todas las tarjetas","4. Volver al menu anterior")

def menu_reportes1():
    clear_screen()
    while True:
        try:
            print("****************************")
            print("BIENVENIDO A REPORTES ")
            print ("***************************")
            print("Escoja la opción que va a realizar")
            print("******************************")
            for o in menu_reportes:
                print(o)
            opc = int(input("Ingrese el número del menú al que desea ingresar: "))
            if opc==1:
                print("Vamos a mostrar las tarjetas del cliente ")
                #Ver_tarjetas_cliente()
            elif opc==2:
                print("Vamos a mostrar las tarjetas segun el numero de cada una de Ellas")
                #ver_tarjetas_numero()
            elif opc==3:
                print("vamos a mostrar TODAS  las tarjetas del sistema ")
                #ver_todas_tarjetas()
            elif opc==4:
                print("VOLVIENDO AL MENU ANTERIOR")
                return
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue 
        
        
menu_principal()