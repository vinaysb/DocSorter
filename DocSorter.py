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
        # print(file)
        wordlen, profane = docx_opr(file)
        if (wordlen > 300) or not profane:
            shutil.move(file, 'Disqualified/' + file)
    os.chdir("..")
