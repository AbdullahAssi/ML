
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
df = pd.read_csv("C:\\Users\\Abdullah's\\Desktop\\no2.csv")
print(df.head())
X = df[['cars_per_hour', 'temperature_at_2am', 'wind_speed', 'hours_of_day']].values
y = df['no2_concentration'].values

df=  pd.DataFrame(X,columns=['cars_per_hour', 'temperature_at_2am', 'wind_speed', 'hours_of_day', ])
df= df.sort_values(['day', 'hour_of_day']).drop('day', axis=1)
cm = plt.get_cmap('coolwarm')
df.plot(use_index=False, figsize=(20,5),cmap=cm)
