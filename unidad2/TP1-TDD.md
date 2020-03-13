# INFO229: Arquitectura de software

### Responsable: Matthieu Vernier, mvernier@inf.uach.cl

## TP1: Introducción al Test-Driven Development (TDD) 

### 1. Introducción

El TDD (o desarrollo basado en pruebas) es una práctica simple de desarrollo de software que recomienda a un equipo de desarrolladores seguir tres pasos (en este orden) para crear software:

1. Escribir una prueba que falla de una funcionalidad del software 
2. Escribir el código mínimo para que la prueba pase
3. Refactorizar el código según sea necesario

Este proceso se conoce comúnmente como el ciclo **Red-Green-Refactor**.

1. Se escribe una prueba automatizada de cómo debería comportarse el nuevo código - **Rojo**
2. Se escribe el código en la aplicación hasta que su prueba pase - **Verde**
3. Se refactoriza el código para hacerlo más legible y eficiente. No hay necesidad de preocuparse de que la refactorización rompa la nueva función, sólo tiene que volver a ejecutar la prueba y asegurarse de que pasa.  - **Refactor**

### 2. ¿Por qué?

El TDD permite responder a requisitos no funcionales:
1. **Robustez**: TDD no elimina todos los errores, pero la probabilidad de encontrarlos es menor.
2. **Evolutividad**: Al tener pruebas automatizadas para todas las funciones, los desarrolladores se sienten más seguros al desarrollar nuevas funciones. Se vuelve trivial probar todo el sistema para ver si los nuevos cambios rompen lo que existía antes.
3. **Mantenibilidad**: Las pruebas requieren que modelamos las entradas y salidas de las funciones - TDD nos obliga a pensar en la API de cada modulo antes de empezar a codificar.
4. **Documentation**: Las pruebas pueden ser usadas como documentación adicional. A medida que escribimos las entradas y salidas de una función, un desarrollador puede mirar la prueba y ver cómo la interfaz del código está destinada a ser utilizada.

### 3. Instalación de las librerías

Python viene con un framework de pruebas  llamado `unittest`, sin embargo en nuestro caso utilizaremos otro framework popular, y tal vez más fácil de usar, llamado `pytest`.

> $pip install pytest

La cobertura de código es una métrica que mide la cantidad de código fuente que está cubierto por sus pruebas. `pytest-cov` es un plugin de `pytest` que permite medir el nivel de cobertura de código. 

> $pip install pytest-cov

La cobertura de código del 100% significa que todo el código que has escrito ha sido utilizado por alguna prueba. Una alta cobertura de código no significa que su aplicación no tenga errores. Es más que probable que el código no haya sido probado para todos los escenarios posibles.

### 4. Un primer ejemplo: calcular la suma de números primos

La mejor manera de entender el TDD es ponerlo en práctica. Comenzaremos escribiendo un programa Python que devuelva la suma de todos los números en una secuencia que sean números primos.

Crearemos dos funciones para hacer esto, una que determina si un número es primo o no y otra que suma los números primos de una secuencia de números.

Instrucciones:
- crear una carpeta *./unidad2-tp1*
- crear dos archivos en esta carpeta: *primes.py* y *test_primes.py*

El primer archivo es donde escribiremos el código de nuestro programa, el segundo archivo es donde estarán nuestras pruebas. `pytest` requiere que nuestros archivos de prueba comiencen con "test_" o terminen con "_test.py".

#### 4.1 Función #1: Devolver un booleano que indica si un número es primo o no.

##### 4.1.1 Rojo

Siguiendro el proceso TDD, escribemos una primera prueba para nuestra primera funcion que determina si un número es primo o no.

**Recordatorio**: Un número primo es un número superior a 1 y que solo se puede dividir por 1 o si mismo.

Nuestra función debe tomar un número y devolver `True` si es primo o `False` en caso contrario.

En nuestro *test_primes.py*, agreguemos nuestra primera prueba:
```python
from primes import is_prime

#Si introducimos 1, entonces no debe ser un número primo.
def test_prime_number():
    assert is_prime(1) == False
```
   
La declaración `assert()` es una palabra clave en Python que genera un error si una condición falla. Esta palabra clave es útil al escribir pruebas porque señala exactamente qué condición falló.

Hagamos ahora nuestra prueba:

> $ pytest -v

¿Qué devuelve la prueba? ¿Por qué?

#### 4.1.2 Green

