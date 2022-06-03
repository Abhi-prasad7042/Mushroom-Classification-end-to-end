## MUSHROOM CLASSIFICATION

### Problem Statement: <br>
The goal of this project is to predict which mushroom is poisonous & which is edible based on different parameters like population, habitat, bruises, cap-shape, and etc. This project can assist people to judge whether the mushroom is edible or poisonous.

### Approach: <br>
The classical machine learning tasks like Data Exploration, Data cleaning, Feature Engineering, Model Building and Model Testing. Tried different machine learning algorithms that's best fit for this case. Machine Learning Models:- Logistic Regression, RandomForestClassifier, Decision Tree Classification, KNeighbors Classifier, Xgboost, and Adaboost.

### Result: <br>
We have to build a soultion that should able to predict whether the mushroom is edible or poisonous.

DEPLOYED APPLICATION LINK: http://mushroom7042.herokuapp.com/ <br>
<br>
FOR DOCUMENTATION LIKE :- LLD, HLD, AND WIREFRAME OF THIS PROJECT VISIT HERE:- https://github.com/Abhi-prasad7042/Mushroom-classification-end-to-end/tree/main/docs
<br>

### STEPS ARE MENTIONED BELOW FOR MAKING THE ENTIRE PIPELINE

Step 1:- Create env
```bash
conda create -n mushroom python=3.7 -y
```
Step 2:- Activate env
```bash
conda activate mushroom
```
##### We used cookie cutter for making template of this project
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
    │   ├── get_data.py           <- Get data file reads the configuration file and reads the data.
    │   │   
    │   │
    │   ├── load_data.py          <- This file reads the data from data source and save it in data/raw 
    │   │                            for futher process.
    │   │
    │   ├── split_data.py         <- This file split the data into train and test dataset and save it 
    │   │                            data/processed folder.
    │   │   
    │   │
    │   └── train_and_evaluate.py  <- This file load the train and test data. Then train the model save
    │                                 save metrics and parameters to reports folder and saves the model
    │                                 to model directory.
    |                                 
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------


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

Step 10:- Create ```params.yaml``` and ```dvc.yaml```

After finish model building now time to create webapp:- <br>
```bash
In webapp folder we have templates of the webpage and for styling we used bootstrap here.
```
Step 11:- 
```app.py``` on root dir for creating flask api
Now make routes like `\` for rendering home page and `/predict` for rendering predictions.

step 20:
For automation of the project create dir `.github\workflow\ci-cd.yaml` we used here github actions for automating our project.

<br>
Author: Abhishek Kumar
<br>
For any queries related to ml/dl contact me <a href="mailto:abhiprasad7042@gmail.com?subject = Feedback&body = Message">abhiprasad7042@gmail.com</a>
<br>

## Thank You