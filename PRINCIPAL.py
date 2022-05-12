#_____________________________________________________________________________________________
#           INICIO LECTURA DE IMAGEN

#Biblioteca nuestra
import lectura_img_mk2

'''
   EXPLICACIÓN FUNCIONES: en esencia lee toda la imagen que queremos analizar, sea recortada o no.
 cambio pa ver qpd con esto
   x,y: son las coordenadas de los pixeles, por ejemplo para el pixel cero esquina superior izquierda serian x[0]y[0], para el pixel uno
       que seguiría del cero para la derecha, osea todavía equina superior izquirda pero un pixel a la derecha, sería x[1]y[1], y así
       sucesivamente. La coordenada x[i]y[i] pertenece al pixel i. Son arreglos de numpy
   z: es un arreglo de numpy que contiene las intensidades de los pixeles i
   l: es la longitud de la imagen pero en pixeles
   h: es la altura de la imagen pero en pixeles
   dire: es la dirección donde encontramos la imagen sea recortada o no.
'''

#IMAGENES que uso
#dire = r'C:\Users\marco\OneDrive\Escritorio\Ingenieria_fisica\Sistemas_de_la_instrumentacion\proyecto\imagenes\img37.jpg'
#dire = r'C:\Users\marco\OneDrive\Escritorio\Ingenieria_fisica\Sistemas_de_la_instrumentacion\proyecto\imagenes\img38.2.jpg'
#Imagenes que se leen en la misma carpeta, sin depender de otras direcciones que solo funcionan para la computadora deseada
dire = r'Imagen_prueba.jpg'
'''Lectura de la imagen en el directorio y así a lo bastardo toda la imagen'''
X , Y , Z, l, h, M = lectura_img_mk2.lec_img(dire)
# M es una matriz que representa a la imagen

#           FINAL LECTURA DE IMAGEN
#__________________________________________________________________________________________________________________






#__________________________________________________________________________________________________________________
#               INICIO GURDADO DE LOS DATOS EN UN ARCHIVO CSV

import numpy as np

#Este es para guardar todo
#DATOS = [x,y,z]
#np.savetxt(r"C:\Users\marco\OneDrive\Escritorio\Ingenieria_fisica\Sistemas_de_la_instrumentacion\proyecto\programa\datos.csv", DATOS, delimiter=",")

#Este solo guarda los datos de intensidad
np.savetxt(r"C:\Users\marco\OneDrive\Escritorio\Ingenieria_fisica\Sistemas_de_la_instrumentacion\proyecto\programa_1\datos.csv", Z, delimiter=",")
#La dirección dada es donde queremos que lo guarde lo ideal sería que fuera iguala la variable 'dire' para evitar tanto texto pero por ahora lo
#   dejamos así.
#   np.savetxt(dirección donde queremos guardar el csv, arreglo de numpy que queremos guardar, el delimitador de los datos)

#MEJORA: Además sería bueno hallar la forma de guardarlo en una USB

#               FINAL GURDADO DE LOS DATOS EN UN ARCHIVO CSV
#__________________________________________________________________________________________________________________







#___________________________________________________________________________________________________________________
#           INICIA EL PROGRAMA QUE HARÁ LA MODELACIÓN DE KRIGGING



#Biblioteca nuestra donde aplicamos el método
import metodo_krig

#metodo_krig.krigging( X , Y , Z , l , h)


if l < h:
    h = l
elif l > h:
    l = h

d = 40

N = (l//d)**2  #Divido mi imagen de lxl en trozos de 40x40

x = np.zeros(d**2)
y = np.zeros(d**2)
z = np.zeros(d**2)
#Funcion para comprobar que esta sucediendo con Z, que es lo importante
Z_gridata = 0
for k in range(N):
    for i in range(d*k,d + d*k):
        for j in range(d*k,d + d*k):
            x[i+j] = j
            y[i+j] = i
            z[i+j] = M[i][j]

    Z = metodo_krig.krigging( x , y , z , l , l)




#                        FINAL PROGRAMA MODELADO DE KRIGGING
#___________________________________________________________________________________________________________________