Ahora agreguemos el código mínimo en nuestra aplicación primes.py para hacer que esta prueba pase:
```python
def is_prime(num):
    if num == 1:
        return False
```
Volvemos a hacer la prueba:

> $ pytest -v

#### 4.1.3 Refactor

¡Nuestra primera prueba pasó! Sabemos que el 1 no es primo, pero por definición el 0 no es primo, ni ningún número negativo. Refactorizamos el código y volvemos a verificar que aún nuestra aplicación pasa los tests. 

```python
def is_prime(num):
    # Prime numbers must be greater than 1
    if num < 2:
        return False
```

#### 4.1.4 Iteración 

Una vez que la aplicación pasa los tests, podemos agregar nuevos tests para seguir completando la aplicación. Sabemos que por ejemplo '29' es número primo. Agregamos la prueba siguiente:

```python
def test_prime_prime_number():
    assert is_prime(29)
```
Nuestra aplicación debería ahora tener un estatuto Rojo. Completamos el código de nuestra función probando si se puede dividir nuestra variable por un número entre 2 y la raíz de la variable:

```python
import math

def is_prime(num):
    # Prime numbers must be greater than 1
    if num < 2:
        return False
    #Prime numbers mu
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True
```
> $ pytest -v

Agregamos otro test para verificar que nuestra función cumple bien los requisitos:

```python
def test_prime_other_number():
    assert is_prime(15) == False
```

#### 4.2 Función #2: Calcular la suma de los números primos a partir de una lista de números.

**Recordatorio**: En Test-Driven-Development, empezamos siempre escribiendo el código de una prueba antes de escribir nuevo código fuente de la aplicación. 

Crearemos una nueva función `sum_of_primes([])` que calcula la suma de los números primos. 

##### 4.2.1 Rojo

Nuestro primer test consiste en verificar que este método devuelve 0 si la lista no contiene números.

```python
from primes import sum_of_primes

def test_sum_of_primes_empty_list():
    assert sum_of_primes([]) == 0
```
> $ pytest -v

##### 4.2.2 Green

Escribemos el código fuente más simple para pasar el test. Esta función devuele simplement la suma de todos los números de la lista:

```python
def sum_of_primes(nums):
    return sum(nums)
```
> $ pytest -v

#### 4.2.3 Iteración

Ya que ahora nuestra aplicación pasa todos los tests, agregamos nuevos tests. Por ejemplo de la lista 11, 15, 17, 18, 20 y 100, sólo 11 y 17 son primos. Nuestra función debería devolver 28:

```python
def test_sum_of_primes_mixed_list():
    assert sum_of_primes([11, 15, 17, 18, 20, 100]) == 28
```
Nuestra aplicación tiene un nuevo estado Rojo.
> $ pytest -v

Completamos el código fuente de la función para filtrar los números que no son primos:

```python
def sum_of_primes(nums):
    return sum([x for x in nums if is_prime(x)])
```

Verificamos si la aplicación pasa los tests evaluando el nivel de cobertura de los tests.

```console
$ pytest --cov=primes
```
### 5. Un segundo ejemplo más avanzado: una aplicación de gestión de inventario

Ahora que hemos visto los fundamentos de TDD, vamos a profundizar en algunas características útiles de `pytest` que nos permiten ser más eficientes en las pruebas.

Como antes en nuestro ejemplo básico, *`inventory.py`*, y un archivo de prueba, *`test-inventory.py`*, serán nuestros dos archivos principales.

#### 5.1 Escenario de requisitos y diseño de la API

**Escenario**:
Una tienda de ropa y zapatos quiere informatizar la gestión de sus artículos. Aunque el propietario desea muchas funciones, sus requisitos más prioritarios es que debería poder realizar las siguientes tareas de inmediato.
- Guardar en su stock las 10 nuevas zapatillas Nike que ha comprado recientemente. Cada una vale 50 dólares.
- Añadir 5 pantalones de chándal Adidas más que cuestan $70.00 cada uno.
- El proprietario espera que un cliente compre 2 de las zapatillas Nike
- Está esperando que otro cliente compre uno de los pantalones de chándal.

**Diseño de la API**:

Antés de crear nuestras primeras pruebas, vamos a diseñar primero las entradas, salidas y nombre de cada función del sistema.

