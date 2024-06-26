# Databricks notebook source
# MAGIC %md
# MAGIC ## 1) Install Packages

# COMMAND ----------

# MAGIC %pip install databricks-sdk --upgrade databricks-vectorsearch langchain==0.2.0 langchain_community transformers databricks-cli mlflow mlflow[databricks]

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ##2) Load dataset, configure secrets & set up variables

# COMMAND ----------

import os
host = "https://" + spark.conf.get("spark.databricks.workspaceUrl")
os.environ['DATABRICKS_TOKEN'] = dbutils.secrets.get("hackathon","token")

# COMMAND ----------

#Fill this out with the catalog where the data is stored and where all objects will be created (eg: tables, models etc)
catalog = "hanna_aggreko" #"hackathon" 

#Fill this out with the schema where the data is stored and where all objects will be created (eg: tables, models etc)
schema = "hack_data" #"default"

# COMMAND ----------

spark.sql(f"""USE CATALOG {catalog}""")
spark.sql(f"""USE DATABASE {schema}""")

# COMMAND ----------

# This is a reference cell that you do not need to use. You have already created tables using the UI. This is an example of how to do it through code:

# spark.read.csv('/Volumes/hackathon/default/engineering-notes/', header=True, inferSchema=True).write.saveAsTable('engineering_notes')

# COMMAND ----------

raw_data = spark.read.table("bbc_news") #<your table name>

# COMMAND ----------

#Replace the names below with the names of the endpoints for embedding model & chat model that would have been pre provisioned within the workspace. Replace the name for vector search endpoint & the name of the table to write to.
embedding_endpoint_name = "bge_m3"
chat_endpoint_name = "meta_llama_3_8b_instruct"
vector_search_endpoint_name = "hackathon_vs"
table_name = "bbc_news_embeddings" #"engineering_notes_embeddings"
