# Reading text files from command line.
import sys



f = open(sys.argv[1], mode='rt', encoding='utf-8')
#   Note that this method has 2 line spacing between each line in the file. This occurs due to '\n' character encountered \
#   during thr processing of read and print() adds it's own new line. Use line.strip() method to remove the line ending after print.
# Alternatively you can use sys.stdout.write() method. This is the same method used to write to the file.
for line in f:
    sys.stdout.write(line)
f.close()



"""Output:

C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python>python FileSys.py wasteland.txt
What are the roots that clutch,what branches grow

Out of this story rubbish? Son of man

You cannot say of guess,for you know only

A heap of broken images,where the sun beats


AFTER sys modification.
C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python>python FileSys.py wasteland.txt
What are the roots that clutch,what branches grow
Out of this story rubbish? Son of man
You cannot say of guess,for you know only
A heap of broken images,where the sun beats

"""
