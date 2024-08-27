import pandas as pd
from dagster import asset


@asset
def load_item_properties_data(context):
    try:
        df_part1 = pd.read_csv('/Users/sanyapandey/RetailAnalytics-Pipeline/data/item_properties_part1.csv')
        df_part2 = pd.read_csv('/Users/sanyapandey/RetailAnalytics-Pipeline/data/item_properties_part2.csv')

        df = pd.concat([df_part1, df_part2])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        #only taking the last value for simplification
        df = df.groupby(['itemid', 'property'])['value'].last().reset_index()

        context.log.info(f"Loaded item properties data: {df.head()}")
        return df

    except Exception as e:
        context.log.error(f"Error in load_item_properties_data: {e}")
        raise
