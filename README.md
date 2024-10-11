# API con Python y FastAPI

Esta es una API para registro, inicio de sesión, actualización de perfil y eliminación de cuentas, mediante Python y FastAPI, utilizando una base de datos MongoDB y JWT.

## Instalación

1. Clonar el repositorio:

    ```bash
    https://github.com/MaximilianoReyes/Python_FastAPI.git
    ```

2. Crear un ambiente virtual, inicializar el ambiente e instalar dependencias:

    ```bash
    python -m venv venv

    .\venv\Scripts\activate

    pip install -r requirements.txt
    ```

3. Crear el archivo .env y despues configurar las variables de entorno en el archivo 

    ```bash
    New-Item -Path .env -ItemType File

    MONGO_URI
    SECRET_KEY
    ALGORITHM
    ``` 

4. Iniciar la API

    ```bash
    uvicorn app.main:app --reload
    ```

## Uso 

* **Swagger UI**

    FastAPI cuenta con un entorno visual para poder ver y probar los endpoints de una API facilmente, se accede de la siguiente forma: 

    ```bash
    http://localhost:8000/docs
    ```

* **Postman**

    Ademas del Swagger tambien es posible utilizar herramientas como [Postman](https://www.postman.com/) para interacturar con la API., Este tipo de herramientas permiten realizar peticiones HTTP a la API y ver las respuestas.

    - Ejemplo de una petición POST:

        ```bash
        Método: POST

        URL: http://localhost:8000/users

        Body: 

            {
                "user_name": "user_test",
                "email": "test@test.com",
                "password": "password_test"
            }
        ```

## Características

- Registro de usuarios

- Inicio de sesión con JSON Web Token (JWT)

- Actualización y eliminación de usuarios

- Validación de contraseñas cifradas con bcrypt

- Protección de rutas usando autenticación con JWT