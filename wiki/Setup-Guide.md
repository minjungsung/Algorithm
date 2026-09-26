# Setup Guide

## BaekjoonHub Chrome 확장 설치

### 1단계: 확장 설치

1. [Chrome 웹 스토어](https://chrome.google.com/webstore)에서 **BaekjoonHub** 검색
2. 또는 [BaekjoonHub GitHub](https://github.com/BaekjoonHub/BaekjoonHub)에서 설치 링크 확인
3. **Chrome에 추가** 클릭

### 2단계: GitHub 연동

1. BaekjoonHub 확장 아이콘 클릭
2. **GitHub 로그인** → OAuth 인증
3. **리포지토리 선택**: `minjungsung/Algorithm`
4. **연동 완료** 확인

### 3단계: LeetCode 연동 설정

```
BaekjoonHub 설정
├── GitHub Repository: minjungsung/Algorithm
├── 디렉토리 구조: LeetCode/{문제이름}/
├── 파일명: Solution.{ext}
├── README 자동 생성: ✅ 활성화
└── 커밋 메시지: 자동 (문제이름 + 난이도)
```

### 4단계: 사용법

1. [LeetCode](https://leetcode.com)에서 문제 풀기
2. 풀이 **Submit** → **Accepted** 확인
3. BaekjoonHub가 자동으로 감지하여 GitHub에 push
4. 확인: `https://github.com/minjungsung/Algorithm/tree/main/LeetCode/{문제이름}`

## 동기화 흐름

```
┌─────────────────────┐
│  LeetCode           │
│  문제 풀이 & Submit  │
└──────────┬──────────┘
           │ Accepted ✓
           ▼
┌─────────────────────┐
│  BaekjoonHub 확장   │
│  (Chrome Extension)  │
│                     │
│  1. 코드 추출       │
│  2. 문제 설명 추출   │
│  3. README.md 생성  │
└──────────┬──────────┘
           │ Git Push
           ▼
┌─────────────────────┐
│  GitHub Repository   │
│  minjungsung/        │
│  Algorithm           │
│                     │
│  LeetCode/          │
│  └── {문제}/        │
│      ├── README.md  │
│      └── Solution.* │
└─────────────────────┘
```

## 로컬 환경에서 문제 풀이

BaekjoonHub 없이 수동으로 코드를 관리할 수도 있습니다.

### C++ 풀이 환경 설정

```bash
# macOS (Homebrew)
brew install gcc

# 컴파일 & 실행
g++ -std=c++17 -o solution Solution.cpp
./solution
```

### Python 풀이 환경 설정

```bash
python3 Solution.py
```

### 디렉토리 생성 규칙

BaekjoonHub의 자동 생성 규칙을 따릅니다:

```bash
# 새 문제 디렉토리 생성
mkdir -p LeetCode/Problem-Name
touch LeetCode/Problem-Name/Solution.cpp
touch LeetCode/Problem-Name/README.md
```

### 수동 커밋

```bash
git add LeetCode/Problem-Name/
git commit -m "feat: solve LeetCode Problem-Name (Medium)"
git push
```

## 추천 도구

| 도구 | 용도 | 링크 |
|------|------|------|
| **BaekjoonHub** | 자동 동기화 | [Chrome 확장](https://github.com/BaekjoonHub/BaekjoonHub) |
| **LeetCode** | 문제 풀이 | [leetcode.com](https://leetcode.com) |
| **VS Code** | 코드 에디터 | [code.visualstudio.com](https://code.visualstudio.com) |
| **C++ Extension** | VS Code C++ | [MS C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) |

## 문제 풀이 팁

### 시간 복잡도 가이드

```
입력 크기 N과 허용 시간 복잡도:
├── N ≤ 10       → O(N!) — 브루트포스
├── N ≤ 20       → O(2^N) — 비트마스크
├── N ≤ 500      → O(N³) — 3중 루프
├── N ≤ 5,000    → O(N²) — 2중 루프
├── N ≤ 100,000  → O(N log N) — 정렬, 이분탐색
├── N ≤ 1,000,000 → O(N) — 선형 탐색
└── N > 1,000,000 → O(log N) — 이분탐색
```

### C++ 풀이 템플릿

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 풀이 함수
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Solution sol;
    // 테스트
    return 0;
}
```
