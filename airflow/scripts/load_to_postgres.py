import pandas as pd
from sqlalchemy import create_engine
import os

def load():
    df = pd.read_csv("/tmp/weather_clean.csv")
    
    db_uri = os.getenv("POSTGRES_URI")
    engine = create_engine(db_uri)
    
    df.to_sql("weather", engine, if_exists="append", index=False)

if __name__ == "__main__":
    load()
