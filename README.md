Currency XChange API

Stack
=====

* FastAPI
* SQLAlchemy
* FastAPI Users
* Alembic
* psycopg2/asyncpg (PostgreSQL)
* Poetry dependency management

Minor usage
===========
* httpx is used to make requests to third-party resources
* BeautifulSoup4 is used to extract currency codes from IBAN web page

Role Model
==========

* Visitor
    - can read from endpoints available to the public;
* Client
    - can do everything Visitors can do, plus:
    - can read from endpoints available to clients, i.e:
        - can exchange currencies;
        - can get currency rates;
* Administator
    - can do everything Clients can do, plus:
        - update currency rates;
        - add and delete currencies;
  
