import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_charts():
    df = pd.read_csv('temp/covid_data.csv')
    country = df['country'][0]
    min_date = df['date'].min()
    max_date = df['date'].max()

    title=f"Covid Cases in {country} from {min_date} to {max_date}"
    fig = plt.subplots(figsize=(20,10))
    x = df["date"]
    y = df["cases"]

    plt.plot(x,y)
    plt.xticks(np.arange(0,len(x), 30),rotation=70)
    plt.yticks(np.arange(0,max(y),20000))

    plt.title(title)
    plt.ylabel("Number of Cases")
    plt.grid()

    plt.savefig(f'../charts/covid_charts_{country}_{min_date}_{max_date}.png')

if __name__ == "__main__":
    plot_charts()
    print("Successfully saved plot. Please refer to charts folder")