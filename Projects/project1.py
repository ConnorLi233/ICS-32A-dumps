# File System
# This program will function as a file system, including functions such as 
# path display, file search, and file editing.

from pathlib import Path 
import os
import shutil

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
    list_of_paths = []
    for element in paths:
        if type(element) == list:
            print_paths(element)
        else:
            list_of_paths.append(str(element))
    list_of_paths.sort()
    for path in list_of_paths:
        print(path)


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
    files = []
    for element in path:
        if element.is_dir():
            path = list(element.iterdir())        
            files.append(extension_search(path, exten))
        else:
            file_extension = os.path.splitext(element)
            if file_extension[1][1:] == exten or file_extension[1] == exten:
                files.append(element)
    
    return files


def text_search(path: list, text: str) -> list:
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


def larger_size(path: list, size: int) -> list:
    files = []
    for element in path:
        if element.is_dir():
            path = list(element.iterdir())
            files.append(larger_size(path, size))
        else:     
            file_size = os.path.getsize(element)
            if file_size > size:
                files.append(element)

    return files


def smaller_size(path: list, size: int) -> list:
    files = []
    for element in path:
        if element.is_dir():
            path = list(element.iterdir())
            files.append(smaller_size(path, size))
        else:     
            file_size = os.path.getsize(element)
            if file_size < size:
                files.append(element)

    return files


def first_line_print(files: list) -> None:
    for file in files:
        if type(file) == list:
            first_line_print(file)
        else:   
            file = open(file, 'r')
            first_line = file.readline()
            if first_line is True:
                print(first_line)
            else:
                print('NOT TEXT')
            

def duplicate_file(files: list) -> None:
    for file in files:
        if type(file) == list:
            duplicate_file(file)
        else:
            shutil.copy(file, f'{file}.dup')

            
def touch_file(files: list) -> None:
    for file in files:
        if type(file) == list:
            touch_file(file)
        else:
            os.utime(file, None)
            
    
previous_input = []
previous_path = []
narrowed_down_files = []

def run():
    user_input = str(input("Enter: "))
    path = Path(user_input[2:])
    

    if user_input.startswith('D '): 
        print_paths(show_directory(path))
        previous_input.append(user_input)
        previous_path.append(Path(user_input[2:]))
        run()

    elif user_input.startswith('R '):
        print_paths(show_subdirectory(path))
        previous_input.append(user_input)
        previous_path.append(Path(user_input[2:]))
        run()

    elif user_input == 'A':
        interesting_files(previous_input)
        run()

    elif user_input.startswith('N '):
        filename = str(user_input[2:])
        search_range = show_directory(previous_path[0])
        searched_files = filename_search(filename, search_range)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()
        
    elif user_input.startswith('E '):
        extension = user_input.split(' ')[-1]
        searched_files = extension_search(show_directory(previous_path[0]), extension)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()

    elif user_input.startswith('T '):
        text = user_input[2:]
        searched_files = text_search(show_directory(previous_path[0]), text)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()

    elif user_input.startswith('> '):
        size = int(user_input[2:])
        larger_files = larger_size(show_directory(previous_path[0]), size)
        print_paths(larger_files)
        narrowed_down_files.append(larger_files)
        run()
        
    elif user_input.startswith('< '):
        size = int(user_input[2:])
        smaller_files = smaller_size(show_directory(previous_path[0]), size)
        print_paths(smaller_files)
        narrowed_down_files.append(smaller_files)
        run()

    elif user_input == 'F' and len(narrowed_down_files) != 0:
        first_line_print(narrowed_down_files)

    elif user_input == 'D' and len(narrowed_down_files) != 0:
        duplicate_file(narrowed_down_files)
    
    elif user_input == 'T' and len(narrowed_down_files) != 0:
        touch_file(narrowed_down_files)
    
    else:
        # If the input does not follow the correct the format, show an error message,
        # and ask for user input until the input is valid.
        print('ERROR')
        run()


if __name__ == '__main__':
    run()



