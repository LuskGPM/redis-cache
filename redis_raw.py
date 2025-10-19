''' Comandos Redis Estudos '''

import redis

r = redis.Redis(
    host='redis-12917.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
    port=12917,
    decode_responses=True,
    username="default",
    password="XPE0SEHNjBaFm9Mo1yrXoNyXBvQYJ5MB",
)

print(r.ping())
# Key value
success = r.set('key 1', 'key 1 acessada')
result = r.get('key 1')
print(result)
r.delete('key 1')

# Hash value
sucess = r.hset('meu_hash', 'nome', 'Lucas')
sucess = r.hset('meu_hash', 'idade', 21)
sucess = r.hset('meu_hash', 'cidade', 'Limoeiro')
result = r.hget('meu_hash', 'nome')
result_all = r.hgetall('meu_hash')
print(result)
print(result_all['cidade'])

# Keys Exists
key_exist = r.exists('key 1')
h_exists = r.hexists('meu_hash', 'cidade')
print(key_exist)
print(h_exists)
# >>> 0:False, 1:True