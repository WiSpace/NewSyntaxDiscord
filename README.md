# NewSyntaxDiscord
New syntax in Discord.

For help type `main -h` or `main --help`

Usage: Go to syntax.py and in the tokens dictionary, the key is the regular expression and the value is the color that the regular expression will be colored with. In colors.py all colors for code.

Example:

```py
from colors import Colors

tokens = {
    # regex: color
    r"\".*\"": Colors.green,
    r"use": Colors.red,
    r"print|stop": Colors.blue
}
```

|Text |Color  |
--- | --- |
|"any"|green|
|use|red|
|print or stop|blue|
