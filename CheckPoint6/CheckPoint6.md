## 1. ¿Para qué usamos Clases en Python?

Una **clase** es un **molde** o **plantilla** que permite agrupar datos y comportamientos relacionados. Los datos se suelen representar mediante **atributos** y los comportamientos mediante **métodos**. A partir de este molde creamos **objetos** tambien llamados **instancias**.

Para crear una clase usaremos la palabra clave **class** seguida del nombre de la clase y dos puntos (:). 

Una analogía sencilla: la clase es el plano de una casa, donde cada casa construida siguiente ese plano es una instancia. Compartirán una estructura, pero cada casa puede tener su propia dirección o color.

<div  style="text-align: center;">
	<img  src="imagenes\figura1.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div> 


### ¿Para qué se utilizan?

- **Organizar el código:** agrupar en un mismo lugar los datos y las acciones de una entidad, como una persona, un producto o una cuenta bancaria.
- **Reutilizar una definición:** crear muchas instancias sin volver a escribir todos sus atributos y métodos.
- **Modelar entidades del problema:** representar elementos del mundo real o del sistema con los que el programa trabaja.
- **Facilitar el mantenimiento:** si un comportamiento común cambia, normalmente basta con modificar el método de la clase.
- **Mantener el código ordenado** a medida que el proyecto crece.

### Sintaxis básica

```python
class NombreDeLaClase:
    def __init__(self, valor):
        self.atributo = valor
 
    def mostrar(self):
        print(self.atributo)
```

### Vocabulario

**class**: Palabra reservada que inicia la definición de una clase.
**NombreDeLaClase**: Convencionalmente se escribe en PascalCase: por ejemplo, CuentaBancaria.
**__init__** : Método especial utilizado normalmente para inicializar la instancia.
**self**: Referencia a la instancia actual; permite acceder a sus atributos y métodos.
**atributo**: Dato asociado a una instancia, como nombre, edad o saldo.
**método**: Función definida dentro de la clase; puede operar con los datos del objeto.


### Ejemplo

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
 
persona_1 = Persona("Lucia", 25)
persona_2 = Persona("Pedro", 31)
 
print(persona_1.saludar())
print(persona_2.saludar())

```

La salida esperada es:

```python
Hola, soy Lucia y tengo 25 años.
Hola, soy Pedro y tengo 31 años.
```

Hay que fijarse que *Persona* es la clase. *persona_1* y *persona_2* son dos instancias distintas. Ambas tienen nombre y edad, pero guardan valores diferentes.


## 2. ¿Qué método se ejecuta automátiamente cuando se crea una instancia de una clase?.

Cuando creas una instancia (objeto) de una clase, Python ejecuta automáticamente el método __init__, también llamado constructor o inicializador.

No se llama directamente. Python lo invoca solo en el momento de la creación del objeto. Su trabajo es inicializar los atributos del objeto recién nacido.

Aclaración importante: en Python, el objeto realmente lo crea el método __new__, pero __init__ es el que inicializa sus atributos. Para quien empieza, lo importante es recordar que __init__ es el que se ejecuta al instanciar.


### Sintasis

```python
class MiClase:
    def __init__(self, parametros...):   # se ejecuta SOLO al crear el objeto
        self.atributo = valor
```

self: hace referencia al objeto que se está creando.

Se ejecuta una sola vez, justo cuando haces objeto = Clase(...)


### Ejemplo

```python
class Persona:
    def __init__(self, nombre, edad):
        print(f"__init__ se ejecutó automáticamente para {nombre}")
        self.nombre = nombre
        self.edad = edad

# Cada vez que creamos una instancia, __init__ se dispara solo:
p1 = Persona("Ana", 28)
# Salida: __init__ se ejecutó automáticamente para Ana

