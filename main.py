import os
import zipfile
import rarfile

os.chdir('./archives')
archives = os.listdir()

for archive in archives:
    if archive.endswith('zip'):
        dir_name = archive[0:-4]
        os.mkdir(dir_name)
        with zipfile.ZipFile(archive) as current_zip:
            current_zip.extractall(dir_name)
    elif archive.endswith('rar'):
        dir_name = archive[0:-4]
        os.mkdir(dir_name)
        with rarfile.RarFile(archive) as current_rar:
            current_rar.extractall(dir_name)
    else:
        print(f'{archive} is not an archive!')
