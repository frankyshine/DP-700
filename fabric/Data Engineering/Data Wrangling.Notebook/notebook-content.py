# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e1d3e9e4-bb7b-4c22-b8f7-7632260ed1eb",
# META       "default_lakehouse_name": "DE_LH_wwilakehouse",
# META       "default_lakehouse_workspace_id": "e59424ee-f4a2-4ca0-9b23-9aabfb1bbc0c"
# META     }
# META   }
# META }

# MARKDOWN ********************

#  ### Wrangling with Pandas DataFrame

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import pandas as pd

# Read a CSV into a Pandas DataFrame
df_pandas = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/titanic.csv")
display(df_pandas)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1 = spark.read.parquet("Files/wwi-raw-data/tables/DimCity.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/wwi-raw-data/tables/DimCity.parquet".
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/" + "Files/wwi-raw-data/tables/DimCity.parquet"
df = pd.read_parquet("/lakehouse/default/" + "Files/wwi-raw-data/tables/DimCity.parquet")
# display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

#  ### Wrangling with Spark DataFrame
# The next code snippet creates a Spark DataFrame with the same sample data used in the pandas Data Wrangler tutorial:

# MARKDOWN ********************


# CELL ********************

import pandas as pd

# Read a CSV into a Spark DataFrame
df_spark = spark.createDataFrame(pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/titanic.csv"))
# display(df_spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
