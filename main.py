from src.helper import connect_or_create, initialize_db
from src.mvp import save_new_runs


def main() -> None:
    conn, curs = connect_or_create()
    initialize_db(conn, curs)
    conn.close()


if __name__ == "__main__":
    save_new_runs()
# TODO: move back to windows. can't read from file like expecting so not worth linux
