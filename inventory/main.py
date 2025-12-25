from fastapi import FastAPI
from redis_om import get_redis_connections, HashModel
import os

app = FastAPI()

redis = get_redis_connections(
    host=os.getenv('host'),
    port=os.getenv('port'),
    password=os.getenv('password'),
    decode_resposes=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get('/products')
def all():
    return[]