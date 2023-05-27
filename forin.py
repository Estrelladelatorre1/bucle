animales= ['gato','perro','loro','cocodrilo']
numeros= [52,16,14,72]
#Recoriendo la lista animales 
for animal in animales:
 print('Ahorala veriables es:' ,[animal])
 
for numero in numeros:
    resultado= numero *10
    print(resultado)
 
#cuenta
for num in range(5,58):
 print(num)

#recorer lista 
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f"Indice={indice} y el valor es: {valor}")
 #else   
for numero in numeros:
 print(f'Bucle actual:{numero}')
else:
    print('El bicle termino')
