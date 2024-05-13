# Currency XChange API

Currency exchange REST API.
Implements CRUD operations for currencies, currency exchange rates. You can get/post
currencies/exchange rates. You can convert currencies.

### Launch instructions
After `git clone`ing the project, you'll need to:
- create an `.env` file in the root folder (TODO: provide `.example.env`)
- create a postgres db according to your `.env` credentials
- launch alembic migrations to populate the database

You can then `uvicorn main:app --reload` and use 
the API directly with Swagger on your `localhost:8000/docs/`.

There is also frontend support which is currently under development and works like so:
- launch `launch_local_nginx.sh` script which will start a local NGINX server in a docker container.
- this script will serve a single page on `localhost:3000` which will make requests to `localhost:8000`
- You'll need to have your uvicorn serving on `localhost:8000`
- currently only the `currencies/` endpoint is supported, it just outputs the list of available currencies



### Endpoints currently available:  

GET currencies/ - returns a list of available currencies.  
GET currency/<currency code> - return concrete currency if it exists.  
POST currencies/ - posts a new currency or returns code 409 if it exists already.  
DELETE currencies/ - deletes a currency by code or returns 404 if it is not found.

# Stack

* FastAPI
* SQLAlchemy
* FastAPI Users
* Alembic
* psycopg2/asyncpg (PostgreSQL)
* Poetry dependency management

###  Minor usage
* httpx is used to make requests to third-party resources
* BeautifulSoup4 is used to extract currency codes from IBAN web page

# Role Model
(not implemented yet)

* Visitor
    - can read from endpoints available to the public;
* Client
    - can do everything Visitors can do, plus:
    - can read from endpoints available to clients, i.e:
        - can exchange currencies;
        - can get currency rates;
* Administrator
    - can do everything Clients can do, plus:
        - update currency rates;
        - add and delete currencies;
  
