from src.scenarios import NOVICE_SCENARIOS, INTERMEDIATE_SCENARIOS, ADVANCED_SCENARIOS
from winreg import OpenKey, HKEY_LOCAL_MACHINE, QueryValueEx
from sqlite3 import connect
from os import listdir, path, mkdir
from vdf import load
from enum import Enum, auto


class Table(Enum):
    NOVICE = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()


class KovaaksNotFound(Exception):
    def __init__(self, *args: object) -> None:
        self.message = (
            "Kovaaks is not in any of the steam folders listed in libraryfolders.vdf"
        )
        super().__init__(*args)


def connect_or_create() -> tuple:
    """simply returns the connection and cursor for use or creates one if 1st time"""
    if not path.exists("./data"):
        mkdir("./data")
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


def find_steam_folders() -> list[str]:
    """if steam not installed or really key doesn't exist will crash"""
    bit_64 = "SOFTWARE\WOW6432Node\Valve\Steam"
    with OpenKey(HKEY_LOCAL_MACHINE, bit_64) as key:
        path = QueryValueEx(key, "InstallPath")[0]

    with open(f"{path}/steamapps/libraryfolders.vdf", "r") as file:
        content = load(file)

    paths = []
    for key in content["libraryfolders"]:
        paths.append(content["libraryfolders"][key]["path"].replace("\\", "/"))
    return paths


def find_kovaaks_folder() -> str:
    steam_folders = find_steam_folders()
    for folder in steam_folders:
        if "FPSAimTrainer" in listdir(f"{folder}/steamapps/common"):
            return f"{folder}/steamapps/common/FPSAimTrainer"
    else:
        raise KovaaksNotFound


def parse(path: str) -> list[str]:
    with open(path, "r") as file:
        content = [i.split(",")[-1].strip() for i in file.readlines()[-24:-22]]
    return content


# store info i care about if new
def update_data(conn, curs) -> None:
    game_folder = find_kovaaks_folder()
    stats_folder = f"{game_folder}/FPSAimTrainer/stats"
    new_novice_scores = []
    new_intermediate_scores = []
    new_advanced_scores = []
    new_files = []
    # for each csv
    for fname in listdir(stats_folder):
        # if not already read
        curs.execute(
            f"""
            SELECT * FROM past_files
            WHERE filename = '{fname}'
            """
        )
        exists = curs.fetchone()
        if not exists:
            new_files.append([fname])
            date = fname.split()[-2]
            data = parse(f"{stats_folder}/{fname}")
            data.append(date)
            scen_name = fname.split(" - Challenge - ")[0]
            if scen_name in [cell.text for cell in NOVICE_SCENARIOS[1:]]:
                new_novice_scores.append(tuple(data))
            elif scen_name in [cell.text for cell in INTERMEDIATE_SCENARIOS[1:]]:
                new_intermediate_scores.append(tuple(data))
            elif scen_name in [cell.text for cell in ADVANCED_SCENARIOS[1:]]:
                new_advanced_scores.append(tuple(data))

    curs.executemany(
        """
        INSERT INTO past_files
        (filename) VALUES (?)
        """,
        new_files,
    )

    curs.executemany(
        """
        INSERT INTO novice
        (score, scenario, date) VALUES (?, ?, ?)
        """,
        new_novice_scores,
    )

    curs.executemany(
        """
        INSERT INTO intermediate
        (score, scenario, date) VALUES (?, ?, ?)
        """,
        new_intermediate_scores,
    )

    curs.executemany(
        """
        INSERT INTO advanced
        (score, scenario, date) VALUES (?, ?, ?)
        """,
        new_advanced_scores,
    )

    conn.commit()


def get_highscores(curs, which_table) -> list[int]:
    highschores = []

    match which_table:
        case Table.NOVICE:
            for scen in [cell.text for cell in NOVICE_SCENARIOS[1:]]:
                curs.execute(
                    f"""
                    SELECT MAX(score)
                    FROM novice
                    WHERE scenario = '{scen}'
                    """
                )
                val = curs.fetchone()[0]
                if val:
                    highschores.append(val)
                else:
                    highschores.append(0)
        case Table.INTERMEDIATE:
            for scen in [cell.text for cell in INTERMEDIATE_SCENARIOS[1:]]:
                curs.execute(
                    f"""
                    SELECT MAX(score)
                    FROM intermediate
                    WHERE scenario = '{scen}'
                    """
                )
                val = curs.fetchone()[0]
                if val:
                    highschores.append(val)
                else:
                    highschores.append(0)
        case Table.ADVANCED:
            for scen in [cell.text for cell in ADVANCED_SCENARIOS[1:]]:
                curs.execute(
                    f"""
                    SELECT MAX(score)
                    FROM advanced
                    WHERE scenario = '{scen}'
                    """
                )
                val = curs.fetchone()[0]
                if val:
                    highschores.append(val)
                else:
                    highschores.append(0)
    return highschores
