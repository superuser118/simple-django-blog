# Simple-Django-blog

> Features
* Post using CKEditor
* Comment moderation
* Standard pagination
* Humanize time filters (posted time ago)



> Download/Clone

 ```bash
git clone https://github.com/superuser118/simple-django-blog.git
cd simple-django-blog
```

>Installation

>For `Unix`, `MacOS`

```bash
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

>For `Windows`, `MacOS`

```
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

<br />

>Set Up Database

```bash
py manage.py makemigrations
py manage.py migrate
```

>Start the app

```bash
python manage.py runserver
```

Finally, the app runs at `http://127.0.0.1:8000/`.

---
>Tech
* Django 4.1
* Bootstrap 5.2
* Python 3.10.6
* PostgreSQL 14
--- 
## Thanks!
