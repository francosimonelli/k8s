# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación Flask al contenedor
COPY ./app /app

# Instala las dependencias de la aplicación (como mysql-connector)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expone el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Define el comando por defecto para iniciar la aplicación Flask
CMD ["python", "app.py"]

