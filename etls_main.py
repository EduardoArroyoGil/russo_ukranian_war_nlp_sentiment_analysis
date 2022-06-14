import etls.setting_db as setting_db
import etls.extraction_twitter as extraction_twitter
import etls.inserting_raw_data_into_db as inserting_raw_data_into_db
import etls.extraction_raw_db as extraction_raw_db
import etls.transforming_gpt3 as transforming_gpt3
import etls.inserting_transformed_gpt3_into_db as inserting_transformed_gpt3_into_db
import pandas as pd

import logging

logging.debug('Inside the ETL')

#  CONNECTING TO DB
setting_db.start()

#  EXTRACTING DATA FROM TWITTER
df = extraction_twitter.start()

#  INSERTING RAW DATA INTO DB
inserting_raw_data_into_db.start(df)

# READ TWEETS FROM DB
df_raw = extraction_raw_db.start()

#  EMOTIONAL ANALYSIS FOR EACH TWEET WITH GPT3
df_trans = transforming_gpt3.start(df_raw)

#  INSERTING GPT3 TRANSFORMED DATA INTO DB
inserting_transformed_gpt3_into_db.start(df_trans)

logging.debug('Finish ETL')
