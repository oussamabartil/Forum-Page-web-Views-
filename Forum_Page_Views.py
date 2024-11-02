import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])

df = df.set_index('date')

high = df['value'].quantile(0.975)
low = df['value'].quantile(0.025)

df_limiter = [(df['value'] <= high) & (df['value'] >= low)]
start = '01/05/2016'
end = '01/12/2019'
df_date = df.loc[start: end]


def draw_line_plot():
    plt.figure(figsize=(14, 14))
    plt.plot(df_date.index, df_date['value'], marker='o')
    plt.title('nembre of vues per day , 2016-2019 , line plot ')
    plt.xlabel = 'year'
    plt.ylabel = "value"
    plt.xticks(rotation=50)
    plt.grid()
    plt.tight_layout()
    plt.show()


df_mouthly_average = df_date.resample('ME').mean()
df_mouthly_average['year'] = df_mouthly_average.index.year
df_mouthly_average['month'] = df_mouthly_average.index.month


def draw_bar_plot():
    df_pivot = df_mouthly_average.pivot_table(index='year', columns='month', values='value')

    plt.xlabel = 'year'
    plt.ylabel = 'value of a month'
    df_pivot.plot(kind='bar')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


draw_bar_plot()

df_date['year'] = df_date.index.year
df_date['month'] = df_date.index.month


def draw_box_plot():
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_date)
    plt.title('Year-wise Box Plot (Trend) ')
    plt.xlabel = 'year'
    plt.ylabel = 'value'
    plt.show()

    plt.subplot(1, 2, 2)
    sns.boxplot(x='year', y='value', data=df_date)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel = 'year'
    plt.ylabel = 'value'
    plt.tight_layout()

    plt.show()


draw_line_plot()
draw_bar_plot()
draw_box_plot()