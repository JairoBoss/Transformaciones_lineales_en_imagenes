import numpy as np
import cv2
import matplotlib.pyplot as plt

#transformaciones lineales a imagenes

class transformaciones:

    def __init__(self, path : str) -> None:
        self.imagen = cv2.imread(path)
        
    def traslacion(self, ejeX : int, ejeY : int):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB) #Convertir de BGR a RGB para que podamos trazar usando matplotlib
        plt.axis('off') #Dsabilitar que se muestre coordenadas y ejes
        
        #Mostrar Imagen
        plt.imshow(self.imagen) 
        plt.show()

        #El metodo shape nos devuelve una tupla y con las dimenciones de la imagen y asignamos los valores
        filas, columnas, dim = self.imagen.shape
        
        #Matriz para la traslacion
        MATRIZTRANSLACION = np.float32([[1, 0, ejeX],
                                        [0, 1, ejeY]])
        
        #Aplicamos ese metodo que hace la transformacion
        imagenTranslacion = cv2.warpAffine(self.imagen, MATRIZTRANSLACION, (columnas, filas))
        
        #Quitramos los ejes y mostramos la imagen
        plt.axis('off')
        plt.imshow(imagenTranslacion)
        plt.show()
        #Guardamos la imagen
        plt.imsave("output\Traslación.jpg", imagenTranslacion)

    def rotacion(self, grados : int):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)
        plt.axis('off')
        
        plt.imshow(self.imagen) 
        plt.show()

        filas, columnas, dim = self.imagen.shape
        #rotacion con respecto a esas coordeadas osea a la mitad
        Cx = filas/2
        Cy = columnas/2
        angulo = np.radians(grados)

        MATRIZROTACION = np.float32([[ np.cos(angulo), np.sin(angulo), Cx - Cx * np.cos(angulo) - Cy*np.sin(angulo)],
                                     [-np.sin(angulo), np.cos(angulo), Cy + Cx * np.sin(angulo) - Cy*np.cos(angulo)]])
        
        imagenRotada = cv2.warpAffine(self.imagen, MATRIZROTACION, (columnas, filas))

        plt.axis('off')
        plt.imshow(imagenRotada)
        plt.show()
        
        plt.imsave("output\Rotada.jpg", imagenRotada)
    
    def escalado(self, ejeX : float, ejeY : float):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)
        plt.axis('off')
        
        plt.imshow(self.imagen) 
        plt.show()

        filas, columnas, dim = self.imagen.shape
        
        MATRIZESCALADO = np.float32([[ejeX, 0, 0],
                                     [0, ejeY, 0]])
                
        imagenEscalado = cv2.warpAffine(self.imagen, MATRIZESCALADO, (columnas, filas))
        
        #Quitramos los ejes y mostramos la imagen
        plt.axis('off')
        plt.imshow(imagenEscalado)
        plt.show()
        #Guardamos la imagen
        plt.imsave("output\Escalado.jpg", imagenEscalado)

    def deformacion(self, ejeX : float, ejeY : float):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)
        #plt.axis('off')
        
        plt.imshow(self.imagen) 
        plt.show()

        filas, columnas, dim = self.imagen.shape
        
        MATRIZDEFORMACION = np.float32([[1, -ejeX, 0],
                                        [-ejeY, 1, 0]])
                
        imagenEscalado = cv2.warpAffine(self.imagen, MATRIZDEFORMACION, (columnas, filas))
        
        #Quitramos los ejes y mostramos la imagen
        plt.axis('off')
        plt.imshow(imagenEscalado)
        plt.show()
        #Guardamos la imagen
        plt.imsave("output\Deformacion.jpg", imagenEscalado)