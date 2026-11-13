# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV 파일을 읽어 유효한 점수 목록(kept)과 제외한 행의 기록(skipped)을 돌려줍니다.
현재 CSV 읽기·검증을 지원하며, 평균·학점 계산 기능은 포함하지 않습니다.

## ② 왜 만들었나요 (Why)

실제 성적 파일에는 빈 점수, 0~100 밖의 점수, 「결석」 같은 글자, 열 개수가 맞지 않는 행이 섞일 수 있습니다.
이런 행을 그대로 읽으면 프로그램이 멈추거나 잘못된 값이 계산에 들어갑니다.
그래서 올바른 행만 골라내고, 제외한 행은 이유와 함께 기록하도록 만들었습니다.

## ③ 어떻게 쓰나요 (How)

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv
```

- 확인한 Python 버전: Python 3.13.15
- set 줄: 옛 Anaconda가 깔린 PC에서 pytest 플러그인 오류를 막습니다. 명령 프롬프트(cmd)용이며, 새 터미널을 열 때마다 pytest 전에 한 번 입력합니다. PowerShell에서는 `$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`을 입력합니다.

예상 결과: 읽은 줄 5개 / 건너뛴 줄 5개

## ④ 어떻게 테스트하나요

```
python -m pytest test_load_scores.py -q
```

실제 결과: 12 passed (기본 11개 + weird.csv 보강 1개)

AI 실험 파일은 비교용 원본이라 일부 테스트가 실패할 수 있습니다.
- test_bug_A.py: 【1단계 결과, 예: 5 passed】 — 【이유 한 줄】
- test_bug_B.py: 2 failed, 3 passed — 최댓값이 마지막에 있으면 틀린 값을 돌려줌 (find_max가 마지막 원소를 확인하지 않는 버그)

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | CSV를 읽어 (kept, skipped)를 돌려주는 함수 |
| scores.csv · empty.csv · weird.csv | 예제 데이터 (정상 / 빈 파일 / 이상한 값이 섞인 파일) |
| test_load_scores.py | load_scores를 검사하는 pytest 테스트 (12개) |
| bug3_logic.py · test_bug_A.py · test_bug_B.py | AI 실험: 버그가 있는 find_max와 AI가 만든 테스트 (A: 코드를 줌, B: 명세를 줌) |
| prompts.txt | AI 실험에 사용한 프롬프트 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : 오명원
- 사용한 AI 도구·모델 :  클로드
- AI에게 도움받은 부분 : test_bug_A.py·test_bug_B.py 테스트 초안 생성, README 문장 정리
- 내가 직접 판단·확인한 부분 : 기대값을 명세로 정하고, 테스트를 직접 실행해 결과를 확인하고, AI 테스트가 실패한 이유를 판단함

## 라이선스

MIT License (LICENSE 파일 참고)