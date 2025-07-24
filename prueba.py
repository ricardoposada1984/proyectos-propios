# estoy probando si me siento comodo con esta
# posición del teclado

# espero quie si , porque sino

# voy a tener que acambair de escritorio
# parece que encontré una posición que puedo estar
# un rato, la probare un poco mas antes de cambiar de escritorio

x = [i for i in range(21)]
y = []

for i in x:
    if i%2 == 0:
        y.append(i)
    
print(y) 
print(x)  

# detector de sarcasmo
# como programarlo?


# vamos a ver como trabajo si solo cambio de posicion
# el teclado, parece aue funciona :)
# osea que solo debo desconectar el teclado o
# comprar uno inalambrico :)

# hola como estas tu
# hola como estas tu ! :)

def mensaje(a,b,c,d):
    
    if a*b < 10:
       mensaje1 = 'buena'
    else:
        mensaje1 = 'mal'       
    if  a+c-d > 5:
        mensaje2 = 'correctamente'  
    else :
        mensaje2 = 'pendiente de confirmacion'
        
    return f' Su tramite ha sido enviado {mensaje2} su resultado es {mensaje1}'
             
print(mensaje(0,1,2,15))  
           
print("Estoy cambiando de posicion para programar")




