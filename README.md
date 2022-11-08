# Coach-ella
Web server to assist an Android virtual assistant for students enrolled at Escuela Superior de Cómputo

Note: This project is **not** associated to the music festival, and the provided name is just provisional.

## API
* Realizado en Python utilizando el framework Flask, el motor de plantillas Jinja y el kit de herramientas WSGI Werkzeug.
* Uso de fábrica de aplicación para crear la aplicación Flask y registrar todos los elementos por usar (lógica del programa, planos, bases de datos) en el contexto de la aplicación
* Servidor recibe solicitudes HTTP de la aplicación móvil (cliente), cuyo cuerpo consiste en un usuario (número de boleta) y una cadena de texto (texto obtenido mediante entrada de voz). 
* Utiliza procesamiento de lenguaje natural (NLP) y consultas de MySQL para analizar la solicitud del cliente y generar un archivo JSON con la información solicitada.
* NLP realizado mediante las bibliotecas Natural Language Toolkit (NLTK) y spaCy con el objetivo de estudiar la cadena entrante en la solicitud mediante operaciones como tokenización, eliminación de palabras stop y lematización.
* Uso de MySQL para almacenar (y consultar) datos semejantes a los datos de kárdex, horario y de créditos de un alumno registrado en el Sistema de Administración Escolar.


## Aplicación móvil
* Aplicación Android escrita en Java para dispositivos Android 12 (SDK nivel 31), con soporte mínimo para Android 5 “Lollipop” (SDK nivel 21).
* En la pantalla principal, se solicita que el usuario hable a través de su micrófono para convertir su voz en texto. Esto es posible mediante la API SpeechRecognizer, disponible en dispositivos Android desde Android 2.2 “Froyo” (SDK nivel 8).
* El resultado del reconocimiento de voz será enviado, junto con una cadena que representa una boleta, como parte de la solicitud HTTP POST hacia el servidor web. Se utiliza el cliente OkHttp3 para construir el cuerpo de la solicitud y enviarla de manera asíncrona. OkHttp3 funciona a partir de Android 5+ (SDK nivel 21).
* La respuesta que recibe del servidor es un archivo JSON que contiene información sobre el horario del alumno, las calificaciones obtenidas en periodos anteriores, o información sobre su trayectoria académica (créditos y materias reprobadas). En su defecto, si no se reconoce la solicitud, se notifica al usuario.
* La aplicación rescata los valores del archivo JSON con la respuesta, la identifica y muestra sus contenidos de manera organizada en una segunda actividad.
* Generación de un archivo instalable APK sin firma, o un paquete de aplicación firmado AAB para poder distribuir la aplicación en la tienda de aplicaciones Google Play.
* Tamaño de APK: 3.6 MB, con un tamaño de descarga de 3 MB.


# Proyect layout
```
coachella: Python package containing application and other files
|   tests: Directory with test modules (TBD)
```

# TODO
* tests: Create *tests/* directory, and proper tests
* Require login to view voice query history
* Test memory usage and clean leaks if found.
* CPU usage
