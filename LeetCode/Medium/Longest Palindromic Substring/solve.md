# Longest Palindromic Substring - Senior Engineer Interview Prep Guide

This guide covers approaches from naive brute force to optimal linear time, analyzing complexities and discussing system-level parallels in string processing.

---

## 1. Algorithmic Approaches & Comparisons

A palindrome is a string that reads the same forwards and backwards. Finding the longest one within a larger string is a classic algorithmic benchmark.

### Approach 1: Brute Force
Check every possible substring and verify if it is a palindrome.
- **Time Complexity:** $O(n^3)$ - $O(n^2)$ to generate all substrings, and $O(n)$ to check each substring for palindromic properties.
- **Space Complexity:** $O(1)$ - Only using pointer indices.
- **When to use:** Never in a real problem, purely theoretical baseline.

### Approach 2: Dynamic Programming (DP)
To improve over brute force, we avoid re-checking palindromes. If `s[i:j]` is a palindrome, then `s[i-1:j+1]` is also a palindrome *if* `s[i-1] == s[j+1]`. 
- **Time Complexity:** $O(n^2)$ - We fill an $n \times n$ DP table.
- **Space Complexity:** $O(n^2)$ - A 2D boolean array to store whether substrings are palindromes.
- **When to use:** Good for explaining overlapping subproblems, but usually sub-optimal in space compared to the next approach.

### Approach 3: Expand Around Center (Optimal in Interviews)
A palindrome mirrors around its center. A center can be a single character (for odd-length palindromes like "aba") or between two characters (for even-length palindromes like "abba"). Therefore, there are $2n - 1$ such centers. We can expand outward from each center.
- **Time Complexity:** $O(n^2)$ - There are $O(n)$ centers, and expanding outward takes at most $O(n)$ steps.
- **Space Complexity:** $O(1)$ - We only need to store the start and maximum length.
- **When to use:** This is the expected and optimal solution in 99% of engineering interviews due to $O(1)$ constant space usage.

### Approach 4: Manacher's Algorithm
A highly specialized algorithmic trick that exploits palindrome symmetries to find the longest palindromic substring in strictly linear time.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$
- **When to use:** Almost never required in an interview unless you're interviewing for a highly specialized competitive programming or hard theoretical computer science role. 

### Trade-off Comparison Table

| Approach | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $O(n^3)$ | $O(1)$ | Unusable beyond extreme edge cases. |
| **Dynamic Programming** | $O(n^2)$ | $O(n^2)$ | Classic DP, but wastes $O(n^2)$ memory. |
| **Expand Around Center** | $O(n^2)$ | $O(1)$ | **Ideal interview answer.** Time efficient, completely avoids memory overhead. |
| **Manacher's Algorithm** | $O(n)$ | $O(n)$ | Theoretically optimal but practically overly complex to code under pressure. |

---

## 2. Implementations (Pseudocode)

Here is the language-agnostic pseudocode for the **Expand Around Center** approach so you can understand the core logic and adapt it to your language of choice.

### Expand Around Center Pseudocode
```text
function expandAroundCenter(s, left_index, right_index):
    // Expand outwards as long as we stay within bounds AND characters match
    while left_index >= 0 AND right_index < length(s) AND s[left_index] == s[right_index]:
        left_index = left_index - 1
        right_index = right_index + 1
        
    // Return the length of the valid palindrome we found
    // Note: The loop breaks when pointers are 1 step beyond the valid palindrome,
    // so length is (right_index - left_index - 1)
    return right_index - left_index - 1


function longestPalindrome(s):
    if s is null or length(s) < 1:
        return ""
        
    start = 0
    max_length = 0
    
    for i from 0 to length(s) - 1:
        // Case 1: Odd length palindromes (center is at character 'i')
        len1 = expandAroundCenter(s, i, i)
        
        // Case 2: Even length palindromes (center is between 'i' and 'i+1')
        len2 = expandAroundCenter(s, i, i + 1)
        
        // The maximum length found treating 'i' as the center
        current_max_len = max(len1, len2)
        
        // If we found a longer palindrome, update our tracking indices
        if current_max_len > max_length:
            max_length = current_max_len
            // Math to calculate start index based on center 'i' and length
            start = i - floor((current_max_len - 1) / 2)
            
    // Return the specific substring using our derived start and length parameters
    return substring(s, start, start + max_length)
```

---

## 3. Conceptual Patterns & Type of Problems It Solves

This problem highlights two critical computing patterns:
1. **Iterate-and-Expand (Seed Expansion):** 
   Instead of searching for boundaries and validating inwards, we pick a valid "seed" (the center) and expand outwards until failure. This reverse-validation is critical in scenarios like flood-fill algorithms, localized search, and generative boundaries.
2. **Parity handling (Odd vs. Even Constraints):**
   This problem gracefully forces engineers to handle structural parity differences (an axis of symmetry resting on a node vs. resting on an edge). 

---

## 4. Real-World Equivalents & System Design Parallels

1. **Genomics & DNA Sequencing (Bioinformatics)**
   - **Real World:** DNA sequences often contain "palindromic sequences" where reading the $5' \to 3'$ strand matches the complementary $3' \to 5'$ strand in reverse. Identifying these is crucial as they form hairpin loops and serve as restriction enzyme recognition sites.
   - **Analogy:** Expand-around-center is directly analogous to how bioinformatic search heuristics locate structural binding anomalies in massive genomic strings.

2. **Data Compression & Run-Length Equivalents**
   - **Real world:** Text compression algorithms (like LZ77 used in Deflate/ZIP) look for repeated or mirrored patterns to compress data. Finding long palindromic or heavily repeated substrings allows the compressor to store a reference to the sequence rather than the raw text.

3. **Signal Processing & Convolution Centers**
   - **Real world:** In 1D signal processing or audio wave analysis, identifying symmetrical spikes or echoes around a central burst involves identical "expand-around-center" mathematical convolution to identify the symmetry bounds of the disruption.

---

## 5. The "Senior" Follow-up Questions

- **When is the $O(n^2)$ Dynamic Programming approach actually better than the $O(n^2)$ Expand Around Center?**
  - *Answer:* If the system demands solving *multiple* queries asking "Is the substring from index A to index B a palindrome?", the DP approach shines. Preparing the $O(n^2)$ table allows querying any subsequent substring $A \to B$ in $O(1)$ time, whereas Expand Around Center would have to recompute. Trade-offs matter!
- **How does character encoding impact your solution? (UTF-8 vs ASCII)**
  - *Answer:* In raw C or C++, jumping indices strictly byte-by-byte (`s[i]`) on a multi-byte UTF-8 string will completely corrupt the palindrome check (since a single emoji might be 4 bytes). A senior must clarify if the string is ASCII or if we need to decode bounds into Unicode Code Points before doing pointer arithmetic.
