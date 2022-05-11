#Estas son las bibliotecas que usaremos para la interpolación de Kriging
from pykrige.ok import OrdinaryKriging

#Bibliotecas usadas para la segunda interpolacion
from scipy.interpolate import griddata
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def krigging(x,y,z,l,h):
    
    #Rango de Interpolación en (x,y)
    natudo = 40  #Esta variable es la responsable del rango de interpolación
                #Es necesario cambiarla según la cantidad de pixeles en la imagen leida

    gridx = np.arange(0.0, l, 1)
    gridy = np.arange(0.0, h, 1)
    
    
    #Aquí se lleva acabo el método de Kriging Ordinario, se reciben los datos x,y,z y se elige
    #el modelo del variograma, ademas de que se puede poner <False> en el enable_plotting  en lugar
    #de <True> para no mostrar el variograma cada vez que se corra el programa
    OK = OrdinaryKriging(   #Aquí empiezan los problemas
        x,
        y,
        z,
        variogram_model="gaussian",
        verbose=False,
        enable_plotting=False,
    )
    
    
    #No cambiar, ya que si no no funciona el método de Kriging
    z, ss = OK.execute("grid", gridx, gridy)

    
    zf = np.zeros(l*h, np.double) #Se cambiaron los limites a esa multiplicacion porque cambio
    yf = np.zeros(l*h, np.int32)  #El limite de la imagen cuando se recorto
    xf = np.zeros(l*h, np.int32)

    
    zf = np.concatenate(z.data.T)[:(natudo**2)] #Se guardan los datos Z interpolados, ya no son las intensidades de la imagen
    
    taco = 0
    for i in range(0, l):     #Se cambiaron los limites a esa multiplicacion porque cambio
        for j in range(0,h):  #El limite de la imagen cuando se recorto
            xf[taco] = i
            yf[taco] = j
            taco+=1
    
    #Aquí creo que es natudo porque antes tenía que era 40 - d pero al deshacerme de d la hice cero entonces solo queda 40
    zf = np.concatenate(z.data.T)[:(natudo*natudo)] #Se guardan los datos Z interpolados, ya no son las intensidades de la imagen
    
    # construcción de la grilla 2D
    xi = np.linspace(min(xf), max(xf))

    yi = np.linspace(min(yf), max(yf))
    X, Y = np.meshgrid(xi, yi)
    
    # interpolación para que se vea como una superficie los datos interpolados
    # ya que al hacerlo con Kriging es una interpolación de datos discretos no continuos
    # esta interpolacion toma esos datos y los vuelve continuos

    Z = griddata((xf, yf), zf, (xi[None,:], yi[:,None]), method='linear')
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=1, antialiased=True)
    plt.plot
    plt.show()
    
    return()