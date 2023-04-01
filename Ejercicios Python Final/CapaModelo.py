######### EjercicioS Finales 1,2,3 SANDRA CARRERA ABILA
import pandas as pd
import sqlite3

ruta="C:\\Users\\SANDRA\\Desktop\\PythonWorkSpace\\Clase 5\\Ejercicios Python Final\\LIM.csv"
df = pd.read_csv(ruta, sep = ';')
col = df[["Provincia","Ingreso"]]
lista_valores = df.values.tolist()
con = sqlite3.connect('demo.db')
cur = con.cursor()

def mostrar_provincia():
    print(df.sort_values(by='Ingreso'))
""" mostrar_provincia() """

def provincia_especifica():
    provincia = input("Ingrese nombre de provincia: ")
    df2 = df[df['Provincia'] == provincia]
    print(df2)
""" provincia_especifica() """

def db_tabla():
    con = sqlite3.connect('prov_lima.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Lima (Provincia, Ingreso);")
    cur.executemany("INSERT INTO Lima VALUES (?, ?);", lista_valores)
    con.commit()
""" db_tabla() """

def mostrar_tabla():
    datos = cur.execute("SELECT * FROM Lima").fetchall()
    print(datos)
""" mostrar_tabla() """

def agregar_nuevo():
    nomprov = input("Ingrese nombre de nueva provincia: ")
    ingprov = int(input("Ingrese el ingreso de esa provincia: "))
    cur.execute("INSERT INTO Lima values(?,?)",(nomprov,ingprov))
    print("Nueva provincia")
    con.commit()
""" agregar_nuevo() """

def salida():
    print("Hasta Luego ")
""" salida() """
    

