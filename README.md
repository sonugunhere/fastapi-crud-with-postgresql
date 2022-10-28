# fastapi-crud-with-postgresql

The example below demonstrates how PostgreSQL can be used alongside FastAPI.
# Step 1
Installation:

pip install pipenv
pipenv shell
pipenv install fastapi fastapi-sqlalchemy pydantic alembic psycopg2-binary uvicorn python-dotenv
# Step 2
Create a file and name it models.py
This file is responsible for creating the model for the database. 
# Step 3
Create another file and name it schema.py. It is used to write how an object in a model can be easily mapped using ORM.
# Step 4
Create a file and name it main.py. This file is used to create functions or classes that visualize how a route will operate.
# Step 5
Create an environment file and name it .env.
Inside the .env file do the following:

DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'

# Step 6
After it, run this command:

alembic init alembic

# Step 7
Run the following code to enable migration.

alembic upgrade head

alembic revision --autogenerate -m "New Migration"

# Step 8
To kickstart the app, use:

uvicorn main:app --reload



