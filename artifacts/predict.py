import pandas as pd
import numpy as np
import joblib

artifacts = joblib.load("price_range_model.joblib")

model = artifacts["model"]
label_encoders = artifacts["label_encoders"]
ohe = artifacts["onehot_encoder"]
one_hot_cols = artifacts["onehot_cols"]
label_cols = artifacts["label_cols"]
target_encoder = artifacts["target_encoder"]
feature_cols = artifacts["feature_columns"]


def get_age_group(age):
    if age < 18: return 'Unknown'
    if age <= 25: return '18-25'
    if age <= 35: return '26-35'
    if age <= 45: return '36-45'
    if age <= 55: return '46-55'
    if age <= 70: return '56-70'
    return '70+'

def predict_price(data: dict):

    df = pd.DataFrame([data])

    # Age → age_group
    df['age_group'] = df['age'].apply(get_age_group)
    df.drop(columns=['age'], inplace=True)

    # Label Encoding (simplified)
    for col in label_cols:
        df[col] = label_encoders[col].transform(df[col])

    # One-hot encoding
    ohe_df = pd.DataFrame(
        ohe.transform(df[one_hot_cols]),
        columns=ohe.get_feature_names_out(one_hot_cols)
    )

    df = pd.concat([df.drop(columns=one_hot_cols), ohe_df], axis=1)

    # Align columns
    df = df.reindex(columns=feature_cols, fill_value=0)

    # Predict
    pred = model.predict(df)
    return target_encoder.inverse_transform(pred)[0]