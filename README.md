# simple-django-blog

>Important before installing:

 ```bash
By default, database 
```

### 👉 Start here

> Download the code

 ```bash
# Get the code
git clone https://github.com/superuser118/simple-django-blog.git
cd simple-django-blog
```

### 👉 Install modules to your virtual environment  

For `Unix`, `MacOS`

```bash
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

For `Windows`, `MacOS`

```
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

<br />

### 👉 Set Up Database

```bash
py manage.py makemigrations
py manage.py migrate
```

### 👉 Start the app

```bash
python manage.py runserver
```

Finally, the app runs at `http://127.0.0.1:8000/`.

---
Thanks!
