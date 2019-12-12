import mysql.connector
import  tkinter as tk
from tkinter import ttk
import pandas as pd
from winsound import *
import winsound
import numpy as np

def cargar():
    dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'root',
        'database':'zelda'
    }

    conexion = mysql.connector.connect(**dbConnect)

    cursor = conexion.cursor()

    sql = "select * from weapon"

    cursor.execute(sql)

    resultados = cursor.fetchall()

    #print (resultados)
    """
    raiz= tk.Tk()
    imagen=tk.PhotoImage(file=str(resultados[0][6]))
    raiz.title('Simón')
    b = tk.Button(raiz, height=imagen.height(), width=imagen.width(), image=imagen, border=10, bg="black")
    b.pack()
    raiz.mainloop()

    """


    """for datos in resultados:
        print(str(datos[0])+" "+str(datos[1]))"""
    return resultados



def armar():
    actual=[]
    persona=[]
    lista=[]
    musica=["m1.wav","m2.wav","m3.wav"]
    p=lambda: PlaySound("music/"+musica[np.random.randint(0,2)], winsound.SND_ASYNC)
    p()
    usuarios=[]
    def guardar():
        with open('usuarios.txt', 'w') as f:
            for usuario in usuarios:
                f.write(usuario[0]+"\t")
                f.write(usuario[1] + "\t")
                f.write(usuario[2] + "\t")
                contador=0
                for dato in usuario[3]:
                    contador=contador+1
                    if (contador!=len(usuario[3])):
                        f.write(dato + ";")
                    else:
                        f.write(dato + "\n")



    def leer():
        with open('usuarios.txt', 'r') as f:
            todo=f.readlines()
            for dato in todo:
                dato = dato.strip('\n')
                no_tupla=(dato.split("\t"))
                no_tupla[3] = no_tupla[3].split((";"))
                usuarios.append(no_tupla)
            #print (usuarios)

    leer()
    #guardar()
    resultados=cargar()

    df = pd.DataFrame(resultados, columns=['Nombre', 'Tipo', 'Poder de ataque', "Durabilidad", "Imagen"])
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[0] + 1)

    """for data in df["Imagen"]:
        imagen = tk.PhotoImage(file=str(data))
        print (imagen)
    """
    raiz = tk.Tk()
    raiz.title("Zelda: compra")
    background_image = tk.PhotoImage(file="images/bg.png")
    background_label = tk.Label(raiz, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # raiz.geometry('2000x1000')
    RWidth = raiz.winfo_screenwidth()
    RHeight = raiz.winfo_screenheight()
    raiz.geometry(("%dx%d") % (RWidth, RHeight))
    #print (df
    w=tk.Label(raiz)
    w.place(x=500, y=300, width=500)
    v = tk.Label(raiz)
    v.place(x=680, y=400)
    correo= tk.Label(raiz,  text="Correo:")
    correo.place(x=1650, y=100)
    ingresa_correo = tk.Text(raiz, height=1, width=20)
    ingresa_correo.place(x=1650, y=150)
    clave = tk.Label(raiz, text="Clave:")
    clave.place(x=1650, y=300)
    ingresa_clave = tk.Text(raiz, height=1, width=20)
    ingresa_clave.place(x=1650, y=350)

    def compra():
        print (persona)
        print (lista)
        """if (persona!=[])&(lista!=[]):
            persona[0][3].append(lista[0])
            print (persona[0][3])"""

        #global persona
        #persona=persona.append("persona")
        #print(persona)

    comprar=tk.Button(raiz, bg="Green", border=10, command=compra, text="Comprar")
    comprar.place(relx=0.9, rely=0.38)
    #global actual


    def seleccionar_arma():
        #global lista
        valor=combo_armas.get()
        if (valor!=-1):
            accion(valor)

    def seleccionar_escudo():
        valor = combo_escudos.get()
        if (valor != -1):
            accion(valor)

    def seleccionar_arco():
        valor = combo_arcos.get()
        if (valor != -1):
            accion(valor)

    def seleccionar_flecha():
        valor = combo_flechas.get()
        if (valor != -1):
            accion(valor)

    def delete():
        w.destroy()
        v.destroy()

    def accion(valor):
        global actual
        global lista
        #delete()

        #raiz.update()
        #print (actual)
        actual=df.loc[(df["Nombre"]==valor)]
        lista_aux=list(actual.apply(lambda x: x.tolist(), axis=1))
        lista=lista_aux[0]
        lista.append(str(lista[2]*lista[3]))

        imagen = tk.PhotoImage(file=lista[4])
        w.configure(text="Nombre: "+lista[0]+" \n"
                                "Tipo: "+lista[1]+"\n"
                                "Poder de ataque: "+str(lista[2])+" \n"
                                "Duración: "+str(lista[3])+" \n"
                                 "Precio: "+ str(lista[5])+" rupias")
        #w.place(x=500,y=300, width=500)
        v.configure(image=imagen)
        #v.place(x=500, y=400)
        v.photo = imagen
        raiz.update()

        #print(lista)

    lista_armas= list(df.loc[(df["Tipo"]!="Shield")&(df["Tipo"]!="Arrow")&(df["Tipo"]!="Bow"), "Nombre"])
    #print (lista_armas)
    lista_escudos = list(df.loc[(df["Tipo"] == "Shield"), "Nombre"])
    #print(lista_escudos)
    lista_arcos = list(df.loc[(df["Tipo"] == "Bow"), "Nombre"])
    #print(lista_arcos)
    lista_flechas = list(df.loc[(df["Tipo"] == "Arrow"), "Nombre"])
    #print(lista_flechas)




    armas= tk.Label(text="Armas")
    armas.place(x=50, y=30)
    combo_armas = ttk.Combobox(raiz, state="readonly")
    combo_armas["values"] = lista_armas
    combo_armas.place(x=50, y=50, width=300)
    b_armas = tk.Button(raiz, bg="Green", border=10, text="Seleccionar arma", command= seleccionar_arma)
    b_armas.place( relx=0.1, rely=0.08)

    escudo = tk.Label(text="Escudos")
    escudo.place(x=400, y=30)
    combo_escudos = ttk.Combobox(raiz, state="readonly")
    combo_escudos["values"] = lista_escudos
    combo_escudos.place(x=400, y=50, width=300)
    b_escudos = tk.Button(raiz, bg="Green", border=10, text="Seleccionar escudo", command= seleccionar_escudo)
    b_escudos.place(relx=0.3, rely=0.08)

    arcos = tk.Label(text="Arcos")
    arcos.place(x=750, y=30)
    combo_arcos = ttk.Combobox(raiz, state="readonly")
    combo_arcos["values"] = lista_arcos
    combo_arcos.place(x=750, y=50, width=300)
    b_arco = tk.Button(raiz, bg="Green", border=10, text="Seleccionar arco", command= seleccionar_arco)
    b_arco.place(relx=0.5, rely=0.08)

    flechas = tk.Label(text="Flechas")
    flechas.place(x=1100, y=30)
    combo_flechas = ttk.Combobox(raiz, state="readonly")
    combo_flechas["values"] = lista_flechas
    combo_flechas.place(x=1100, y=50, width=300)
    b_flecha = tk.Button(raiz, bg="Green", border=10, text="Seleccionar flecha", command= seleccionar_flecha)
    b_flecha.place(relx=0.7, rely=0.08)

    persona_loggeada = tk.Label(text="Usuario:")
    persona_loggeada.place(x=1650, y=500)
    info = tk.Label(text="Compras:")
    info.place(x=1650, y=600)
    combo_persona = ttk.Combobox(raiz, state="readonly")
    combo_persona.place(x=1550, y=650, width=300)

    def entrar():

        [persona.append(x) for x in usuarios if (x[0]==str(ingresa_correo.get("1.0",tk.END)).strip('\n')) & (x[1]==str(ingresa_clave.get("1.0",tk.END)).strip('\n'))]
        #print(persona)
        if persona!=[]:
            persona_loggeada.configure(text="Usuario: "+ str(persona[0][0]))
            combo_persona["values"]=persona[0][3]

        raiz.update()


    log_in=tk.Button(raiz, bg="Green", border=10, text="Entrar", command= entrar)
    log_in.place(relx=0.85, rely=0.38)


    raiz.mainloop()






if __name__=="__main__":
    armar()




