# Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly: Создать набор визуализаций с использованием Matplotlib, Seaborn и Plotly, сравнить их функциональность и удобство использования.

## Введение

### Актуальность темы
Визуализация данных играет ключевую роль в современном мире науки и бизнеса. С увеличением объемов данных, которые необходимо анализировать и интерпретировать, становится всё более важным умение представлять информацию в наглядной и доступной форме.

### Цель исследования
Целью данной работы является сравнительный анализ функциональности и удобства использования трех популярных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly.

### Задачи исследования
1. Изучить основные возможности каждой из рассматриваемых библиотек.
2. Провести сравнительный анализ функциональных возможностей и удобства использования этих библиотек.
3. Разработать примеры визуализаций с использованием всех трех библиотек.
4. Сделать выводы о преимуществах и недостатках каждой из библиотек.

## Глава 1: Теоретические основы визуализации данных

### 1.1. Понятие визуализации данных
Визуализация данных — это процесс представления информации в графическом формате, что позволяет легче воспринимать и анализировать данные.

### 1.2. История развития библиотек для визуализации данных
- **Matplotlib**: Создана в 2003 году Джоном Хантером.
- **Seaborn**: Разработана в 2012 году для упрощения работы с Matplotlib.
- **Plotly**: Запущена в 2013 году, предлагает интерактивные графики.

### 1.3. Основные функции и возможности библиотек
- **Matplotlib**: Базовая библиотека для построения графиков и диаграмм.
- **Seaborn**: Специализируется на статистических графиках.
- **Plotly**: Поддержка создания интерактивных графиков.
#Глава 2. Практическое применение библитек Matplotlib, Seaborn и Plotly
## 2.1 Установка библиотек

Для установки необходимых библиотек используйте pip:

```bash
pip install matplotlib seaborn plotly
```
Демонстрация работы
В проекте представлены следующие примеры визуализаций:

1. Линейные графики
2. Гистограммы
3. Диаграммы рассеяния
4. Тепловые карты

### Файлы проекта
example.py - Примеры визуализаций библитек Matplotlib, Seaborn и Plotly
При необходимости, вы можете ознакомиться с кодом в соответствующих файлах проекта.

## Примеры работы

### 1. Линейный график курса валюты

Данный график демонстрирует изменение курса USD/EUR в течение 100 дней.

# Методы:
- ```generate_currency_data(start_date, periods)```: Генерирует случайные данные для курса валюты USD/EUR на заданный период, начиная с указанной даты. Возвращает массив дат и соответствующих значений курса.
- ```plot_currency_rate(dates, usd_to_eur)```: Строит линейный график курса валюты с использованием трех библиотек: Matplotlib, Seaborn и Plotly.

    - Matplotlib: Строится линейный график с синим цветом, отображающий курс USD/EUR по датам. Заголовок, метки осей и легенда добавляются для ясности.
    - Seaborn: Используется для построения аналогичного линейного графика, но с использованием стиля Seaborn, который делает график более эстетически привлекательным с зеленым цветом.
    - Plotly: Создается интерактивный график, который позволяет пользователю взаимодействовать с данными (например, увеличивать или перемещать график). Заголовок включает информацию о библиотеке.
