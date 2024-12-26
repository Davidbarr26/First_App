Filepath = 'files/App.txt'

def get_todos(filepath=Filepath):
    """ Read a text file and return the data store in a list of To-Do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=Filepath):
    """ Write the to-do items and store the data in a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())