from fastapi import APIRouter
import pandas as pd

router = APIRouter()

df = pd.read_parquet('data/Netflix Userbase.parquet')

class AgeDistribution:
    @router.get('/')
    def age_distribution():
        age_distribution = df['Age'].value_counts().reset_index().rename(columns={'index': 'Age', 'Age': 'Count'})

        return age_distribution.to_dict(orient='records')

age = AgeDistribution()