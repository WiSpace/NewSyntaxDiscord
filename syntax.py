from colors import Colors

tokens = {
    # regex: color
    r"\".*\"": Colors.green,
    r"use": Colors.red,
    r"print|stop": Colors.blue
}