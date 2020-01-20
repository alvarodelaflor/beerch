% prepara el repositorio para su despliegue. 
release: sh -c 'cd beerch && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd beerch && gunicorn --graceful-timeout=900 --timeout 900 base.wsgi --log-file -'