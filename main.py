from extract_contents import extract_contents
from parse_xml import parse_xml
import os

if __name__ == '__main__':
    root_dir = os.getcwd()

    assert 'hwpx' in os.listdir(root_dir), 'There is no hwpx data directory.'

    hwpx_dir = os.path.join(root_dir, 'hwpx')

    for file in os.listdir(hwpx_dir):
        if file.endswith('.hwpx'):
            extract_contents(os.path.join(hwpx_dir, file))

    for file in os.listdir(hwpx_dir):
        if file.endswith('.xml'):
            parse_xml(os.path.join(hwpx_dir, file))