- Cada tipo de artículo tendrá un nombre, un precio y un stock.
- Podemos añadir nuevos artículos, añadir stock a artículos existentes, y por supuesto eliminar el stock.
- Cuando creamos un inventario (`Inventory`), querremos que el usuario proporcione un límite (`limit`). El límite tendrá un valor por defecto de 100. 

Nuestra primera prueba sería comprobar el límite cuando instanciamos un objeto **Inventory**. Para asegurarnos de no sobrepasar nuestro límite, tendremos que llevar un registro del contador de artículos totales. Cuando se inicialice, este debería ser 0.

Tendremos que añadir 10 zapatillas Nike y 5 pantalones de deporte Adidas al sistema. Podemos crear un método **add_new_stock()** que toma como parametros un nombre, precio y cantidad.

Deberíamos probar que podemos añadir un artículo a nuestro inventario. No deberíamos poder añadir un artículo con una cantidad negativa, el método debería generar una excepción. Tampoco deberíamos poder añadir más artículos si estamos en nuestro límite, eso también debería generar una excepción.

Los clientes comprarán estos artículos poco después de la entrada, por lo que también necesitaremos un método `remove_stock()`. Esta función necesitaría el nombre del stock y la cantidad de artículos que se están eliminando. Si la cantidad que se está eliminando es negativa o si hace que la cantidad total del stock esté por debajo de 0, entonces el método debería generar una excepción. Además, si el nombre proporcionado no se encuentra en nuestro inventario, el método debería generar una excepción.

#### 5.2 Primeros tests

Creamos una primera serie de tests que representa el escenario planteado:

```python
from inventory import Inventory

def test_default_inventory():
    """Test that the default limit is 100"""
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0
    
def test_buy_and_sell_nikes_adidas():
    # Create inventory object
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

    # Add the new Nike sneakers
    inventory.add_new_stock('Nike Sneakers', 50.00, 10)
    assert inventory.total_items == 10

    # Add the new Adidas sweatpants
    inventory.add_new_stock('Adidas Sweatpants', 70.00, 5)
    assert inventory.total_items == 15

    # Remove 2 sneakers to sell to the first customer
    inventory.remove_stock('Nike Sneakers', 2)
    assert inventory.total_items == 13

    # Remove 1 sweatpants to sell to the next customer
    inventory.remove_stock('Adidas Sweatpants', 1)
    assert inventory.total_items == 12
```
Después cada acción hacemos una afirmación (`assert`) sobre el estado del inventario. Es mejor hacer la afirmación después de que una acción se haya realizado, así cuando estés debuggeando sabrás el último paso que se ha dado.

```console
$ pytest --cov=primes
```

Vamos a crear nuestra clase de inventario, con un parámetro límite que por defecto es 100:

```python
class Inventory:
    def __init__(self, limit=100):
        self.limit = limit
        self.total_items = 0
```
Antes de continuar el desarrollo, queremos estar seguros de que nuestro inventario puede ser inicializado con un límite personalizado, y debe ser configurado correctamente. Deberiamos poder hacer algo así:

```python
def test_custom_inventory_limit():
    """Test that we can set a custom limit"""
    inventory = Inventory(limit=25)
    assert inventory.limit == 25
    assert inventory.total_items == 0
```
```console
$ pytest --cov=primes
```

#### 5.3 *Fixtures*

Nuestras dos primeras pruebas requirieron que instanciáramos un inventario antes de poder empezar. Es más que probable que tengamos que hacer lo mismo para todas las pruebas futuras. Esto es un poco repetitivo.
Podemos usar el concepto de *fixture* para ayudar a resolver este problema. Un *fixture* es un estado conocido y fijo con el que se realizan pruebas para asegurar que los resultados son repetibles.

Es una buena práctica que las pruebas se realicen de forma aislada entre sí. Los resultados de un caso de prueba no deberían afectar a los resultados de otro caso de prueba.

Vamos a crear nuestro primer *fixture* (Noten el uso del decorador pytest.fixture).

```python
import pytest

@pytest.fixture
def no_stock_inventory():
    """Returns an empty inventory that can store 10 items"""
    return Inventory(10)
```
Usemos este *fixture* para añadir una prueba para el método `add_new_stock()`:

```python
def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Jacket', 10.00, 5)
    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Jacket']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Jacket']['quantity'] == 5
```
Para asegurarnos de que los stocks se añadieron tenemos que probar un poco más que el total de artículos almacenados hasta ahora. Escribir esta prueba nos ha obligado a considerar cómo mostrar el precio de cada stock y la cantidad restante.

