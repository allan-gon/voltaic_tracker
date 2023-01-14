from sqlite3 import connect


def connect_or_create() -> tuple:
    """simply returns the connection and cursor for use or creates one if 1st time"""
    connection = connect("./data/scores.db")
    return connection, connection.cursor()


def initialize_db(conn, curs) -> None:
    curs.execute(
        """
        CREATE TABLE IF NOT EXISTS novice (scenario VARCHAR(36), score FLOAT, date TEXT)
        """
    )
    curs.execute(
        """
        CREATE TABLE IF NOT EXISTS intermediate (scenario VARCHAR(36), score FLOAT, date TEXT)
        """
    )
    curs.execute(
        """
        CREATE TABLE IF NOT EXISTS advanced (scenario VARCHAR(36), score FLOAT, date TEXT)
        """
    )
    curs.execute(
        """
        CREATE TABLE IF NOT EXISTS past_files (filename text)
        """
    )
    conn.commit()


def find_steam_folder() -> str:
    # TODO: see if there's a better way than register
    return ""
