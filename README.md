Currency XChange API

Stack
=====
* FastAPI
* SQLAlchemy
* FastAPI Users
* Alembic
* psycopg2 (PostgreSQL)

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
  
