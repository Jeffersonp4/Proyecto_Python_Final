import sqlite3
import os
import requests
import json
from geopy.geocoders import Nominatim
import unidecode
geolocator = Nominatim(user_agent='ITLA')
import jinja2
from matplotlib import pyplot
from playsound import playsound

#Jefferson20197974
#buscar= jinja2.Environment(loader= jinja2.FileSystemLoader("C:/Users/ARCUS COMP/Desktop/fundamentos de programacion/tarea 7/Metioritos/"))
#enlazar= buscar.get_template("metiorito.html")


def limpiar():
    os.system("cls")

def cedulas():
    global pais, coordenadas, provincia, zodiaco
    miconexion = sqlite3.connect("base_coronavirus")
    playsound("sonidos/dato.wav")
    try:
        cedula = input("Digite la cedula del paciente (si tiene) si no, digite la de su madre,padre o tutor: ")
        url = requests.get("http://173.249.49.169:88/api/test/consulta/"+ cedula)
        persona = json.loads(url.text)
        Nombre = persona["Nombres"]
        Apellido = persona["Apellido1"]
        Apellido2 = persona["Apellido2"]
        Fecha_nac = persona["FechaNacimiento"]
        age= Fecha_nac[0:4]
        mes= Fecha_nac[5:7]
        dia= Fecha_nac[8:10]
        nacimiento= f"{age}-{mes}-{dia}"
        nacimientomes1 = persona['FechaNacimiento']
        nacimientomes2 = persona['FechaNacimiento']
        dia1 = persona['FechaNacimiento']
        dia2 = persona['FechaNacimiento']
        nacimientomes1 = nacimientomes1[5]
        nacimientomes2 = nacimientomes2[6]
        dia1 = dia1[8]
        dia2 = dia2[9]

        mes = nacimientomes1 + nacimientomes2
        dia = dia1 + dia2
        if mes == '01' and dia <= '19':
            zodiaco = (" Capricornio.")
        elif mes == '01' and dia >= '20' and dia <= '30':
            zodiaco = (" Acuario.")
        elif mes == '02' and dia <= '18':
            zodiaco = (" Acuario.")
        elif mes == '02' and dia >= '19' and dia <= '29':
            zodiaco = (" Piscis.")
        elif mes == '03' and dia <= '20':
            zodiaco = (" piscis.")
        elif mes == '03' and dia >= '21' and dia <= '31':
            zodiaco = (" Aries.")
        elif mes == '04' and dia <= '19':
            zodiaco = (" Aries.")
        elif mes == '04' and dia >= '20' and dia <= '30':
            zodiaco = (" Tauro.")
        elif mes == '05' and dia <= '20':
            zodiaco = (" Tauro.")
        elif mes == '05' and dia >= '21' and dia <= '31':
            zodiaco = (" Geminis.")
        elif mes == '06' and dia <= '20':
            zodiaco = (" Geminis.")
        elif mes == '06' and dia >= '21' and dia <= '30':
            zodiaco = ("Cancer.")
        elif mes == '07' and dia <= '22':
            zodiaco = (" Cancer.")
        elif mes == '07' and dia >= '23' and dia <= '31':
            zodiaco = (" Leo.")
        elif mes == '08' and dia <= '22':
            zodiaco = (" Leo.")
        elif mes == '08' and dia >= '23' and dia <= '31':
            zodiaco = (" Virgo.")
        elif mes == '09' and dia < '22':
            zodiaco = (" Virgo.")
        elif mes == '09' and dia >= '23' and dia <= '30':
            zodiaco = (" Libra.")
        elif mes == '10' and dia <= '22':
            zodiaco = (" Libra.")
        elif mes == '10' and dia >= '23' and dia <= '31':
            zodiaco = (" Escorpio.")
        elif mes == '11' and dia <= '21':
            zodiaco = (" Escorpio.")
        elif mes == '11' and dia >= '22' and dia <= '30':
            zodiaco = (" Sagitario.")
        elif mes == '12' and dia <= '22':
            zodiaco = (" Sagitario.")
        elif mes == '12' and dia >= '23' and dia <= '31':
            zodiaco = (" Capricornio.")

        dicionario={
            "Nombres": Nombre,
            "Apellido1": Apellido,
            "Apellido2": Apellido2,
            "FechaNacimiento": nacimiento,
            "Signo": zodiaco
                                         }
        nombre = dicionario["Nombres"]
        apellido = dicionario["Apellido1"]
        nacimiento = dicionario["FechaNacimiento"]
        signo= dicionario["Signo"]

    except:
            print("Porfavor Digita una cedula valida")
            input("Presione Enter para volver a intentarlo: ")
            cedulas()

    pasaporte = input("Digite su pasaporte en caso de que lo tenga: ")
    id = input("digite el id en caso de que tenga pasaporte: ")
    sexo = input("Digite el sexo del paciente: ")
    nacinalida = input("Digite su Nacionalidad: ")
    estado = input("Digite el estado en que se encuentra el paciente (Enfermo o Recuperado): ")
    telefono = input("Digite su numero de telefono: ")
    correo = input("Digite su correo electronico: ")

    try:
        lat = input('Ingrese la latitud en la que se encuentra el caso: ')
        log = input('Ingrese la longitud en la que se encuentra el caso: ')

        coordenadas = lat, log
        localizacion = geolocator.reverse(coordenadas)

        pais = localizacion.raw['address']['country']  # Obteniendo el nombre del pais
        provincia = localizacion.raw['address']['state']  # Obteniendo el nombre de la provincia
    except:
        input('Por favor introduzca coordenadas correctas\nPresione enter para intentarlo Desde el principio: ')
        cedulas()

    if pais == 'República Dominicana':
        pass
    else:
        input(
            'La coordenada que ingreso no pertenece a la Republica Dominciana\nPresione enter para intentarlo Desde el principio: ')
        cedulas()

    while True:
        provin = input('Ingrese el nombre de su provincia: ')
        if 'ñ' in provin:
            mi = provincia.lower()
            if provin == provincia or provin == mi:
                break
            else:
                print(
                    f'La provincia que digito no pertenece a las coordenadas {coordenadas}\nPor favor vuelva a intentarlo')
        else:
            minu = provincia.lower()
            if provin == unidecode.unidecode(
                    provincia) or provin == provincia or provin == minu or provin == unidecode.unidecode(minu):
                break
            else:
                print(
                    f'La provincia que digito no pertenece a las coordenadas {coordenadas}\nPor favor vuelva a intentarlo')

    print('Provincia: ' + provincia + '\nCoordenadas: ', coordenadas)


    micursor = miconexion.cursor()
    #micursor.execute("CREATE TABLE coronaviru (llave integer PRIMARY KEY AUTOINCREMENT,cedula varchar(100),pasaporte varchar(100),id varchar(100),nombre varchar(100),apellido varchar(100),sexo varchar(50),Fecha_nacimiento date, Signo varchar(50), nacionalidad varchar(100), estado varchar(50),telefono varchar(50),correo varchar(100),Latitud real, Longitud real, provincia varchar(200)) ")
    micursor.execute("INSERT INTO coronaviru (cedula,pasaporte,id,nombre,apellido,sexo,fecha_nacimiento,Signo,nacionalidad,estado,correo,telefono,latitud,longitud,provincia) values ('" + str(cedula) + "', '" + str(pasaporte) + "', '" + str(id) + "', '" + str(nombre) + "', '" + str( apellido) + "', '" + str(sexo) + "', '" + str(nacimiento) + "', '" + str(signo) + "', '" + str(nacinalida) + "', '" + str(estado) + "', '" + str(telefono) + "', '" + str(correo) + "', '" + str(lat) + "','" + str(log) + "','" + str(provincia) + "')")
    miconexion.commit()
    miconexion.close()


