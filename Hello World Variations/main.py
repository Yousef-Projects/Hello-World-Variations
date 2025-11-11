from colorama import Fore, Style, init
init()

text = "Hello World"
colors = [Fore.WHITE, Fore.GREEN]
print(Style.BRIGHT + "".join(colors[i % 2] + c for i, c in enumerate(text)))
