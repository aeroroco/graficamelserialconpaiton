# Test b hasta antes de ser modificado
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import serial



def CreacionDelGrafico(X,Y,  El_Titulo, El_EjeX,  El_EjeY, Lim_X, Lim_Y): 
	# Creacion del grafico 
	fig, ax = plt.subplots()

	#datos = np.random.randn(100)
	#X = np.linspace(0, 2*math.pi, 100 ) 
	 
	line, = ax.plot(X,X)

	# -------------------------------------------------------------
	# 	Seteo de propiedades del grafico que no cambian
	# -------------------------------------------------------------
	#
	# Texto de Mierda que va al Grafico
	#
	ax.set_title(El_Titulo)
	ax.set_xlabel(El_EjeX)
	ax.set_ylabel(El_EjeY)
	# Seteo de limites del grafico 
	ax.set_xlim(Lim_X)
	ax.set_ylim(Lim_Y)
	return fig, ax, line

def ActualizateElGrafico(Y):
	line.set_ydata( Y ) 	#  Carga datos 
	fig.canvas.draw() 					#  Dibuja
	fig.canvas.flush_events()				#  Enjuaga	
	return line, fig


# ------------------------------------------
# Creacion de los puntos del grafico inicial
# ------------------------------------------
Xinicial  = 0
Xfinal    = 10
Npuntos_X = 10
# 
X = np.linspace(Xinicial, Xfinal , Npuntos_X )  # Puntos del eje X
Y = X						# Puntos del eje Y	
#
El_Titulo = 'Titulo de Mierda'
El_EjeX  = 'Eje equis x'
El_EjeY  =' Eje Y de mierda'
Lim_X = [0, 10]
Lim_Y = [0, 256]





fig, ax, line = CreacionDelGrafico( X, Y,  El_Titulo, El_EjeX,  El_EjeY, Lim_X, Lim_Y)


plt.pause(1)
tstart = time.time()
num_plots = 0




ser = serial.Serial('/dev/ttyACM0', 9600, timeout=None)

# while time.time()-tstart < 10:
# 	line,fig = ActualizateElGrafico( np.sin( X + math.pi/(10)*num_plots ) )
# 	num_plots += 1
# print(num_plots)
lastCoordY = None

Y=[]
counter=0
while 1:
	try:
            a = ser.readline()      # Lee el string que sale el puerto serial
            print(a)     
            #line, fig = ActualizateElGrafico(int(a))
            if ( counter < 10 ) :
                Y.append(int(a))
                print Y,a
                counter+=1
                if ( len(Y) == 10 ) :
                    line, fig = ActualizateElGrafico(Y)
		    ser.flushOutput()
                    counter = 0     
                    Y=[]
        

	except serial.serialutil.SerialException:
        	print "Data could not be read"