p2 = Persona("Luis", 35)
# Salida: __init__ se ejecutó automáticamente para Luis
```

self representa al objeto mismo, al que acaba de crearse.
Es siempre el primer parámetro de los métodos de instancia.
Gracias a self, cada objeto guarda sus propios valores:


```python
p1 = Persona("Ana", 28)   # self → p1  →  self.nombre = "Ana"
p2 = Persona("Luis", 35)  # self → p2  →  self.nombre = "Luis"
```

*Errores comunes*									 *Consecuencia*

Olvidar self en los parámetros de __init__			TypeError: __init__() recibe 2 argumentos posicionales pero se dieron 3

Escribir _init_ con un solo guion bajo				No se ejecuta automáticamente (__init__ tiene dos guiones bajos a cada lado).

Llamar __init__ manualmente (p1.__init__(...))		Funciona pero es mala práctica; solo se crea con Persona(...)


En resumen: __init__ es el método que Python ejecuta automáticamente al crear una instancia, y su misión es darle sus valores iniciales al objeto.



## 3. ¿Cuáles son los tres verbos de API?

Los verbos de API son las acciones que le indicas a un servidor que realice sobre la información, los tres más utilizados en el día a día son ‌GET, POST y PUT. (Existe también DELETE para borrar, pero GET, POST y PUT son el núcleo de la interacción).

*GET*: Obtiene datos del servidor. No modifica nada. Por ejemplo obtener la lista de productos.
*POST*: Enviar datos; a menudo crea un recurso o inicia una acción. Por ejemplo Registrar un nuevo producto.
*PUT*: Reemplazar la representación de un recurso existente. Por ejemplo actualizar un producto completo.

No existe un estándar universal que diga que una API tiene exactamente tres verbos. En HTTP hay varios métodos. En cursos introductorios se suelen destacar GET, POST y PUT, pero DELETE y PATCH también son muy habituales en las APIs web.

*PATCH*: Aplicar una modificación parcial. Por ejemplo Cambiar solo el precio de un producto.
*DELETE*: Solicitar la eliminación de un recurso. Por ejemplo eliminar un producto.

<div  style="text-align: center;">
	<img  src="imagenes\figura2.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div> 


### Ejemplo

```Python
import requests

# GET → Leer datos
respuesta = requests.get("https://jsonplaceholder.typicode.com/users")
print(respuesta.status_code)   # 200 → "¡Todo salió bien!"

# POST → Crear un dato nuevo
nuevo_usuario = {"nombre": "Ana", "email": "ana@mail.com"}
respuesta = requests.post("https://jsonplaceholder.typicode.com/users", json=nuevo_usuario)
print(respuesta.status_code)   # 201 → "¡Recurso creado!"

# PUT → Actualizar un dato existente
cambios = {"email": "nuevo@mail.com"}
respuesta = requests.put("https://jsonplaceholder.typicode.com/users/1", json=cambios)
print(respuesta.status_code)   # 200 → "¡Actualizado!"
```


### Códigos de respuesta comunes 

Código	Significado

200	    OK — la petición fue exitosa
201 	Created — el recurso se creó correctamente
404 	Not Found — no se encontró lo que buscabas
500 	Server Error — falló el servidor


## 4. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL orientada a documentos. En vez de organizar principalmente la información en tablas relacionales, almacena registros como documentos BSON, un formato binario relacionado con JSON que admite distintos tipos de datos.

<div  style="text-align: center;">
	<img  src="imagenes\figura3.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div>

¿Por qué no es SQL?

Las bases de datos SQL tradicionales guardan la información en tablas con filas y columnas con una estructura fija que debes definir de antemano. En cambio MongoDB guarda la información en formato BSON (similar a JSON), sin necesidad de definir una estructura rígida.

### Ejemplo

*Base de datos SQL*: Tienes que crear primero una tabla Usuarios con columnas nombre, correo, edad y no puedes agregar un nuevo campo sin modificar toda la tabla.

*MongoDB*: Puedes guardar dos usuarios con estructuras diferentes sin problemas:

```Json
// Documento 1 de usuario
{
  "_id": 1,
  "nombre": "Ana",
  "correo": "ana@ejemplo.com"
}

