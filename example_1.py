import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

class DataVisualizer:
    def __init__(self):
        """Инициализация класса DataVisualizer."""
        pass

    def generate_currency_data(self, start_date, periods):
        """
        Генерация случайных данных для курса валюты.

        :param start_date: Дата начала генерации данных.
        :param periods: Количество периодов (дней) для генерации.
        :return: Даты и случайные значения курса USD/EUR.
        """
        dates = pd.date_range(start=start_date, periods=periods)
        usd_to_eur = np.random.uniform(low=0.8, high=1.2, size=periods)
        return dates, usd_to_eur

    def plot_currency_rate(self, dates, usd_to_eur):
        """
        Построение линейного графика курса валюты с использованием трех библиотек.

        :param dates: Даты для оси X.
        :param usd_to_eur: Значения курса USD/EUR для оси Y.
        """
        # Matplotlib
        plt.figure(figsize=(10, 5))
        plt.plot(dates, usd_to_eur, label='USD/EUR (Matplotlib)', color='blue')
        plt.title('Курс USD/EUR (Matplotlib)')
        plt.xlabel('Дата')
        plt.ylabel('Курс')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.text(0.5, 0.9, 'Библиотека: Matplotlib', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Seaborn
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=dates, y=usd_to_eur, label='USD/EUR (Seaborn)', color='green')
        plt.title('Курс USD/EUR (Seaborn)')
        plt.xlabel('Дата')
        plt.ylabel('Курс')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.text(0.5, 0.9, 'Библиотека: Seaborn', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Plotly
        fig = px.line(x=dates, y=usd_to_eur, labels={'x': 'Дата', 'y': 'Курс'},
                       title='Курс USD/EUR (Plotly)')
        fig.update_layout(title_text='Курс USD/EUR<br><sup>Библиотека: Plotly</sup>', title_x=0.5)
        fig.show()

    def plot_histogram(self, data):
        """
        Построение гистограммы с использованием трех библиотек.

        :param data: Данные для построения гистограммы.
        """
        # Matplotlib
        plt.figure(figsize=(10, 5))
        plt.hist(data, bins=30, color='blue', alpha=0.7)
        plt.title('Гистограмма цен на акции (Matplotlib)')
        plt.xlabel('Цена')
        plt.ylabel('Частота')
        plt.grid()
        plt.text(0.5, 0.9, 'Библиотека: Matplotlib', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Seaborn
        plt.figure(figsize=(10, 5))
        sns.histplot(data, bins=30, kde=True, color='green')
        plt.title('Гистограмма цен на акции (Seaborn)')
        plt.xlabel('Цена')
        plt.ylabel('Частота')
        plt.grid()
        plt.text(0.5, 0.9, 'Библиотека: Seaborn', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Plotly
        fig = px.histogram(data_frame=pd.DataFrame(data, columns=['Цена']),
                           x='Цена', title='Гистограмма цен на акции (Plotly)')
        fig.update_layout(title_text='Гистограмма цен на акции<br><sup>Библиотека: Plotly</sup>', title_x=0.5)
        fig.show()

    def generate_asset_prices(self, num_samples):
        """
        Генерация случайных данных для цен активов.

        :param num_samples: Количество генерируемых цен активов.
        :return: Случайные цены активов.
        """
        return np.random.normal(loc=100, scale=20, size=num_samples)

    def plot_scatter(self, x, y):
        """
        Построение диаграммы рассеяния с использованием трех библиотек.

        :param x: Данные для оси X.
        :param y: Данные для оси Y.
        """
        # Matplotlib
        plt.figure(figsize=(10, 5))
        plt.scatter(x, y, color='blue')
        plt.title('Цены на Bitcoin и Ethereum (Matplotlib)')
        plt.xlabel('Цена Bitcoin')
        plt.ylabel('Цена Ethereum')
        plt.grid()
        plt.text(0.5, 0.9, 'Библиотека: Matplotlib', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Seaborn
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=x, y=y, color='green')
        plt.title('Цены на Bitcoin и Ethereum (Seaborn)')
        plt.xlabel('Цена Bitcoin')
        plt.ylabel('Цена Ethereum')
        plt.grid()
        plt.text(0.5, 0.9, 'Библиотека: Seaborn', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Plotly
        fig = px.scatter(x=x, y=y, labels={'x': 'Цена Bitcoin', 'y': 'Цена Ethereum'},
                         title='Цены на Bitcoin и Ethereum (Plotly)')
        fig.update_layout(title_text='Цены на Bitcoin и Ethereum<br><sup>Библиотека: Plotly</sup>', title_x=0.5)
        fig.show()

    def plot_heatmap(self, data):
        """
        Построение тепловой карты с использованием трех библиотек.

        :param data: Данные для построения тепловой карты.
        """
        # Matplotlib
        plt.figure(figsize=(8, 6))
        plt.imshow(data, cmap='hot', interpolation='nearest')
        plt.title('Тепловая карта корреляции цен на активы (Matplotlib)')
        plt.colorbar()
        plt.text(0.5, 1.05, 'Библиотека: Matplotlib', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Seaborn
        plt.figure(figsize=(8, 6))
        sns.heatmap(data, cmap='hot')
        plt.title('Тепловая карта корреляции цен на активы (Seaborn)')
        plt.text(0.5, 1.05, 'Библиотека: Seaborn', horizontalalignment='center',
                 verticalalignment='center', transform=plt.gca().transAxes,
                 fontsize=10, color='red')
        plt.show()

        # Plotly
        fig = go.Figure(data=go.Heatmap(z=data, colorscale='Hot'))
        fig.update_layout(title='Тепловая карта корреляции цен на активы (Plotly)',
                          title_x=0.5,
                          xaxis_title='Активы',
                          yaxis_title='Активы')
        fig.update_layout(title_text='Тепловая карта корреляции цен на активы<br><sup>Библиотека: Plotly</sup>', title_x=0.5)
        fig.show()

    def run_visualizations(self):
        """Запуск всех визуализаций."""
        # Линейный график курса валюты
        dates, usd_to_eur = self.generate_currency_data('2023-01-01', 100)
        self.plot_currency_rate(dates, usd_to_eur)

        # Гистограмма цен на активы
        asset_prices = self.generate_asset_prices(1000)
        self.plot_histogram(asset_prices)

        # Диаграмма рассеяния цен на криптовалюту
        bitcoin_prices = np.random.rand(100) * 100  # Случайные цены Bitcoin
        ethereum_prices = np.random.rand(100) * 100  # Случайные цены Ethereum
        self.plot_scatter(bitcoin_prices, ethereum_prices)

        # Тепловая карта корреляции
        correlation_data = np.random.rand(10, 10)
        self.plot_heatmap(correlation_data)

# Запуск визуализаций
if __name__ == "__main__":
    visualizer = DataVisualizer()
    visualizer.run_visualizations()
