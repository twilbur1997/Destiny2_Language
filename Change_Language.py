from os import listdir, mkdir, getcwd, chdir
from os.path import join, isfile, exists, isdir
from shutil import copy2


D2_packages = "C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages"
lang_dir = "languages"

lang_dict = {
    "en":"english",
    "de": "german",
    "sp": "spanish"
}


'''
Thanks to others who have explored local language hacks with Destiny 2's files
https://steamcommunity.com/app/1085660/discussions/0/1628539187763929500

Download the latest Python here:
https://www.python.org/downloads/

C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages


Likely one program to create a backup of the current language,
and another program to actually shift between established backups

Biggest issue is how to change text in the UI without changing Steam settings


The recommended usage of this app is to change the language of the game on Steam to the audio language that you'd like.
Then, save those files using the program.

Then, set the language in Steam to the language you want for the UI.

Finally, you can use the program to set the audio language to your preferred language.
'''

def get_max(num_dict):
    # TODO replace with comparing dict values instead of if statements

    if num_dict["en"] > num_dict["de"] and num_dict["en"] > num_dict["sp"]:
        lang_true = input("English is the current selected language. Is this true? (y/n): ")
        if lang_true == "y":
            return "en"

    if num_dict["de"] > num_dict["en"] and num_dict["de"] > num_dict["sp"]:
        lang_true = input("German is the current selected language. Is this true? (y/n): ")
        if lang_true == "y":
            return "de"

    if num_dict["sp"] > num_dict["en"] and num_dict["sp"] > num_dict["de"]:
        lang_true = input("Spanish is the current selected language. Is this true? (y/n): ")
        if lang_true == "y":
            return "sp"

    lang = input("Can't tell which language is being used, please enter one (en, de, sp): ")
    while lang not in lang_dict:
        lang = input("Invalid input, please enter the language abreviation (en, de, sp): ")

    if num_dict[lang] == 0:
        confirm = input("No files were found for this language, are you sure that is your langauge? (y/n): ")

    return lang


def get_language():
    file_list = listdir(D2_packages)
    file_list_audio = [x for x in file_list if "audio" in x]

    print("Found the following number of files for each language:")
    for abrv in lang_dict.keys():
        file_list_lang = [x for x in file_list if abrv in x]
        num_dict[abrv] = len(set(file_list_lang) & set(file_list_audio))
        print(abrv, " ", num_dict[abrv])

    print("\n")

    lang = get_max(num_dict)
    return lang


def backup_audio_files(dir_name, lang_abrev):
    print("\nCreating Language Backup...\n\nThis may take up to 10 seconds...\n\n\n")

    if not isdir(dir_name):
        mkdir(dir_name)

    print(dir_name, lang_abrev)
    print(getcwd())

    file_list = listdir(D2_packages)
    file_list_lang = [x for x in file_list if lang_abrev in x]
    file_list_audio = [x for x in file_list if "audio" in x]
    file_set = set(file_list_lang) & set(file_list_audio)

    pack_prefix = D2_packages+"\\" # Need to use double \ to escape just one
    lang_prefix = D2_packages.replace("packages", lang_dir)+"\\"+dir_name+"\\"
    for file in file_set:
        file_src = pack_prefix+file
        file_dest = lang_prefix+file
        copy2(file_src, file_dest)


def create_language_backup():
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

        # Check which language the user currently has selected
        selected_lang = get_language()

        # Copy the audio files over
        chdir(lang_dir)
        selected_lang_dir = lang_dict[selected_lang]+"_audio"

        backup_audio_files(selected_lang_dir, selected_lang)


    else:
        print("\nSkipping backup step")

    # TODO:
    # Copy the text files over
def restore_language_backup():
    print("TODO")


def main():
    print("\nWelcome to the Destiny 2 Local Language Changer!")
    print("Would you like to: ")
    print("1. Backup current audio language \nor")
    response = input("2. Restore Audio\n")

    if "1" in response:
        create_language_backup()

    if "2" in response:
        restore_language_backup()


if __name__ == "__main__":
    main()

# End of file
