from dagster import op, In, Out, AssetMaterialization, Output
from connection.db_connection import engine
import pandas as pd

# Database connection
from sqlalchemy import create_engine, exc



@op(config_schema={"table_name": str}, ins={"df": In()}, out=Out())
def materialize_data(context, df):
    table_name = context.op_config["table_name"]

    try:
        # Optimize DataFrame before saving
        if isinstance(df, pd.DataFrame):
            for col in df.select_dtypes(include=['timedelta']).columns:
                df[col] = df[col].astype(str)

        # Use chunking to reduce memory usage
        with engine.connect() as connection:
            df.to_sql(table_name, con=connection, if_exists='replace', index=False, chunksize=30000)
            yield AssetMaterialization(asset_key=table_name, description=f"Materialized data in table {table_name}")
            yield Output(df)

    except exc.SQLAlchemyError as e:
        context.log.error(f"An error occurred while writing to the database: {e}")
        raise


