import json
import pandas as pd

def transform():
    with open("/tmp/weather_raw.json") as f:
        raw = json.load(f)
    
    records = []
    for item in raw:
        records.append({
            "city": item["name"],
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "wind_speed": item["wind"]["speed"],
            "timestamp": pd.to_datetime(item["dt"], unit='s')
        })

    df = pd.DataFrame(records)
    df.to_csv("/tmp/weather_clean.csv", index=False)

if __name__ == "__main__":
    transform()
