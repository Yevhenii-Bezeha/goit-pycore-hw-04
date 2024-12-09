import sys
from pathlib import Path
from colorama import init, Fore, Style

init()

def print_directory_structure(directory_path, indent_level=0):
    try:
        entries = sorted(Path(directory_path).iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        for entry in entries:
            indent = ' ' * 4 * indent_level
            if entry.is_dir():
                print(f"{indent}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
                print_directory_structure(entry, indent_level + 1)
            else:
                print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Доступ заборонено: {directory_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python {sys.argv[0]} /шлях/до/директорії{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}Структура директорії '{directory_path}':{Style.RESET_ALL}")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
