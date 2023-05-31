# File Organiser
Python file organiser for Windows, with edit registry script to add new right-click option to organise current folder

## Supported file extensions and associated folders
Below you can check the folder names that will be used, and the extensions that the script will include on each one of them:
- "Excel" folder: `'.xlsx', '.xls','.ods','.csv','.xlsm'`
- "Word" folder: `'.doc','.docx','.odt', '.ppt', '.pptx','.rtf'`
- "PDF" folder: `'.pdf', '.epub','.mobi','.azw3'`
- "Images" folder: `'.jpg','.bmp', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.ico', '.pcapng','.HEIC'`
- "Software" folder: `'.exe', '.pkg', '.dmg','.deb'`
- "Video" folder: `'.mp4', '.mkv', '.mpg', '.mpeg', '.mov', '.avi'`
- "Zipped" folder: `'.zip', '.7z', '.rar', '.tar.gz', '.tar.bz2'`
- "Audio" folder: `'.mp3','.wav','.ogg', 'm4a','.opus','.flac','.aac'`
- "Code" folder: `'.py','.java','.jsp','.html','.css','.apk', '.ipynb', '.parquet','.sws','.jar','.c'`
- "Plain text" folder: `'.txt', '.in', '.out', '.json', 'xml','.log','.md', '.sql'`

You can easily add missing file extensions on `file_organiser.py` file to the desired folder. You can even do this and replicate the necessary code to add your own custom folders with custom file extensions.

## How to use
- Run `python make_key.py` on cmd to create a new option on right-click menu. It has instant effect and no further information is shown.
- You're ready to go!! You should see your new option when right-clickcking any folder on Windows explorer. The script is ready to apply effect instantly over the current working directory (cwd), but it will ask for the creation of every type of folder, just in case you don't want to organise certain type of files.
