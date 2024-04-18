from datetime import datetime

from sqlalchemy import (
    MetaData,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
    JSON,
    DECIMAL,
    Index,
)

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("role_name", String, nullable=False, unique=True),
    Column("role_permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("role_id", ForeignKey("roles.id"), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
)

currencies = Table(
    "currencies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("code", String, nullable=False, unique=True, index=True),
    Column("fullname", String, nullable=False),
)

exchange_rates = Table(
    "exchange_rates",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "base_currency_id",
        ForeignKey("currencies.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "target_currency_id",
        ForeignKey("currencies.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("rate", DECIMAL, nullable=False),
    Index("exchange_rate_index", "base_currency_id", "target_currency_id", unique=True),
)
