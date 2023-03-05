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
        
        
    def get_objects(self, active: bool | None = None, text: str | None = None):
        objects = []
        
        if active is not None:
            self.__cursor.execute(f"SELECT * FROM `sports_objects` WHERE `is_active` = '{'Y' if active else 'N'}' LIMIT 800")
        elif text is not None:
            self.__cursor.execute("SELECT * FROM sports_objects WHERE address_lower LIKE ? LIMIT 800", (f'%{text.lower()}%',))

        
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[4],
                "active": row[2],
                "address": row[7],
                "action": row[10].title(),
                "objectType": row[11].title() if row[11] else row[11],
                "sportType": row[12].title() if row[12] else row[12],
                "coordinates": {"lat": row[13], "lng": row[14]},
                "phone": ''.join(x for x in row[21] if x.isdigit()) if row[21] else row[21],
                "workingTime": row[22],
                "url": row[23],
                "oktmo": row[8],
                "fcp": row[9]
            })
        return objects
    
    
    def get_cash_object(self, id_object: int):
        cash = []
        
        self.__cursor.execute(f"SELECT `financing_federal`, `financing_subject`, `financing_municipal`, `financing_outside` FROM `sports_objects` WHERE `id` = ?", (id_object,))
        for row in self.__cursor.fetchone():
            cash.append(row)
        return cash
    
    
    def get_search_object(self, text: str):
        objects = []
        self.__cursor.execute("SELECT * FROM sports_objects WHERE address_lower LIKE ? LIMIT 800", (f'%{text.lower()}%',))
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[4],
                "active": row[2],
                "address": row[7],
                "action": row[10].title(),
                "objectType": row[11].title() if row[11] else row[11],
                "sportType": row[12].title() if row[12] else row[12],
                "coordinates": {"lat": row[13], "lng": row[14]},
                "phone": row[21],
                "workingTime": row[22],
                "url": row[23],
                "oktmo": row[8],
                "fcp": row[9]
            }
        )
        return objects