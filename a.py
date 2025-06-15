import re  # Importamos el módulo de expresiones regulares


def validar_texto(texto):
    
#inciso inciso a
    fechas_cortas = re.findall(r'\b\d{2}-\d{2}-\d{2}\b', texto)

    fechas_largas = re.findall(
        r'\b(?:lunes|martes|miércoles|jueves|viernes|sábado|domingo), \d{2} de (?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}\b',
        texto,
        re.IGNORECASE)

    if fechas_cortas:
        print(" Fechas en formato corto encontradas:", fechas_cortas)
    else:
        print(" No se encontraron fechas en formato corto.")

    if fechas_largas:
        print(" Fechas en formato largo encontradas:", fechas_largas)
    else:
        print(" No se encontraron fechas en formato largo.")
#fin inciso a

texto_de_prueba = """
Hoy es sábado, 15 de junio de 2024. También tenemos una fecha abreviada: 24-06-15. Y otra larga: lunes, 03 de marzo de 2025.
"""
validar_texto(texto_de_prueba)

#inicio inciso b

textoB = "El Perro del vecino duerme en el jardín. Mi perro duerme en mi cuarto."

# Reemplaza "perro" por "gato" sin importar si son mayúsculas
resultado = re.sub(r"\bperro\b", "gato", textoB, flags=re.IGNORECASE)

print("Texto original:", textoB)
print("Texto modificado:", resultado)

#fin inciso b


#### Inciso D, validacion de usuarios
def validar_usuario(nombre_usuario):
    patron = r'^[a-zA-Z0-9_-]{8,12}$'
    if re.fullmatch(patron, nombre_usuario):
        return True
    else:
        return False

#Ejemplos
usuarios = [
    "usuario_01",     # válido
    "user-1234",      # válido
    "user!",          # inválido (carácter no permitido y menos de 8 caracteres)
    "us",             # inválido (muy corto, menos de 8 caracteres)
    "usuario_extralargo",  # inválido (muy largo, mas de 8 caracteres)
    "user_name-12"    # válido
]

#Prueba de usuarios
for u in usuarios:
    print(f"{u}: {'Válido' if validar_usuario(u) else 'Inválido'}")
####Fin de inciso d

#inicio inciso e

contrasenas = ["Clave123!", "insegura", "Segura2025", "P@ssword1", "Fuerte*2025"]

# Regex para validar contraseña segura
regex_segura = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"

for c in contrasenas:
    if re.fullmatch(regex_segura, c):
        print(f"Contraseña segura: {c}")
    else:
        print(f"Contraseña insegura: {c}")

#fin inciso e

