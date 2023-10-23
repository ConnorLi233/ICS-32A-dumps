# File System
# This program will function as a file system, including functions such as path display, 

from pathlib import Path 
import os

def show_directory(path: Path) -> list:
    directory = list(path.iterdir())
  
      
    return directory


def show_subdirectory(path: Path) -> list:
    directory = list(path.iterdir())
    subs = []
    
    for element in directory:
        if element.is_dir():
            subs.append(show_subdirectory(element))
        else:
            subs.append(element)

    return subs


def print_paths(paths: list) -> None:
    for element in paths:
        if type(element) == list:
            print_paths(element)
        else:
            print(element)


def interesting_files(pre_input: str) -> list:
    pre_path = Path(pre_input[2:])
    if pre_input.startswith('D'):
        return show_directory(pre_path)
    elif pre_input.startswith('R'):
        return show_subdirectory(pre_path)


def filename_search(filename: str, range: list) -> list:
    files = []
    for file in range:
        if file.is_dir():
            range = list(file.iterdir())
            files.append(filename_search(filename, range))
        else:  
            if file.name == filename:
                files.append(file)
    
    return files


def extension_search(path: list, exten: str) -> None:
    for element in path:
        if element.is_dir():
            path = list(element.iterdir())        
            extension_search(path, exten)
        else:
            file_extension = os.path.splitext(element)
            
            if file_extension[1][1:] == exten or file_extension[1] == exten:
                print(element)


def text_search(path: Path, text: str) -> list:
    files = []
    for element in path:
        if element.is_dir():
            path = list(element.iterdir())        
            files.append(text_search(path, text))
        else:
            try:
                file = open(element, 'r')
                for line in file:
                    if text in line:
                        files.append(element)
            except:
                pass
    
    return files





previous_input = []
previous_path = []

def run():
    user_input = str(input("Enter: "))
    path = Path(user_input[2:])
    
    if user_input.startswith('D'):
        print_paths(show_directory(path))
        previous_input.append(user_input)
        previous_path.append(Path(user_input[2:]))
        run()
    elif user_input.startswith('R'):
        print_paths(show_subdirectory(path))
        previous_input.append(user_input)
        previous_path.append(Path(user_input[2:]))
        run()
    elif user_input == 'A':
        interesting_files(previous_input)
        run()
    elif user_input.startswith('N'):
        filename = str(user_input[2:])
        search_range = show_directory(previous_path[0])
        print_paths(filename_search(filename, search_range))
        run()
    elif user_input.startswith('E'):
        extension = user_input.split(' ')[-1]
        print(extension)
        extension_search(show_directory(previous_path[0]), extension)
    elif user_input.startswith('T'):
        text = user_input[2:]
        print_paths(text_search(show_directory(previous_path[0]), text))


    
        





if __name__ == '__main__':
    run()


