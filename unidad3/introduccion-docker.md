## Universidad Austral de Chile

# INFO133: Base de Datos

### Responsable: Matthieu Vernier, mvernier@inf.uach.cl

## TP1: Introducción al despliegue de software con Docker y Docker-Compose

Este tutorial es inspirado del tutorial de [Alexander Ryabtsev](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/). Introduce los conceptos de contenedores Docker para facilitar el despliegue de arquitecturas de software en producción más frecuentes y rápidos. Al final de este artículo, podrán utilizar Docker en su máquina local y despliegar contenedores en un servidor remoto.

### ¿Qué es Docker y la integración por contenedores?

[Docker](https://www.docker.com/resources/what-container) corresponde a una herramienta de código abierto  que sirve para empaquetar, transportar y ejecutar cualquiera aplicación como si fuese un contenedor ligero. Esta herramienta es un nuevo modelo de virtualización que se encarga de crear una capa de abstracción con el sistema operativo.

La idea principal de esta herramienta es crear contenedores portables para que las aplicaciones de software puedan ser ejecutadas en cualquier máquina que tenga Docker instalado, sin importar el sistema operativo que la máquina tenga instalado, facilitando enormemente los despliegues de aplicaciones.

Cuando se desarrolla una aplicación, se necesita proporcionar el código junto con todas las dependencias posibles como bibliotecas, el servidor web, bases de datos, etc. Es posible que se encuentre en una situación en la que la aplicación esté funcionando en su ordenador, pero que ni siquiera se inicie en el servidor de test o de producción.

Este desafío puede ser resuelto aislando la aplicación para que sea independiente del sistema.

### ¿En qué se diferencia de la virtualización?

Tradicionalmente, se utilizaban [máquinas virtuales](https://es.wikipedia.org/wiki/M%C3%A1quina_virtual) para evitar este comportamiento inesperado. El principal problema de la VM es que un "sistema operativo adicional" en la parte superior del sistema operativo del host añade gigabytes de espacio al proyecto. La mayoría de las veces su servidor alojará varias máquinas virtuales que ocuparán aún más espacio. Y por cierto, por el momento, la mayoría de los proveedores de servidores basados en la nube le cobrarán por ese espacio extra. Otro inconveniente significativo de la VM es un arranque lento.

Docker elimina todo lo anterior simplemente compartiendo el kernel del SO a través de todos los contenedores que se ejecutan como procesos separados del sistema operativo del host.

![](vm-contenedores.png)

Nota bene: El Instituto de Informática dispone de un servidor físico, dividido en máquinas virtuales. Utilizaremos una de esta máquina virtual para despliegar nuestros de contenedores Docker.

Docker no es la primera ni la única plataforma de contenedorización. Sin embargo, en la actualidad, Docker es el mayor y más poderoso actor del mercado.

### ¿Por qué se necesita a Docker?

La lista corta de beneficios incluye:

- **Proceso de desarrollo más rápido**

No hay necesidad de instalar aplicaciones de terceros como MySQL, Redis, Elasticsearch en el sistema - puede ejecutarlo en contenedores.

- **Práctica encapsulación de aplicaciones**

Usted puede entregar su solicitud en una sola pieza. La mayoría de los lenguajes de programación, frameworks y todos los sistemas operativos tienen sus propios gestores de paquetes. E incluso si su aplicación puede ser empaquetada con su gestor de paquetes nativo, podría ser difícil crear un puerto para otro sistema.

Docker le ofrece un formato de imagen unificado para distribuir sus aplicaciones a través de diferentes sistemas host y servicios cloud. Puede entregar su aplicación en una sola pieza con todas las dependencias requeridas (incluidas en una imagen) listas para ser ejecutadas.


- **El mismo comportamiento en la máquina local / desarrollo / servidores de producción**

Docker no puede garantizar al 100% la paridad desarrollo / puesta en escena / producción, porque siempre está el factor humano. Pero reduce a casi cero la probabilidad de error causado por diferentes versiones de sistemas operativos, dependencias del sistema, etc.

Con el enfoque correcto para construir imágenes Docker, su aplicación utilizará la misma imagen base con la misma versión del sistema operativo y las dependencias necesarias.

- **Monitoreo fácil y claro**

Docker provee una manera unificada de leer los archivos de registro de todos los contenedores en ejecución. No necesita recordar todas las rutas específicas donde su aplicación y sus dependencias almacenan los archivos de registro y escriben ganchos personalizados para manejar esto.
Puede integrar un controlador de registro externo y supervisar los archivos de registro de la aplicación en un solo lugar.

- **Fácil de escalar**

Por diseño, Docker le obliga a seguir sus principios básicos, como la configuración sobre variables de entorno, la comunicación sobre puertos TCP/UDP, etc. Y si ha hecho bien su aplicación, estará lista para ser escalada y facilmente despliegable en cualquier servidor.

### Plataformas soportadas

La plataforma nativa de Docker es Linux, ya que se basa en las características proporcionadas por el núcleo de Linux. Sin embargo, todavía puede ejecutarlo en macOS y Windows. La única diferencia es que en macOS y Windows, Docker está encapsulado en una pequeña máquina virtual. Por el momento, Docker para macOS y Windows ha alcanzado un nivel significativo de usabilidad y se siente más como una aplicación nativa.

### Instalación

Puede consultar las instrucciones de instalación de Docker [aquí](https://docs.docker.com/install/).
Si está ejecutando Docker en Linux, necesita ejecutar todos los siguientes comandos como root o añadir su usuario al grupo de dockers y volver a iniciar sesión:

```
sudo usermod -aG docker username
```

**NB:** reemplazar username por su nombre de usuario



