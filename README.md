# digital_ocean_flask
### Setting Up Your Gunicorn Configuration

Gunicorn is a Python WSGI HTTP server that many developers use to deploy their Python applications. This WSGI (Web Server Gateway Interface) is necessary because traditional web servers do not understand how to run Python applications. For your purposes, a WSGI allows you to deploy your Python applications consistently. You can also configure multiple threads to serve your Python application, should you need them. In this example, you will make your application accessible on port 8080, the standard App Platform port. You will also configure two worker-threads to serve your application.

Open a file named gunicorn_config.py:
```
touch gunicorn_config.py
```


Enter the following command in Run Command
```
gunicorn --worker-tmp-dir /dev/shm app:app
```

To generate class diagram
pyreverse -o png -p componentplain app_entity/
