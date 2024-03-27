from colorama import Fore, Back, Style

def cprint(text, color):
  """Prints text in a specified color.

  Args:
    text: The text to print.
    color: The color to print the text in.
  """

  color_codes = {
      'black': Fore.BLACK,
      'red': Fore.RED,
      'green': Fore.GREEN,
      'yellow': Fore.YELLOW,
      'blue': Fore.BLUE,
      'magenta': Fore.MAGENTA,
      'cyan': Fore.CYAN,
      'white': Fore.WHITE,
  }

  print(color_codes[color] + text + Style.RESET_ALL)
