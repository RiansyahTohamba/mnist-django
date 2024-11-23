
# generate mnist h5 model
1. create .ipynb file (by using jupyter lab)
2. introduction numpy
    - numpy.array
3. generate model
4. test h5 model by using cli

# integrating django with h5 model
1. django-admin startproject uhomnist
    a. python manage.py migrate
    b. python manage.py createsuperuser
        - create superuser account
            Username: uhomnist
            Email address: muh.riansyaht@uho.ac.id
            password: pelatihanuho
2. cd uhomnist
3. python manage.py startapp predictor
    

4. Create a form in predictor/forms.py:
    a. create uhomnist/predictor/urls.py
    a. edit uhomnist/urls.py, add 
        path('', include(predictor.urls))


5. update predictor/views.py
    - load h5 model 
    - copy logic from cli to this file
6. update predictor/forms.py
7. templates/index.html
8. templates/result.html

# add persitent layer for saving logs
1. a
2. b


# create automation test
1. a
2. b
3. c

# deployment ke server
1. install python on server
2. konfigurasi nginx
3. use the web!

