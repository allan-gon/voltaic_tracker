from src.helper import connect_or_create
from src.scenarios import NOVICE
from os import listdir

# TODO: import all 3


def save_new_runs() -> None:
    conn, curs = connect_or_create()
    # TODO: make this path more general.
    # hardcoded for mvp
    # NOTE: this / is a quirk of linux. i dont think
    # / would be enough to indicate root on no unix OS
    # VT psalmTS Novice - Challenge - 2023.01.14-01.04.33 Stats.csv
    for file in listdir(
        "/../../media/sf_SteamLibrary/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats"
    ):
        curs.execute(
            f"""
            SELECT * FROM past_files WHERE filename = '{file}'
            """
        )

        if not curs.fetchone():
            # add to list
            curs.execute(
                f"""
                INSERT INTO past_files (filename) VALUES {file}
                """
            )
            # if a benchmark scenario
            # save data
    return
