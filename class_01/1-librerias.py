from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola yo deberia estar en camelcase'

resultado = instancia.hump(texto)

print(resultado)