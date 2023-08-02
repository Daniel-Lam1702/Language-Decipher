#Elaborado por Miguel Andrés Aguilar Brenes y Daniel Eduardo Lam He
#Fecha de creación:24/04/21 7:00 pm
#Última fecha de modificación: 01/05/2021 09:45 pm
#Versión: 3.9.2
#Llamada de librería
#Definición de funciones

#Reto 1 Murcielago
def descifrarCifrarMurcielago(Ptexto):
    """
    Funcionamiento: codificar un texto a codigo Murcielago y decodificarlo
    Entradas: Ptexto(str), texto a codificar o decodificar
    Salidas: textomurcielago(str), texto codificado o decodificado
    """
    textomurcielago = ""
    listacarac1= ["M","U","R","C","I","E","L","A","G","O"]
    listacarac2=["0","1","2","3","4","5","6","7","8","9"]
    for caracter in Ptexto:
        if caracter == " ":
            textomurcielago +="*"
        elif caracter == "*":
            textomurcielago += " "
        elif caracter in  listacarac1:
            for i in range(len( listacarac1)):
                if caracter ==  listacarac1[i]:
                    textomurcielago += listacarac2[i]
                    break
        elif caracter in listacarac2:
            for i in range(len(listacarac2)):
                if caracter == listacarac2[i]:
                    textomurcielago += listacarac1[i]
                    break
        else:
            textomurcielago += caracter
    return  textomurcielago

#Reto 2 Eucalipto
def descifrarCifrarEucalipto(Ptexto):
    """
    Funcionamiento: codificar un texto a codigo Eucalipto y decodificarlo
    Entradas: Ptexto(str), texto a codificar o decodificar
    Salidas: textoeucalipto(str), texto codificado o decodificado
    """
   
    textoeucalipto = ""
    listacarac1= ["e","u","c","a","l","i","p","t","o"]
    listacarac2= ["1","2","3","4","5","6","7","8","9"]
    for caracter in Ptexto:
        if caracter == " ":
            textoeucalipto += "º"
        elif caracter == "º":
           textoeucalipto += " "
        elif caracter in  listacarac1:
            for i in range(len( listacarac1)):
                if caracter ==  listacarac1[i]:
                    textoeucalipto += listacarac2[i]
                    break
        elif caracter in listacarac2:
            for i in range(len(listacarac2)):
                if caracter == listacarac2[i]:
                    textoeucalipto += listacarac1[i]
                    break
        else:
            textoeucalipto += caracter
    return  textoeucalipto

#Reto 3
def descifrarCifrarTextoCenitPolar(pTexto):
    """
    Funcionamiento: Descifrar un texto codificado en CenitPolar o cifrar un texto a CenitPolar
    Entradas: pTexto(str), el texto a codificar o decodificar
    Salidas: textoCenitPolar(str), texto codificado o decodificado
    Nota: No se eliminaron los caracteres especiales durante la codificación; es decir, cuando se ingresa un texto con coma, se mantiene la coma
    """
    textoCenitPolar = ""
    listaCaracteres1 = ["c","e","n","i","t"]
    listaCaracteres2 = ["p","o","l","a","r"]
    for caracter in pTexto:
        if caracter == " ":
            textoCenitPolar += "¬"
        elif caracter == "¬":
            textoCenitPolar += " "
        elif caracter in listaCaracteres1:
            for i in range(len(listaCaracteres1)):
                if caracter == listaCaracteres1[i]:
                    textoCenitPolar += listaCaracteres2[i]
                    break
        elif caracter in listaCaracteres2:
            for i in range(len(listaCaracteres2)):
                if caracter == listaCaracteres2[i]:
                    textoCenitPolar += listaCaracteres1[i]
                    break
        else:
            textoCenitPolar += caracter
    return textoCenitPolar
#Reto 4.1
def cifrarTextoMorse(pTexto):
    """
    Funcionamiento: Cifrar un texto a código Morse
    Entradas: pTexto(str), el texto a codificar
    Salidas: textoCifrado(str), texto codificado en Morse
    """
    textoCifrado = ""
    listaMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-","-.--","--..",".----",
                "..---","...--","....-",".....","-....","--...","---..","----.","-----"]
    listaNormal = ["a","b","c","d","e","f","g","h","i",
                   "j","k","l","m","n","o","p","q","r",
                   "s","t","u","v","w","x","y","z","1",
                   "2","3","4","5","6","7","8","9","0"]
    for posicion in range (len(pTexto)):
        if pTexto[posicion] == " ":
            textoCifrado += "|"
        else:
            for i in range(len(listaNormal)):
                if pTexto[posicion] == listaNormal[i]:
                    if posicion+1 != len(pTexto):
                        if pTexto[posicion+1] == " ":
                            textoCifrado = textoCifrado + listaMorse[i]
                        else:
                            textoCifrado = textoCifrado + listaMorse[i] + "^"
                    else:
                        textoCifrado = textoCifrado + listaMorse[i]
                    break
    return textoCifrado
