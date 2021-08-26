# Destiny 2 Language Changer

You're here because you don't want to toggle the Steam settings every time to change between languages.
It requires a download every time, and simply deletes the local files instead of  moving them around for some reason.

Heads up - this program only changes the audio, and doesn't change subtitles or the user interface.

Maybe that can come in a later patch, but right now it's tough with Steam settings.


You'll need to download Python to run this program:

Download the latest Python here:
https://www.python.org/downloads/

You can run the program using ```py .\Change_Language.py```


The program has a few prompts to help understand what is needed from the user.

Specifically, the program will first check if the current language selected has been saved locally.
If not, it will ask if you want to locally save the current language selected.

When the game saves these files, it will create a new directory outside of the packages directory.
By default, this directory is:

*C:\Program Files (x86)\Steam\steamapps\common\Destiny 2\packages*

Note: If this is not your path to the Destiny 2 packages, you should change line 5 in the Change_Language.py file to the correct path.


*If you need to exit the program at any point, just hold Control then press C*


The recommended usage of this app is to change the language of the game on Steam to the audio language that you'd like.
Then, save those files using the program.

Then, set the language in Steam to the language you want for the UI.

Finally, you can use the program to set the audio language to your preferred language. 




This is a work in progress, so feel free to comment with suggestions!
