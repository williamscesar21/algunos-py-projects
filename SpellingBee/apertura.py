import os

palabras = ["pet", "sky", "toy", "eye", "boot", "dot", "hen", "May", "say", "way", "draw", "have", "June", "make", "sure"]


# Crear un archivo para cada palabra
for palabra in palabras:
    # Guardar la palabra completa en un archivo TXT
    with open(f"{palabra}.txt", "w") as archivo:
        archivo.write(f"{palabra}")  # Escribe la palabra completa

# Comprobar que los archivos se crearon correctamente
for palabra in palabras:
    if os.path.exists(f"{palabra}.txt"):
        print(f"El archivo '{palabra}.txt' se creó correctamente.")