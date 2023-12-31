FILEPATH = "todo_list.txt"


def read_todo_list(filepath=FILEPATH):
    with open(filepath, "r") as local_file:
        local_todo_list = local_file.readlines()
    return local_todo_list


def write_todo_list(todo_list_arg, filepath=FILEPATH):
    with open(filepath, "w") as write_file:
        write_file.writelines(todo_list_arg)
