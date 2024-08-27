import pandas as pd
from dagster import build_op_context
from assets.item_properties import load_item_properties_data

def test_load_item_properties_data():
    context = build_op_context()
    item_properties_df = load_item_properties_data(context)

    assert isinstance(item_properties_df, pd.DataFrame), "Output should be a DataFrame"
    assert 'itemid' in item_properties_df.columns, "'itemid' column should exist"
    assert 'value' in item_properties_df.columns, "'value' column should exist"

    # Test that aggregation works
    unique_items = item_properties_df['itemid'].nunique()
    assert unique_items > 0, "There should be unique items"
