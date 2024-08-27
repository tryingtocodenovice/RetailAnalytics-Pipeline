import pandas as pd
from dagster import op

@op
def event_type_analysis(context,events_df):
    try:
        #Converts the grouped data into a pivot table where the rows are hours, the columns are event types, and the values are the counts of events.
        event_type_counts = events_df.groupby([events_df['timestamp'].dt.hour, 'event']).size().unstack(fill_value=0)

        # Log the result
        context.log.info(f"Event type analysis result: {event_type_counts.head()}")
        return event_type_counts
    
    except Exception as e:

        context.log.error(f"Error in event_type_analysis: {e}")
        raise

@op
def hourly_trend_analysis(context, events_df):
    try:
        # Group by hour and count the number of events per hour
        hourly_counts = events_df.groupby(events_df['timestamp'].dt.hour).size()

        # Calculate the rolling average with a window of 3 hours
        rolling_avg = hourly_counts.rolling(window=3).mean()

        # Calculate the hourly trend by dividing the counts by the rolling average
        hourly_trend = hourly_counts / rolling_avg

        # Convert the hourly trend to a DataFrame
        hourly_trend_df = pd.DataFrame({
            'hour': hourly_trend.index,
            'trend': hourly_trend.values
        })

        # Log the result
        context.log.info(f"Hourly trend analysis result: {hourly_trend_df.head()}")

        # Return the DataFrame
        return hourly_trend_df

    except Exception as e:
        context.log.error(f"Error in hourly_trend_analysis: {e}")
        raise

