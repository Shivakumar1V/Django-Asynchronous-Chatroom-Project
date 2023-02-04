
# Django Chatroom App

This chat application is built using Django, Django-channels and daphne, In this chat application users can chat together in a chatroom asynchronously

#### Included
- User Authentication System
- Messages saved to database

## How to use?

Clone the project

```bash
  git clone https://github.com/Shivakumar1V/Django-Asynchronous-Chatroom-Project
```

Go to the project directory

```bash
  cd chatroom_proj
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```
- It will run the application on localhost
- Open the browser visit [localhost:8000](http://localhost:8000) and enjoy the application

## Note
In this project used "In-Memory Channel Layer" as "CHANNEL_LAYERS" as the project running on local server, use "Redis Channel Layer" on production 

More about using Channel Layers visit [Channel Layers](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)