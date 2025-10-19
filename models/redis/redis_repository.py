from redis import Redis
from typing import Dict, Any
from .connection import RedisConnection

class RedisRepository(RedisConnection):
    def __init__(self) -> None:
        super().__init__()
        self.__redis_conn: Redis = self.getConn()
           
    ## Seterssss
    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)
    
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.setex(name=key, value=value, time=ex)
    
    def insert_hash_ex(self, name_hash: str, key: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(name_hash, key, value)
        self.__redis_conn.expire(name_hash, ex)
    
    def insert_hash(self, name_hash: str, key: str, value: any) -> None:
        self.__redis_conn.hset(name_hash, key, value)
    
    ## Getersss
    def get(self, key) -> Any | None:
        return self.__redis_conn.get(key)
        
    def get_hash(self, name_hash: str, key: str) -> Any | None:
        return self.__redis_conn.hget(name_hash, key)
    
    def get_hash_all(self, key: str) -> Dict | None:
        return self.__redis_conn.hgetall(key)