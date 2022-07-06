import os
import sys
import zipfile
import shutil


def extract_contents(hwpxPath, workPath=None):
    filePath = os.path.dirname(hwpxPath)
    filename = os.path.basename(hwpxPath)

    if workPath is None:
        workPath = os.path.join(filePath, 'temp')

        try:
            if not os.path.exists(workPath):
                os.makedirs(workPath)
            else:
                print('[Error] There already exist temp dir path: ' + workPath)
                sys.exit()
        except OSError:
            print('[ERROR] while making dirs, os error occurred')
            sys.exit()

    copied = os.path.join(workPath, filename + '.zip')
    shutil.copyfile(hwpxPath, copied)
    _zip = zipfile.ZipFile(copied)
    _zip.extractall(workPath)
    _zip.close()

    contentsPath = os.path.join(workPath, 'Contents')
    section0Path = os.path.join(contentsPath, 'section0.xml')
    destPath = os.path.join(filePath, filename + '.xml')
    shutil.move(section0Path, destPath)

    shutil.rmtree(workPath)
