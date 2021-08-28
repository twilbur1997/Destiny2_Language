from os import listdir, mkdir, getcwd, chdir, rename
from os.path import join, isfile, exists, isdir
from shutil import copy2
from operator import itemgetter


D2_packages = "C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages"
lang_dir = "languages"

lang_dict = {
    "en":"english",  # 42 files x
    "fr": "french",  # 43 files x
    "de": "german",  # 43 files x
    "it": "italian",  # 45 files x
    "jpn": "japanese",  # 44 files x
    "pt": "br_portuguese",  # 44 files x
    "sp": "sp_spanish",  # 44 files x
    "ru": "russian",  # 43 files x
    "po": "polish",  # 43 files x
    "cs": "sim_chinese",  # 31 files x
    "ct": "tra_chinese",  # 31 files x
    "mx": "mx_spanish",  # 43 files x
    "ko": "korean"  # 45 files x
}


'''
Thanks to others who have explored local language hacks with Destiny 2's files
https://steamcommunity.com/app/1085660/discussions/0/1628539187763929500


Likely one program to create a backup of the current language,
and another program to actually shift between established backups

Biggest issue is how to change text in the UI without changing Steam settings


The recommended usage of this app is to change the language of the game on Steam to the audio language that you'd like.
Then, save those files using the program.

Then, set the language in Steam to the language you want for the UI.

Finally, you can use the program to set the audio language to your preferred language.


TODO: Make a matrix showing which languages have which files

File Lang en mx sp pt jpn
123       x  x  x  x  x
124       x  x  x
125       x  x     x  x
'''

def no_files_found_warning():
    confirm = input("No files were found for this language, are you sure that is your langauge? (y/n): ")
    if "n" in confirm:
        print("Exiting program")
        exit()


def get_lang_from_user():
    print_langs = ""
    for abrv in lang_dict.keys():
        print_langs = print_langs+abrv+", "
    print(print_langs[:-2], end="")
    lang = input("): ")

    while lang not in lang_dict:
        print_langs = ""
        print("Invalid input, please enter the language abreviation (", end="")
        for abrv in lang_dict.keys():
            print_langs = print_langs+abrv+", "
        print(print_langs[:-2], end="")
        lang = input("): ")
    return lang


def get_max(num_dict):
    num_dict["en"] = num_dict["en"] - 40 # English never gets deleted by Steam, so we need to correct this number
    abrv = max(num_dict.items(), key=itemgetter(1))[0]

    print("It looks like this is your language: ", lang, "\n\nIs that correct?", end="")
    confirmed = input(" (y/n): ")
    if "y" in confirmed:
        return abrv

    print("Can't tell which language is being used...")
    print("Please enter the language you are using (", end="")
    abrv = get_lang_from_user()

    if num_dict[abrv] == 0:
        no_files_found_warning()
    return abrv


def get_language():
    file_list = listdir(D2_packages)
    file_list_audio = [x for x in file_list if "audio" in x]
    num_dict = {}

    print("Found the following number of files for each language:")
    for abrv in lang_dict.keys():
        file_list_lang = [x for x in file_list if abrv in x]
        num_dict[abrv] = len(set(file_list_lang) & set(file_list_audio))
        print(abrv, " ", num_dict[abrv])
    print("\n")

    abrv = get_max(num_dict)
    return abrv


# Copies over all files with the language abreviation as well as audio in the name
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

    print("You've chosen to backup the current audio files. \n")

    # Check which language the user currently has selected
    selected_lang_abrv = get_language()

    # Copy the audio files over
    chdir(lang_dir)
    selected_lang_dir = lang_dict[selected_lang]+"_audio"

    backup_audio_files(selected_lang_dir, selected_lang)


def restore_language_backup():
    chdir(D2_packages)
    chdir("..")
    if not isdir(lang_dir):
        print("No language directory detected... Exiting.")
        exit()

    # Look for majority language in packages
    selected_lang_abrv = get_language()

    # Get language from user
    print("Please enter the language you want to hear (", end="")
    audio_lang_abrv = get_lang_from_user()
    audio_lang_dir = lang_dict[audio_lang_abrv]+"_audio"

    chdir(lang_dir)
    file_list = listdir(audio_lang_dir)
    if len(file_list) == 0:
        no_files_found_warning()

    for file_name in file_list:
        print(file_name)
        new_name = file_name.replace(audio_lang_abrv, "lang")
        rename(old_name, new_name)

    # Copy files to package area in the Destiny 2 folder, overwriting existing ones
    lang_prefix = D2_packages.replace("packages", lang_dir)+"\\"+dir_name+"\\"

    for file in file_set:
        file_src = pack_prefix+file
        file_dest = lang_prefix+file
        copy2(file_src, file_dest)

    # Change name of existing files back (idempotency go brrrrr)


def get_abrv(dir_name):
    dir_name = dir_name.replace("_audio", "")

    for key, value in lang_dict.items():
        if(value == dir_name):
             return key
    print("Language abreviation not found. Exiting...")
    exit()


def main():
    print("\nWelcome to the Destiny 2 Local Language Changer!")
    print("Would you like to: ")
    print("1. Backup current audio language \nor")
    print("2. Restore Audio\nor")
    print("3. Randomly Restore Audio\n")
    print("5. Show Audio file Matrix\n")
    response = input("\n")

    if "1" in response:
        create_language_backup()

    if "2" in response:
        restore_language_backup()

    if "3" in response:
        print("Coming soon, leave a comment in the GitHub if randomly assigning language is of interest")

    if "5" in response:
        print("Printing Laguage Matrix")
        langs = D2_packages.replace("packages", lang_dir)
        all_files = []
        lang_files = []
        print_string = ""

        for dir in listdir(langs):
            abrv = get_abrv(dir)
            lang = abrv
            while len(lang) < 4:
                lang = " "+lang
            print_string = print_string+lang
            this_lang = []
            for file in listdir(langs+"\\"+dir):
                file = file.replace(abrv, "lang")
                if file not in all_files:
                    all_files.append(file)
                this_lang.append(file)
            lang_files.append(this_lang)
        print(print_string)

        print_string = ""
        for count, file in enumerate(all_files):
            stuff = str(count)+". "+str(all_files[count])
            print_string = print_string+stuff
            for lang in lang_files:
                file_here = "    "
                if all_files[count] in lang:
                    file_here = "  X "
                    print_string = print_string+file_here+" "

            print_string = print_string+"\n"
        print(print_string)

if __name__ == "__main__":
    main()

# End of file
