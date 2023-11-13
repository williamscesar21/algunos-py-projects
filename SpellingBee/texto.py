import os

palabras = ["hola"]

# Crear un archivo para cada palabra
for palabra in palabras:
    # Guardar la palabra completa y las letras de la palabra en un archivo TXT
    with open(f"{palabra}.txt", "w") as archivo:
        for letra in palabra:
            archivo.write(f"{letra}.\n")  # Escribe cada letra separada por líneas

# Comprobar que los archivos se crearon correctamente
for palabra in palabras:
    if os.path.exists(f"{palabra}.txt"):
        print(f"El archivo '{palabra}.txt' se creó correctamente.")
