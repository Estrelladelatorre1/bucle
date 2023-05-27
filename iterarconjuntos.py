cadena= 'HOLA'
numeros=[2,5,8]
frutas=('manzana','ceresa','platano')
#evitando una 
for fruta in frutas:
    if fruta== "manzana":
        continue
    print(f"me voy a comer una {fruta}")
print('............')
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta== "ceresa":
        break
    print("termine")
   
 #RECURER UNA CADENA     
for letra in cadena:
    print( letra)
 #For en una sola lisata 1.1
##for numero in numeros:
   # numeros_duplicados.append(numero*2)
    #print(numeros_duplicados)

#For en una sola lisata 1.2

numeros_duplicados = [x/2 for x in numeros]
print(numeros_duplicados)
    

    
    
    
    
    