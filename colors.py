import re
#The reset and getting rid of colors 
reset = "\033[0m"
ansi_escape = re.compile(r'\033\[\d+m')

#Colors for text and font
text_black = "\033[30m"
text_red = "\033[31m"
text_green = "\033[32m"
text_yellow = "\033[33m"
text_blue = "\033[34m"
text_magenta = "\033[35m"
text_cyan = "\033[36m"
text_white = "\033[37m"
text_bright_black = "\033[90m"
text_bright_red = "\033[91m"
text_bright_green = "\033[92m"
text_bright_yellow = "\033[93m"
text_bright_blue = "\033[94m"
text_bright_magenta = "\033[95m"
text_bright_cyan = "\033[96m"
text_bright_white = "\033[97m"

#colors for pixels (highlight)
red = "\033[41m"
green = "\033[42m"
yellow = "\033[43m"
blue = "\033[44m"
magenta = "\033[45m"
cyan = "\033[46m"
white = "\033[47m"
black = "\033[40m"
purple = "\033[48;5;54m"
#brigh colors for pixels (highlight)
bright_black = "\033[100m"
bright_red = "\033[101m"
bright_green = "\033[102m"
bright_yellow = "\033[103m"
bright_blue = "\033[104m"
bright_magenta = "\033[105m"
bright_cyan = "\033[106m"
bright_white = "\033[107m"
bright_purple = "\033[105m"
bright_orange = "\033[101m"
bright_lime = "\033[102m"
bright_teal = "\033[104m"
bright_pink = "\033[105m"

#Rainbow colors
rainbow = [red, green, yellow, blue, magenta, cyan, white]
rainbow_bright = [bright_red, bright_orange, bright_yellow, bright_green, bright_blue, bright_purple]

