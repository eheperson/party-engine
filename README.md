
# preparing steps : 


* django-admin startproject musiccontroller
* django-admin startapp api
* django-admin startapp frontend

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

* touch frontend/babel.config.json
* touch frontend/webpack.config.js
  
* touch frontend/src/index.js
* touch frontend/templates/frontend/index.html

* touch frontend/static/css/index.css