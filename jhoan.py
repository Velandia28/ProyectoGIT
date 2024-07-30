from main import *
import json
import os
import pathlib


desicion=("1.Si","2.No")
tipo_tarjeta=("1.American Express", "2.MasterCard","3.Visa")
modificar=("1.Datos Tarjeta", "2.Datos Cliente", "3.Volver")

def id_existe_globalmente(registros, id):
    for categoria in registros.values():
        if str(id) in categoria:
            return True
    return False

# Funcion crear tarjetas
def crear_tarjeta():
    while True:
        try:
            clear_screen()
            Archivo="Gestion_tarjetas.json"
            Gestion= crear_leer_json(Archivo)
            while True:
                tarjeta={}
                id_tarjeta=str(input("Introduzca 16 digitos de la tarjeta nueva\n--> "))
                if len(id_tarjeta) <16:
                    print("Error en los digitos de la tarjeta vuelva a empezar")
                    continue
                if Gestion.get(id_tarjeta,None)==None:
                    print("¿Cual es el tipo de tarjeta?")
                    for i in tipo_tarjeta:
                        print(i)
                    opc=int(input("--> "))
                    if opc == 1:
                        tipo="American Express"
                    elif opc == 2:
                        tipo="MasterCard"
                    elif opc == 3:
                        tipo="Visa"
                    else:
                        print("Error en la seleccion del tipo de tarjeta\nVuleva empezar")
                        continue
                    mes=int(input("Cual es el numero del mes:\n -->"))
                    if mes <=0 and mes >12:
                        print("Error en el mes\nVuelva a empezar")
                        continue
                    año=int(input("Cuales son los 2 ultimos digitos del año:\n -->"))
                    if año <=0 and año >99:
                        print("Error en el año\nVuelva a empezar")
                        continue
                    validez= f"{mes}/{año}"
                    cvv=int(input("Escriba el codigo de verificacion de 100 a 999:\n --> "))
                    if cvv <100 or cvv >999:
                        print("Error en codigo de Verificacion\nVuelva empezar")
                        continue
                    id_cliente=input("Introduzca la Identificacion del cliente\n--> ")
                    nombre=input("Escriba el nombre completo del cliente\n-->")
                    telefono=input("Escriba el telefono del cliente\n--> ")
                    sexo=input("Escriba el sexo del cliente\n--> ")
                    tarjeta[id_tarjeta] = {
                        "tipo": tipo,
                        "validez": validez,
                        "cvv": cvv,
                        id_cliente:{
                            "nombre": nombre,
                            "telefono": telefono,
                            "sexo": sexo
                        }
                    }
                    print("~"*100)
                    print("Estos son los datos a guardar")
                    print(tarjeta)
                    print("~"*100)
                    print ("¿Desea continuar y guardar?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Vuelva a empezar")  
                        print("~"*100)  
                        continue
                    elif opc1==1: 
                        Gestion.update(tarjeta)
                        guardar_JSON(Gestion,Archivo)
                    else:
                        print("Digite un valor correcto")
                        continue 
                    print("¿Desea agregar otra tarjeta?")
                    for i in desicion:
                        print(i)
                    opc1=int(input("--> "))
                    if opc1==2:
                        print("Saliendo...")  
                        print("~"*100) 
                        return
                    elif opc1==1:
                        continue
                    else:
                        print("Digite un valor correcto")
                        continue
                else:
                    print("Error la tarjeta ya fue creada\nVuelva a empezar")
        except ValueError:
            print("Digite un valor correcto")
            continue 


# crear_tarjeta()


def modificar_tarjeta():
    while True:
        try:
            # clear_screen()
            Archivo="Gestion_tarjetas.json"
            Gestion= crear_leer_json(Archivo)
            print("~"*100)
            tarjeta={}
            print("¿Desea modificar una tarjeta existente?")
            for i in desicion:
                print(i)
            opc1=int(input("--> "))
            if opc1==2:
                print("Saliendo...")
                print("~"*100)
                return
            elif opc1==1:
                id_tarjeta=input("¿Cual es el número de tarjeta?\n--> ")
                if Gestion.get(id_tarjeta,None)==None:
                    print("Error la tarjeta no existe")
                    continue
                else:
                    print("~"*100)
                    print("¿Que desea modificar?")
                    for i in modificar:
                        print(i)
                    opc = int(input("-->"))
                    if opc==3:
                        print("Saliendo...")
                        return
                    elif opc==1:
                        print("~"*100)
                        print(f"Numero de la tarjeta: {id_tarjeta}")
                        for llave, valor in Gestion[id_tarjeta].items():
                            print(f"{llave}: {valor}")
                        print("~"*100)
                        print("Se va a modificar toda la informacion de la tarjeta, menos el numero de tarjeta\n¿Desea continuar?")
                        for i in desicion:
                            print(i)
                        opc1=int(input("--> "))
                        if opc1==2:
                            print("Saliendo...")
                            print("~"*100)
                            return
                        elif opc1==1:
                            print("¿Cual es el tipo de tarjeta?")
                            for i in tipo_tarjeta:
                                print(i)
                            opc=int(input("--> "))
                            if opc == 1:
                                tipo="American Express"
                            elif opc == 2:
                                tipo="MasterCard"
                            elif opc == 3:
                                tipo="Visa"
                            else:
                                print("Error en la seleccion del tipo de tarjeta\nVuleva empezar")
                                continue
                            mes=int(input("Cual es el numero del mes:\n -->"))
                            if mes <=0 and mes >12:
                                print("Error en el mes\nVuelva a empezar")
                                continue
                            año=int(input("Cuales son los 2 ultimos digitos del año:\n -->"))
                            if año <=0 and año >99:
                                print("Error en el año\nVuelva a empezar")
                                continue
                            validez= f"{mes}/{año}"
                            cvv=int(input("Escriba el codigo de verificacion de 100 a 999:\n --> "))
                            if cvv <100 or cvv >999:
                                print("Error en codigo de Verificacion\nVuelva empezar")
                                continue
                            # tarjeta[id_tarjeta][id_cliente]=Gestion[id_tarjeta]
                            # tarjeta[id_tarjeta] = {
                            #     "tipo": tipo,
                            #     "validez": validez,                                   ESTO DEBE SER CORREGIDO
                            #     "cvv": cvv,
                            #     id_cliente:{
                            #         "nombre": nombre,
                            #         "telefono": telefono,
                            #         "sexo": sexo
                            #     }
                            # }

                            print("~"*100)
                            print("Estos son los datos a guardar")
                            print(tarjeta)
                            print("~"*100)
                            print ("¿Desea continuar y guardar?")
                            for i in desicion:
                                print(i)
                            opc1=int(input("--> "))
                            if opc1==2:
                                print("Vuelva a empezar")  
                                print("~"*100)  
                                continue
                            elif opc1==1: 
                                Gestion.update(tarjeta)
                                guardar_JSON(Gestion,Archivo)
                            else:
                                print("Digite un valor correcto")
                                continue 
                            print("¿Desea agregar otra tarjeta?")
                            for i in desicion:
                                print(i)
                            opc1=int(input("--> "))
                            if opc1==2:
                                print("Saliendo...")  
                                print("~"*100) 
                                return
                            elif opc1==1:
                                continue
                            else:
                                print("Digite un valor correcto")
                                continue
                        else:
                            print("Numero invalido")
                            continue
                    else:
                        print("Numero invalido")
                        continue
            else:
                print("Numero invalido")
                continue
        except ValueError:
            print("Digite un valor correcto")
            print("~"*100)
            continue 


modificar_tarjeta()