def alerta():
    miconexion = sqlite3.connect("base_coronavirus")
    micursor = miconexion.cursor()
    micursor.execute("SELECT  * FROM coronaviru")

    token = "1074586596:AAFRRnb-fOSi4E-dLd2jzTrEjPRxO1iTaKA"  # nuestro token del boot
    cont=""
    data = micursor
    for tmp in data:
        for t in tmp[1]:
            cont += t
            r = requests.post('https://api.telegram.org/bot1081416240:AAFGrnRVAdccwYPlPHSt6eDS9qPf0PCf6tM/sendMessage',data=dict(chat_id='-1001418835486',text='' 'Se ha registrado un nuevo caso de Coronavirus, Hasta el momento van ' + str(cont) + " Casos encontrados "    ''))
            return r

    miconexion.close()


def mostrar():
    miconexion=sqlite3.connect("base_coronavirus")
    micursor= miconexion.cursor()
    micursor.execute("SELECT  * FROM coronaviru")

    print("\t llave \t\t\t  Cedula  \t\t  Pasaporte \t\t  Id \t\t  Nombre \t\t  apellido \t\t  Sexo \t\t\t   Fecha_nac  \t\t\t  Signo zodiacal  \t\t\t  Nacionalidad \t\t\t   Estado \t\t  Correo \t\t  Telefono  \t\t  Latitud \t\t  Longitud \t\t  Provincia \t ")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for tmp in micursor:
        cl = '\t\t' + str(tmp[0]) + '\t\t' +str(tmp[1]) + '\t\t\t' + str(tmp[2]) + '\t\t\t' + str(tmp[3]) + '\t\t' + str(tmp[4]) + '\t\t' + str(tmp[5]) + '\t\t' + str(tmp[6]) + '\t\t' + str(tmp[7]) + '\t\t\t\t\t'  + str(tmp[8]) +  '\t\t\t\t\t' + str(tmp[9]) + '\t\t\t\t' + str(tmp[10]) + '\t\t\t\t' + str(tmp[11]) + '\t\t\t' + str(tmp[12]) + '\t\t' + str(tmp[13]) + '\t\t' + str(tmp[14]) + '\t\t' + str(tmp[15])
        print(cl)

    miconexion.close()

