import os
import sys
import xml.etree.ElementTree as ET


def parse_xml(path):
    assert os.path.exists(path)

    filename = os.path.basename(path)[:-9]
    hwpx_path = os.path.dirname(path)
    outDir = os.path.join(os.path.dirname(hwpx_path), 'out')
    outPath = os.path.join(outDir, filename + '.txt')

    if os.path.exists(outPath):
        os.remove(path)
        assert not os.path.exists(outPath)

    _text = ""

    ET.register_namespace('hp', "http://www.hancom.co.kr/hwpml/2011/paragraph")
    root = ET.parse(path).getroot()
    for text in root.iter():
        if text.tag == '{http://www.hancom.co.kr/hwpml/2011/paragraph}t':
            if text.text is not None:
                _text += text.text
            else:
                _text += ' '
        elif text.tag == '{http://www.hancom.co.kr/hwpml/2011/paragraph}p':
            _text += '\n'

    outFile = open(outPath, 'w', encoding='utf-8')
    outFile.write(_text)
    outFile.close()

    os.remove(path)
