import json

def remove_newline(string):
    """Remove the newline character from the end of a string."""
    return string.rstrip('\n')

def get_line_in_file(file_path, line_number):
    """Takes a file path and line number and returns the contents of the file on that line"""
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return json.loads(line.strip()) 
    print("error out of range")
    return None 

def overwrite_line(file_path, line_number, new_content):
    with open(file_path, 'r') as file:
            lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print(f"Line number '{line_number}' is out of range.")
        return
    lines[line_number - 1] = new_content + '\n'
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"Line {line_number} overwritten successfully.")