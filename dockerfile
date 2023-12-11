# Utiliza la imagen base de apache en la versión 2.4.12.
FROM httpd:2.4.12

# Copia los archivos del proyecto a la ruta especificada.
COPY . /usr/local/apache2/htdocs/

# Expone el puerto de conexión para el servicio de apache.
EXPOSE 80 

# Inicia el servicio httpd con argumentos -D FOREGROUND
CMD [ "httpd", "-D", "FOREGROUND"]