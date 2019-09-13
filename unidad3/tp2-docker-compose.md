## Universidad Austral de Chile

# INFO229: Arquitectura de software

### Responsable: Matthieu Vernier, mvernier@inf.uach.cl

## TP2: Introducción al despliegue de software con Docker-Compose

### 1. ¿Qué es Docker-Compose?

Docker-Compose es una herramienta para definir y ejecutar aplicaciones Docker **multicontenedores**. Con Docker-Compose, se utiliza un archivo [YAML](https://es.wikipedia.org/wiki/YAML) para configurar los servicios de la aplicación. Luego, con un solo comando, usted crea e inicia todos los servicios desde su configuración. 

El uso de Docker-Compose es básicamente un proceso de tres pasos:
- Se define el **entorno** de cada servicio con un _Dockerfile_ para que pueda ser reproducido en cualquier lugar.
- Se define los **servicios** que componen su aplicación en _docker-compose.yml__ para que puedan ejecutarse juntos en un entorno aislado.
- Se ejecuta docker-compose, para levantar la arquitectura con los distintos servicios.

### 2. ¿Cuál es la síntaxis del archivo docker-compose.yml?

Un archivo ``docker-compose.yml`` tiene la estructura siguiente. NB: El texto en negrita corresponde a la síntaxis de la versión actual de docker-compose. Todo el resto, son parámetros que se pueden cambiar.

```
**version:** '3.7'
**services:**
  web:
    **build:** .
    **ports:**
    **-** "5000:5001"
    **volumes:**
    **-** .:/code
    **-** logvolume01:/var/log
    **links:**
    - redis
  redis:
    **image:** redis
**volumes:**
  logvolume01: {}
```

- **version** corresponde a la versión del formato de archivo Docker-Compose que se utiliza (ver más detalles en la [documentación](https://docs.docker.com/compose/compose-file/)).
- **services** permite listar los distintos servicios de su arquitectura de software. Pueden observar que en la arquitectura ejemplo, existen 2 servicios llamados "web" y "redis".
- **volumes** permite específicar los repositorios o archivos del computador que estarán directamente asociados a los contenedores de nuestro software. Podemos montar varios volúmenes en un contenedor y en varios contenedores podemos montar un mismo volumen. Ver más detalles en la sección 4 - _¿Cómo Docker gestiona la persistencia de los datos?_

En la arquitectura ejemplo, tenemos 2 servicios conectados:
- **redis**: un servicio basado sobre el SGBD Redis. Para levantar el servicio, se utiliza la imagen oficial existente llamada "redis". Se instalará un contenedor integrando Redis con la configuración por defecto.
- **web**: es una aplicación que se construye (**build**) a partir de un archivo Dockerfile que se encuentra en la carpeta corriente (**.**). Dentro del contenedor, se podrá comunicar con la aplicación a partir de la puerta 5001 (**ports**). Desde a fuera del contenedor, se podrá comunicar con la aplicación con la puerta 5000. En la configuración, explicitamos que las dos puertas están vinculadas (HOST_PORT:CONTAINER_PORT). Finalmente, la aplicación necesitará utilizar dos volumenes, uno corresponde al código de la aplicación y el otro permitirá almacenar datos de _logs_.

Finalmente, se levanta la arquitectura con el comando ``docker-compose up`` (en cualquier máquina donde está instalado Docker).

### 3. ¿Cuál es la diferencia con el archivo Dockerfile?

Un Dockerfile es un archivo de texto que contiene una serie de instrucciones sobre cómo crear una imagen correspondiente a un servicio (es decir, 1 sólo contenedor). El Dockerfile está basado sobre un sencillo conjunto de comandos. Hay varios comandos soportados como por ejemplo: FROM, CMD, ENTRYPOINT, VOLUME, ENV y más.

El uso de Dockerfile sigue básicamente un proceso de tres pasos:

- Se crea localmente los archivos necesarios al funcionamiento del servicio (scripts, archivos de configuración, imagenes, etc.)
- Se crea un Dockerfile que explicita las instrucciones que ejecutar para levantar el servicio
- Se utilizar el comando ``Docker build`` para crear una imagen del servicio. NB: En caso de utilizar un archivo Docker-compose, el comando ``build`` se realiza al momento de desplegar la arquitectura con el comando ``docker-compose up``.


Una imagen Docker consiste en capas de sólo lectura. Cada instrucción Dockerfile representa una capa. Las capas están apiladas y cada una es un delta de los cambios de la capa anterior. Considere este archivo Dockerfile básico:

```
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

Cada instrucción crea una capa:

- FROM crea una capa a partir de la imagen ubuntu:18.04 Docker.
- COPY añade archivos del directorio actual de su cliente Docker.
- RUN construye su aplicación con make.
- CMD especifica qué comando ejecutar dentro del contenedor.

Cuando se ejecuta una imagen y se genera un contenedor, se añade una nueva capa de escritura (la "capa de contenedor") encima de las capas subyacentes. Todos los cambios realizados en el contenedor en ejecución, como la escritura de nuevos archivos, la modificación de archivos existentes y la eliminación de archivos, se escriben en esta delgada capa de contenedor con escritura.

**Crear contenedores efímeros**

La imagen definida por su Dockerfile debe generar contenedores que sean lo más efímeros posible. Por "efímero" entendemos que el contenedor puede ser detenido y destruido, luego reconstruido y reemplazado con un mínimo absoluto de instalación y configuración.

**Otros comandos del Dockerfile**

- EXPOSE: ej. "EXPOSE 80", permite abrir el puerto mencionado en la imagen del docker para permitir el acceso al mundo exterior.

- ENV: ej. "ENV HOME /root", permite definir variables de entorno. En el ejemplo hemos creado una variable HOME que se refiere a la ruta /root. La síntaxis es ``ENV key value``.

- WORKDIR: ej. "WORKDIR /home". Permite específicar a partir de qué carpeta trabajaba el contenedor.

- ENTRYPOINT: ENTRYPOINT y CMD permiten definir programas o comandos que ejecutar una vez que se levantó el contenedor.

- USER: Permite especificar que usuario del sistema debe realizar ciertos comandos.

Para ir más lejo:
- Buenas prácticas para construir un Dockerfile: [ejemplos de buenas prácticas](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/), [otros ejemplos](https://www.campusmvp.es/recursos/post/mejores-practicas-para-crear-dockerfiles-excelentes.aspx)
- Ver algunos problemas al momento de escribir un archivo Dockerfile: [ejemplos de malas prácticas](https://pythonspeed.com/articles/dockerizing-python-is-hard/)


### 4. ¿Cómo Docker gestiona la persistencia de los datos?

(por completar)

- [Docker: Volúmenes de Datos (Data Volumes)](https://moidev.com/posts/docker-volumenes-de-datos/)

### 5. Ejercicios prácticos básicos

5.1 Construir un archivo Docker-Compose para desplegar MySQL en un contenedor y un script python básico que se conecta a MySQL
5.2 Construir un archivo Docker-Compose para desplagar una aplicación Django (_o de su framework web favorito_)
5.3 Construir un archivo Docker-Compose para desplagar un sitio web Wordpress

### 6. Ejercicio de integración

Queremos crear una arquitectura de software llamada _Sophia2_ que permite recopilar noticias de medios de comunicación chilenos y mundiales. Queremos que la arquitectura sea facilmente despliegable, que se pueda hacer evolucionar y mantener. 

Para empezar queremos almacenar las noticias de unos primeros medios almacendando, idealmente, los tipos de datos siguientes:
- Texto de la noticia
- Título de la noticia
- Autor de la noticia
- Genero del autor
- Fecha
- Medio
- URL de la noticia

1) A partir de los scripts a su disposición, despliegar localmente una arquitectura que pueda recopilar las nuevas noticias publicadas por un medio de comunicación. Cuidarán no enviar consultas HTTP de manera excesiva al servidor del medio de comunicación.

2) En términos de procesos de Arquitectura de Software, ¿qué problemas surgen?



