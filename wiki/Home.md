# Algorithm

알고리즘 문제 풀이 리포지토리입니다. LeetCode 문제 풀이를 **BaekjoonHub** Chrome 확장을 통해 자동으로 GitHub에 동기화합니다.

## 리포지토리 개요

| 항목 | 내용 |
|------|------|
| **주요 언어** | C++, Python, SQL, JavaScript |
| **문제 소스** | LeetCode |
| **자동 동기화** | BaekjoonHub Chrome 확장 |
| **파일 구조** | `LeetCode/{Problem-Name}/Solution.{ext}` |

## 디렉토리 구조

```
Algorithm/
├── LeetCode/
│   ├── Two-Sum/
│   │   ├── Solution.cpp (또는 .py)
│   │   └── README.md       # 문제 설명 (자동 생성)
│   ├── 3Sum/
│   │   ├── Solution.cpp
│   │   └── README.md
│   ├── Longest-Palindromic-Substring/
│   │   ├── Solution.cpp
│   │   └── README.md
│   └── ... (70+ 문제)
└── .github/workflows/        # CI
```

## 자동 동기화 설정 (BaekjoonHub)

### BaekjoonHub란?

[BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)는 온라인 저지(LeetCode, 백준 등)에서 문제를 풀면 **자동으로 GitHub에 커밋**해주는 Chrome 확장 프로그램입니다.

### 동기화 흐름

```
LeetCode에서 문제 풀이 제출
        │
        ▼ (Submit → Accepted)
BaekjoonHub 확장이 감지
        │
        ▼
자동 커밋 & 푸시
├── LeetCode/{문제이름}/README.md   (문제 설명)
└── LeetCode/{문제이름}/Solution.{ext}  (풀이 코드)
        │
        ▼
GitHub Repository 자동 업데이트
```

### 각 문제 디렉토리 구조

```
LeetCode/{Problem-Name}/
├── README.md         # 문제 설명 (BaekjoonHub 자동 생성)
│   ├── 문제 제목
│   ├── 문제 설명
│   ├── 입출력 예시
│   └── 제약 조건
└── Solution.{ext}    # 풀이 코드
    └── C++, Python, SQL, JavaScript 등
```

## 통계

| 항목 | 수량 |
|------|------|
| **총 문제 수** | 70+ |
| **LeetCode** | 70+ |
| **주요 언어** | C++ (대부분), Python, SQL, JS |

## 문제 난이도 분포

LeetCode 문제들은 Easy / Medium / Hard로 분류됩니다.

| 난이도 | 예시 문제 |
|--------|----------|
| **Easy** | Two Sum, Valid Parentheses, Climbing Stairs, Plus One |
| **Medium** | 3Sum, Longest Palindromic Substring, Zigzag Conversion |
| **Hard** | Median of Two Sorted Arrays, Minimum Number of K Consecutive Bit Flips |

## Wiki 페이지 목록

- [[Problem Categories]] — 문제 카테고리별 정리
- [[Setup Guide]] — BaekjoonHub 확장 설정