// Documento 2 de usuario, con un campo extra sin problemas
{
  "_id": 2,
  "nombre": "Luis",
  "correo": "luis@ejemplo.com",
  "edad": 28,
  "ciudad": "Madrid"
}
```

### Ventajas 

No necesitas aprender sintaxis compleja de SQL para empezar a guardar y consultar datos, se asemeja mucho a la forma en la que ya escribes código en Python.


## 5. ¿Qué es una API?

API significa Application Programming Interface, en español, Interfaz de Programación de Aplicaciones. Es un conjunto de reglas y formas de acceso que permite que un programa utilice capacidades o datos proporcionados por otro programa.

Una analogía útil es la de un restaurante: el cliente no entra a la cocina a preparar cada plato. Consulta el menú, hace un pedido siguiendo unas reglas y recibe una respuesta. En una API, el cliente hace una petición y el servicio responde de acuerdo con lo que ofrece y permite.

<div  style="text-align: center;">
	<img  src="imagenes\figura4.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div>


### ¿Para qué se utiliza?

•Permite que una aplicación móvil consulte información de un servidor.

•Conecta el frontend con un backend sin que ambos tengan que compartir toda su implementación interna.

•Permite integrar servicios externos, por ejemplo pagos, mapas o envío de notificaciones.

•Define una frontera clara: qué operaciones existen, qué datos esperan y qué respuestas pueden devolver.

### Ejemplo 

Cuando abres una app del clima en tu teléfono:

Tu app le envía una petición a la API del clima con el nombre de tu ciudad
La API se comunica con el servidor que tiene todos los datos meteorológicos
La API devuelve la respuesta con la temperatura, la probabilidad de lluvia, etc.
Tu app muestra esa información en pantalla para ti

Sin APIs, cada app tendría que recolectar toda la información del clima por su cuenta, lo que sería imposible para los desarrolladores principiantes.


## 6. ¿Qué es Postman?

Postman es una herramienta gráfica (aplicación de escritorio/web) que permite probar, enviar y documentar peticiones hacia APIs sin necesidad de tener un frontend o escribir código.

Postman no es una API en sí misma ni sustituye al backend. Es una herramienta que ayuda a interactuar con una API y comprobar que responde como se espera.

### ¿Para qué sirve?

• Probar métodos HTTP como GET, POST, PUT, PATCH y DELETE sin construir primero una interfaz web.
• Enviar cabeceras, parámetros y cuerpos JSON.
• Inspeccionar el código de estado, las cabeceras y el cuerpo de la respuesta.
• Guardar peticiones en colecciones, reutilizar variables y automatizar pruebas básicas.

### Pasos para probar una API

1. Abre Postman y crea una petición nueva.
2. Selecciona un método, por ejemplo GET.
3. Introduce la URL del endpoint que quieres consultar.
4. Si hace falta, configura parámetros, cabeceras o un cuerpo de petición.
5. Pulsa Send y revisa el estado HTTP y el contenido de la respuesta.
6. Guarda la petición para repetirla o compartirla más adelante.

### Ejemplo

Supongamos que una API de pruebas expone el recurso https://postman-echo.com/get. Al enviar una petición GET en Postman, puedes observar cómo la herramienta muestra la petición realizada y la respuesta devuelta por el servicio. El ejemplo sirve para practicar el flujo; una API real puede exigir autenticación y tener sus propias reglas.

<div  style="text-align: center;">
	<img  src="imagenes\figura5.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div>



## 7. ¿Qué es el polimorfismo?

El polimorfismo es uno de los conceptos fundamentales de la Programación Orientada a Objetos (POO). La palabra proviene del griego poly (muchos) y morphos (formas), lo que significa literalmente "muchas formas".

En programación, el polimorfismo es la capacidad de diferentes objetos de responder a la misma instrucción o llamada a un método de manera específica según su propia naturaleza.

<div  style="text-align: center;">
	<img  src="imagenes\figura6.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div>


### ¿Cómo se usa y para qué sirve?

Se utiliza para escribir código más flexible, reutilizable y fácil de mantener. En lugar de escribir lógica condicional compleja (muchos if/else para comprobar el tipo de objeto), el polimorfismo te permite tratar objetos de diferentes clases de manera uniforme.

La analogía clásica:

Imagina la instrucción "hablar".

- Si se la das a un Perro, ladrará.
- Si se la das a un Gato, maullará.
- Si se la das a un Pato, graznará.

La instrucción es la misma (hablar), pero el comportamiento (la "forma") cambia dependiendo de quién la reciba.

### ¿Cómo es el polimorfismo en Python?

Python es un lenguaje de tipado dinámico, lo que significa que no requiere que declares el tipo de una variable. Por lo tanto, el polimorfismo en Python tiene dos características principales:

Sobrescritura de métodos (Method Overriding): Se da mediante la herencia. Una clase hija redefine (sobrescribe) un método que heredó de su clase padre.

Duck Typing (Tipado Pato): Es la forma más "pythonica" de polimorfismo. Python no se fija en el tipo o clase del objeto, sino en si el objeto tiene el método que se está llamando. "Si camina como pato y grazna como pato, entonces es un pato".

(Nota: A diferencia de Java o C++, Python no soporta la sobrecarga de métodos tradicional —tener varios métodos con el mismo nombre pero distintos parámetros en la misma clase—).


### Ejemplo

Polimorfismo por Herencia (Sobrescritura)
Este es el ejemplo clásico. Creamos una clase base y varias clases hijas que implementan el método a su manera.

```Python
# Clase base (o padre)
class Animal:
    def hacer_sonido(self):
        pass # Método vacío que será sobrescrito

# Clases hijas
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"

