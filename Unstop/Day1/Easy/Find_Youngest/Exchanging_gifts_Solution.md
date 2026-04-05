# 🎄 The Royal Christmas Puzzle (C Solution)

## 🚩 Problem Overview
In a royal family of `n` members, everyone exchanges gifts. We need to find the **youngest member**, who is defined by two strict rules:
1. They **receive** a gift from every other family member (`n - 1` gifts).
2. They **give** absolutely no gifts in return.

## 🧠 The "Net Score" Approach
Instead of maintaining two separate arrays for gifts given and gifts received, this solution optimizes space by using a single `score` array:
* When a member **gives** a gift, we heavily penalize them (or simply decrement).
* When a member **receives** a gift, we increment their score.
* The youngest member will be the only one with a final score of exactly `n - 1`.

## 💻 Code Snippet
```c
#include <stdio.h>
#include <stdlib.h>

void find_youngest_member(int n, int m, int gifts[][2]) {
    // We only need one array to track the "net score"
    // calloc dynamically allocates memory and initializes it to 0
    int *score = (int *)calloc(n + 1, sizeof(int)); //<-- AI helped here
    
    // Process the gifts
    for (int i = 0; i < m; i++) {
        int giver = gifts[i][0];
        int receiver = gifts[i][1];
        
        score[giver]--;      // Penalize giving
        score[receiver]++;   // Reward receiving
    }

    int youngest = -1;
    for (int i = 1; i <= n; i++) {
        if (score[i] == n - 1) {
            youngest = i;
            break;
        }
    }

    printf("%d\n", youngest);
    free(score); // Always free dynamically allocated memory!
}

int main() {
    // Example test case driver
    int gifts[2][2] = {{1, 3}, {2, 3}};
    find_youngest_member(3, 2, gifts);
    return 0;
}
