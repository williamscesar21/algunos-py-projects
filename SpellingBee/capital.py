import os

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Lista de letras del abecedario
directorio = "archivos_abecedario"  # Directorio donde se guardarán los archivos

# Crea un directorio si no existe
os.makedirs(directorio, exist_ok=True)

# Crear un archivo para cada letra del abecedario
for letra in abecedario:
    palabra = f"Capital {letra}"
    nombre_archivo = os.path.join(directorio, f"{palabra}.txt")
    
    # Guardar la palabra completa en un archivo TXT
    with open(nombre_archivo, "w") as archivo:
        archivo.write(palabra)

    # Comprobar que los archivos se crearon correctamente
    if os.path.exists(nombre_archivo):
        print(f"El archivo '{palabra}.txt' se creó correctamente en '{directorio}'.")

print("Archivos de texto generados satisfactoriamente.")
