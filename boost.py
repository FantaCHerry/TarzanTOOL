import webbrowser
import ctypes
from colorama import init, Fore, Style
import os

# Initialize Colorama
init(autoreset=True)

def set_window_title(title):
    """Sets the window title on Windows."""
    if os.name == 'nt':  # Check if the operating system is Windows
        ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear_console():
    """Clears the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_invite():
    """Displays the invitation message and opens the URL."""
    clear_console()
    set_window_title("TARZAN | INVITE")
    
    print(Fore.LIGHTCYAN_EX + """
██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔═══██╗╚══██╔══╝
██████╔╝███████║██████╔╝██║██╔██╗ ██║██║   ██║   ██║   
██╔═══╝ ██╔══██║██╔══██╗██║██║╚██╗██║██║   ██║   ██║   
██║     ██║  ██║██║  ██║██║██║ ╚████║╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   
    """ + Style.RESET_ALL)
    
    print(Fore.LIGHTGREEN_EX + "Join our Discord server for more support and updates!" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "Opening your browser to the Discord server..." + Style.RESET_ALL)
    
    # Open the Discord server URL in the default web browser
    url = "https://discord.gg/AxJJTGtZQh"
    webbrowser.open(url)

def main():
    """Main function to run the invite script."""
    print_invite()

if __name__ == "__main__":
    main()
