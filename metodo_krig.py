#Estas son las bibliotecas que usaremos para la interpolación de Kriging o eso dicen
from pykrige.ok import OrdinaryKriging

#Bibliotecas usadas para la segunda interpolacion
from scipy.interpolate import griddata
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def krigging(x,y,z,l,h,m):
    
    #Rango de Interpolación en (x,y)
    natudo = 500  #Esta variable es la responsable del rango de interpolación
                #Es necesario cambiarla según la cantidad de pixeles en la imagen leida

    gridx = np.arange(0.0, natudo*m, 1*m)
    gridy = np.arange(0.0, natudo*m, 1*m)
    
    #Aquí se estarán desechando datos usados, para evitar que haya demasiados y que
    #kriging falle debido a un exceso de memoria utilizada
    
    #Creamos 3 variables (x_c,y_c,z_c) que nos permitan modificar la cantidad de datos de las originales
    #y luego las renombraremos como x,y,z eliminando las originales
    x_c = np.zeros(natudo)
    y_c = np.zeros(natudo)
    z_c = np.zeros(natudo)



  
    #En el siguiente for queremos que solo se guarden <una cantidad de puntos = nata>
    #los cuales estaran distanciados entre ellos, por algunas cuantas unidades
    
    cont__ = 0
    for patos in range(0,len(x)-1,int(len(x)/natudo)):
        x_c[cont__] = x[patos]
        y_c[cont__] = y[patos] 
        z_c[cont__] = z[patos]
        cont__ +=1
        
        

    x = x_c
    y = y_c
    z = z_c

    #Aquí se lleva acabo el método de Kriging Ordinario, se reciben los datos x,y,z y se elige
    #el modelo del variograma, ademas de que se puede poner <False> en el enable_plotting  en lugar
    #de <True> para no mostrar el variograma cada vez que se corra el programa
    OK = OrdinaryKriging(   #Aquí empiezan los problemas
        x,
        y,
        z,
        variogram_model="spherical",
        verbose=False,
        enable_plotting=True,
    )
    
    
    #No cambiar, ya que si no no funciona el método de Kriging
    z, ss = OK.execute("grid", gridx, gridy)

    

   

    #Se cambiaron los limites a esa multiplicacion porque cambio
    yf = np.zeros(natudo**2, np.int32)  #El limite de la imagen cuando se recorto
    xf = np.zeros(natudo**2, np.int32)
    
    
    zf = np.concatenate(z.data.T) #Se guardan los datos Z interpolados, ya no son las intensidades de la imagen
    
    
    taco = 0
    for i in range(0, natudo):     #Se cambiaron los limites a esa multiplicacion porque cambio
        for j in range(0,natudo):  #El limite de la imagen cuando se recorto
            xf[taco] = i*m
            yf[taco] = j*m
            taco+=1
    
    #Aquí creo que es natudo porque antes tenía que era 40 - d pero al deshacerme de d la hice cero entonces solo queda 40
    zf = np.concatenate(z.data.T)[:(natudo*natudo)] #Se guardan los datos Z interpolados, ya no son las intensidades de la imagen
    

    # construcción de la grilla 2D
    xi = np.linspace(min(gridx), max(gridx))

    yi = np.linspace(min(gridy), max(gridy))
    X, Y = np.meshgrid(xi, yi)
    
    # interpolación para que se vea como una superficie los datos interpolados
    # ya que al hacerlo con Kriging es una interpolación de datos discretos no continuos
    # esta interpolacion toma esos datos y los vuelve continuos
    print("gridx: ", len(gridx))
    print("gridy: ", len(gridy))
    print("zf: ", len(zf))
    
    print("x: ", len(x))
    print("yi: ",len(yi))
    Z = griddata((xf, yf), zf, (xi[None,:], yi[:,None]), method='linear')
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=1, antialiased=True)
    plt.plot
    plt.show()
    
    return()
