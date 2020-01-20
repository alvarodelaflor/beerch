% prepara el repositorio para su despliegue. 
release: sh -c 'python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'gunicorn --graceful-timeout=900 --timeout 900 base.wsgi --log-file -'