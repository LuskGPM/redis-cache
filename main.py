from models.redis import RedisConnection, RedisRepository
from datetime import datetime
from configs import class_start_form

##################################################
# Passo 1: Conectar e buscar dados
redis_repository = RedisRepository()

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')
hash_data = redis_repository.get_hash_all(data_formatada)
###################################################
# Passo 2: Carregar dados ao formulário
class_start_form.set_cache(hash_data)
print(hash_data)
###################################################
# Passo 3: Resgatar os dados armazenados em cache
dados_para_utilizar = class_start_form.get_cache('Suco4')
print(dados_para_utilizar)