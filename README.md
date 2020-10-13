# Django project with DRF embedding Vuecli + Webpack autoload
Inspired by  https://medium.com/@jrmybrcf/how-to-build-api-rest-project-with-django-vuejs-part-i-228cbed4ce0c

- Use django webpack loader to insert build into django template
- Customized in case you need multiple entry points for your vueJS app
- I use these settings when i still want django do routing urls and templating and main.js is not enough
- DRF is installed and webbrowsable url is initiated


VueJS app is in the "frontend" dir

### Before running app do (assuming Python >3.6 is installed)

```
$ git clone https://github.com/bdamay/drf-vuejs-config.git
$ cd drf-vuejs-config
$ virtualenv venv
$ . venv/bin/activate 
$ pip install -r requirements
$ python manage.py makemigrations 
$ python manage.py migrate 
$ python manage.py runserver python manage.py runserver 
$ cd frontend
$ npm install
$ npm run serve
```

vueapp Acces at http://localhost:8080/
django is at http://localhost:8000/


