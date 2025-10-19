from redis import Redis
from .connection_options import optionsDb

class RedisConnection:
    def __init__(self,) -> None:
        self.__host = optionsDb['HOST']
        self.__port = optionsDb['PORT']
        self.__decode_responses = optionsDb['DECODE_RESPONSES']
        self.__username = optionsDb['USERNAME']
        self.__password = optionsDb['PASSWORD']
        self.__db = optionsDb['DB']
    
    def getConn(self) -> Redis:
        return self.__conn()
        
    def __conn(self) -> Redis:
        try:
            r = Redis(
                host=self.__host,
                port=self.__port,
                decode_responses=self.__decode_responses,
                username=self.__username,
                password=self.__password,
                db=self.__db,
            )
            print(f'Conectado: {r.ping()}')
            return r
        except ConnectionError as e:
            print(f'Erro ao conectar ao banco: {e}')
        except Exception as e:
            print(f'Erro: {e}')
    