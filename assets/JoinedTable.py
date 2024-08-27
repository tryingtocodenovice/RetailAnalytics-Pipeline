import pandas as pd
from dagster import asset


@asset
def transform_and_join_data(context,events_df, agg_df):
    try:
        joined_df = pd.merge(events_df, agg_df, on='itemid', how='left')

        joined_df['time_since_last_event'] = joined_df.groupby('itemid')['timestamp'].diff().fillna(
            pd.Timedelta(seconds=0))
        joined_df['hour_of_day'] = joined_df['timestamp'].dt.hour
        joined_df['previous_event'] = joined_df.groupby('itemid')['event'].shift(1)
        joined_df['view_to_purchase'] = (
                    (joined_df['previous_event'] == 'view') & (joined_df['event'] == 'purchase')).astype(int)


        context.log.info(f"Transformed and joined data: {joined_df.head()}")
        return joined_df

    except Exception as e:
        context.log.error(f"Error in transform_and_join_data: {e}")
        raise
