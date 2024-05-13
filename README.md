# Currency XChange API

Currency exchange REST API.
Implements CRUD operations for currencies, currency exchange rates. You can get/post
currencies/exchange rates. You can convert currencies.

### Endpoints currently available:  

GET currencies/ - returns a list of available currencies.  
GET currency/<currency code> - return concrete currency if it exists.  
POST currencies/ - posts a new currency or returns code 409 if it exists already.  

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
  
