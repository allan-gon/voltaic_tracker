from functools import partial
from src.scenarios import *
from src.helper import (
    connect_or_create,
    initialize_db,
    update_data,
    get_highscores,
    Table,
)
from PyQt5.QtGui import QColor, QBrush, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QRadioButton,
    QTableWidget,
    QTableWidgetItem,
)


def remove_last_widget(layout: QVBoxLayout) -> None:
    last_widget = layout.itemAt(layout.count() - 1).widget()
    layout.removeWidget(last_widget)
    last_widget.setParent(None)


def populate_table(
    table: QTableWidget,
    categories,
    subcategories,
    scenarios,
    benchmarks,
    colors,
    highscores,
) -> None:
    # draw categories
    row = 0
    for cell in categories:
        cell.draw(table, row, 0)
        row += cell.row_span
    # draw sub-categories
    row = 0
    for cell in subcategories:
        cell.draw(table, row, 1)
        row += cell.row_span
    # draw scenario names
    row = 0
    for cell in scenarios:
        cell.draw(table, row, 2)
        row += cell.row_span
    # draw max score column
    table.setItem(0, 3, QTableWidgetItem("High Score"))
    table.item(0, 3).setBackground(QBrush(QColor("#5231DD")))
    table.item(0, 3).setForeground(QBrush(QColor("#FFFFFF")))
    for row, score in enumerate(highscores, 1):
        table.setItem(row, 3, QTableWidgetItem(str(score)))
        for idx, benchmark in reversed(list(enumerate(benchmarks[row - 1]))):
            if score >= benchmark:
                rank = idx
                break
        else:
            continue
        table.item(row, 3).setBackground(QBrush(QColor(colors[rank][-1])))
    # draw benchmark titles
    for col, title_info in enumerate(colors, 4):
        table.setItem(0, col, QTableWidgetItem(title_info[0]))
        table.item(0, col).setBackground(QBrush(QColor(title_info[1])))
    # draw benchmark scores
    for row, scen_bench in enumerate(benchmarks, 1):
        for col, score in enumerate(scen_bench, 4):
            table.setItem(row, col, QTableWidgetItem(str(score)))
            table.item(row, col).setBackground(QBrush(QColor(colors[col - 4][2])))


def create_novice_table(curs) -> QTableWidget:
    highscores = get_highscores(curs, Table.NOVICE)
    table = QTableWidget()
    font = QFont("Blinker", 9)
    table.setFont(font)
    table.setRowCount(13)
    table.setColumnCount(8)
    populate_table(
        table,
        NOVICE_CATEGORYS,
        NOVICE_SUBCATEGORYS,
        NOVICE_SCENARIOS,
        NOVICE_BENCHMARKS,
        NOVICE_BENCH_COLORS,
        highscores,
    )
    return table


def create_intermediate_table(curs) -> QTableWidget:
    highscores = get_highscores(curs, Table.INTERMEDIATE)
    table = QTableWidget()
    font = QFont("Blinker", 9)
    table.setFont(font)
    table.setRowCount(17)
    table.setColumnCount(8)
    populate_table(
        table,
        OTHER_CATEGORYS,
        OTHER_SUBCATEGORYS,
        INTERMEDIATE_SCENARIOS,
        INTERMEDIATE_BENCHMARKS,
        INTERMEDIATE_BENCH_COLORS,
        highscores,
    )
    return table


def create_advanced_table(curs) -> QTableWidget:
    highscores = get_highscores(curs, Table.ADVANCED)
    table = QTableWidget()
    font = QFont("Blinker", 9)
    table.setFont(font)
    table.setRowCount(17)
    table.setColumnCount(8)
    populate_table(
        table,
        OTHER_CATEGORYS,
        OTHER_SUBCATEGORYS,
        ADVANCED_SCENARIOS,
        ADVANCED_BENCHMARKS,
        ADVANCED_BENCH_COLORS,
        highscores,
    )
    return table


def place_new_table(layout: QVBoxLayout, which_table: Table, conn, curs) -> None:
    update_data(conn, curs)
    remove_last_widget(layout)
    match which_table:
        case Table.NOVICE:
            layout.addWidget(create_novice_table(curs))
        case Table.INTERMEDIATE:
            layout.addWidget(create_intermediate_table(curs))
        case Table.ADVANCED:
            layout.addWidget(create_advanced_table(curs))


def setup(window: QWidget, conn, curs) -> None:
    # outer most layout
    layout = QVBoxLayout()
    # layout for labels and buttons
    selector = QGridLayout()
    labels = (QLabel("Novice"), QLabel("Intermediate"), QLabel("Advanced"))
    buttons = (QRadioButton(), QRadioButton(), QRadioButton())
    # add callbacks
    buttons[0].clicked.connect(
        partial(place_new_table, layout, Table.NOVICE, conn, curs)
    )
    buttons[1].clicked.connect(
        partial(place_new_table, layout, Table.INTERMEDIATE, conn, curs)
    )
    buttons[2].clicked.connect(
        partial(place_new_table, layout, Table.ADVANCED, conn, curs)
    )
    # add widgets to correct layout
    for idx, label in enumerate(labels):
        selector.addWidget(label, 0, idx)
    for idx, btn in enumerate(buttons):
        selector.addWidget(btn, 1, idx)

    table = QTableWidget()

    layout.addLayout(selector)
    layout.addWidget(table)

    window.setLayout(layout)
    # check btn and use callback
    buttons[0].setChecked(True)
    place_new_table(layout, Table.NOVICE, conn, curs)


def main() -> None:
    # basic setup
    conn, curs = connect_or_create()
    initialize_db(conn, curs)
    app = QApplication([])
    window = QWidget()
    # setup widgets
    setup(window, conn, curs)
    # more basic setup
    window.show()
    app.exec_()
