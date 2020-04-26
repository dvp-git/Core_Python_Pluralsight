# RecamanSequence Reader from Recaman.dat file
import sys
# def recaman_sequence_reader(filename):
#     try:
#         f = open(filename, mode='rt', encoding='utf-8')
#         for line in f:
#             print(line.strip())
#     except FileNotFoundError as e:
#         print(f"{e!r}",file=sys.stderr)


# The Recaman Series is a file in text format. To read it need to output to screen

def recaman_sequence_reader(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        # for line in f:
        #     a = int(line.strip())
        #     series.append(a)
        # Refactorin using list comprehensions
        return [int(line.strip()) for line in f if line.strip().isdigit()]  ## Omitting alpha character "oops" which was added for demonstration of finally block
    except FileNotFoundError as e:
        print(f"{e!r}",file=sys.stderr)
    finally :
        f.close()


def main(filename):
    series = recaman_sequence_reader(filename)
    print(series)


if __name__ == "__main__":
    main(sys.argv[1])


""" If a string is included in the .dat file.
C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python>echo "oops" >> RecamanSequence.dat

C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python>python RecamanSequenceReader.py RecamanSequence.dat
Traceback (most recent call last):
  File "RecamanSequenceReader.py", line 34, in <module>
    main(sys.argv[1])
  File "RecamanSequenceReader.py", line 29, in main
    series = recaman_sequence_reader(filename)
  File "RecamanSequenceReader.py", line 19, in recaman_sequence_reader
    a = int(line.strip())
ValueError: invalid literal for int() with base 10: '"oops"'"""
