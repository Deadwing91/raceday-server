# Race Day Server


## Installation
Follow the steps below to download and run this project on your computer
- [ ] Client is required for full functionality. [View client repo here](https://github.com/Deadwing91/raceday-client)
- [ ] Clone this repository
- [ ] From server directory, run "pipenv install"
- [ ] Make sure to be in a virtual environment. "pipenv shell"
- [ ] Run this code:
```bash
rm db.sqlite3
rm -rf ./rareapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations racedayapi
python3 manage.py migrate racedayapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata series_tracks
python3 manage.py loaddata track_types
python3 manage.py loaddata series
python3 manage.py loaddata tracks
```
- [ ] Run "python manage.py runserver"
