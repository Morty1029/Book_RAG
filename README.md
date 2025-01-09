# ml

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Раг был обучен на всех 7 книгах "Гарри Поттер", разбитых на абзацы с указанием принадлежности к конкретной книге и главе. В качестве llm модели используется GPT-4o mini. На вход ей подается ответ от RAG, системный промт и промт пользователя. 
```
{
    "role": "user",
    "content": f"""
        {self.sys_prompt}]\n
        'Запрос пользователя: {data.prompt}\n
        'Результаты rag: {"".join(res.page_content for res in retriever_res)}
        'Использованные части: {"".join(str(res.metadata) for res in retriever_res)}
                    """,
}
```
Системный промт - начальный промт вида:

"Ты часть RAG системы по поиску информации по книгам о Гарри Поттере.
Пользователь задает вопросы по сюжету/персонажам книги, ты предоставляешь ответ на основе базы знаний по книге, с указанием глав/частей книги, на основе которых был сформирован ответ.
Информация о частях книги тебе будет подаваться RAG составляющей, не забудь ее упомянуть при ответе.
Перед ответом проверяй себя - из-за неверных твоих ответов пользователь может не выжить, ты же не хочешь, чтобы кто-то из-за тебя умер."

В результате получаем развернутый ответ на запрос пользователя с указанием глав, где содержится ответ на его вопрос. Например, пользователь хочет узнать: 
#### "Какие были испытания в соревнованиях за кубок огня?"

#### Ответ:

В соревнованиях за Кубок Огня Гарри Поттеру предстояло пройти три основных испытания:

1. **Первое испытание**: Гарри и другие участники должны были получить яйцо от дракона. Каждому нужно было определить, как обойти опасного дракона и заполучить его клад. Это испытание проходило на открытом воздухе, и участникам требовалось показать свои навыки в борьбе.

2. **Второе испытание**: Участники должны были спуститься на дно озера и спасти своих пленников, которым являлись близкие им люди. Это испытание проверяло не только силу и ловкость, но и умение решать задачи в условиях стресса.

3. **Третье испытание**: Это было лабиринт, полный различных препятствий и противников, в котором участники должны были найти кубок. Это испытание ставило акцент на тактическое мышление и умение преодолевать трудности.

Эта информация собрана на основе нескольких частей книги "Гарри Поттер и Кубок огня" (4 книга).

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         recsys and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── setup.cfg          <- Configuration file for flake8
│
└── RAG   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes recsys a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

