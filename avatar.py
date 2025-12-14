import os
from colorama import init, Fore

init(autoreset=True)

def center_text(text, width=None):
    if width is None:
        try:
            width = os.get_terminal_size().columns
        except:
            width = 80
    
    centered_lines = []
    for line in text.split('\n'):
        clean_line = line.replace(Fore.RED, '').replace('\033[0m', '')
        padding = max(0, (width - len(clean_line)) // 2)
        centered_lines.append(' ' * padding + line)
    
    return '\n'.join(centered_lines)

os.system('cls' if os.name == 'nt' else 'clear')

print("\n" * 15)

no_data = f"""{Fore.RED}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  ███╗   ██╗ ██████╗        ██████╗  █████╗ ████████╗ █████╗               ║
║  ████╗  ██║██╔═══██╗      ██╔════╝ ██╔══██╗╚══██╔══╝██╔══██╗              ║
║  ██╔██╗ ██║██║   ██║█████╗██║  ███╗███████║   ██║   ███████║              ║
║  ██║╚██╗██║██║   ██║╚════╝██║   ██║██╔══██║   ██║   ██╔══██║              ║
║  ██║ ╚████║╚██████╔╝      ╚██████╔╝██║  ██║   ██║   ██║  ██║              ║
║  ╚═╝  ╚═══╝ ╚═════╝        ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝              ║
║                                                                           ║
║  ══════════════════════════════════════════════════════════════════════   ║
║  [ ERROR 0x7F ] • [ DATA NOT FOUND ] • [ SYSTEM OFFLINE ]                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

centered_output = center_text(no_data)
print(centered_output)

print("\n" * 5)

try:
    cols = os.get_terminal_size().columns
    prompt = "Press Enter to exit..."
    padding = max(0, (cols - len(prompt)) // 2)
    input(' ' * padding + prompt)
except:
    input("Press Enter to exit...")