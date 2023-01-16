from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QColor, QBrush


class Cell:
    def __init__(
        self, text: str, bg_color: str = None, fg_color: str = None, row_span: int = 1
    ) -> None:
        self.text = text
        self.background_color = bg_color
        self.foreground_color = fg_color
        self.row_span = row_span

    def draw(self, table, row: int, col: int) -> None:
        table.setItem(row, col, QTableWidgetItem(self.text))
        if self.background_color:
            table.item(row, col).setBackground(QBrush(QColor(self.background_color)))
        if self.foreground_color:
            table.item(row, col).setForeground(QBrush(QColor(self.foreground_color)))
        if self.row_span:
            table.setSpan(row, col, self.row_span, 1)


# each list is a column except for the benchmarks, those represent
NOVICE_CATEGORYS = [
    Cell("", "#5231DD"),
    Cell("Clicking", "#CC0000", "#FFFFFF", 4),
    Cell("Tracking", "#1155CC", "#FFFFFF", 4),
    Cell("Switching", "#351C75", "#FFFFFF", 4),
]

NOVICE_SUBCATEGORYS = [
    Cell("", "#5231DD"),
    Cell("Dynamic", "#F1C232", "#FFFFFF", 2),
    Cell("Static", "#E06666", "#FFFFFF", 2),
    Cell("Precise", "#45818E", "#FFFFFF", 2),
    Cell("Reactive", "#3C78D8", "#FFFFFF", 2),
    Cell("Speed", "#A64D79", "#FFFFFF", 2),
    Cell("Evasive", "#674EA7", "#FFFFFF", 2),
]

OTHER_CATEGORYS = [
    Cell("", "#5231DD"),
    Cell("Clicking", "#CC0000", "#FFFFFF", 6),
    Cell("Tracking", "#1155CC", "#FFFFFF", 6),
    Cell("Switching", "#351C75", "#FFFFFF", 4),
]

OTHER_SUBCATEGORYS = [
    Cell("", "#5231DD"),
    Cell("Dynamic", "#F1C232", "#FFFFFF", 2),
    Cell("Static", "#E06666", "#FFFFFF", 2),
    Cell("Strafe", "#FED0FE", "#FFFFFF", 2),
    Cell("Precise", "#45818E", "#FFFFFF", 2),
    Cell("Reactive", "#3C78D8", "#FFFFFF", 2),
    Cell("Strafe", "#FED0FE", "#FFFFFF", 2),
    Cell("Speed", "#A64D79", "#FFFFFF", 2),
    Cell("Evasive", "#674EA7", "#FFFFFF", 2),
]

NOVICE_SCENARIOS = [
    Cell("Scenario", "#5231DD", "#FFFFFF"),
    Cell("VT Pasu Rasp Novice", "#FFF1AA"),
    Cell("VT Bounceshot Novice", "#FFF1AA"),
    Cell("VT 1w6ts Rasp Novice", "#EA9999"),
    Cell("VT Multiclick 120 Novice", "#EA9999"),
    Cell("VT Smoothbot Novice", "#A2C4C9"),
    Cell("VT PreciseOrb Novice", "#A2C4C9"),
    Cell("VT Plaza Novice", "#A4C2F4"),
    Cell("VT Air Novice", "#A4C2F4"),
    Cell("VT psalmTS Novice", "#D5A6BD"),
    Cell("VT skyTS Novice", "#D5A6BD"),
    Cell("VT evaTS Novice", "#B4A7D6"),
    Cell("VT bounceTS Novice", "#B4A7D6"),
]

NOVICE_BENCHMARKS = [
    [550, 650, 750, 850],
    [500, 600, 700, 800],
    [600, 700, 800, 900],
    [1160, 1260, 1360, 1460],
    [2300, 2500, 3100, 3500],
    [1300, 1600, 1900, 2200],
    [2000, 2300, 2700, 2900],
    [1750, 2050, 2350, 2650],
    [620, 690, 760, 830],
    [780, 860, 950, 1040],
    [450, 510, 560, 620],
    [490, 550, 610, 680],
]

# requires index to relate to benchmarks so list is used
NOVICE_BENCH_COLORS = [
    ["Iron", "#999999", "#EFEFEF"],
    ["Bronze", "#FF9900", "#FCE5CD"],
    ["Silver", "#CBD9E6", "#DCE5EC"],
    ["Gold", "#CAB148", "#E4DAB0"],
]