#### Matplotlib
![1](https://github.com/user-attachments/assets/6b28cf5c-cc3e-4252-b4e6-2c46e0f64b5a)
#### Seaborn
![2](https://github.com/user-attachments/assets/5ad8a8e1-27a5-49b1-bb32-5218921fe00c)
#### Plotly
![3](https://github.com/user-attachments/assets/b1088099-df5f-4aea-ba83-a6f71fa38fb4)
### 2. Гистограмма цен на активы

Гистограмма показывает распределение цен на акции
# Методы:

- ```generate_asset_prices(num_samples)```: Генерирует случайные данные для цен активов, используя нормальное распределение.
- ```plot_histogram(data)```: Строит гистограмму распределения цен активов с использованием трех библиотек.

    - Matplotlib: Строится гистограмма с 30 бинами, отображающая частоту цен на активы. График имеет заголовок, метки осей и сетку.
    - Seaborn: Аналогичная гистограмма, дополненная кривой плотности (KDE), что позволяет лучше визуализировать распределение данных.
    - Plotly: Создается интерактивная гистограмма, позволяющая пользователю исследовать данные более детально.
#### Matplotlib
![4](https://github.com/user-attachments/assets/3acf7447-b773-44c9-83b6-1e637298979a)
#### Seaborn
![5](https://github.com/user-attachments/assets/6e217b3a-e5d9-44d3-afe3-ddd36e05e690)
#### Plotly
![6](https://github.com/user-attachments/assets/150ca787-ae12-490b-8427-1c4e44e18b0f)
### 3. Диаграмма рассеяния цен на криптовалюту

Эта визуализация показывает взаимосвязь между ценами Bitcoin и Ethereum
# Методы:

- ```plot_scatter(x, y)``` : Строит диаграмму рассеяния для двух наборов данных (цен Bitcoin и Ethereum) с использованием трех библиотек.

     - Matplotlib: Строится диаграмма рассеяния с синими точками, отображающая зависимость цен Bitcoin от цен Ethereum. График включает заголовок и метки осей.
     - Seaborn: Используется для построения аналогичной диаграммы с зеленым цветом, что делает график более стильным.
     - Plotly: Создается интерактивная диаграмма рассеяния, позволяющая пользователю взаимодействовать с точками данных.
#### Matplotlib
![7](https://github.com/user-attachments/assets/bbff61b9-47dd-48db-9932-94788641f9c2)
#### Seaborn
![8](https://github.com/user-attachments/assets/8af99827-7216-470e-9c06-a123cbd26acd)
#### Plotly
![9](https://github.com/user-attachments/assets/6deaaec1-7028-4c15-a42b-f83f0673f660)
### 4. Тепловая карта корреляции

Тепловая карта показывает корреляцию между ценами на активы
# Методы:

- ```plot_heatmap(data)```: Строит тепловую карту для визуализации корреляции между ценами на активы с использованием трех библиотек.

    - Matplotlib: Строится тепловая карта, где цветовая палитра отображает значения матрицы. График включает заголовок и цветовую шкалу.
    - Seaborn: Аналогичная тепловая карта, которая более эстетична благодаря стилю Seaborn.
    - Plotly: Создается интерактивная тепловая карта, что позволяет пользователю исследовать значения матрицы более детально.
#### Matplotlib
![10](https://github.com/user-attachments/assets/5cf2cb01-1f28-4c60-ac39-aeb1f594304e)
#### Seaborn
![11](https://github.com/user-attachments/assets/08a950c6-d269-446e-9d37-525fca6a09bd)
#### Plotly
![12](https://github.com/user-attachments/assets/389ca506-f52c-41ad-bfe4-cb7134cfa97f)

## 2.2. Сравнительный анализ функциональности 

На основе созданных примеров можно провести сравнительный анализ функциональности библиотек:

- **Легкость создания графиков**: Matplotlib требует больше кода для построения, в то время как Seaborn и Plotly предлагают более лаконичный и интуитивный синтаксис.
- **Возможность настройки внешнего вида**: Matplotlib предоставляет широкие возможности для настройки, но Seaborn делает это более удобным благодаря предустановленным стилям.
- **Поддержка сложных типов графиков**: Plotly выделяется за счет интерактивных графиков, что делает его лучшим выбором для веб-приложений.
- **Интерактивность**: Plotly обеспечивает интерактивность "из коробки", в то время как для Matplotlib и Seaborn потребуется дополнительная настройка.

## 2.3. Удобство использования

Оценим удобство использования каждой библиотеки, рассматривая такие аспекты, как:

- **Интуитивность интерфейса**: Seaborn и Plotly имеют более интуитивный интерфейс по сравнению с Matplotlib.
- **Наличие документации и примеров кода**: Все три библиотеки имеют хорошую документацию, но Plotly предлагает более обширные примеры интерактивных графиков.
- **Время, необходимое для освоения**: Seaborn и Plotly могут быть освоены быстрее благодаря более простому синтаксису.
- **Совместимость с другими инструментами**: Все три библиотеки хорошо интегрируются с Pandas и Numpy, что делает их удобными для анализа данных.

## Сравнительная таблица

| Критерий                | Matplotlib                    | Seaborn                      | Plotly                       |
|-------------------------|------------------------------|------------------------------|------------------------------|
| **Удобство использования** | Требует больше кода, но высоко настраиваемая | Более интуитивный синтаксис, предустановленные стили | Интуитивный интерфейс, интерактивные графики |
| **Масштабируемость**    | Хорошо подходит для больших наборов данных | Оптимизирован для статистических данных | Отлично подходит для динамических данных |
| **Интерактивность**     | Ограниченная интерактивность | Ограниченная интерактивность | Высокий уровень интерактивности |
| **Документация**        | Хорошая документация        | Хорошая документация        | Обширная документация с примерами |
| **Типы графиков**       | Широкий выбор графиков      | Специализация на статистических графиках | Широкий выбор интерактивных графиков |

# Заключение

В ходе проведенной работы мы рассмотрели три популярных библиотеки для визуализации данных: Matplotlib, Seaborn и Plotly. Каждая из этих библиотек обладает уникальными характеристиками и функциональностью, что делает их подходящими для различных задач и предпочтений пользователей.

- **Matplotlib** является основой для многих других библиотек и предлагает широкие возможности для настройки графиков. Тем не менее, его синтаксис может показаться сложным и требовать больше кода для достижения желаемого результата. Это делает Matplotlib отличным выбором для пользователей, которые нуждаются в глубокой настройке своих визуализаций.
  
- **Seaborn** упрощает процесс создания красивых графиков благодаря предустановленным стилям и более лаконичному синтаксису. Эта библиотека особенно полезна для статистической визуализации и анализа данных, предоставляя удобные функции для работы с комплексными графиками. Seaborn идеально подходит для пользователей, которые хотят быстро и эффективно создавать визуализации без необходимости в глубоком понимании кода.
  
- **Plotly**, в свою очередь, выделяется своей интерактивностью, что делает его идеальным выбором для веб-приложений и презентаций. Возможность легко добавлять интерактивные элементы, такие как всплывающие подсказки и масштабирование, позволяет пользователям глубже взаимодействовать с данными. Plotly является отличным инструментом для визуализации данных в реальном времени и создания динамичных отчетов.

В результате сравнительного анализа мы пришли к выводу, что выбор библиотеки для визуализации данных зависит от конкретных задач и предпочтений пользователя. Если требуется высокая степень настройки и контроль над графиками, Matplotlib будет лучшим выбором. Для быстрого и эстетически приятного создания графиков, особенно в контексте статистического анализа, Seaborn будет предпочтительным. Наконец, для интерактивных визуализаций и работы с веб-приложениями рекомендуется использовать Plotly.
