from os import walk, getcwd
from os import listdir
import os

def ls_method(ruta = getcwd()):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        listaarchivos.extend(archivos)
        print(listaarchivos)
    return listaarchivos

ls_method()    

