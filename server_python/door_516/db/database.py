# -*- coding: utf-8 -*-

import sqlite3


class Database:
    def __init__(self, db_file: str):
        self._conn = sqlite3.connect(db_file)


# Table: DoorLog
# Cols: Timestamp, Operation
class DatabaseDoor(Database):
    def __init__(self, db_file: str = "./db/data.db"):
        super().__init__(db_file)

    def open_door(self, time: float):
        try:
            cursor = self._conn.cursor()
            sql = "INSERT INTO DoorLog VALUES (?, ?)"
            cursor.execute(sql, (time, "OPEN"))
            self._conn.commit()
        finally:
            pass

    def close_door(self, time: float):
        try:
            cursor = self._conn.cursor()
            sql = "INSERT INTO DoorLog VALUES (?, ?)"
            cursor.execute(sql, (time, "CLOSE"))
            self._conn.commit()
        finally:
            pass

    def retrieve_logs(self, start_num: int = 0, rec_num: int = 25) -> list:
        start_num = start_num if isinstance(start_num, int) else 0
        rec_num = rec_num if isinstance(rec_num, int) else 25

        try:
            cursor = self._conn.cursor()
            sql = "SELECT * FROM DoorLog LIMIT ?, ?"
            return list(cursor.execute(sql, (start_num, rec_num)))
        finally:
            pass

