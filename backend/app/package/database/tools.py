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
        
    def get_online_objects(self):
        objects = []

        self.__cursor.execute("SELECT * FROM `sports_objects` WHERE `is_active` = 'Y' LIMIT 800")
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[3],
                "active": row[2],
                "address": row[7],
                "action": row[10].title(),
                "objectType": row[11].title() if row[11] else row[11],
                "sportType": row[12].title() if row[12] else row[12],
                "coordinates": {"lat": row[13], "lng": row[14]}
            }
        )
        return objects
    
    
    def get_offline_objects(self):
        objects = []

        self.__cursor.execute("SELECT * FROM `sports_objects` WHERE `is_active` = 'N' LIMIT 800")
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[3],
                "active": row[2],
                "address": row[7],
                "action": row[10].title(),
                "objectType": row[11].title() if row[11] else row[11],
                "sportType": row[12].title() if row[12] else row[12],
                "coordinates": {"lat": row[13], "lng": row[14]}
            }
        )
        return objects
    
    
    def get_cash_object(self, id_object: int):
        cash = []
        
        self.__cursor.execute(f"SELECT `financing_federal`, `financing_subject`, `financing_municipal`, `financing_outside` FROM `sports_objects` WHERE `id` = '{id_object}'")
        for row in self.__cursor.fetchone():
            cash.append(row)
        return cash