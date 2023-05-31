import code
from genericpath import exists
from posixpath import splitext
from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory

import datetime
import os
os.environ['SETUPTOOLS_USE_DISTUTILS'] = 'stdlib'
import setuptools
import shutil
import time

# request user to select the source directory
source_dir = os.getcwd()
if source_dir=='':
    exit()

folder_names = ['Excel', 'Word', 'PDF', 'Images', 'Software', 'Video', 'Zipped', 'Audio', 'Code', 'Plain Text', 'AI']

destination_dir_excel = os.path.join(source_dir, 'Excel')
destination_dir_word = os.path.join(source_dir, 'Word')
destination_dir_pdf = os.path.join(source_dir, 'PDF')
destination_dir_img = os.path.join(source_dir, 'Images')
destination_dir_software = os.path.join(source_dir, 'Software')
destination_dir_video = os.path.join(source_dir, 'Video')
destination_dir_zip = os.path.join(source_dir, 'Zipped')
destination_dir_audio = os.path.join(source_dir, 'Audio')
destination_dir_code = os.path.join(source_dir, 'Code')
destination_dir_plain_text = os.path.join(source_dir, 'Plain Text')
destination_dir_ai = os.path.join(source_dir, 'AI')

#Check if folders exist and create if they do not
for folder_name in folder_names:
    destination_dir = os.path.join(source_dir, folder_name)
    if not os.path.exists(destination_dir):
        create_or_not = messagebox.askquestion('Create folder or Not', f'Do you want to create the {folder_name} folder?')
        if create_or_not == 'yes':
            os.makedirs(destination_dir)
        else:
            exit()

destionation_dir_list = []

# file types
doc_types_excel=('.xlsx', '.xls','.ods','.csv','.xlsm')
doc_types_word=('.doc','.docx','.odt', '.ppt', '.pptx','.rtf')
doc_types_pdf=('.pdf', '.epub','.mobi','.azw3')
img_types = ('.jpg','.bmp', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.ico', '.pcapng','.HEIC')
software_types = ('.exe', '.pkg', '.dmg','.deb')
video_types = ('.mp4', '.mkv', '.mpg', '.mpeg', '.mov', '.avi')
zip_types = ('.zip', '.7z', '.rar', '.tar.gz', '.tar.bz2')
audio_types = ('.mp3','.wav','.ogg', 'm4a','.opus','.flac','.aac')
code_types = ('.py','.java','.jsp','.html','.css','.apk', '.ipynb', '.parquet','.sws','.jar','.c')
plain_text_types = ('.txt', '.in', '.out', '.json', 'xml','.log','.md','.sql')
ai_types = ('.pt', '.ckpt')




#list of files in source directory
files=[i for i in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir,i))]
#print('Files to move: ',files)

# Mapping of file types to destination directories
type_dir_map = {
    doc_types_excel: destination_dir_excel,
    doc_types_word: destination_dir_word,
    doc_types_pdf: destination_dir_pdf,
    img_types: destination_dir_img,
    software_types: destination_dir_software,
    video_types: destination_dir_video,
    zip_types: destination_dir_zip,
    audio_types: destination_dir_audio,
    code_types: destination_dir_code,
    plain_text_types: destination_dir_plain_text,
    ai_types: destination_dir_ai
}

#move files to respective directories based on file extension
for f in files:
    for doc_type, destination_dir in type_dir_map.items():
        if os.path.join(source_dir, f).endswith(doc_type):
            filename, extension = os.path.splitext(f)
            if os.path.exists(os.path.join(destination_dir, f)):
                date_time = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir, f"{filename}_({date_time}){extension}"))
            else:
                shutil.move(os.path.join(source_dir, f), destination_dir)

   
