# docker-compose examples

You can find example compose files for deploying SilverStrike. `demo` contains the stack used for the demo deployment at demo.silverstrike.org.

If you want to try out silverstrike, change into the demo folder and run `docker-compose up`.
You can create a superuser in the running container `docker exec -it demo-ags-1 python manage.py createsuperuser`

The `production` stack is an example stack using sqlite, which should be more than enough for your needs.
If you'd rather use postgres or mariadb, there are example for using them.
