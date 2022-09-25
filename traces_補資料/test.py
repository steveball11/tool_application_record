import traces
import sqlite3
import pandas as pd

conn_read = sqlite3.connect(os.path.join(BASE_PATH,"OA.db"))
df_OA = pd.read_sql(sql="SELECT * FROM History",con=conn_read)
df_OA["Time"] = pd.to_datetime(df_OA["Time"]).dt.tz_convert("Asia/Taipei")
df_OA.set_index(df_OA["Time"],inplace=True,drop=True)
df_OA = df_OA.drop("Time",axis=1)
df_OA = df_OA["2021-03-01":"2021-04-01"]
df_OA = df_OA[~df_OA.index.duplicated(keep='first')]

ts = traces.TimeSeries(df_OA["Temp"])
regularized = ts.moving_average(sampling_period=datetime.timedelta(minutes=15),
    start=pd.Timestamp("2021-03-01 00:00:00").tz_localize("Asia/Taipei"),
    end=pd.Timestamp("2021-03-02 00:00:00").tz_localize("Asia/Taipei"),
    placement='left',pandas=True)
ts = traces.TimeSeries(df_OA["Temp"])
regularized = ts.moving_average(sampling_period=datetime.timedelta(minutes=15),
    start=pd.Timestamp("2021-03-01 00:00:00+08:00").tz_convert("Asia/Taipei"),
    end=pd.Timestamp("2021-03-02 00:00:00+08:00").tz_convert("Asia/Taipei"),
    placement='left',pandas=True)

df.groupby("id").apply(resample)