# Bi-Gram-Model
Bi-Gram Model By MapReduce
텍스트 파일을 입력으로 받아 BIGRAM을 생성하는 프로그램입니다.
MapReduce 방식을 사용하여 BIGRAM모델을 생성합니다.

mapper는 Mapper.py, reducer는 Reducer.py라는 이름으로 작성되어 있습니다.

예를 들어, count_number.txt 파일로 BIGRAM 모델을 생성하려면
cat count_number.txt | python Mapper.py | python Reducer.py
로 실행합니다