# Función polimórfica: no le importa qué clase sea el objeto, 
# solo necesita que tenga el método "hacer_sonido"
def emitir_sonido(animal):
    print(animal.hacer_sonido())

# Uso:
mi_perro = Perro()
mi_gato = Gato()
mi_vaca = Vaca()

# La misma función, distintos comportamientos
emitir_sonido(mi_perro)  # Salida: ¡Guau!
emitir_sonido(mi_gato)   # Salida: ¡Miau!
emitir_sonido(mi_vaca)   # Salida: ¡Muuu!
```


### Resumen de beneficios

*Extensibilidad*: Si en el futuro quieres añadir un Caballo al Ejemplo, solo creas la clase y sobrescribes hacer_sonido(). No tienes que tocar ni modificar la función emitir_sonido().

*Legibilidad*: El código se lee más como el lenguaje humano y se centra en qué hacen los objetos en lugar de qué tipo de objetos son.

*Desacoplamiento*: Las funciones no dependen de clases específicas, sino de interfaces implícitas (métodos compartidos), haciendo el código mucho más modular.


## 8. ¿Qué es un método dunder?

**Dunder** es la abreviatura de Duble Underscore (doble guion bajo).

En Python, un método dunder es simplemente un método especial cuyo nombre empieza y termina con dos guiones bajos **(__nombre__)**. También se les conoce como "métodos mágicos".


Ejemplos que ya has visto si has programado un poco en Python:

__init__ (el constructor)
__str__ y __repr__ (representación en texto)
__add__ (el operador +)
__len__ (usado por la función len())

### ¿Cómo se aplican?

La magia de los métodos dunder es que casi nunca los llamas directamente. En su lugar, actúan como "ganchos" (hooks) que Python usa por debajo para conectar tu objeto con la sintaxis nativa del lenguaje.

Cuando usas un operador o una función integrada de Python, el intérprete busca el método dunder correspondiente en tu objeto y lo ejecuta.

**Sintaxis de Python	Método dunder que Python llama por detrás**
str(objeto)			    objeto.__str__()
len(objeto)			    objeto.__len__()
objeto + otro			objeto.__add__(otro)
objeto == otro			objeto.__eq__(otro)
objeto[indice]			objeto.__getitem__(indice)
for x in objeto:		objeto.__iter__()

Regla de oro: No escribas mi_objeto.__add__(otro). Escribe mi_objeto + otro. 

### Ejemplo 

Representación de objetos (__str__ y __repr__)

Si creas una clase y la imprimes, Python no sabe cómo mostrarla y te da una dirección de memoria fea. Los métodos dunder solucionan esto.

```Python
class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

# Sin métodos dunder:
c1 = Cliente("Ana", 1000)
print(c1)  
# Salida: <__main__.Cliente object at 0x7f8b9c0> (¡Horrible!)
```

Vamos a aplicar __str__ y __repr__:

```Python
class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    # 1. __str__: Para el usuario final (se llama con print() o str())
    def __str__(self):
        return f"Cliente: {self.nombre} | Saldo: ${self.saldo:,.2f}"

    # 2. __repr__: Para el desarrollador (se llama en la consola REPL o con repr())
    # Debe ser lo más detallado posible, idealmente para recrear el objeto.
    def __repr__(self):
        return f"Cliente(nombre='{self.nombre}', saldo={self.saldo})"

c1 = Cliente("Ana", 1500.5)

# Python llama a __str__ automáticamente
print(c1)  
# Salida: Cliente: Ana | Saldo: $1,500.00

# Python llama a __repr__ si __str__ no está definido, o en la consola interactiva
print(repr(c1)) 
# Salida: Cliente(nombre='Ana', saldo=1500.5)
```

### 3 Reglas de Oro para los métodos dunder

1. No inventes tus propios métodos dunder.

Los nombres que empiezan y terminan con __ están reservados por Python. Si creas un __mi_metodo__, podrías romper algo internamente o confundir a otros programadores. Para tus propios métodos, usa guiones simples si es necesario (_metodo_privado).

2. No los llames directamente si hay una función integrada.

Malo: mi_lista.__len__()
Bueno: len(mi_lista)
Malo: a.__add__(b)
Bueno: a + b

3. Mantenlos simples y sin efectos secundarios.

Un método como __add__ debería devolver un nuevo objeto, no modificar el original ni imprimir cosas en pantalla por sí solo. Si haces cosas raras dentro de un *dunder`, romperás las expectativas de cómo funciona Python normalmente.


### Resumen

