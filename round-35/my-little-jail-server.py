flag = "ictf{REDACTED}"

def execute():
    try:
        command = input("> ")
        if command in ['exit', 'quit']:
            return False

        # Disallow certain keywords and built-in methods
        disallowed = ['.','help','print', '__', 'import', 'eval', 'exec', 'os', 'sys', 'open']
        if any(x in command for x in disallowed):
            print("Error: Command not allowed!")
            return True
        
        # Execute command
        result = exec(command)
        if result:
            print(result)
        return True
    except Exception as e:
        print(f"Error")
        return True

if __name__ == "__main__":
    print("Welcome to the Python Jail! You can execute any Python command.")
    print("The goal is to reveal the flag. Type 'exit' or 'quit' to leave.")
    while execute():
        pass
