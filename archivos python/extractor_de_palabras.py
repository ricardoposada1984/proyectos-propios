
texto = input("Escribe acá el texto a analizar: ")
palabra = input("Escribe acá la palabra que quieres encontrar dentro del texto: ")

inicio = 0
final = 0

def extractor(texto, palabra):

    for i in range(len(texto)):
        if texto[i] == palabra[0] and texto[i+len(palabra)-1] == palabra[-1]:
           inicio = i
           final = i+len(palabra)-1
         
    return texto[inicio:final+1]           
    
print(extractor(texto, palabra))    