import sqlite3 as sql
import os
from sqlite3 import Connection
from .connection_config import connection_config


class SqliteConnection:
    def __init__(self) -> None:
        self.__local = connection_config['LOCAL']
        
    def __conn(self) -> Connection:
        try:
            os.makedirs(os.path.dirname(self.__local), exist_ok=True)
            return sql.connect(self.__local)
        except Exception as e:
            print(f'Erro ao iniciar conexão: {e}')
    
    def getConn(self) -> Connection:
        return self.__conn()
