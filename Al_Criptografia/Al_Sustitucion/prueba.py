def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter) - ord('a')
            codigo = (codigo + desplazamiento) % 26
            caracter_cifrado = chr(codigo + ord('a'))
            
            if mayuscula:
                caracter_cifrado = caracter_cifrado.upper()
            
            resultado += caracter_cifrado
        else:
            resultado += caracter
    
    return resultado
