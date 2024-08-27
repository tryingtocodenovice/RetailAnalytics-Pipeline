from dagster import job, op, In, Out, AssetMaterialization, Output,multiprocess_executor
from assets.events import load_events_data
from assets.item_properties import load_item_properties_data
from assets.JoinedTable import transform_and_join_data
from ops.aggregations import event_type_analysis, hourly_trend_analysis
from ops.materialization import materialize_data
import logging
import gc
from sqlalchemy import create_engine,exc
from sqlalchemy.pool import StaticPool


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




@job(config={
    "ops": {
        "materialize_data_1": {
            "config": {"table_name": "table_1"}
        },
        "materialize_data_2": {
            "config": {"table_name": "table_2"}
        },
        "materialize_data_3": {
            "config": {"table_name": "joined_table"}
        },
        "materialize_data_4": {
            "config": {"table_name": "hourly_trend"}
        },
        "materialize_data_5": {
            "config": {"table_name": "event_type_counts"}
        }

    }
},
    executor_def=multiprocess_executor.configured({"max_concurrent": 2}),
)
def retailAnalytics_job():
    try:
        events_df = load_events_data()
        item_properties_df = load_item_properties_data()

        event_type_counts = event_type_analysis(events_df)
        hourly_trend = hourly_trend_analysis(events_df)
        joined_df = transform_and_join_data(events_df, item_properties_df)

        materialize_data.alias('materialize_data_1')(df=events_df)
        materialize_data.alias('materialize_data_2')(df=item_properties_df)
        materialize_data.alias('materialize_data_3')(df=joined_df)
        materialize_data.alias('materialize_data_4')(df=hourly_trend)
        materialize_data.alias('materialize_data_5')(df=event_type_counts)

    except Exception as e:
        logger.error(f"Error in retailAnalytics_job: {e}")
        raise
