import pandas as pd
from assets.JoinedTable import transform_and_join_data
from dagster import build_op_context

def test_transform_and_join_data():
    events_df = pd.DataFrame({
        'itemid': [1, 2, 1, 2],
        'timestamp': pd.to_datetime(['2023-01-01 10:00:00', '2023-01-01 11:00:00', '2023-01-01 12:00:00', '2023-01-01 13:00:00']),
        'event': ['view', 'view', 'purchase', 'purchase']
    })

    agg_df = pd.DataFrame({
        'itemid': [1, 2],
        'value': [100, 200]
    })

    context = build_op_context()

    joined_df = transform_and_join_data(context,events_df, agg_df)

    assert 'time_since_last_event' in joined_df.columns, "'time_since_last_event' column should exist"
    assert 'hour_of_day' in joined_df.columns, "'hour_of_day' column should exist"
    assert 'previous_event' in joined_df.columns, "'previous_event' column should exist"
    assert 'view_to_purchase' in joined_df.columns, "'view_to_purchase' column should exist"

