import json

def remove_newline(string):
    """Remove the newline character from the end of a string."""
    return string.rstrip('\n')

def get_line_in_file(file_path, line_number):
    """Takes a file path and line number and returns the contents of the file on that line"""
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line.strip() 
    print("error out of range")
    return None 
def get_plant_specs(id):
    return json.loads(get_line_in_file("plants.txt",id))



print(get_plant_specs(2))