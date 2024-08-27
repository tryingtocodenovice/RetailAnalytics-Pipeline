from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

# Database connection with connection pooling for SQLite
engine = create_engine(
    'sqlite:///retailanalytics.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
    pool_pre_ping=True
)
