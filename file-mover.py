# Mover archivos de descargas a su carpeta respectiva

from PIL import Image;
# Importar OS para poder leer los archivos que se encuentra en nuestra carpeta de descargas
import os

# definimos la carpeta a la cual nosotros vamos a buscar los archivos

# TODO: Colocar la ruta de Downloads, segun su usuario
downloadsFolder = "C:/Users/User/Downloads/"

# TODO: Colocar la ruta de Pictures, segun su usuario
picturesFolder = "C:/Users/User/Pictures/"

# Continuamos preguntando si es que el archivo que estamos buscando lo estamos ejecutando directamente nosotrs desde la terminal

if __name__ == "__main__":
    # luego iteramos todos los archivos que se encuentra dentro de la carpeta (descargas) y le asignamos el nombre "filename"
    for filename in os.listdir(downloadsFolder):
        # a continuacion tomamos el nombre del archivo y luego lo separamos entre archivo y su extensión
        name, extension = os.path.splitext(downloadsFolder + filename)
        # preguntamos si es que su extensión se encuentra dentro de .jpg .jpeg o png. en el caso de que sea así significa que estamos trabajando con un archivo de imagen
        if extension in ['.jpg', '.jpeg' , '.png']:
            # ahora, abrimos esta imagen pero esto no significa que la abre como tal, pero si permite trabajar con ella en el codigo
            picture = Image.open(downloadsFolder + filename);
            # a continuación lo que hacemos es guardarla en la misma carpeta pero agragamos al comienzo "compressed_" luego le pasamos la propiedad "optimize" en true e indicamos la calidad que queremos que tenga esta imagen
            # * le dejamos la calidad en 60 porque se cree que no se sacrifica tanto una imagen cuando la dejamos solamente en 60
            picture.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60);
            
            # Eliminar los archivos que se encuentran dentro de la carpeta de descargas
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in ['.mp3']:
            musicFolder = "C:/Users/User/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)