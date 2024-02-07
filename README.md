# ScrapperProject
Scrap proxy data and save in DB

# Steps to setup:

- Create and activate virtual environment (python3.8 is recommended)
  - virtualenv venv
  - . venv/bin/activate

- Install required packages
  - pip install -r requirements.txt

- Setup DB
  - python manage.py makemigrations
  - python manage.py migrate
  
- Open one terminal and run below cmd
  - celery -A Scrapper worker --loglevel=info
  
- Open another terminal and run below cmd
  - celery -A Scrapper  beat --loglevel=info

- To run the task manually, run below cmds
  - python manage.py shell
  - from app_scrapper.tasks import *
  - scrap_and_save_data.apply_async()
