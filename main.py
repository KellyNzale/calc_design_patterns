from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def print_menu(commands):
    print("Available commands:")
    for cmd in commands:
        print(f" - {cmd}")

def main():
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
    }

    print_menu(commands)
    
    while True:
        user_input = input("\nEnter command and numbers (or 'menu' to show commands, 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if user_input.lower() == 'menu':
            print_menu(commands)
            continue
        
        parts = user_input.split()
        if not parts:
            continue
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        if cmd not in commands:
            print(f"Unknown command: {cmd}")
            continue
        
        try:
            result = commands[cmd].execute(*args)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
