[![Build Status](https://travis-ci.org/bleachjade/Kvent.svg?branch=master)](https://travis-ci.org/bleachjade/Kvent)
[![codecov](https://codecov.io/gh/bleachjade/Kvent/branch/develop/graph/badge.svg?token=JLOHNQNY5P)](https://codecov.io/gh/bleachjade/Kvent)
[![Maintainability](https://api.codeclimate.com/v1/badges/2c2d5aefb36a8455cdf5/maintainability)](https://codeclimate.com/github/bleachjade/Kvent/maintainability)

# Kvent
![Kvent](Kvent/static/images/kvent.png)
Kvent, a web application that can be implemented and used for optimizing efficiency in online booking and appointment by
finding an exhibition or event that you are interested in. It's a great way to get know that the exhibition or event are
available and book the ticket before you go.

## Contributors
<a href="https://github.com/bleachjade/Kvent/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=bleachjade/Kvent" />
</a>

| Name | Roles | GitHub |
|---------------------------|--------------------------|-------------------------------------------------------|
| Nattapol Boonyapornpong | Developer | [bleachjade](https://github.com/bleachjade) |
| Chananya Photan | Developer | [forfeen](https://github.com/forfeen) |
| Kasidit Wongpaiboon | Developer | [BenZacs](https://github.com/BenZacs) |
| Jirawadee Sampusri | Developer | [JirawadeeSampusri](https://github.com/JirawadeeSampusri) |


## Project Documents
- ***[Project Proposal](https://docs.google.com/document/d/1kKmqQyxYT80sFmmCRFkBxXxryh4iwUrwxve9PMhY3_w/edit?usp=sharing)***
- ***[Mockups Design](https://www.figma.com/file/EhMc6OpqAQH1RkHAkma8Lq/Kvent?node-id=0%3A1)***
- ***[Jira Board](https://kvent-kasetsart.atlassian.net/jira/software/projects/KVEN/boards/1)***
- ***[Code Review Checklist](../../wiki/Code%20Review%20Checklist)***
- ***[Code Review Script](../../wiki/Code%20Review%20Script)***


## Prerequisite
- [Python](https://www.python.org/downloads/) 3.7 or newer 
- [Django](https://www.djangoproject.com/download/) 3.1 or newer
- Python add-on modules as in [requirements.txt](requirements.txt)


### Getting Started
1. Clone the repository.
```
  $ git clone https://github.com/bleachjade/Kvent.git
```
2. Change directory to the directory that contain `manage.py` directory.
```
  $ cd Kvent/
```
3. Create `.env` for your local app environment settings, if you want to use Google oauth.
```
SECRET_KEY='YOUR-SECRET-KEY'
DEBUG=True
TIME_ZONE=Asia/Bangkok
DATABASE_URL=sqlite:///db.sqlite3
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=175809729145-m240g50lhbae9lc972knk67qh5irqjur.apps.googleusercontent.com
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=RfxNZ861IKTYhsqqnSe3-unM
```
4. Create virtualenv in the directory and activate virtualenv.    
```
  $ virtualenv venv
```
##### On MacOS and Linux:
```
  $ source venv/bin/activate
```

##### On Windows:
```
  $ venv\Scripts\activate
```

5. Install all required packages and then run database migrations.
##### On MacOS and Linux:
```
  (venv) pip3 install -r requirements.txt
  (venv) python3 manage.py makemigrations
  (venv) python3 manage.py migrate
  (venv) python3 manage.py collectstatic
```
On MacOS, If you can't install psycopg2, try this and install again.
```
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```

##### On Windows:
```
  (venv) pip install -r requirements.txt
  (venv) python manage.py makemigrations
  (venv) python manage.py migrate
  (venv) python manage.py collectstatic
```
6. Run the server.

##### On MacOS and Linux:
```
  (venv) python3 manage.py runserver
```

##### On Windows:
```
  (venv) python manage.py runserver
```
#### Don't forget to exit the virtualenv after you finish testing.
```
  (venv) deactivate
```
