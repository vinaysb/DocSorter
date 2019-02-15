import os
import shutil


def GetFiles(extension):
    import glob

    file_list = [j for j in glob.glob('*.{}'.format(extension))]
    return(file_list)


def docx_opr(file_name):
    import docx2txt
    from profanityfilter import ProfanityFilter

    pf = ProfanityFilter()
    document = docx2txt.process(file_name)
    words = document.split()
    profane = pf.is_clean(document)
    return(len(words), profane)


try:
    max_len = int(input('Enter the maxumum number of allowed words'))
except ValueError:
    print('Please enter only numeric values')

folders = [name for name in os.listdir(".") if os.path.isdir(name)]

for folder in folders:
    # print(folder)
    os.chdir(folder)
    try:
        os.mkdir('Disqualified')
    except FileExistsError:
        pass
    file_list = GetFiles('docx')
    for file in file_list:
        print(file, 'Processed')
        wordlen, profane = docx_opr(file)
        if (wordlen > max_len) or not profane:
            shutil.move(file, 'Disqualified/' + file)
    os.chdir("..")
input('Press enter to close the window')
