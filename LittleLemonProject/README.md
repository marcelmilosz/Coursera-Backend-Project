# Django admin <- use this for token
Username: admin <br/>
Password: admin

# Django admin user 
email: admin@lemon.com <br/>
username: admin


# SQL settings
"NAME": reservations <br/>
"USER": root <br/>
"PASSWORD": employee@123! <br/>
"HOST": 127.0.0.1 <br/>
"PORT": 3306 <br/>

# Routes -- Check them
## Djoser 
- http://127.0.0.1:8000/auth/users/
- http://127.0.0.1:8000/auth/token/login

## Index (Page)
- http://127.0.0.1:8000/restaurant/

## Api 
- http://127.0.0.1:8000/restaurant/api/menu
- http://127.0.0.1:8000/restaurant/api/menu/<int:pk>
- http://127.0.0.1:8000/restaurant/api/booking
- http://127.0.0.1:8000/restaurant/api/booking/<int:pk>

to test token with POST 
http://127.0.0.1:8000/restaurant/api-token-auth/