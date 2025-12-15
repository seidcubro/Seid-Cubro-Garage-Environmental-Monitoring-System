from pymongo import MongoClient
import pandas as pd

MONGO_URI = "mongodb_uri"
DB_NAME = "iot_env"
COLLECTION = "readings"

client = MongoClient(MONGO_URI)
collection = client[DB_NAME][COLLECTION]

docs = list(collection.find({}, {"_id": 0}))

if not docs:
    print("No data found.")
    exit()

df = pd.DataFrame(docs)

df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True).dt.tz_convert("US/Eastern")

df = df.sort_values("timestamp")

df.to_csv(
    "iot_data.csv",
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print(f"CSV updated correctly with {len(df)} records")