def editar():
    virus=[]
    miconexion = sqlite3.connect("base_coronavirus")
    micursor = miconexion.cursor()
    micursor.execute("SELECT * FROM coronaviru")
    playsound("sonidos/elija.wav")
    print("\t llave \t\t\t  Cedula  \t\t  Pasaporte \t\t  Id \t\t  Nombre \t\t  apellido \t\t  Sexo \t\t\t   Fecha_nac  \t\t\t  Signo zodiacal  \t\t\t  Nacionalidad \t\t\t   Estado \t\t  Correo \t\t  Telefono  \t\t  Latitud \t\t  Longitud \t\t  Provincia \t ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for tmp in micursor:
        virus.append(tmp)
        cl = '\t\t' + str(tmp[0]) + '\t\t' +str(tmp[1]) + '\t\t\t' + str(tmp[2]) + '\t\t\t' + str(tmp[3]) + '\t\t' + str(tmp[4]) + '\t\t' + str(tmp[5]) + '\t\t' + str(tmp[6]) + '\t\t' + str(tmp[7]) + '\t\t\t\t\t'  + str(tmp[8]) +  '\t\t\t\t\t' + str(tmp[9]) + '\t\t\t\t' + str(tmp[10]) + '\t\t\t\t' + str(tmp[11]) + '\t\t\t' + str(tmp[12]) + '\t\t' + str(tmp[13]) + '\t\t' + str(tmp[14]) + '\t\t' + str(tmp[15])
        print(cl)

    llave= input("Elija el numero del Paciente que desea editar: ")

    for tmp in virus:
        print(tmp[0])
        if int(tmp[0]) == int(llave):
            llave = tmp[0]
            cedula = tmp[1]
            pasaporte = tmp[2]
            id = tmp[3]
            nombre = tmp[4]
            apellido = tmp[5]
            sexo= tmp[6]
            nacimiento = tmp[7]
            signo = tmp[8]
            nacio = tmp[9]
            estado = tmp[10]
            correo = tmp[11]
            tele = tmp[12]
            lati = tmp[13]
            long = tmp[14]
            prov = tmp[15]

    try:
        cedula = input(f"Digite la nueva cedula del paciente " + cedula + "\n  (si tiene) si no digite la su madre,padre o tutor: ")
        url = requests.get("http://173.249.49.169:88/api/test/consulta/" + cedula)
        persona = json.loads(url.text)
        Nombre = persona["Nombres"]
        Apellido = persona["Apellido1"]
        Apellido2 = persona["Apellido2"]
        Fecha_nac = persona["FechaNacimiento"]
        age = Fecha_nac[0:4]
        mes = Fecha_nac[5:7]
        dia = Fecha_nac[8:10]
        nacimiento = f"{age}-{mes}-{dia}"
        nacimientomes1 = persona['FechaNacimiento']
        nacimientomes2 = persona['FechaNacimiento']
        dia1 = persona['FechaNacimiento']
        dia2 = persona['FechaNacimiento']
        nacimientomes1 = nacimientomes1[5]
        nacimientomes2 = nacimientomes2[6]
        dia1 = dia1[8]
        dia2 = dia2[9]

        mes = nacimientomes1 + nacimientomes2
        dia = dia1 + dia2
        if mes == '01' and dia <= '19':
            zodiaco = (" Capricornio.")
        elif mes == '01' and dia >= '20' and dia <= '30':
            zodiaco = (" Acuario.")
        elif mes == '02' and dia <= '18':
            zodiaco = (" Acuario.")
        elif mes == '02' and dia >= '19' and dia <= '29':
            zodiaco = (" Piscis.")
        elif mes == '03' and dia <= '20':
            zodiaco = (" piscis.")
        elif mes == '03' and dia >= '21' and dia <= '31':
            zodiaco = (" Aries.")
        elif mes == '04' and dia <= '19':
            zodiaco = (" Aries.")
        elif mes == '04' and dia >= '20' and dia <= '30':
            zodiaco = (" Tauro.")
        elif mes == '05' and dia <= '20':
            zodiaco = (" Tauro.")
        elif mes == '05' and dia >= '21' and dia <= '31':
            zodiaco = (" Geminis.")
        elif mes == '06' and dia <= '20':
            zodiaco = (" Geminis.")
        elif mes == '06' and dia >= '21' and dia <= '30':
            zodiaco = ("Cancer.")
        elif mes == '07' and dia <= '22':
            zodiaco = (" Cancer.")
        elif mes == '07' and dia >= '23' and dia <= '31':
            zodiaco = (" Leo.")
        elif mes == '08' and dia <= '22':
            zodiaco = (" Leo.")
        elif mes == '08' and dia >= '23' and dia <= '31':
            zodiaco = (" Virgo.")
        elif mes == '09' and dia < '22':
            zodiaco = (" Virgo.")
        elif mes == '09' and dia >= '23' and dia <= '30':
            zodiaco = (" Libra.")
        elif mes == '10' and dia <= '22':
            zodiaco = (" Libra.")
        elif mes == '10' and dia >= '23' and dia <= '31':
            zodiaco = (" Escorpio.")
        elif mes == '11' and dia <= '21':
            zodiaco = (" Escorpio.")
        elif mes == '11' and dia >= '22' and dia <= '30':
            zodiaco = (" Sagitario.")
        elif mes == '12' and dia <= '22':
            zodiaco = (" Sagitario.")
        elif mes == '12' and dia >= '23' and dia <= '31':
            zodiaco = (" Capricornio.")

        dicionario = {
            "Nombres": Nombre,
            "Apellido1": Apellido,
            "Apellido2": Apellido2,
            "FechaNacimiento": nacimiento,
            "Signo": zodiaco}

    except:
        print("Porfavor Digita una cedula valida")
        input("Presione Enter para volver a intentarlo: ")
        editar()

    pasaporte = input("Digite su nuevo pasaporte en caso de que lo tenga Actualmente: "+pasaporte+" \n: ")
    id = input("digite el id en caso de que tenga pasaporte: " "Actualmente: "+id+"\n:")
    nombre =   dicionario["Nombres"]
    apellido = dicionario["Apellido1"]
    sexo = input("Digite el nuevo sexo del paciente: " "Actualmente: "+sexo+ " \n: ")
    nacimiento = dicionario["FechaNacimiento"]
    signo= dicionario["Signo"]
    nacinalida = input("Digite la nueva Nacionalidad de " "Actualmente: "+nacio+" \n: ")
    estado = input("Digite el nuevo estado en que se encuentra el nuevo paciente (Enfermo o Recuperado) Estaba:"+estado+"\n:" )
    telefono= input("Digite su nuevo numero de telefono, telefono actual: "+tele+ "\n:")
    correo = input("Digite su nuevo correo electronico, correo actual: "+correo+"\n:")

    try:
        lat = input("Digite la nueva latitud del lugar donde ocurrio el caso: Latitud actual:" + str(lati) + "\n:")
        log = input("Digite la nueva longitud del lugar donde ocurrio el caso: Longitud actual: " + str(long) + "\n:")

        coordenadas = lat, log
        localizacion = geolocator.reverse(coordenadas)

        pais = localizacion.raw['address']['country']  # Obteniendo el nombre del pais
        provincia = localizacion.raw['address']['state']  # Obteniendo el nombre de la provincia
    except:
        input('Por favor introduzca coordenadas correctas\nPresione enter para intentarlo Desde el principio: ')
        editar()

    if pais == 'República Dominicana':
        pass
    else:
        input('La coordenada que ingreso no pertenece a la Republica Dominciana\nPresione enter para intentarlo Desde el principio: ')
        editar()

    while True:
        provin = input('Ingrese el nombre de su nueva provincia: ')
        if 'ñ' in provin:
            mi = provincia.lower()
            if provin == provincia or provin == mi:
                break
            else:
                print(
                    f'La provincia que digito no pertenece a las coordenadas {coordenadas}\nPor favor vuelva a intentarlo')
        else:
            minu = provincia.lower()
            if provin == unidecode.unidecode(
                    provincia) or provin == provincia or provin == minu or provin == unidecode.unidecode(minu):
                break
            else:
                print(
                    f'La provincia que digito no pertenece a las coordenadas {coordenadas}\nPor favor vuelva a intentarlo')

    print('Provincia: ' + provincia + '\nCoordenadas: ', coordenadas)

    sql = "UPDATE coronaviru set   cedula= '" +str(cedula)  + "', pasaporte='" + str(pasaporte) + "', id='" + str(id) + "', nombre='" + str(nombre) + "', apellido='" + str(apellido) + "', sexo='" + str(sexo) + "', Fecha_nacimiento='"+str(nacimiento)+ "', Signo='"+str(signo)+"' , nacionalidad='" + str(nacinalida) + "', estado='" + str(estado) + "' , correo='" + str(telefono) + "' , telefono='" + str(correo) + "', Latitud='" + str(lat) + "', Longitud='" + str(long) + "', provincia='" + str(provincia) + "'  where llave = " + str(llave)
    micursor.execute(sql)
    miconexion.commit()
    miconexion.close()
    print("Paciente Actualizado")
    playsound("sonidos/actualizar.wav")
    input("Presione ENTER para volver al menu: ")
    playsound("sonidos/menu.wav")
    menu()


def conseguir_archivo(archivo):
    if os.path.exists(archivo):
        fp= open(archivo, "r")
        contenido= fp.read()
        fp.close()
        return contenido


def exportar():
    miconexion = sqlite3.connect("base_coronavirus")
    micursor = miconexion.cursor()
    SQL = ("SELECT * FROM coronaviru")
    micursor.execute(SQL)
    base = conseguir_archivo("casos_corona.html")
    entrar=[]

    for virus in micursor:
        temporal= """L.marker(["""+str(virus[13])+""", """+str(virus[14])+"""])
                        .addTo(map)
                        .bindPopup('cedula:""" +virus[1]+ """ , pasaporte:"""+str(virus[2])+""" , id:"""+(virus[3])+""" , nombre:"""+(virus[4])+""" , apellido:"""+(virus[5])+""" , sexo:"""+(virus[6])+""" , Fecha_nacimiento:"""+(virus[7])+""" , signo:"""+(virus[8])+""" , nacionalidad:"""+(virus[9])+""" , estado:"""+(virus[10])+""" , correo:"""+(virus[11])+""" , telefono:"""+(virus[12])+""" , provincia:"""+(virus[15])+""" ');"""
        entrar.append(temporal)

    sep=" "
    camb= sep.join(entrar)
    base= base.replace ("{MARCADORES}" , camb)

    f = open("casos_encontrados.html", "w")
    f.write(base)
    f.close()
    miconexion.commit()
    miconexion.close()

def exportar_un_caso():
    miconexion = sqlite3.connect("base_coronavirus")
    micursor = miconexion.cursor()
    SQL = ("SELECT * FROM coronaviru")
    micursor.execute(SQL)
    entrar = []
    print("\t llave \t\t Cedula \t\t Pasaporte \t\t Id \t\t Nombre \t\t apellido \t\t Sexo \t\t Fecha_nac \t\t Nacionalidad \t\t Estado \t\t Telefono \t\t Correo  \t\t Latitud \t\t Longitud \t\t\t Provincia \t ")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    for tmp in micursor:
        entrar.append(tmp)
        cl = '\t\t' + str(tmp[0]) + '\t\t' +str(tmp[1]) + '\t\t\t' + str(tmp[2]) + '\t\t\t' + str(tmp[3]) + '\t\t' + str(tmp[4]) + '\t\t' + str(tmp[5]) + '\t\t' + str(tmp[6]) + '\t\t' + str(tmp[7]) + '\t\t' + str(tmp[8]) + '\t\t' + str(tmp[9]) + '\t\t' + str(tmp[10]) + '\t\t' + str(tmp[11]) + '\t\t' + str(tmp[12]) + '\t\t' + str(tmp[13]) + '\t\t' + str(tmp[14]) + '\t\t' + str(tmp[15])
        print(cl)

    llave = input("Elija el numero del paciente que desea exportar: ")


    for caso in entrar:
        print(caso[0])
        if caso[0] == int(llave):
            cedula= caso[1]
            pasaporte= caso[2]
            Id= caso[3]
            nombre= caso[4]
            apellido= caso[5]
            sexo= caso[6]
            fecha_nac= caso[7]
            signo=caso[8]
            nacionalidad= caso[9]
            estados= caso[10]
            telefono= caso[11]
            correo= caso[12]
            latitud= caso[13]
            longitud= caso[14]
            provin= caso[15]

            diccionario={
                "cedula": cedula,
                "pasaporte": pasaporte,
                "Id": Id,
                "nombre": nombre,
                "apellido": apellido,
                "sexo": sexo,
                "fecha_nac": fecha_nac,
                "Signo": signo,
                "nacionalidad": nacionalidad,
                "estado": estados,
                "telefono": telefono,
                "correo": correo,
                "latitud": latitud,
                "longitud": longitud,
                "provincia": provin
            }


            env = jinja2.Environment(loader=jinja2.FileSystemLoader("C:/Users/ARCUS COMP/Desktop/fundamentos de programacion/Proyecto final/"))
            enlazar = env.get_template("un_caso_corona.html")
            datos= diccionario
            html=enlazar.render(datos)

            entrar = []

            temporal = """L.marker([""" + str(latitud) + """, """ + str(longitud) + """])
                                    .addTo(map)
                                    .bindPopup('cedula:""" + cedula + """ , pasaporte:""" + str(pasaporte) + """ , id:""" + (Id) + """ , nombre:""" + (nombre) + """ , apellido:""" + (apellido) + """ , sexo:""" + (sexo) + """ , Fecha_nacimiento:""" + (fecha_nac) + """ , Signo:""" + (signo) + """ , nacionalidad:""" + (nacionalidad) + """ , estado:""" + (estados) + """ , correo:""" + (correo) + """ , telefono:""" + (telefono) + """ , provincia:""" + (provin) + """ ');"""
            entrar.append(temporal)

            sep = " "
            camb = sep.join(entrar)
            html = html.replace("{MARCADORES}", camb)

            f = open(f"{nombre}.html", "w")
            f.write(html)
            f.close()

    miconexion.commit()
    miconexion.close()
    print("Caso Exportado")
    playsound("sonidos/exportado.wav")
    input("Presione ENTER para volver al menu:")
    playsound("sonidos/menu.wav")
    menu()

def estadistica():
    miconexion = sqlite3.connect("base_coronavirus")
    micursor = miconexion.cursor()
    micursor.execute("SELECT  * FROM coronaviru")

    capricornio=0
    acuario=0
    picis=0
    aries=0
    tauro=0
    geminis=0
    cancer=0
    leo=0
    virgo=0
    escorpio=0
    libra=0
    sagitario=0
    a=""
    datos=micursor

    for virus in datos:
        for r in virus[7]:
            a += r

        mes = a[5:7]
        dia = a[8:11]

        if mes == '01' and dia <= '19':
            capricornio += 1
        elif mes == '01' and dia >= '20' and dia <= '30':
            acuario += 1
        elif mes == '02' and dia <= '18':
            acuario += 1
        elif mes == '02' and dia >= '19' and dia <= '29':
            picis += 1
        elif mes == '03' and dia <= '20':
            picis += 1
        elif mes == '03' and dia >= '21' and dia <= '31':
            aries += 1
        elif mes == '04' and dia <= '19':
            aries += 1
        elif mes == '04' and dia >= '20' and dia <= '30':
            tauro += 1
        elif mes == '05' and dia <= '20':
            tauro += 1
        elif mes == '05' and dia >= '21' and dia <= '31':
            geminis += 1
        elif mes == '06' and dia <= '20':
            geminis += 1
        elif mes == '06' and dia >= '21' and dia <= '30':
            cancer += 1
        elif mes == '07' and dia <= '22':
            cancer += 1
        elif mes == '07' and dia >= '23' and dia <= '31':
            leo += 1
        elif mes == '08' and dia <= '22':
            leo += 1
        elif mes == '08' and dia >= '23' and dia <= '31':
            virgo += 1
        elif mes == '09' and dia < '22':
            virgo += 1
        elif mes == '09' and dia >= '23' and dia <= '30':
            libra += 1
        elif mes == '10' and dia <= '22':
            libra += 1
        elif mes == '10' and dia >= '23' and dia <= '31':
            escorpio += 1
        elif mes == '11' and dia <= '21':
            escorpio += 1
        elif mes == '11' and dia >= '22' and dia <= '30':
            sagitario += 1
        elif mes == '12' and dia <= '22':
            sagitario += 1
        elif mes == '12' and dia >= '23' and dia <= '31':
            capricornio += 1
        a = ""
    print(f"Casos de corona virus por signo zodiacal\n"
          f"Capricornio: {capricornio}\n"
          f"Acuario: {acuario}\n"
          f"Picis: {picis}\n"
          f"Aries: {aries}\n"
          f"Tauro: {tauro}\n"
          f"Geminis: {geminis}\n"
          f"Cancer: {cancer}\n"
          f"Leo: {leo}\n"
          f"Virgo: {virgo}\n"
          f"Escorpio: {escorpio}\n"
          f"Libra: {libra}\n"
          f"Sagitario: {sagitario}\n")

    input("Presione Enter para ver la interfaz grafica: ")
    playsound("sonidos/interfaz.wav")
    signo=["Capricornio","Acuario","Picis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Escorpio","Libra","Sagitario"]
    Valores = [int(capricornio), int(acuario), int(picis), int(aries), int(tauro), int(geminis), int(cancer), int(leo), int(virgo), int(escorpio), int(libra), int(sagitario)]
    colores=["red","blue","green","yellow","pink","orange","gray","black","purple","brown","violet","White"]
    pyplot.title("Interfaz Grafica de casos de coronavirus")
    pyplot.bar(signo, height=Valores, color=colores, width=1)
    pyplot.show()
    miconexion.close()


def menu():
    limpiar()
    print("Bienvenido Al Registro de Casos de coronavirus en el pais")
    playsound("sonidos/bienvenido.wav")
    print("------------------------------------------------------------------")
    print("1.- Registrar Caso ")
    print("2.- Mostrar caso de paciente infectado")
    print("3.- Editar caso de algun paciente")
    print("4.- Mostrar todos los casos en un mapa")
    print("5.- Exportar caso de algun paciente")
    print("6.- Mostrar la cantidad de casos por Signo")
    print("7.- Salir ")
    playsound("sonidos/opcion valida.wav")
    opcion = input("Digite una opcion valida: ")



    if opcion == "1":
        limpiar()
        print("Vamos a agregar un  Caso")
        playsound("sonidos/agregar.wav")
        cedulas()
        print("Paciente agregado exitosamente!")
        playsound("sonidos/agrego.wav")
        alerta()
        input("Presione ENTER para volver al menu: ")
        playsound("sonidos/menu.wav")
        menu()

    elif opcion == "2":
        limpiar()
        print("Vamos a mostrar los Casos de coronavirus")
        playsound("sonidos/mostrar.wav")
        mostrar()
        input("Presione ENTER para volver al menu: ")
        playsound("sonidos/menu.wav")
        menu()

    elif opcion == "3":
        limpiar()
        print("Vamos a editar un caso de algun paciente: ")
        playsound("sonidos/editar.wav")
        editar()

    elif opcion == "4":
        limpiar()
        exportar()
        print("Todos los Casos se han exportado!! ")
        playsound("sonidos/exporta.wav")
        input("Presione ENTER para volver al menu: ")
        playsound("sonidos/menu.wav")
        menu()

    elif opcion == "5":
        print("Vamos a exportar un caso de algun paciente")
        playsound("sonidos/exportas.wav")
        exportar_un_caso()

    elif opcion== "6":
        print("Estadistica Misteriosa")
        playsound("sonidos/misterio.wav")
        estadistica()
        input("Presione ENTER para volver al menu:")
        playsound("sonidos/menu.wav")
        menu()

    elif opcion== "7":
        print("Gracias por tu tiempo")
        playsound("sonidos/tiempo.wav")

    else:
        playsound("sonidos/opcion invalida.wav")
        print("Digite una opcion valida!!")
        input("Preseione ENTER para volver al menu: ")
        menu()



menu()
