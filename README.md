# ScrapperProject
Scrap proxy data and save in DB

# Steps to setup:

1). Create virtual environment
  -> virtualenv venv_copy

2). Install required packages
  -> pip install -r requirements.txt

3). Setup DB
  -> python manage.py makemigrations
  -> python manage.py migrate
  
4). Open one terminal and run below cmd
  -> celery -A Scrapper worker --loglevel=info
  
5). Open another terminal and run below cmd
  -> celery -A Scrapper  beat --loglevel=info

6). To run the task manually, run below cmds
  -> python manage.py shell
  -> from app_scrapper.tasks import *
  -> scrap_and_save_data.apply_async()
