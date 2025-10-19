# Redis Cache Implementation

Este projeto implementa Redis como cache à frente de um banco SQLite para otimizar consultas de dados.

## Arquitetura

```
Cliente → Redis (Cache) → SQLite (Banco Principal)
```

## Como Funciona

### 1. Busca de Dados
- **Cache Hit**: Se os dados existem no Redis, retorna diretamente
- **Cache Miss**: Se não existem no Redis, busca no SQLite e armazena no cache

### 2. Fluxo da Função `buscarDados()`

```python
def buscarDados(id: int):
    # 1. Tenta buscar no Redis primeiro
    dados = redis_rp.get_hash_all(id)
    
    if not dados:
        # 2. Se não encontrou, busca no SQLite
        dados = sqlite_rp.view(id=id)
        
        # 3. Armazena no Redis com TTL de 200 segundos
        redis_rp.insert_hash_ex(dados['ID'], 'nome', dados['NOME'], 200)
    
    return dados
```

## Estrutura do Projeto

```
models/
├── redis/
│   ├── connection/         # Configuração Redis
│   └── redis_repository.py # Operações Redis
├── sqlite/
│   ├── connection/         # Configuração SQLite
│   └── sqlite_repository.py # Operações SQLite
└── __init__.py
```

## Configuração

### Redis
Edite `models/redis/connection/connection_options.py`:
```python
optionsDb = {
    'HOST': 'localhost',
    'PORT': 6379,
    'USERNAME': 'seu-username',
    'PASSWORD': 'sua-senha',
    'DB': 0
}
```

### SQLite
O banco é criado automaticamente em `models/sqlite/connection/database/banco.db`

## Uso

```python
from models import RedisRepository, SqliteRepository

# Buscar dados (com cache automático)
dados = buscarDados(1)
```

## Benefícios

- **Performance**: Consultas em cache são ~100x mais rápidas
- **Redução de Carga**: Menos consultas ao banco principal
- **TTL**: Cache expira automaticamente (200s)
- **Transparente**: Aplicação não precisa saber se veio do cache ou banco