Los métodos dunder son la forma en que Python te dice: "Oye, si quieres que tu objeto personalizado se comporte como un número, una lista o un texto, solo tienes que decirme cómo hacer las operaciones básicas implementando estos métodos especiales".


## 9. ¿Qué es un decorador de python?

Un decorador es una función (o, en ciertos casos, otro objeto invocable) que recibe una función o clase y devuelve una versión modificada o envuelta de ella. En Python suele aplicarse mediante el símbolo @ colocado justo encima de la definición.

Se utiliza para añadir una responsabilidad reutilizable sin repetir ese código dentro de cada función: por ejemplo registrar cuándo se ejecuta, verificar permisos, medir duración o aplicar caché.

<div  style="text-align: center;">
	<img  src="imagenes\figura7.jpg"  alt="ejemplo clase"  width="300"  height="400">
</div>


La analogía del "Envoltorio"

Imagina que tienes un regalo (tu función original). Un decorador es como el papel de regalo y el lazo: envuelve el regalo, le añade algo estético o funcional, pero el regalo de adentro sigue siendo exactamente el mismo.

En código, se ven así (usando el símbolo @):

```Python
@mi_decorador
def mi_funcion():
    pass
```

### ¿Para qué sirven? 

Sirven para aplicar el principio DRY (Don't Repeat Yourself) y separar responsabilidades.

Imagina que tienes 10 funciones en tu programa y quieres que todas midan cuánto tardan en ejecutarse, o que verifiquen si el usuario está logueado antes de ejecutarse.

Sin decoradores: Tendrías que copiar y pegar el código de "medir tiempo" o "verificar usuario" dentro de las 10 funciones.

Con decoradores: Escribes la lógica una sola vez en el decorador y simplemente "pegas" el @decorador encima de las 10 funciones.


Para entenderlos, primero debes recordar que en Python las funciones son ciudadanos de primera clase. Esto significa que puedes pasarlas como argumentos a otras funciones.

```Python
# 1. Definimos el decorador
def mi_decorador(funcion_original):
    
    # 2. Definimos la función "envoltura" (wrapper)
    def envoltura():
        print(">>> Algo pasa ANTES de la función")
        funcion_original()  # Llamamos a la función original
        print("<<< Algo pasa DESPUÉS de la función")
        
    # 3. Devolvemos la envoltura (¡Ojo! sin los paréntesis, devolvemos la función, no su resultado)
    return envoltura
```

La magia del @ 

Si hacemos esto:

```python
@mi_decorador
def saludar():
    print("Hola mundo")

saludar()
```

Python hace exactamente esto por detrás:

```Python
def saludar():
    print("Hola mundo")

saludar = mi_decorador(saludar) # Reemplaza la función original por la envoltura
```

### Ejemplo

```Python
def decorador_cafe(func):
    def envoltura():
        print("Calentando la máquina...")
        func()
        print("¡Disfruta tu café!")
    return envoltura

@decorador_cafe
def preparar_cafe():
    print("Moliendo granos y preparando el espresso.")

preparar_cafe()
```

Salida:

```Python
Calentando la máquina...
Moliendo granos y preparando el espresso.
¡Disfruta tu café!
``` 

### Los Metadatos Perdidos.

Cuando decoras una función, la función original es reemplazada por la envoltura. Esto tiene un efecto secundario: pierdes el nombre y la documentación de la función original.


```Python
@medir_tiempo
def mi_funcion():
    """Esta es mi función"""
    pass

print(mi_funcion.__name__)  # Imprime: "envoltura" (¡No "mi_funcion"!)
print(mi_funcion.__doc__)   # Imprime: None (¡Perdimos el docstring!)
```

La solución: functools.wraps

Siempre que escribas un decorador profesional, debes importar y usar @wraps de la librería estándar functools. Esto copia los metadatos de la función original a la envoltura.

```Python
from functools import wraps

def medir_tiempo_pro(func):
    @wraps(func)  # <--- ¡Añade esto siempre!
    def envoltura(*args, **kwargs):
        # ... lógica ...
        pass
    return envoltura
```

Con @wraps(func), mi_funcion.__name__ volverá a imprimir "mi_funcion" correctamente.


### Resumen

Qué es: Una función que envuelve a otra para extender su comportamiento sin modificar su código interno.

Sintaxis: Se usa el símbolo @nombre_decorador justo encima de la función a decorar.

Uso principal: Evitar repetir código transversal (logging, autenticación, medición de tiempo, validación de tipos, caché, etc.).

Regla de oro: Usa siempre *args, **kwargs en la función envoltura para que tu decorador sea universal, y usa @functools.wraps para preservar los metadatos.