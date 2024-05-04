import json
import ast

def remove_newline(string):
    """Remove a newline character from the end of a string."""
    return string.rstrip('\n')

def get_line_in_file(file_path, line_number):
    """Takes a file path and line number and returns the contents of the file on that line"""
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                try:
                    return json.loads(line.strip()) 
                except:
                    return ast.literal_eval(line.strip())
    print(f"error {line_number} out of range in {file_path}")
    return None 

def overwrite_line(file_path, line_number, new_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print(f"Line number '{line_number}' is out of range.")
        return
    new_content_str = str(new_content)
    
    lines[line_number - 1] = new_content_str + '\n'
    
    with open(file_path, 'w') as file:
        file.writelines(lines)
        
    print(f"Line {line_number} overwritten successfully.")