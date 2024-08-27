import pandas as pd
from dagster import asset, HourlyPartitionsDefinition

# Define hourly partitions
hourly_partition_def = HourlyPartitionsDefinition(start_date="2015-06-01-00:00")


@asset(partitions_def=hourly_partition_def)
def load_events_data(context):
    try:
        df = pd.read_csv('/Users/sanyapandey/RetailAnalytics-Pipeline/data/events.csv')
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        context.log.info(f"Loaded events data: {df.head()}")
        return df

    except Exception as e:
        context.log.error(f"Error in load_events_data: {e}")
        raise
