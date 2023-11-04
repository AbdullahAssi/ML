# Import statements: 
# 1. Import the built-in json python package
# 2. From employee.py, import the details function and the employee_name, age, title variables

import json
from employee import details, employee_name, age, title
def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    [IMPLEMENT ME]
        1. Return a dictionary that maps "first_name" to name (string), "age" to age (int), and "title" to title (string)

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments with correct data types.
    """
    employee_dict = {
        "first_name": str(name),  # Ensure name is converted to a string
        "age": int(age),          # Ensure age is converted to an integer
        "title": str(title)       # Ensure title is converted to a string
    }
    return employee_dict


def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    [IMPLEMENT ME]
        1. Open a new file defined by output_file
        2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    with open(output_file, 'w') as file:
        file.write(json_obj)

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()
