Mushroom_classifications
==============================

Mushroom classification, predicting wether the mushroom is edible or not

Step 1:- Create env
```bash
conda create -n mushroom python=3.7 -y
```
Step 2:- Activate env
``bash
conda activate mushroom
```
Step 3:- Install cookiecutter
```bash
pip install cookiecutter
```
Step 4:- Run cookiecutter command for starting new project
```bash
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```
Step 5:- It will give options in command line.
```bash
1. Project_name:
2. Repo_name:
3. Author_name:
4. Description:
5. Select open_source_license:
6. s3_bucket [Optional]:
7. Select python_interpreter:
```
Step 6:- Download dataset :- https://www.kaggle.com/datasets/uciml/mushroom-classification

Step 7:- Initialize git then dvc
```bash
git init
dvc init
``` 
Step 8:- Add data into dvc for tracking
```bash
dvc add data_given/dataset.csv
```
Step 9:- Add to github
```bash
git add -A
git commit -m "first commit"
git remote add origin https://github.com/Abhi-prasad7042/Mushroom-classification-end-to-end.git
git branch -M main
git push -u origin main
```

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
