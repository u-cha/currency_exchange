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
    Boolean,
)

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("role_name", String, nullable=False, unique=True),
    Column("role_permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("email", String(length=320), index=True, nullable=False, unique=True),
    Column("role_id", ForeignKey(role.c.id), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

currency = Table(
    "currency",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("code", String, nullable=False, unique=True, index=True),
    Column("fullname", String, nullable=False),
)

exchange_rate = Table(
    "exchange_rate",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "base_currency_id",
        ForeignKey(currency.c.id, ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "target_currency_id",
        ForeignKey(currency.c.id, ondelete="CASCADE"),
        nullable=False,
    ),
    Column("rate", DECIMAL, nullable=False),
    Index("exchange_rate_index", "base_currency_id", "target_currency_id", unique=True),
)
