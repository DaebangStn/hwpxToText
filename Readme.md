### hwpx는 machine-readable 문서를 타겟으로 만들어진 문서이다.

## How to Read Hwpx
1. doc.hwpx의 확장자를 .zip으로 바꾼다.
2. doc.zip의 압축을 해제하면 아래와 같은 트리 구조가 생긴다.

```
doc
|-- mimetype
|-- settings.xml
|-- version.xml
|-- BinData
|  `-- 그림들
|-- Contents
|  |-- content.hpf
|  |-- header.xml
|  `-- section0.xml
|-- META-INF
|  |-- container.rdf
|  |-- container.xml
|  `-- manifest.xml
|-- Preview
|  |-- PrvImage.png
|  `-- PrvText.txt
`-- Scripts
   |-- headerScripts.js
   `-- sourceScripts.js
```
3. 문서의 실질적인 구조를 담당하는 파일은 header.xml과 section0.xml이다.
4. header.xml은 문서의 형식을 지정하는 파일이고 section0.xml은 문서의 내용을 지정한다.
5. section0.xml의 태그 중 알아낸 것은 다음과 같다.
```
<hp:p> # 단락의 분리를 나타낸다.
<hp:t> # 글자의 입력을 나타낸다.
<hp:linesegarray> # 각 줄의 위치를 지정한다.
```

## 프로젝트에서 텍스트화 한 방식
### section0.xml 파일에서 \<hp:t> 태그만 읽어서 텍스트 파일로 전환한다. </br>
### \<hp:p> 태그가 삽입된 곳에는 줄 바꿈을 삽입하여 문단의 구분을 표시한다.
