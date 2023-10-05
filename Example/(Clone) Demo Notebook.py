# Databricks notebook source
# MAGIC %md
# MAGIC [Databricks Official Website](https://databricks.com/)
# MAGIC

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(fullname)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

text = dbutils.fs.head('dbfs:/databricks-datasets/SPARK_README.md')
display(text)

# COMMAND ----------


