from os import listdir, mkdir, getcwd, chdir
from os.path import join, isfile, exists, isdir
from shutil import copy2


D2_packages = "C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages"
lang_dir = "languages"


'''
Thanks to others who have explored local language hacks with Destiny 2's files
https://steamcommunity.com/app/1085660/discussions/0/1628539187763929500

Download the latest Python here:
https://www.python.org/downloads/

C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages


Likely one program to create a backup of the current language,
and another program to actually shift between established backups

Biggest issue is how to change text in the UI without changing Steam settings

'''


def backup_german_audio_files():
    # Starting with just copying English audio files
    de_dir = "german_audio"
    if not isdir(de_dir):
        mkdir(de_dir)

    file_list = listdir(D2_packages)
    file_list_de = [x for x in file_list if "de" in x]
    file_list_audio = [x for x in file_list if "audio" in x]
    file_set = set(file_list_de) & set(file_list_audio)

    pack_prefix = D2_packages+"\\" # Need to use double \ to escape just one
    lang_prefix = D2_packages.replace("packages", lang_dir)+"\\"+de_dir+"\\"
    for file in file_set:
        file_src = pack_prefix+file
        file_dest = lang_prefix+file
        copy2(file_src, file_dest)


def backup_english_audio_files():
    # Starting with just copying English audio files
    en_dir = "english_audio"
    if not isdir(en_dir):
        mkdir(en_dir)

    file_list = listdir(D2_packages)
    file_list_en = [x for x in file_list if "en" in x]
    file_list_audio = [x for x in file_list if "audio" in x]
    file_set = set(file_list_en) & set(file_list_audio)

    pack_prefix = D2_packages+"\\" # Need to use double \ to escape just one
    lang_prefix = D2_packages.replace("packages", lang_dir)+"\\"+en_dir+"\\"
    for file in file_set:
        file_src = pack_prefix+file
        file_dest = lang_prefix+file
        # print(file_src, "\n", file_dest, "\n\n")
        copy2(file_src, file_dest)


def create_language_backup():
    print("\nCreating Language Backup...\n\nThis may take up to 10 seconds...\n\n\n")

    # Check for languages directory
    chdir(D2_packages)
    chdir("..")
    if not isdir(lang_dir):
        mkdir(lang_dir)

    copy_wanted = input("\n\nWould you like to backup the current audio files? (y/n): ")
    count = 0
    skip_copy = False
    while copy_wanted!="y":
        if copy_wanted == "n":
            skip_copy = True
            break
        copy_wanted = input("\nInvalid Response... \nWould you like to backup the current audio files? (y/n): ")
        count +=1
        if count>2:
            print("Invalid input 3 times in a row, exiting program")
            sys.exit()

    if not skip_copy:
        print("You've chosen to backup the current audio files. \n")
        # lang_selected = input("What language are you currently using? (en, de, sp):")

        # Copy the audio files over
        chdir(lang_dir)
        backup_english_audio_files()

    else:
        print("\nSkipping backup step")

    # TODO:
    # Copy the text files over


def main():
    print("Welcome to the Destiny 2 Local Language Changer!")
    print("Let's change directories to the Destiny 2 packages\n\n")

    create_language_backup()




if __name__ == "__main__":
    main()

# End of file
