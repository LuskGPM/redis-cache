from sqlite3 import Connection, Cursor
from typing import Dict
from contextlib import contextmanager
from .connection import SqliteConnection

class SqliteRepository(SqliteConnection):
    def __init__(self) -> None:
        super().__init__()
    
    @contextmanager
    def get_db_cursor(self):
        conn: Connection = self.getConn()
        print('Status: ', 'Conectado' if conn else 'Não Conectado')
        cursor: Cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    
    def createDb(self) -> Cursor:
        with self.get_db_cursor() as cursor:
            cursor.execute('create table if not exists teste (id integer primary key, nome text, sobrenome text)')
        
    def insert(self, nome: str, sobrenome: str) -> Cursor:
        with self.get_db_cursor() as cursor:
            cursor.execute('insert into teste (nome, sobrenome) values (?, ?)', (nome, sobrenome))
    
    def update(self, id: int, nome: str, sobrenome: str) -> Cursor:
        with self.get_db_cursor() as cursor:
            cursor.execute('update teste set nome = ?, sobrenome = ? where id = ?', (nome, sobrenome, id))
    
    def view(self, id: int) -> Dict:
        with self.get_db_cursor() as cursor:
            cursor.execute('select * from teste where id = ?', (id,))
            dados = cursor.fetchall()[0]
            return {
                'ID': dados[0],
                'NOME': f'{dados[1]} {dados[2]}',
            }
    
    def delete(self, id: int) -> Cursor:
        with self.get_db_cursor() as cursor:
            cursor.execute('delete from teste where id = ?', (id,))
    