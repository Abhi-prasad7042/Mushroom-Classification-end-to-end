# load the train and test data
# train algo
# save the metrices and params

import os
from pyexpat import XML_PARAM_ENTITY_PARSING_ALWAYS
import warnings
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from get_data import read_params
import argparse
import joblib
import json

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    n_estimators = config["estimators"]["RandomForestClassifier"]["params"]["n_estimators"]
    criterion = config["estimators"]["RandomForestClassifier"]["params"]["criterion"]
    
    target = config["base"]["target_col"]

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)

    y_train = train[target]
    y_test = test[target]

    X_train = train.drop(target,axis=1)
    X_test = test.drop(target, axis=1)
    
    model = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion, random_state=random_state)
    model.fit(X_train,y_train)

    y_preds = model.predict(X_test)
    cm = confusion_matrix(y_test,y_preds)
    cr = classification_report(y_test,y_preds)

    print(cm)
    print(cr)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)