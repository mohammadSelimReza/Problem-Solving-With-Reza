<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=40&pause=1000&color=58A6FF&center=true&vCenter=true&width=700&height=80&lines=Learn+With+Reza+%F0%9F%9A%80;Competitive+Programming+%7C+DSA+%7C+Problem+Solving" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://leetcode.com/u/selim_reza/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode" /></a>
  <a href="https://codeforces.com/profile/"><img src="https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white" alt="Codeforces" /></a>
  <a href="https://github.com/mohammadSelimReza"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://www.linkedin.com/in/selim-reza-b66042278/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/400%2B-Problems%20Solved-brightgreen?style=flat-square" alt="Problems Solved" />
  <img src="https://img.shields.io/badge/Goal-Grandmaster%20🏆-gold?style=flat-square" alt="Goal" />
  <img src="https://img.shields.io/badge/Language-Python%20%7C%20C++-blue?style=flat-square" alt="Language" />
</p>

---

## 🧠 About This Repository

> **A structured, battle-tested collection of competitive programming solutions, patterns, and insights — built while grinding from scratch to Grandmaster.**

This is my personal war journal. Every problem solved, every concept learned, and every technique mastered — documented here for **my own growth** and for **anyone who wants to learn alongside me**.

I'm **Selim Reza** — a Backend Engineer who believes that **strong algorithmic thinking is what separates a coder from an engineer**. This repo tracks my journey through **500+ LeetCode problems** and my push toward **Codeforces Grandmaster**.

---

## 🎯 Current Goals

| Goal | Target | Status |
|------|--------|--------|
| LeetCode Problems | 400 – 500 solved | 🔥 In Progress |
| Codeforces Rating | Grandmaster (2400+) | 🚀 Grinding |
| Master DSA Topics | All core patterns | 📚 Ongoing |

---

## 📂 Repository Structure

```
learn-with-reza/
│
├── 📁 LeetCode/
│   ├── 📁 Easy/
│   ├── 📁 Medium/
│   └── 📁 Hard/
│
├── 📁 Codeforces/
│   ├── 📁 Div2/
│   ├── 📁 Div3/
│   └── 📁 Educational/
│
├── 📁 Patterns/
│   ├── sliding-window.md
│   ├── two-pointers.md
│   ├── binary-search.md
│   ├── dynamic-programming.md
│   ├── graphs.md
│   ├── trees.md
│   └── ...
│
├── 📁 Templates/
│   ├── cp-template.py
│   ├── cp-template.cpp
│   └── io-template.py
│
└── README.md
```

---

## 🗺️ Topic Roadmap

### Phase 1 — Foundations (Weeks 1–2)
- [ ] Arrays & Hashing
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Stack & Queues
- [ ] Linked Lists

### Phase 2 — Core Patterns (Weeks 3–4)
- [ ] Binary Search (on answer, rotated arrays)
- [ ] Sorting Algorithms & Custom Comparators
- [ ] Recursion & Backtracking
- [ ] Trees (BFS, DFS, BST)
- [ ] Heaps / Priority Queues

### Phase 3 — Advanced (Weeks 5–6)
- [ ] Graphs (BFS, DFS, Dijkstra, Topological Sort)
- [ ] Dynamic Programming (1D, 2D, Knapsack, LCS, LIS)
- [ ] Greedy Algorithms
- [ ] Tries & String Algorithms (KMP, Rabin-Karp)
- [ ] Segment Trees & Fenwick Trees

### Phase 4 — Grandmaster Push (Weeks 7–8)
- [ ] Number Theory (Sieve, GCD, Modular Arithmetic)
- [ ] Combinatorics & Probability
- [ ] Advanced Graph Theory (Flow, SCC, Bridges)
- [ ] Interactive / Constructive Problems
- [ ] Contest Strategy & Speed Optimization

---

## 📊 Progress Tracker

### LeetCode Breakdown

| Difficulty | Solved | Target |
|------------|--------|--------|
| 🟢 Easy   | 0      | 150    |
| 🟡 Medium | 0      | 250    |
| 🔴 Hard   | 0      | 100    |
| **Total**  | **0**  | **500**|

### Codeforces Rating Journey

```
Rating Goal: ████████████████████░░░░░░░░░░ Grandmaster (2400+)
```

---

## 🧩 Problem-Solving Patterns Cheatsheet

<details>
<summary><b>🔹 Sliding Window</b></summary>

**When to use:** Subarray/Substring problems with contiguous elements.

```python
def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```
</details>

<details>
<summary><b>🔹 Two Pointers</b></summary>

**When to use:** Sorted arrays, pair-sum, or partitioning problems.

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
```
</details>

<details>
<summary><b>🔹 Binary Search</b></summary>

**When to use:** Searching in sorted data or "binary search on the answer."

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```
</details>

<details>
<summary><b>🔹 BFS / DFS</b></summary>

**When to use:** Graph traversal, shortest path (unweighted), connected components.

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```
</details>

<details>
<summary><b>🔹 Dynamic Programming</b></summary>

**When to use:** Overlapping subproblems + optimal substructure.

```python
# Fibonacci - Bottom Up
def fib(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```
</details>

---

## ⚡ Competitive Programming Templates

### Python Fast I/O
```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Solution here

t = int(input())
for _ in range(t):
    solve()
```

### C++ Template
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define all(x) x.begin(), x.end()
#define fast ios::sync_with_stdio(0); cin.tie(0);

void solve() {
    int n;
    cin >> n;
    // Solution here
}

int main() {
    fast;
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
```

---

## 🏆 Contest Log

| Date | Platform | Contest | Rank | Rating Change | Problems Solved |
|------|----------|---------|------|---------------|-----------------|
| — | — | — | — | — | — |

---

## 🧰 Resources I Use

| Resource | Link |
|----------|------|
| LeetCode | [leetcode.com](https://leetcode.com) |
| Codeforces | [codeforces.com](https://codeforces.com) |
| CP Algorithms | [cp-algorithms.com](https://cp-algorithms.com) |
| CSES Problem Set | [cses.fi](https://cses.fi/problemset/) |
| NeetCode Roadmap | [neetcode.io](https://neetcode.io) |
| Striver's A2Z Sheet | [takeuforward.org](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2) |

---

## 🤝 Connect With Me

<p align="center">
  <b>Selim Reza</b> — Backend Engineer | Competitive Programmer
</p>

<p align="center">
  <a href="mailto:selimreza6996@gmail.com">📧 Email</a> •
  <a href="https://www.linkedin.com/in/selim-reza-b66042278/">💼 LinkedIn</a> •
  <a href="https://github.com/mohammadSelimReza">🐙 GitHub</a> •
  <a href="https://leetcode.com/u/selim_reza/">⚡ LeetCode</a>
</p>

---

<p align="center">
  <i>"The only way to learn competitive programming is by solving problems. Not tomorrow. Not after this tutorial. NOW."</i>
</p>

<p align="center">
  ⭐ Star this repo if you're on the same grind!
</p>
