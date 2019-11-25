import os
from shutil import copyfile

root_src_dir = os.path.dirname(os.path.abspath(__file__))
root_target_dir = "/Users/nabiharaza/PycharmProjects/MoveDirectory/Destination_Folder"


def move_folder(file_path, session_id):
    target = root_target_dir + "/" + str(session_id)
    if not os.path.isdir(target):
        os.mkdir(target)

    main_path = target + os.path.dirname(file_path)
    print(main_path)

    # making directory
    if not os.path.exists(main_path):
        os.makedirs(main_path)

    # extract file name
    file_name = str(file_path.rsplit('/', 1)[1])
    print(file_name)

    # copying file from src to dest
    copyfile(file_path, main_path + '/' + file_name)


if __name__ == '__main__':
    file_path = "/Users/nabiharaza/Desktop/Test_Directory/Folder A/Folder 1A/AOS-SW-Access Security Guide-v16.05.pdf"
    session_id = 12312
    move_folder(file_path, session_id)
