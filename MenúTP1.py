#Elaborado por Miguel Aguilar y Daniel Lam He
#Fecha de creación:14/04/21 7:30 pm
#Última fecha de modificación: 01/05/2021 11:11 pm
#Versión: 3.9.2
#Llamada de librería
#Definición de funciones
import re
from  funcionesTP1 import* 
from datetime import datetime
#Reto 1 Murcielago
def cifrarMurcielagoAux(Ptexto):
    """
    Funcionamiento: Valida a Ptexto para cifrarlo
    Entradas:Ptexto(str), texto a cifrar
    Salidas:textomurcielago(str), texto cifrado 
    """
    try:
        if Ptexto== "":
            print("El texto no puede estar vacío")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù*]+$",Ptexto.lower()):
            return descifrarCifrarMurcielago(Ptexto)
        elif "*" in Ptexto:
            print("Ingrese un texto sin cifrar")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionCifrarMurcielago():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto cifrado
    """
   
    try:
        print("***********Murcielago***********")
        cifrar=input("Ingrese el texto sin cifrar: ").upper()
        descifrar=cifrarMurcielagoAux(cifrar)
        if descifrar== 0:
            return opcionCifrarMurcielago()
        else:
            print("El texto cifrado es :",descifrar)
            return bitacora("Murcielago-Cod: ",cifrar, descifrar)
    except:
        print("Ingrese un texto válido")
        return opcionCifrarMurcielago()
#Reto 1.1 Murcielago
def descifrarMurcielagoAux(Ptexto):
    """
    Funcionamiento: Valida a Ptexto para descifrarlo
    Entradas:Ptexto(str), texto a descifrar
    Salidas:textomurcielago(str), texto descifrado 
    """
    try:
        if Ptexto == "":
            print("El texto no puede estar vacío")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù\s]+$",Ptexto.lower()):
            return descifrarCifrarMurcielago(Ptexto)
        elif " " in Ptexto:
            print("Ingrese un texto cifrado")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionDescifrarMurcielago():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto descifrado
    """
    try:
        print("***********Murcielago***********")
        descifrar=input("Ingrese el texto cifrado: ").upper()
        cifrar=descifrarMurcielagoAux(descifrar)
        
        if cifrar==0:
            return opcionDescifrarMurcielago()
        else:
            print("El texto descifrado es :",cifrar)
            return bitacora("Murcielago-Dec: ",descifrar, cifrar)
    except:
        print("Se generó un error inténtelo de nuevo.")
        return opcionDescifrarMurcielago()


#Reto 2 Eucalipto-------------------------------------------------------------------------------------------
def cifrarEucaliptoAux(Ptexto):
    """
    Funcionamiento: Valida a Ptexto para cifrarlo
    Entradas:Ptexto(str), texto a cifrar
    Salidas: textoeucalipto (str), texto cifrado 
    """
    try:
        if Ptexto== "":
            print("El texto no puede estar vacío")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüùº]+$",Ptexto):
            return descifrarCifrarEucalipto(Ptexto)
        elif "º" in Ptexto:
            print("Ingrese un texto sin cifrar")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionCifrarEucalipto():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto cifrado
    """
    try:
        print("***********Eucalipto***********")
        cifrar=input("Ingrese el texto sin cifrar: ").lower()
        descifrar=cifrarEucaliptoAux(cifrar)
        if descifrar== 0:
            return opcionCifrarEucalipto()
        else:
            print("El texto cifrado es :",descifrar)
            return bitacora("Eucalipto-Cod: ",cifrar, descifrar)
    except:
        print("Ingrese un texto válido")
        return opcionCifrarEucalipto()
#Reto 2.1 Eucalipto
def descifrarEucaliptoAux(Ptexto):
    """
    Funcionamiento: Valida a Ptexto para descifrarlo
    Entradas:Ptexto(str), texto a descifrar
    Salidas:textoeucalipto(str), texto descifrado 
    """
    try:
        if Ptexto == "":
            print("El texto no puede estar vacio")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù\s]+$",Ptexto):
            return descifrarCifrarEucalipto(Ptexto)
        elif " " in Ptexto:
            print("Ingrese un texto cifrado")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionDescifrarEucalipto():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto descifrado
    """
    try:
        print("***********Eucalipto***********")
        descifrar=input("Ingrese el texto cifrado: ").lower()
        cifrar=descifrarEucaliptoAux(descifrar)
        if cifrar==0:
            return opcionDescifrarEucalipto()
        else:
            print("El texto descifrado es :",cifrar)
            return bitacora("Eucalipto-Dec :",descifrar, cifrar)
    except:
        print("Se generó un error inténtelo de nuevo.")
        return opcionDescifrarEucalipto()
#Reto 3--------------------------------------------------------------------------------------------------

def cifrarTextoCenitPolarAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el cifrado del texto
    Entradas: pTexto(str), el texto a cifrar
    Salidas:textoCenitPolar(str), texto cifrado o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù¬]+$",pTexto):
            return descifrarCifrarTextoCenitPolar(pTexto)
        elif "¬" in pTexto:
            print("Debe digitar un texto sin cifrar")
            return 0 
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionCifrarTextoCenitPolar():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto cifrado
    """
    try:
        print("***********Cenit-Polar***********")
        textoSinCifrar = input("Ingrese el texto sin cifrar(omita ortografía): ").lower()
        textoCifrado=cifrarTextoCenitPolarAux(textoSinCifrar)
        if   textoCifrado== 0:
            return opcionCifrarTextoCenitPolar()
        else:
            print("El texto cifrado es el siguiente:",textoCifrado)
            return bitacora("CenitPolar-Cod: ",textoSinCifrar, textoCifrado)
    except:
        print("Ingrese un texto válido")
        return opcionCifrarTextoCenitPolar()
#Reto 3.1
def descifrarTextoCenitPolarAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el descifrado del texto
    Entradas: pTexto(str), el texto a descifrar
    Salidas:textoCenitPolar(str), texto descifrado o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù\s]+$",pTexto):
            return descifrarCifrarTextoCenitPolar(pTexto)
        elif " " in pTexto:
            print("Debe digitar un texto cifrado")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionDescifrarTextoCenitPolar():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto descifrado
    """
    try:
        print("***********Cenit-Polar***********")
        textoCifrado = input("Ingrese el texto cifrado (omita ortografía): ").lower() 
        textoDescifrado= descifrarTextoCenitPolarAux(textoCifrado)
        if  textoDescifrado == 0:
            return opcionDescifrarTextoCenitPolar()
        else:
            print("El texto descifrado es el siguiente:", textoDescifrado)
            return bitacora("CenitPolar-Dec :",textoCifrado, textoDescifrado)
    except:
        print("Ingrese un texto válido")
        return opcionDescifrarTextoCenitPolar()

#Reto 4---------------------------------------------------------------------------------------------------------------------


def descifrarTextoMorseAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el descifrado del texto
    Entradas: pTexto(str), el texto a descifrar
    Salidas:textoDescifrado(str), texto descifrado o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        if re.match("^[.\-|^]+$",pTexto): 
            if re.search("[.\-]{5,}[^^|]",pTexto) != None: #previene que el usuario ingrese una letra inexistente en morse, son de maximo 5 puntos o guiones
                print("Debe ingresar un texto cifrado válido")
                return 0
            elif "^|" in pTexto or "|^" in pTexto or "^^" in pTexto:
                print("Debe ingresar un texto cifrado válido")
                return 0
            else:
                return descifrarTextoMorse(pTexto)
        else:
            print("Debe ingresar un texto en código Morse")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo")
        return 0
def opcionDescifrarTextoMorse():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto descifrado
    """
    try:
        print("***********Morse***********")
        textoCifrado = input("Ingrese el texto en Morse que va a descifrar: ")
        textoDescifrado= descifrarTextoMorseAux(textoCifrado)
        if  textoDescifrado== 0:
            return opcionDescifrarTextoMorse()
        else:
            print("El texto descifrado es:",textoDescifrado)
            return bitacora("Morse-dec: ",textoCifrado, textoDescifrado)
    except:
        print("Debe ingresar un texto de tipo string")
        return opcionDescifrarTextoMorse()
#Reto 4.1
def cifrarTextoMorseAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el cifrado del texto
    Entradas: pTexto(str), el texto a cifrar
    Salidas:textoCifrado(str), texto cifrado en Morse o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        elif re.match("^[a-z\s0-9]+$",pTexto):
            if "\t" in pTexto or "\n" in pTexto or "\r" in pTexto or "\f" in pTexto:
                print("Debe ingresar un texto sin cifrar válido. Solo se permiten espacios")
                return 0
            return cifrarTextoMorse(pTexto)
        else:
            print("Debe ingresar un texto sin cifrar válido. Solo se permiten letras y números")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo")
        return 0
def opcionCifrarTextoMorse():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto cifrado
    """
    try:
        print("***********Morse***********")
        textoDescifrado = input("Ingrese el texto que va a cifrar: ").lower()
        textoCidrado=cifrarTextoMorseAux(textoDescifrado)
        if textoCidrado == 0:
            return opcionCifrarTextoMorse()
        else:
            print("El texto cifrado es:",textoCidrado)
            return bitacora("Morse-Cod: ",textoDescifrado, textoCidrado)
    except:
        print("Debe ingresar un texto de tipo string")
        return opcionCifrarTextoMorse()
#Reto 5------------------------------------------------------------------------------------------------------

def cifrarTextoSufamelicoAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el cifrado del texto
    Entradas: pTexto(str), el texto a cifrar
    Salidas:textoSufamelico(str), texto cifrado en Sufamelico o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù]+$", pTexto):
            return cifrarDescifrarTextoSufamelico(pTexto)
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionCifrarTextoSufamelico():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto cifrado
    """
    try:
        print("***********Sufamelico***********")
        textoDescifrado = input("Digite el texto a cifrar(omita la ortografía): ").lower()
        textoCifrado=cifrarTextoSufamelicoAux(textoDescifrado)
        if textoCifrado == 0:
            return opcionCifrarTextoSufamelico()
        else:
            print("El texto cifrado es:",textoCifrado)
            return bitacora("Sufamelico-Cod :",textoDescifrado, textoCifrado)
    except:
        print("Debe ingresar un texto de tipo string")
        return opcionCifrarTextoSufamelico()
#Reto 5.1
def descifrarTextoSufamelicoAux(pTexto):
    """
    Funcionamiento: Validar la entrada pTexto para realizar el descifrado del texto
    Entradas: pTexto(str), el texto a descifrar
    Salidas:textoSufamelico(str), texto descifrado o 0 en caso de que el usuario no digite el texto correctamente
    """
    try:
        if pTexto == "":
            print("Debe ingresar un texto")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù]+$", pTexto):
            return cifrarDescifrarTextoSufamelico(pTexto)
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionDescifrarTextoSufamelico():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String que es el texto descifrado
    """
    try:
        print("***********Sufamelico***********")
        textoCifrado = input("Digite el texto a descifrar(omita la ortografía): ").lower()
        textoDescifrado = descifrarTextoSufamelicoAux(textoCifrado)
        if textoDescifrado == 0:
            return opcionDescifrarTextoSufamelico()
        else:
            print("El texto descifrado es:",textoDescifrado)
            return bitacora("Sufamelico-Dec : ",textoCifrado,textoDescifrado)
    except:
        print("Debe ingresar un texto de tipo string")
        return opcionDescifrarTextoSufamelico()
##Reto 6.2----------------------------------------------------    
def cifrarDeletreoAux(pTexto):
    """
    Funcionamiento: Valida a pTexto para cifrarlo
    Entradas:pTexto(str), texto a cifrar
    Salidas:textodeletreo(str), texto cifrado 
    """
    try:
        if pTexto== "":
            print("El texto no puede estar vacío")
            return 0
        elif re.match("^[^áâäàéêëèíîïìóôöòúûüù~\d]+$",pTexto.lower()):
            return cifrarcifrardeletreo(pTexto)
        elif "~" in pTexto:
            print("Ingrese un texto sin cifrar")
            return 0
        elif pTexto.isalnum():
            print("Ingrese un texto valido")
            return 0
        else:
            print("Debe omitir la ortografía en el texto")
            return 0
    except:
        print("Se ha generado un errorooo, inténtelo de nuevo.")
        return 0
