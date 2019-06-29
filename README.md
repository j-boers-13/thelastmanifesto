# thelastmanifesto
A Django powered website, which contains a restful API and an overhaul of the front-end in ReactJS.
This website was designed as a platform for users all over the world to share and read about climate change.

See this image for the front page:
https://ibb.co/yfdpbPv

## Starting off

The files have been structured in the standard Django format, using 'myproject' as the folder
where the settings reside. In order to get the website up and running as strictly a Django
website use a virtual environment and run:
```
pip3 install -r requirements.txt
python3 manage.py runserver
```

In the folder called frontend, you can run:

```
npm start
```

to get the ReactJS front-end to work.
You will then be able to go to either 127.0.0.1:8000, or 127.0.0.1:3000 to see the Django+HTML version and the Django+ReactJS version respectively.

## Apps within the website

As you can see in the folder structure, it is still quite a mess, because it is a work in progress and it is built up from scratch.
I have however, created a few website functionalities which work quite well.

### Accounts

I used django auth to make a User Creation form, and a Log In button. These are still in progress, because i would much rather make it by means of ReactJS.

### Boards

This part was used to create a message board, at the moment it is not being used in the website, but it was very useful practice.

### News

This part is where i have built a webscraper and wrote climate related articles to a database which could be served by Django directly, to HTML with a paginator,
or by a RESTful API (and served by ReactJS).

