from fastapi import APIRouter
import pandas as pd

router = APIRouter()

df = pd.read_parquet('data/Netflix Userbase.parquet')

df['Join Month'] = df['Join Date'].dt.to_period('M')

class Payment:
    @router.get('/')
    def ingresos_por_pais():
        ingresos_por_pais = df.groupby(['Country', 'Join Month'])['Monthly Revenue'].sum().reset_index()

        return ingresos_por_pais.to_dict(orient='records')
    
payment = Payment()