#fuentes:   https://wizardprogrammer.blogspot.com/2019/03/convertir-imagen-blanco-y-negro-python.html
#           https://numpy.org/doc/stable/reference/generated/numpy.matrix.transpose.html
#           https://numpy.org/doc/stable/reference/generated/numpy.matrix.html

from PIL import Image
import numpy as np

#dire es la dirección donde está guradada la imagen dice marco
def lec_img(dire):

    IMG = []
    X = []
    Y = []
    Z = []

    #Abrimos la Imagen
    # lo malo es que tengo que indicar la dirección exacta, no se porqué, se supone que no debe ser así.
    im = Image.open(dire)

    #Obtenemos sus dimensiones
    x = im.size[0]
    y = im.size[1]

    for i in range(y):
        aux = []
        for j in range(x):

            #Obtenemos el valor RGB de cada pixel
            r, g, b = im.getpixel((j,i))

            #Obtenemos su equivalente en la escala de gris
            p = (r * 0.3 + g * 0.59 + b * 0.11)

            #guardamos
            X.append(j)
            Y.append(i)
            Z.append(p)
            aux.append(p)
        
        IMG.append(aux)

    #convierto los arrays a como los quería el andrés
    X = np.array(X , np.int32)
    Y = np.array(Y , np.int32)
    Z = np.array(Z , np.double)

    #regreso los datos que quería
    return (X,Y,Z,x,y,IMG)