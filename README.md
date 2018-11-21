# Alfunduqapi
# Alfunduqapi

git clone repo
In settings.py file change your DB.

## create python virtual environment
follow https://docs.python.org/3/tutorial/venv.html
<code>
  virtualenv venvhms
 </code>
## activate virtual env created in above step in windows
<code>
  source venvhms/Scripts/activate
  </code>


## install dependencies in the virtual environment
<code> 
pip install -r requirements.txt
</code>


## Update DB
```
python manage.py makemigrations 
python manage.py migrate
```

## Run server
```python
python manage.py runserver
```