Ejecutar la prueba para observar que ahora hay 2 fallas y 2 pasadas. 

```console
$ pytest --cov=primes
```

Ahora añadiremos el método `add_new_stock()`:

```python
class Inventory:
    def __init__(self, limit=100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}

    def add_new_stock(self, name, price, quantity):
        self.stocks[name] = {
            'price': price,
            'quantity': quantity
        }
        self.total_items += quantity
```

#### 5.4 Pruebas parametrizadas

Pytest proporciona funciones parametrizadas que nos permiten probar múltiples escenarios usando una función. Escribamos una función de prueba parametrizada para asegurarnos de que nuestra validación de entrada funciona:

```python
@pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item'))
])
def test_add_new_stock_bad_input(name, price, quantity, exception):
    inventory = Inventory(10)
    try:
        inventory.add_new_stock(name, price, quantity)
    except InvalidQuantityException as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        pytest.fail("Expected error but found none")
```
Esta prueba intenta añadir un stock, obtiene una excepción y luego comprueba que es la excepción correcta. Si no obtenemos una excepción, falla la prueba. La cláusula "else" es muy importante en este escenario. Sin ella, una excepción que no fue lanzada contaría como un pase. Nuestra prueba tendría por lo tanto un falso positivo.

Usamos decoradores pytest para añadir un parámetro a la función. El primer argumento contiene una cadena de todos los nombres de los parámetros. El segundo argumento es una lista de tuplas donde cada tupla es un caso de prueba.

Ejecute pytest para ver que nuestra prueba falla ya que InvalidQuantityException no está definida. De vuelta en inventory.py creemos una nueva excepción sobre la clase Inventory:

```python
class InvalidQuantityException(Exception):
    pass
```
Y cambiamos el `método add_new_stock()`:

```python
def add_new_stock(self, name, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityException(
                'Cannot add a quantity of {}. All new stocks must have at least 1 item'.format(quantity))
        self.stocks[name] = {
            'price': price,
            'quantity': quantity
        }
        self.total_items += quantity
```
Ejecutar las pruebas para ver que nuestra prueba más reciente ahora pasa. Ahora agreguemos una segunda prueba, se plantea una excepción si nuestro inventario no puede almacenarlo. Cambie la prueba de la siguiente manera:

```python
@pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item')),
    ('Test Jacket', 10.00, 25, NoSpaceException(
        'Cannot add these 25 items. Only 10 more items can be stored'))
])
def test_add_new_stock_bad_input(name, price, quantity, exception):
    inventory = Inventory(10)
    try:
        inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        pytest.fail("Expected error but found none")
```
En lugar de crear una función totalmente nueva, modificamos ésta ligeramente para recoger nuestra nueva excepción y añadir otra tupla al decorador! Ahora se ejecutan dos pruebas en una sola función.

Las funciones parametrizadas reducen el tiempo necesario para añadir nuevos casos de prueba.

En inventory.py, primero añadiremos nuestra nueva excepción `InvalidQuantityException`:

```python
class NoSpaceException(Exception):
    pass
```
Y cambiamos el `método add_new_stock()`:

```python
def add_new_stock(self, name, price, quantity):
    if quantity <= 0:
        raise InvalidQuantityException(
            'Cannot add a quantity of {}. All new stocks must have at least 1 item'.format(quantity))
    if self.total_items + quantity > self.limit:
        remaining_space = self.limit - self.total_items
        raise NoSpaceException(
            'Cannot add these {} items. Only {} more items can be stored'.format(quantity, remaining_space))
    self.stocks[name] = {
        'price': price,
        'quantity': quantity
    }
    self.total_items += quantity
```

Ejecutar pytest para verificar que las pruebas pasan.

Podemos usar *fixtures* con nuestra función parametrizada. Refactoricemos nuestra prueba para usar el *fixture* de inventario vacío:

```python
def test_add_new_stock_bad_input(no_stock_inventory, name, price, quantity, exception):
    try:
        no_stock_inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        pytest.fail("Expected error but found none")
```

Mirando un poco más el código, no hay razón para que tenga que haber dos métodos para añadir nuevos stocks. Podemos probar los errores y el éxito en una función.

Eliminar `test_add_new_stock_bad_input()` y `test_add_new_stock_success()` y añadiremos una nueva función:

