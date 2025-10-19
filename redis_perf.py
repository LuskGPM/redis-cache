from models import RedisRepository, SqliteRepository

sqlite_rp = SqliteRepository()
redis_rp = RedisRepository()

def buscarDados(id: int):
    dados = redis_rp.get_hash_all(id)
    obs = 'buscou do redis'
    if not dados:
        dados = sqlite_rp.view(id=id)
        obs = 'buscou do banco'
        redis_rp.insert_hash_ex(dados['ID'], 'nome', dados['NOME'], 200)
    
    print(obs)
    print('Dados após if: ',dados)
    return dados

data = buscarDados(1)
print(data)