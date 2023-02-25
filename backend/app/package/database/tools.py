import sqlite3

class Database:
    """
    Весь .csv файл был загружен в SQL базу данных - а именно LiteSQL
    Выбор на эту базу данных пал в связи с тем, что для маленькой API
    она подойдет лучше, а в случае масштабирования проекта - переписать
    методы этого класса не составит труда, так как в той же MySQL 
    синтаксис с LiteSQL не различается
    """
    
    __db = None
    __cursor = None
    
    def __init__(self) -> None:
        self.__db = sqlite3.connect('database.db', check_same_thread=False)
        self.__cursor = self.__db.cursor()
        # self.__create_tables()
        
    def get_objects(self):
        objects = []

        self.__cursor.execute("SELECT * FROM `sports_objects`")
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "active": row[2],
                "address": row[7],
                "coordinates": {
                    "X": row[14],
                    "Y": row[13],
                    "all": [row[14], row[13]],
                }
            })
        return objects