INTERMEDIATE_SCENARIOS = [
    Cell("Scenario", "#5231DD", "#FFFFFF"),
    Cell("VT Pasu Rasp Intermediate", "#FFF1AA"),
    Cell("VT Bounceshot Intermediate", "#FFF1AA"),
    Cell("VT 1w5ts Rasp Intermediate", "#EA9999"),
    Cell("VT Multiclick 120 Intermediate", "#EA9999"),
    Cell("VT AngleStrafe Intermediate", "#FED0FE"),
    Cell("VT ArcStrafe Intermediate", "#FED0FE"),
    Cell("VT Smoothbot Intermediate", "#A2C4C9"),
    Cell("VT PreciseOrb Intermediate", "#A2C4C9"),
    Cell("VT Plaza Intermediate", "#A4C2F4"),
    Cell("VT Air Intermediate", "#A4C2F4"),
    Cell("VT PatStrafe Intermediate", "#FED0FE"),
    Cell("VT AirStrafe Intermediate", "#FED0FE"),
    Cell("VT psalmTS Intermediate", "#D5A6BD"),
    Cell("VT skyTS Intermediate", "#D5A6BD"),
    Cell("VT evaTS Intermediate", "#B4A7D6"),
    Cell("VT bounceTS Intermediate", "#B4A7D6"),
]

INTERMEDIATE_BENCHMARKS = [
    [750, 850, 950, 1050],
    [600, 700, 800, 900],
    [1000, 1100, 1200, 1300],
    [1360, 1460, 1560, 1660],
    [740, 830, 920, 1000],
    [660, 750, 850, 940],
    [3050, 3450, 3850, 4250],
    [1700, 2100, 2500, 2900],
    [2680, 2980, 3280, 3530],
    [2450, 2700, 2950, 3200],
    [2260, 2620, 2800, 3050],
    [2800, 3000, 3200, 3400],
    [810, 880, 950, 1020],
    [1030, 1130, 1220, 1300],
    [550, 600, 650, 700],
    [630, 670, 710, 760],
]

INTERMEDIATE_BENCH_COLORS = [
    ["Platinum", "#2FCFC2", "#A8E2EA"],
    ["Diamond", "#A8E4FD", "#E7FAFF"],
    ["Jade", "#79EB8F", "#CEFDCE"],
    ["Master", "#D647CD", "#F8C0ED"],
]

ADVANCED_SCENARIOS = [
    Cell("Scenario", "#5231DD", "#FFFFFF"),
    Cell("VT Pasu Rasp Advanced", "#FFF1AA"),
    Cell("VT Bounceshot Advanced", "#FFF1AA"),
    Cell("VT 1w3ts Rasp Advanced", "#EA9999"),
    Cell("VT Multiclick 180 Advanced", "#EA9999"),
    Cell("VT AngleStrafe Advanced", "#FED0FE"),
    Cell("VT ArcStrafe Advanced", "#FED0FE"),
    Cell("VT Smoothbot Advanced", "#A2C4C9"),
    Cell("VT PreciseOrb Advanced", "#A2C4C9"),
    Cell("VT Plaza Advanced", "#A4C2F4"),
    Cell("VT Air Advanced", "#A4C2F4"),
    Cell("VT PatStrafe Advanced", "#FED0FE"),
    Cell("VT AirStrafe Advanced", "#FED0FE"),
    Cell("VT psalmTS Advanced", "#D5A6BD"),
    Cell("VT skyTS Advanced", "#D5A6BD"),
    Cell("VT evaTS Advanced", "#B4A7D6"),
    Cell("VT bounceTS Advanced", "#B4A7D6"),
]

ADVANCED_BENCHMARKS = [
    [940, 1040, 1120, 1180],
    [800, 900, 1000, 1060],
    [1280, 1380, 1460, 1510],
    [1680, 1820, 1940, 2000],
    [880, 1020, 1150, 1190],
    [940, 1080, 1150, 1190],
    [3300, 3600, 3950, 4060],
    [2500, 2850, 3250, 3350],
    [3275, 3475, 3600, 3679],
    [3050, 3350, 3600, 3700],
    [3050, 3240, 3400, 3450],
    [3400, 3600, 3700, 3800],
    [1080, 1160, 1200, 1220],
    [1300, 1450, 1500, 1540],
    [680, 740, 780, 810],
    [820, 920, 970, 1000],
]

ADVANCED_BENCH_COLORS = [
    ["Grandmaster", "#E7CC17", "#FFF1AA"],
    ["Nova", "#6E0AFD", "#C089FF"],
    ["Astra", "#E7296F", "#FF89AA"],
    ["Celestial", "#010A17", "#999999"],
]
