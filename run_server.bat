@echo off
CALL .env\Scripts\activate

set FLASK_APP=.\server\routes.py
set FLASK_ENV=development

flask run --cert=adhoc &&