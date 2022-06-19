import pandas as pd
import matplotlib.pyplot as plt


def plot_charts():
    df = pd.read_csv('../temp/covid_data.csv')
    country = df['country'][0]
    min_date = df['date'].min()
    max_date = df['date'].max()

    title=f"Covid Cases in {country} from {min_date} to {max_date}"
    fig = plt.figure(figsize=(20,10))
    ax = fig.subplots()
    df.plot(kind='line',x='date', y='cases',ax = ax, title=title, rot=70)

    plt.savefig(f'../charts/covid_charts_{country}_{min_date}_{max_date}.png')

if __name__ == "__main__":
    plot_charts()
    print("Successfully saved plot. Please refer to charts folder")