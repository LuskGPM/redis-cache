from models import SqliteRepository, RedisRepository
from datetime import datetime

banco_redis = RedisRepository()
banco_sqlite = SqliteRepository()

data_atual = datetime.now().strftime('%d-%m-%Y')

dados_sqlite = banco_sqlite.view(1)
print(f'dados do banco: {dados_sqlite}')

for key, value in dados_sqlite.items():
    banco_redis.insert_hash_ex(data_atual, key=key, value=value, ex=200)
    
dados_redis = banco_redis.get_hash_all(data_atual)
print(f'dados do redis: {dados_redis}')
