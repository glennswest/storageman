flask --app ./setup_schema.py db init 
flask --app ./setup_schema.py db migrate -m "Initial migration."

