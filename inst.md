export FLASK_ENV=development // to tell it we are runing in development in termina
export FLASK_APP=app // to tell it the start app point
flask run

export FLASK_APP=src /// changing the app start point to the directory that holding the init file with app settings
export FLASK_APP=src
export FLASK_ENV=development
flask run
