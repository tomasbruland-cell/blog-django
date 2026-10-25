# Mi Blog

Blog web hecho con Django. Permite registrarse, iniciar sesión y publicar, editar y eliminar posts con imagen.

## Tecnologías utilizadas

- Python
- Django
- SQLite (base de datos)
- Pillow (para manejar las imágenes)
- python-decouple (para manejar variables de entorno)

## Funcionalidades principales

- Ver la lista de posts y el detalle de cada uno.
- Crear, editar y eliminar posts desde la página web.
- Subir una imagen en cada post. Si un post no tiene imagen, la página funciona igual.
- Registro de usuarios, inicio de sesión y cierre de sesión.
- Rutas protegidas: solo los usuarios con sesión iniciada pueden crear, editar y eliminar posts.
- Solo el autor de un post puede editarlo o eliminarlo.

## Instalación

Se necesita tener instalado Python 3 y Git.

**1. Clonar el repositorio y entrar a la carpeta**

```
git clone    git clone https://github.com/tomasbruland-cell/blog-django.git
cd blog-django
```

**2. Crear y activar el entorno virtual**

En Mac o Linux:

```
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```
python -m venv venv
venv\Scripts\activate
```

Cuando está activo, aparece `(venv)` al principio de la línea de la terminal.

**3. Instalar las dependencias**

```
pip install -r requirements.txt
```

**4. Crear el archivo de variables de entorno**

El proyecto necesita un archivo llamado `.env` con sus claves. Se crea copiando el archivo de ejemplo:

```
cp .env.example .env
```

(En Windows: `copy .env.example .env`)

Después hay que abrir el archivo `.env` y reemplazar el valor de `SECRET_KEY` por una clave propia. Se puede generar una con este comando:

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

El archivo `.env` tiene que quedar así (con la clave generada, sin comillas ni espacios):

```
SECRET_KEY=la-clave-generada
DEBUG=True
```

**5. Crear la base de datos**

```
python manage.py migrate
```

**6. Crear un superusuario (opcional)**

Sirve para entrar al panel de administración. El comando pide un nombre de usuario, un email (se puede dejar vacío) y una contraseña:

```
python manage.py createsuperuser
```

**7. Iniciar el servidor**

```
python manage.py runserver
```

## Cómo usarlo

- Página principal: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

Para probar el blog:

1. Entrar a `/registro/` y crear una cuenta.
2. Iniciar sesión en `/login/`.
3. Hacer clic en "Nuevo post" y publicar uno con imagen y otro sin imagen.
4. Entrar a un post para editarlo o eliminarlo.
5. Cerrar sesión e intentar entrar a `/post/nuevo/`: la página redirige al inicio de sesión.

Las imágenes subidas se guardan en una carpeta `media/`, que se crea sola la primera vez que se sube una.

## Autor

Tomás Bruland