#Reto 4.2
def descifrarTextoMorse(pTexto):
    """
    Funcionamiento: Descifrar un texto cifrado en Morse
    Entradas: pTexto(str), el texto a descifrar
    Salidas: textoDescifrado(str), texto descifrado del Morse
    """
    textoDescifrado = ""
    listaMorse = [".-","a","-...","b","-.-.","c","-..","d",".","e","..-.","f","--.","g","....","h","..","i",
    ".---","j","-.-","k",".-..","l","--","m","-.","n","---","o",".--.","p","--.-","q",".-.","r",
    "...","s","-","t","..-","u","...-","v",".--","w","-..-","x","-.--","y","--..","z",".----","1",
    "..---","2","...--","3","....-","4",".....","5","-....","6","--...","7","---..","8","----.","9","-----","0"]
    palabra = ""
    for caracter in pTexto:
        palabra = palabra + caracter
        if caracter == "^":
            palabra = palabra.replace("^","")
            for i in range(0,len(listaMorse),2):
                if palabra == listaMorse[i]:
                    textoDescifrado += listaMorse[i+1]
                    palabra = palabra.replace(palabra,"")
                    break
        elif caracter == "|":
            palabra = palabra.replace("|","")
            for i in range(0,len(listaMorse),2):
                if palabra==listaMorse[i]:
                    textoDescifrado += listaMorse[i+1]+" "
                    palabra = palabra.replace(palabra,"")
                    break
    for i in range(0,len(listaMorse),2):
        if palabra==listaMorse[i]:
            textoDescifrado += listaMorse[i+1]+" "
            palabra = palabra.replace(palabra,"")
            break  
    return textoDescifrado
#Reto 5
def cifrarDescifrarTextoSufamelico(pTexto):
    """
    Funcionamiento: Descifrar un texto codificado en Sufamelico o cifrar un texto a Sufamelico
    Entradas: pTexto(str), el texto a codificar o decodificar
    Salidas: textoSufamelico(str), texto codificado o decodificado
    """
    textoSufamelico = ""
    listaCaracteres1 = ["s","u","f","a","m","e","l","i","c","o"]
    listaCaracteres2 = ["u","s","a","f","e","m","i","l","o","c"]
    for caracter in pTexto:
        if caracter in listaCaracteres1:
            for i in range(len(listaCaracteres1)):
                if caracter == listaCaracteres1[i]:
                    textoSufamelico += listaCaracteres2[i]
                    break
        else:
            textoSufamelico += caracter
    return textoSufamelico
#Reto 6--------------------------------------------------------------
def cifrarcifrardeletreo(pTexto):
    """
    Funcionamiento: Cifrar un texto a Deletreo
    Entradas: pTexto(str), el texto a codificar
    Salidas: textodeletreo(str), texto codificado a Deletreo
    """
    alfabeto = ['A','Alpha', 'B','Bravo', 'C','Charlie',
                    'D','Delta', 'E','Echo', 'F','Foxtrot',
                    'G','Golf', 'H','Hotel', 'I','India',
                    'J','Juliet', 'K','Kilo', 'L','Lima',
                    'M','Mike', 'N','November', 'O','Oscar',
                    'P','Papa', 'Q','Quebec', 'R','Romeo',
                    'S','Sierra', 'T','Tango', 'U','Uniform',
                    'V','Victor', 'W','Whiskey', 'X','X-ray',
                    'Y','Yankee', 'Z','Zulu']
    textodeletreo=""
    for caracter in pTexto:
        letra=caracter.upper()
        if letra in alfabeto:
            for i in range(0,len(alfabeto),2):
                if letra==alfabeto[i]:
                    textodeletreo+=alfabeto[i+1]+"~"
                    break
        elif letra==" ":
            textodeletreo = textodeletreo[:-1]
            textodeletreo+=" "
                
    return textodeletreo[:-1]
def descifrardeletreo(Ptexto):
    """
    Funcionamiento: Descifrar un texto cifrado a Deletreo
    Entradas: Ptexto(str), el texto a descifrar
    Salidas: textodeletreo(str), texto descifrado a Deletreo
    """

    textodeletreo = ""
    alfabeto = ['Alpha','A', 'Bravo','B', 'Charlie','C',
                    'Delta','D', 'Echo','E', 'Foxtrot','F',
                    'Golf','G', 'Hotel','H', 'India','I',
                    'Juliet','J', 'Kilo','K', 'Lima','L',
                    'Mike','M', 'November','N', 'Oscar','O',
                    'Papa','P', 'Quebec','Q', 'Romeo','R',
                    'Sierra','S', 'Tango','T', 'Uniform','U',
                    'Victor','V', 'Whiskey','W', 'X-ray','X',
                    'Yankee','Y', 'Zulu','Z']
    palabra = ""
    for caracter in Ptexto:
        palabra = palabra + caracter
        if caracter == "~":
            palabra = palabra.replace("~","")
        elif caracter == " ":
            textodeletreo += " "
            palabra = palabra.replace(palabra,"")
        if palabra.capitalize() in alfabeto:
            for i in range(0,len(alfabeto),2):
                if palabra.capitalize()==alfabeto[i]:
                    textodeletreo+=alfabeto[i+1]
                    palabra = palabra.replace(palabra,"")
                    break
    return textodeletreo