import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for file in files:
            current_dir = os.path.join(d, file)
            if os.path.isdir(current_dir):
                print("\t"*tab_stop + "Directory " + file)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + file)

    tab_stop = 0
    if os.path.exists(s):
        print(f'Directory listing of {s}')
        dir_list(s)
    else:
        print(f"{s} does not exist")


list_directories('.')

# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)
