
import sqlite3
conn = sqlite3.connect('retailanalytics.db')
cursor = conn.cursor()

# Execute a query to fetch data from the table
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")

# Database connection with connection pooling for SQLite
engine = create_engine(
    'sqlite:///retailanalytics.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
    pool_pre_ping=True
)

""""
       "materialize_data_4": {
           "config": {"table_name": "hourly_trend"}
       },
       "materialize_data_5": {
           "config": {"table_name": "event_type_counts"}
       }
       """
