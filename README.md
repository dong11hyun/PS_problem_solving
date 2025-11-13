# PS_problem_solving
---

## 함수 
---
#### enumerate()
- 리스트를 순회하면서 (인덱스, 값) 쌍을 동시에 반환
- 반복문 실행 과정
```python
for idx, value in enumerate(sorted_coords):
    compress[value] = idx
```

#### 언패킹 *list or *tuple
- 요소들을 풀어서 개별값으로 전달
```python
numbers = [10, 20, 30]
result = add(*numbers)  # add(10, 20, 30)과 동일
print(result) # 60
print(*numbers)  # 10 20 30
```

#### sorted() / .sort()
- sorted()
  > 어떤 iterable(반복 가능한 객체)이든 받아서 항상 정렬된 리스트를 반환 
  > (집합, 문자열, 튜플, 딕셔너리..)

- .sort()
  > 리스트 전용 메서드, 원본 직접 정렬