```python
@pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item')),
    ('Test Jacket', 10.00, 25, NoSpaceException(
        'Cannot add these 25 items. Only 10 more items can be stored')),
    ('Test Jacket', 10.00, 5, None)
])
def test_add_new_stock(no_stock_inventory, name, price, quantity, exception):
    try:
        no_stock_inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        assert no_stock_inventory.total_items == quantity
        assert no_stock_inventory.stocks[name]['price'] == price
        assert no_stock_inventory.stocks[name]['quantity'] == quantity
```

Finalmente podemos desarrollar rápidamente la función remove_stock con TDD:

Prueba:

```python
# The import statement needs one more exception
from inventory import Inventory, InvalidQuantityException, NoSpaceException, ItemNotFoundException

# ...
# Add a new fixture that contains stocks by default
# This makes writing tests easier for our remove function
@pytest.fixture
def ten_stock_inventory():
    """Returns an inventory with some test stock items"""
    inventory = Inventory(20)
    inventory.add_new_stock('Puma Test', 100.00, 8)
    inventory.add_new_stock('Reebok Test', 25.50, 2)
    return inventory

# ...
# Note the extra parameters, we need to set our expectation of
# what totals should be after our remove action
@pytest.mark.parametrize('name,quantity,exception,new_quantity,new_total', [
    ('Puma Test', 0,
     InvalidQuantityException(
         'Cannot remove a quantity of 0. Must remove at least 1 item'),
        0, 0),
    ('Not Here', 5,
     ItemNotFoundException(
         'Could not find Not Here in our stocks. Cannot remove non-existing stock'),
        0, 0),
    ('Puma Test', 25,
     InvalidQuantityException(
         'Cannot remove these 25 items. Only 8 items are in stock'),
     0, 0),
    ('Puma Test', 5, None, 3, 5)
])
def test_remove_stock(ten_stock_inventory, name, quantity, exception,
                      new_quantity, new_total):
    try:
        ten_stock_inventory.remove_stock(name, quantity)
    except (InvalidQuantityException, NoSpaceException, ItemNotFoundException) as inst:
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        assert ten_stock_inventory.stocks[name]['quantity'] == new_quantity
        assert ten_stock_inventory.total_items == new_total

```

Código fuente:

```python
class ItemNotFoundException(Exception):
    pass
```
```python
def remove_stock(self, name, quantity):
    if quantity <= 0:
        raise InvalidQuantityException(
            'Cannot remove a quantity of {}. Must remove at least 1 item'.format(quantity))
    if name not in self.stocks:
        raise ItemNotFoundException(
            'Could not find {} in our stocks. Cannot remove non-existing stock'.format(name))
    if self.stocks[name]['quantity'] - quantity <= 0:
        raise InvalidQuantityException(
            'Cannot remove these {} items. Only {} items are in stock'.format(
                quantity, self.stocks[name]['quantity']))
    self.stocks[name]['quantity'] -= quantity
    self.total_items -= quantity
```
Con pytest, todas las pruebas deberían pasar ahora.

### 6. Conclusión

El desarrollo dirigido por pruebas (TDD) es un proceso de desarrollo de software en el que se utilizan pruebas para guiar el diseño de un sistema. TDD ordena que para cada funcionalidad escribamos una prueba que falle, agreguemos la menor cantidad de código para que la prueba pase, y finalmente refactoricemos ese código para que sea más limpio.

Las **pruebas unitarias** se utilizan para asegurar que un módulo individual se comporte como se espera, mientras que las **pruebas de integración** aseguran que un conjunto de módulos interopere como esperamos.

Con TDD, nos vemos obligados a pensar en las entradas y salidas de nuestro sistema y, por lo tanto, en su diseño general. Escribir pruebas proporciona beneficios adicionales como el aumento de la confianza en la funcionalidad de nuestro programa después de los cambios. TDD ordena un proceso fuertemente iterativo que puede ser eficiente aprovechando un conjunto de pruebas automatizadas como pytest.

### 7. Katas de TDD para prácticar

Utilizando Python, PyTest y la metodología TDD, resolver los problemas de programación siguientes
- Fizzbuzz: http://codingdojo.org/kata/FizzBuzz/
- Números romanos: http://codingdojo.org/kata/RomanNumerals/
- Trading cards Kata: http://codingdojo.org/kata/TradingCardGame/
- Diamond Kata: http://codingdojo.org/kata/Diamond/

### 8. Lectura adicional

Does TDD lead to good design? https://codurance.com/2015/05/12/does-tdd-lead-to-good-design/