def opcionCifrarDeletreo():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto cifrado
    """
   
    try:
        print("***********Deletreo***********")
        cifrar=input("Ingrese el texto sin cifrar: ").upper()
        descifrar=cifrarDeletreoAux(cifrar)
        if descifrar== 0:
            return opcionCifrarDeletreo()
        else:
            print("El texto cifrado es :",descifrar)
            return bitacora("deletreo-Cod: ",cifrar, descifrar)
    except:
        print("Ingrese un texto válido")
        return opcionCifrarDeletreo()
#Reto 6.2 Deletreo
def descifrarDeletreoAux(pTexto):
    """
    Funcionamiento: Valida a pTexto para descifrarlo
    Entradas:pTexto(str), texto a descifrar
    Salidas:textodeletreo(str), texto descifrado 
    """
    alfabeto = ['Alpha','Bravo', 'Charlie',
                    'Delta', 'Echo', 'Foxtrot',
                    'Golf', 'Hotel', 'India',
                    'Juliet', 'Kilo', 'Lima',
                    'Mike', 'November','Oscar',
                    'Papa', 'Quebec', 'Romeo',
                    'Sierra', 'Tango', 'Uniform',
                    'Victor', 'Whiskey', 'X-ray',
                    'Yankee', 'Zulu']    
    try:
        listaTextoFinal = []
        if "~~" in pTexto:
            print("Ingrese un texto codificado válido")
            return 0
        listaTexto = pTexto.split("~")
        for palabraInicial in listaTexto:
            if " " in palabraInicial:
                listaTextoFinal += palabraInicial.split(" ")
            else:
                listaTextoFinal.append(palabraInicial)
        for palabraFinal in listaTextoFinal:
            if palabraFinal.capitalize() not in alfabeto:
                print("Ingrese un texto codificado válido")
                return 0
        else:
            return descifrardeletreo(pTexto)
    except:
        print("Se ha generado un error, inténtelo de nuevo.")
        return 0
def opcionDescifrarDeletreo():
    """
    Funcionamiento: Responsable de permitir la entrada y salida de datos 
    Entradas: NA
    Salidas: String con el texto descifrado
    """
    try:
        print("***********Deletreo***********")
        descifrar=input("Ingrese el texto cifrado: ")
        cifrar=descifrarDeletreoAux(descifrar)
        if cifrar==0:
            return opcionDescifrarDeletreo()
        else:
            print("El texto descifrado es :",cifrar)
            return bitacora("Deletreo-Dec: ",descifrar, cifrar)
    except:
        print("Se generó un error inténtelo de nuevo.")
        return opcionDescifrarDeletreo
#Reto 7----------------------------------------------------  
def bitacora(pNombre,pEntra,pSale):
    """
    Funcionamiento: Añadirle contenido (textos codificados y decodificados) a la bitacora. 
    Entradas: 
    -pNombre(str): Estrategia usada para codificar o decodificar 
    -pEntra(str): Texto ingresado por el usuario
    -pSale(str): Texto codificado o decodificado
    Salidas: NA
    """
    try:
        tiempo = datetime.now()
        bitacora = open("bitacora.txt","a")
        texto = str(tiempo.time())+"\t\t"+pNombre+"entra("+pEntra+"), sale("+pSale+")\n"
        bitacora.write(texto)
        bitacora.close()
        return ""
    except:
        return ""
def eliminarBitacora():
    """
    Funcionamiento: Eliminar el contenido de la bitácora. 
    Entradas: NA
    Salidas: string indicando que se eliminó el contenido de la bitácora.
    """
    open("bitacora.txt", "w").close()
    print("El contenido de la bitácora se ha eliminado efectivamente.")
    return ""
#Menú
def opcionCodificar():
    """
    Funcionamiento: De manera repetitiva, muestra las opciones de la opción codificar al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    try:
        print ("\n**************************\n\
Codificar texto\n**************************\n\
¿En cuál estrategia de codificación desea cifrar?\n\
**************************\n\
1. Murciélago\n\
2. Eucalipto\n\
3. Cenit Polar\n\
4. Morse\n\
5. Sufamelico\n\
6. Deletreo\n\
0. No desea codificar")
        opcion = int (input ("Escoja una opción: "))
        if opcion >=0 and opcion <=6:
            if opcion == 1:
                opcionCifrarMurcielago()
            elif opcion == 2:
                opcionCifrarEucalipto()
            elif opcion == 3:
                opcionCifrarTextoCenitPolar()
            elif opcion == 4:
                opcionCifrarTextoMorse()
            elif opcion == 5:
                opcionCifrarTextoSufamelico()
            elif opcion == 6:    
                opcionCifrarDeletreo()
            else:
                return 0
        else:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
            opcionCodificar()
    except:
        print("Ingrese un número entero correspondiente a las opciones")
        opcionCodificar()
def opcionDecodificar():
    """
    Funcionamiento: De manera repetitiva, muestra las opciones de la opción decodificar al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    try:
        print ("\n**************************\n\
Decodificar texto\n**************************\n\
¿En cuál estrategia de codificación desea descifrar?\n\
**************************\n\
1. Murciélago\n\
2. Eucalipto\n\
3. Cenit Polar\n\
4. Morse\n\
5. Sufamelico\n\
6. Deletreo\n\
0. No desea decodificar")
        opcion = int (input ("Escoja una opción: "))
        if opcion >=0 and opcion <=6:
            if opcion == 1:
                opcionDescifrarMurcielago()
            elif opcion == 2:
                opcionDescifrarEucalipto()
            elif opcion == 3:
                opcionDescifrarTextoCenitPolar()
            elif opcion == 4:
                opcionDescifrarTextoMorse()
            elif opcion == 5:
                opcionDescifrarTextoSufamelico()
            elif opcion == 6:    
                opcionDescifrarDeletreo()
            else:
                return 0
        else:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
            opcionDecodificar()
    except:
        print("Ingrese un número entero correspondiente a las opciones")
        opcionDecodificar()
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    try:
        print("\n**************************\n\
Tarea Programada 1\n**************************\n\
¿Qué desea realizar?\n\
**************************\n\
1. Codificar texto\n\
2. Decodificar texto\n\
3. Eliminar bitácora\n\
0. Terminar")
        opcion = int (input ("Escoja una opción: "))
        if opcion >=0 and opcion <=3:   
            if opcion == 1:
                opcionCodificar()          
            elif opcion == 2:
                opcionDecodificar()
            elif opcion == 3:
                eliminarBitacora()
            else:
                return 0
        else:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
        menu()
    except:
        print("Debe ingresar un número entero correspondiente a las opciones")
        menu()
#Programa principal
menu()