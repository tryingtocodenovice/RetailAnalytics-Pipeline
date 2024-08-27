import pandas as pd
from dagster import build_op_context
from assets.events import load_events_data

def test_load_events_data():
    context = build_op_context()
    events_df = load_events_data(context)

    assert isinstance(events_df, pd.DataFrame), "Output should be a DataFrame"
    assert 'timestamp' in events_df.columns, "'timestamp' column should exist"
    assert events_df['timestamp'].dtype == 'datetime64[ns]', "'timestamp' column should be datetime"
