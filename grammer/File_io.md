# <span style = "color : ">파일 입출력</span>
## <span style = "color : yellow">파일 쓰기모드</span>
```python
score_file = open("score.txt", "w", encoding = "utf8") #(덮어)쓰기모드로 열기
print("수학 : 90", file = score_file) #파일에 작성
print("영어 : 80", file = score_file) #파일에 작성
score_file.close()

score_file = open("score.txt", "a", encoding = "utf8") #(이어)쓰기모드로 열기
score_file.write("과학 : 80") # 줄바꿈을 해주어야함
score_file.write("\n코딩 : 100")
score_file.close()
```
## <span style = "color : yellow">파일 읽기모드</span>
```python
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read()) #파일 전체 읽기
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()
```
## <span style = "color : orange">pickle</span>
텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것  
wb = write byte  
rb = read byte
```python
import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름" : "홍성표", "나이" : "98년생", "취미" : ["농구", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close() # write

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
```
## <span style = "color : orange">with</span>
```python
# close가 따로 필요하지 않음
import pickle

with open("profile.pickle", "rb") as profile_file: #profile.pickle을 읽어와 profile_file에 저장
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 공부중입니다.")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file)
```