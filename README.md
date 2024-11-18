# Proyecto-Pelican

Este es un proyecto de web de desarrollo de software hecho en Pelican

## Documentación de Pelican

https://docs.getpelican.com/en/latest/index.html

## Crear entorno virtual python

python -m vevn .venv --prompt Proyecto-Pelican

## Instalar dependencias

- Activar entorno virtual
- pip install -r requirements.txt

## Cambiar de temas

En pelcian existe un comando propio para tratar los temas de la pagina, este es `pelican-themes`, para ver los temas que tienes instalados en tu proyecto se usa el comando `pelican-themes -l `esto listará los temas.

Para instalar un tema se emplea el comando `pelican-themes -i <ruta>`

Luego hay que modificar el archivo pelicanconf.py para agregar la variable THEME.
` THEME= <ruta-absoluta al tema>`
