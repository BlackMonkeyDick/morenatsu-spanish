# On recompiling this stupid project

If you get an error where screens.rpy is breaking on the line that says hbox, then it is due to bad line endings.
To fix this, open the file file in notepad++, go to Edit > EOL Conversion > Macintosh (CR), then save the file.
Now you should be able to successfully force recompile.
