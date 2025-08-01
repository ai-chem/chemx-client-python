

**ChemX** это платформа для работы с научными данными о наноматериалах. Наша цель - предоставить исследователям и аналитикам готовые инструменты для доступа и анализа данных.

Экосистема состоит из трёх ключевых компонентов:

1.   **[ChemX-DBT](https://github.com/ai-chem/ChemX-dbt):** Пайплайн обработки данных (ELT), который очищает, стандартизирует и готовит витрины данных для анализа.
2.   **[ChemX-Backend](https://github.com/ai-chem/ChemX-backend):** API-сервер на FastAPI, который предоставляет доступ к данным через REST API. [**Посмотреть документацию API**](https://chemx-backend.onrender.com/docs).
3.   **[ChemX-Client-Python](https://github.com/ai-chem/chemx-client-python):** Python-библиотека для получения данных с нашего API. [**Начать работу с библиотекой**](https://github.com/ai-chem/chemx-client-python/blob/main/Tutorial.ipynb).

# ChemX Python Client
Python-клиент для работы с [ChemX API](https://chemx-backend.onrender.com/docs), который предоставляет доступ к обработанным научным данным о наноматериалах.
Этот клиент абстрагирует вас от необходимости делать прямые HTTP-запросы и возвращает данные в удобном формате `pandas.DataFrame`, готовом для анализа и использования в Jupyter Notebooks, ML-моделях и других Python-скриптах.

## Туториал
Документацию и туториал по использованию вы можете найти в файле [Tutorial.ipynb](Tutorial.ipynb)

