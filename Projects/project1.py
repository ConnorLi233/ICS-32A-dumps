# project1.py
#
# ICS 32A Fall 2023
# Project #1: Digging in the Dirt
#
# This program will work as a file system, including functions such as 
# directory/subdirectory display, file search, and file editing.

from pathlib import Path 
import os
import shutil

def show_directory(path: Path) -> list:
    '''Finds and returns all the files under the directory'''
    directory = list(path.iterdir())
    mains = []
    subs = []
    paths = []

    for element in directory:
        if element.is_dir():
            subs.append(element)
        else:
            mains.append(element)
    
    sorted(mains)
    sorted(subs)
    paths.append(mains)
    paths.append(subs)
    return paths


def show_subdirectory(path: Path) -> list:
    '''Finds and returns all the files under the directory and its subdirectories'''
    directory = list(path.iterdir())
    subs = []
    mains = []
    paths = []
    
    for element in directory:
        if element.is_dir():
            subs.append(show_subdirectory(element))
        else:
            mains.append(element)
        
    sorted(mains)
    sorted(subs)
    paths.append(mains)
    paths.append(subs)
    return paths


def print_paths(paths: list) -> None:
    '''Prints out all the paths in the list with the correct format'''
    for element in paths:
        if type(element) == list:
            print_paths(element)
        else:
            print(element)
        


def interesting_files(pre_input: str) -> list:
    '''Finds and returns all the files found in the previous step'''
    pre_path = Path(pre_input[2:])
    if pre_input.startswith('D'):
        return show_directory(pre_path)
    elif pre_input.startswith('R'):
        return show_subdirectory(pre_path)


def filename_search(filename: str, range: list) -> list:
    '''Finds and returns all the files that match a particular name'''
    files = []
    for file in range:
        if type(file) == list:
            files.append(filename_search(filename, file))
        else:  
            if file.name == filename:
                files.append(file)
    
    return files


def extension_search(path: list, exten: str) -> list:
    '''Finds and returns all the files that have a particular extension'''
    files = []
    for element in path:
        if type(element) == list:
            files.append(extension_search(element, exten))
        else:
            file_extension = os.path.splitext(element)
            if file_extension[1][1:] == exten or file_extension[1] == exten:
                files.append(element)
    
    return files


def text_search(path: list, text: str) -> list:
    '''Finds and returns all the files that contain a particular text'''
    files = []
    for element in path:
        if type(element) == list:
            files.append(text_search(element, text))
        else:
            try:
                file = open(element, 'r')
                for line in file:
                    if text in line and element not in files:
                        files.append(element)
            except:
                pass
    
    return files


def larger_size(path: list, size: int) -> list:
    '''Finds and returns all the files whose size is larger than the threshold, measured in bytes'''
    files = []
    for element in path:
        if type(element) == list:
            files.append(larger_size(element, size))
        else:     
            file_size = os.path.getsize(element)
            if file_size > size:
                files.append(element)

    return files


def smaller_size(path: list, size: int) -> list:
    '''Finds and returns all the files whose size is smaller than the threshold, measured in bytes'''
    files = []
    for element in path:
        if type(element) == list:
            files.append(smaller_size(element, size))
        else:     
            file_size = os.path.getsize(element)
            if file_size < size:
                files.append(element)

    return files


def first_line_print(files: list) -> None:
    '''Prints the first line of text from the file if it's a text file; print 'NOT TEXT' if it's not'''
    for file in files:
        if type(file) == list:
            first_line_print(file)
        else:   
            file = open(file, 'r')
            first_line = file.readline()
            if first_line:
                print(first_line, end = '')
            else:
                print('NOT TEXT')
            

def duplicate_file(files: list) -> None:
    '''Makes a duplicate copy of the file with '.dup' appended to the filename, 
    stores it in the same directory as the original file'''
    for file in files:
        if type(file) == list:
            duplicate_file(file)
        else:
            shutil.copy(file, f'{file}.dup')

            
def touch_file(files: list) -> None:
    '''Modifies the file's last modified timestamp to be the current date/time'''
    for file in files:
        if type(file) == list:
            touch_file(file)
        else:
            os.utime(file, None)
            
# Lists to store the user's previous input, 
# or the files found in the previous step
previous_input = []
previous_path = []
narrowed_down_files = []

def run():
    '''Calls different functions according to user's input'''
    user_input = str(input(""))
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

    elif user_input == 'A' and len(previous_input) != 0:
        print_paths(interesting_files(previous_input[-1]))
        run()

    elif user_input.startswith('N ') and len(previous_path) != 0:
        filename = str(user_input[2:])
        search_range = show_subdirectory(previous_path[-1])
        searched_files = filename_search(filename, search_range)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()
        
    elif user_input.startswith('E ') and len(previous_path) != 0:
        extension = user_input.split(' ')[-1]
        searched_files = extension_search(show_subdirectory(previous_path[-1]), extension)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()

    elif user_input.startswith('T ') and len(previous_path) != 0:
        text = user_input[2:]
        searched_files = text_search(show_subdirectory(previous_path[-1]), text)
        print_paths(searched_files)
        narrowed_down_files.append(searched_files)
        run()

    elif user_input.startswith('> ') and len(previous_path) != 0:
        size = int(user_input[2:])
        larger_files = larger_size(show_subdirectory(previous_path[-1]), size)
        print_paths(larger_files)
        narrowed_down_files.append(larger_files)
        run()
        
    elif user_input.startswith('< ') and len(previous_path) != 0:
        size = int(user_input[2:])
        smaller_files = smaller_size(show_subdirectory(previous_path[-1]), size)
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
        # If the input does not follow the correct format, show an error message,
        # and continue asking for user input until the input is valid
        print('ERROR')
        run()


if __name__ == '__main__':
    run()



