
# preparing steps

* pip install requests
* pip install django
* pip install djangorestframework

* django-admin startproject musiccontroller
* django-admin startapp api
* django-admin startapp frontend
* python startapp spotify

* mkdir frontend/src
* mkdir frontend/src/components
* mkdir frontend/static
* mkdir frontend/static/css
* mkdir frontend/static/images
* mkdir frontend/static/frontend
* mkdir templates
* mkdir templates/frontend

* cd frontend
* npm init -y
* npm i webpack webpack-cli --save-dev
* npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
* npm i react react-dom --save-dev
* npm install @material-ui/core
* npm install @babel/plugin-proposal-class-properties
* npm install react-router-dom
* npm install @material-ui/icons
* npm install @material-ui/lab

* touch frontend/babel.config.json
* touch frontend/webpack.config.js
  
* touch frontend/src/index.js
* touch frontend/templates/frontend/index.html

* touch frontend/static/css/index.css

* touch spotify/urls.py
* touch spotify/credentials.py
* touch spotify/util.py


## ***** readme page will be updated *****

## To run project :

* install the python requirements : 


        pip install -r requirements.txt

* run the django web server :

        python manage.py runserver


* install and run node.js :


        #change dir to music-controller/frontend
        cd frontend 

        # install all dependicies.
        npm i

        # to run the production compile script
        npm run build

        # or run development :
        node run dev