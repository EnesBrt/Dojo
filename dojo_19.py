the_input = 1

def flippingBits(n):
    binaire = bin(n)[2:]
    binaire_32_bits = binaire.zfill(32)
    
    chaine = str(binaire_32_bits)
    
    liste = [int(char) for char in chaine]
    
    for n in range(len(liste)):
        if liste[n] == 0:
            liste[n] = 1
        elif liste[n] == 1:
            liste[n] = 0
            
    nombre_concatene = ''.join(map(str, liste))
    
    nombre_entier = int(nombre_concatene, 2)
    
    return nombre_entier
    
print(flippingBits(the_input))