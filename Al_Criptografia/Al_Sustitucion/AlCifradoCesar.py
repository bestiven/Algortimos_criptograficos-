def cifrado_cesar(texto, clave):
    texto_encriptado = ""
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo_ascii = ord(caracter)
            codigo_ascii = ((codigo_ascii - 97 + clave) % 26) + 97
            if mayuscula:
                caracter = chr(codigo_ascii).upper()
            else:
                caracter = chr(codigo_ascii)
        texto_encriptado += caracter
    return texto_encriptado

# Ejemplo de uso:
texto_original = "la"
clave = 5
texto_encriptado = cifrado_cesar(texto_original, clave)

print("Texto Original:", texto_original)
print("Texto Encriptado:", texto_encriptado)
