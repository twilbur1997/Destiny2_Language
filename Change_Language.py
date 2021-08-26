from os import listdir, mkdir, getcwd, chdir
from os.path import join, isfile, exists


'''


'''

# File locations found based on
# https://steamcommunity.com/app/1085660/discussions/0/1628539187763929500
'''
C:\Program Files (x86)\Steam\steamapps\common\Destiny 2
C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages

Just Audio

Exploration:

"Audio" search in packages reveals
in English: X files
in Spanish: X files
in German: X files

"en" reveals
"de" reveals extras - city defense
"sp" reveals


Just Text




'''

'''
How to tell which languages the user wants to use?
How to create directories for each of the text and audio for each language?

Maybe one program to create a backup of the current language,
and another program to actually shift between established backups



'''



# Prompt User for Text Interface, Audio, or both

def create_language_backup():
    # Make a new directory


    # Copy the audio files over

    # Copy the text files over



# Changes directory to D2 packages. Returns nothing
def cd_D2_packages():
    D2_packages = "C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages"

    print("Current directory:", getcwd())
    chdir(D2_packages)
    print("Current directory:", getcwd())


def main():
    print("Welcome to the Destiny 2 Local Language Changer!")

    print("Let's change directories to the Destiny 2 packages\n\n")
    cd_D2_packages()



if __name__ == "__main__":
    main()

# End of file
