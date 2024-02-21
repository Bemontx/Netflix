from fastapi import APIRouter
import pandas as pd

router = APIRouter()

df = pd.read_parquet('data/Netflix Userbase.parquet')

class Suscriptions:
    @router.get('/')
    def suscriptions():
        total_suscriptions = df.shape[0] 

        return {"total_suscriptions": total_suscriptions}
    
suscriptions = Suscriptions()