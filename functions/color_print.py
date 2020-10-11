# Some ANSI escape sequences for colours and effects
import colorama


BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """Prints text with specified effect

    Args:
        text (str): text to print
        effect (str): effect to use
    """
    effect_string = "".join(effects)
    output_string = f"{effect_string} {text},{RESET}"
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED, BOLD)
colour_print("Hello, Red", RED)
colour_print("Hello, Red", RED, UNDERLINE, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()
