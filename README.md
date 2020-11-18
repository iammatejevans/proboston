# Proboston Python developer exercise

Simple python project for Proboston company

## Installation

1. Install requirements listed in requirements.txt
2. Create DB
3. Start server
5. Your app will now run on 127.0.0.1:8000

### Sample installation code (unix)

```bash
git clone https://github.com/iammatejevans/proboston.git
cd proboston
python -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Requirements

1. Python 3.8
2. Django 3
3. Ares-util 0.2

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what 
you would like to change.

Please make sure to update/create tests as well.

## License
[MIT](https://choosealicense.com/licenses/mit/)
