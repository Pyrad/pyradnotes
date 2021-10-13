# Top 100 Liked Problems Solutions

- 1 - 10

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 1     | [Two Sum](https://leetcode.com/problems/two-sum)             |              | 40.2%          | Easy           |               |
| 2     | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) |              | 30.4%          | Medium         |               |
| 3     | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) |              | 26.1%          | Medium         |               |
| 4     | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) |              | 25.3%          | Hard           |               |
| 5     | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) |              | 26.4%          | Medium         |               |
| 10    | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) |              | 24.9%          | Hard           |               |
| 11    | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) |              | 42.1%          | Medium         |               |
| 15    | [3Sum](https://leetcode.com/problems/3sum)                   |              | 23.2%          | Medium         |               |
| 17    | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) |              | 40.1%          | Medium         |               |
| 19    | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) |              | 33.9%          | Medium         |               |



## 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

 

**Constraints:**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **Only one valid answer exists.**

 

**Follow-up:** Can you come up with an algorithm that is less than `O(n2) `time complexity?

```cpp

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::vector<int> res;
    if (nums.empty()) {
        return res;
    }

    std::unordered_map<int, int> imap;
    int idx = 0;
    for (const auto i : nums) {
        int sup = target - i;
        if (imap.count(sup) != 0) {
            res.push_back(imap[sup]);
            res.push_back(idx);
        }
        imap.emplace(i, idx);
        idx++;
    }
    return  res;
}

```









- 11 - 20

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 20    | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) |              | 35.7%          | Easy           |               |
| 21    | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) |              | 45.5%          | Easy           |               |
| 22    | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) |              | 52.8%          | Medium         |               |
| 23    | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) |              | 32.6%          | Hard           |               |
| 31    | [Next Permutation](https://leetcode.com/problems/next-permutation) |              | 30.0%          | Medium         |               |
| 32    | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) |              | 24.8%          | Hard           |               |
| 33    | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) |              | 32.6%          | Medium         |               |
| 34    | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) |              | 32.8%          | Medium         |               |
| 39    | [Combination Sum](https://leetcode.com/problems/combination-sum) |              | 46.3%          | Medium         |               |
| 42    | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) |              | 41.5%          | Hard           |               |

- 21 - 30

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 46    | [Permutations](https://leetcode.com/problems/permutations)   |              | 53.0%          | Medium         |               |
| 48    | [Rotate Image](https://leetcode.com/problems/rotate-image)   |              | 46.4%          | Medium         |               |
| 49    | [Group Anagrams](https://leetcode.com/problems/group-anagrams) |              | 44.3%          | Medium         |               |
| 53    | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) |              | 42.6%          | Easy           |               |
| 55    | [Jump Game](https://leetcode.com/problems/jump-game)         |              | 31.1%          | Medium         |               |
| 56    | [Merge Intervals](https://leetcode.com/problems/merge-intervals) |              | 34.6%          | Medium         |               |
| 62    | [Unique Paths](https://leetcode.com/problems/unique-paths)   |              | 46.1%          | Medium         |               |
| 64    | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum) |              | 45.2%          | Medium         |               |
| 70    | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) |              | 43.2%          | Easy           |               |
| 72    | [Edit Distance](https://leetcode.com/problems/edit-distance) |              | 36.2%          | Hard           |               |

- 31 - 40

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 75    | [Sort Colors](https://leetcode.com/problems/sort-colors)     |              | 41.1%          | Medium         |               |
| 76    | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) |              | 29.6%          | Hard           |               |
| 78    | [Subsets](https://leetcode.com/problems/subsets)             |              | 50.5%          | Medium         |               |
| 79    | [Word Search](https://leetcode.com/problems/word-search)     |              | 30.2%          | Medium         |               |
| 84    | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram) |              | 30.1%          | Hard           |               |
| 85    | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle) |              | 32.2%          | Hard           |               |
| 94    | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) |              | 54.7%          | Medium         |               |
| 96    | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees) |              | 44.8%          | Medium         |               |
| 98    | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree) |              | 25.1%          | Medium         |               |
| 101   | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree) |              | 42.5%          | Easy           |               |

- 41 - 50

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 102   | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) |              | 46.7%          | Medium         |               |
| 104   | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) |              | 58.9%          | Easy           |               |
| 105   | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) |              | 39.1%          | Medium         |               |
| 114   | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) |              | 40.8%          | Medium         |               |
| 121   | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) |              | 46.0%          | Easy           |               |
| 124   | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum) |              | 29.1%          | Hard           |               |
| 128   | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) |              | 40.7%          | Hard           |               |
| 136   | [Single Number](https://leetcode.com/problems/single-number) |              | 58.7%          | Easy           |               |
| 139   | [Word Break](https://leetcode.com/problems/word-break)       |              | 34.1%          | Medium         |               |
| 141   | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle) |              | 35.5%          | Easy           |               |

- 51 - 60

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 142   | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii) |              | 30.7%          | Medium         |               |
| 146   | [LRU Cache](https://leetcode.com/problems/lru-cache)         |              | 23.7%          | Hard           |               |
| 148   | [Sort List](https://leetcode.com/problems/sort-list)         |              | 33.6%          | Medium         |               |
| 152   | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray) |              | 28.4%          | Medium         |               |
| 155   | [Min Stack](https://leetcode.com/problems/min-stack)         |              | 35.3%          | Easy           |               |
| 160   | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists) |              | 31.9%          | Easy           |               |
| 169   | [Majority Element](https://leetcode.com/problems/majority-element) |              | 51.2%          | Easy           |               |
| 198   | [House Robber](https://leetcode.com/problems/house-robber)   |              | 40.7%          | Easy           |               |
| 200   | [Number of Islands](https://leetcode.com/problems/number-of-islands) |              | 40.0%          | Medium         |               |
| 206   | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) |              | 52.3%          | Easy           |               |

- 61 - 70

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 207   | [Course Schedule](https://leetcode.com/problems/course-schedule) |              | 36.4%          | Medium         |               |
| 208   | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree) |              | 36.4%          | Medium         |               |
| 215   | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array) |              | 45.5%          | Medium         |               |
| 221   | [Maximal Square](https://leetcode.com/problems/maximal-square) |              | 32.1%          | Medium         |               |
| 226   | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree) |              | 56.8%          | Easy           |               |
| 234   | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list) |              | 35.2%          | Easy           |               |
| 236   | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) |              | 35.0%          | Medium         |               |
| 238   | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) |              | 53.6%          | Medium         |               |
| 239   | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum) |              | 36.8%          | Hard           |               |
| 240   | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii) |              | 40.1%          | Medium         |               |

- 71 - 80

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 253   | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii) |              | 41.9%          | Medium         |               |
| 279   | [Perfect Squares](https://leetcode.com/problems/perfect-squares) |              | 40.4%          | Medium         |               |
| 283   | [Move Zeroes](https://leetcode.com/problems/move-zeroes)     |              | 53.4%          | Easy           |               |
| 287   | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number) |              | 48.0%          | Medium         |               |
| 297   | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree) |              | 39.0%          | Hard           |               |
| 300   | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence) |              | 40.1%          | Medium         |               |
| 301   | [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses) |              | 38.2%          | Hard           |               |
| 309   | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) |              | 43.4%          | Medium         |               |
| 312   | [Burst Balloons](https://leetcode.com/problems/burst-balloons) |              | 46.0%          | Hard           |               |
| 322   | [Coin Change](https://leetcode.com/problems/coin-change)     |              | 28.8%          | Medium         |               |

- 81 - 90

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 337   | [House Robber III](https://leetcode.com/problems/house-robber-iii) |              | 47.1%          | Medium         |               |
| 338   | [Counting Bits](https://leetcode.com/problems/counting-bits) |              | 63.8%          | Medium         |               |
| 347   | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) |              | 53.1%          | Medium         |               |
| 394   | [Decode String](https://leetcode.com/problems/decode-string) |              | 43.6%          | Medium         |               |
| 406   | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height) |              | 58.7%          | Medium         |               |
| 416   | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum) |              | 39.7%          | Medium         |               |
| 437   | [Path Sum III](https://leetcode.com/problems/path-sum-iii)   |              | 41.8%          | Easy           |               |
| 438   | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string) |              | 36.1%          | Easy           |               |
| 448   | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array) |              | 52.6%          | Easy           |               |
| 461   | [Hamming Distance](https://leetcode.com/problems/hamming-distance) |              | 70.0%          | Easy           |               |

- 91 - 100

| **#** | **Title**                                                    | **Solution** | **Acceptance** | **Difficulty** | **Frequency** |
| ----- | ------------------------------------------------------------ | ------------ | -------------- | -------------- | ------------- |
| 494   | [Target Sum](https://leetcode.com/problems/target-sum)       |              | 44.8%          | Medium         |               |
| 538   | [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree) |              | 49.8%          | Easy           |               |
| 543   | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree) |              | 46.1%          | Easy           |               |
| 560   | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k) |              | 41.5%          | Medium         |               |
| 572   | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree) |              | 41.1%          | Easy           |               |
| 581   | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray) |              | 29.6%          | Easy           |               |
| 617   | [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees) |              | 69.0%          | Easy           |               |
| 621   | [Task Scheduler](https://leetcode.com/problems/task-scheduler) |              | 44.1%          | Medium         |               |
| 647   | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings) |              | 55.5%          | Medium         |               |
| 771   | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones) |              | 82.6%          | Easy           |               |



**出现频度为5** 

1. Leet Code OJ 1. Two Sum [Difficulty: Easy] 
2. Leet Code OJ 8. String to Integer (atoi) [Difficulty: Easy] 
3. Leet Code OJ 15. 3Sum [Difficulty: Medium] 
4. Leet Code OJ 20. Valid Parentheses [Difficulty: Easy] 
5. Leet Code OJ 21. Merge Two Sorted Lists [Difficulty: Easy] 
6. Leet Code OJ 28. Implement strStr() [Difficulty: Easy] 
7. Leet Code OJ 56. Merge Intervals [Difficulty: Hard] 
8. Leet Code OJ 57. Insert Interval [Difficulty: Hard] 
9. Leet Code OJ 65. Valid Number [Difficulty: Hard] 
10. Leet Code OJ 70. Climbing Stairs [Difficulty: Easy] 
11. Leet Code OJ 73. Set Matrix Zeroes [Difficulty: Medium] 
12. Leet Code OJ 88. Merge Sorted Array [Difficulty: Easy] 
13. Leet Code OJ 98. Validate Binary Search Tree [Difficulty: Medium] 
14. Leet Code OJ 125. Valid Palindrome [Difficulty: Easy] 
15. Leet Code OJ 127. Word Ladder [Difficulty: Medium]

**出现频度为4**

1. Leet Code OJ 2. Add Two Numbers [Difficulty: Medium] 
2. Leet Code OJ 12. Integer to Roman 
3. Leet Code OJ 13. Roman to Integer 
4. Leet Code OJ 22. Generate Parentheses 
5. Leet Code OJ 23. Merge k Sorted Lists 
6. Leet Code OJ 24. Swap Nodes in Pairs 
7. Leet Code OJ 27. Remove Element [Difficulty: Easy] 
8. Leet Code OJ 46. Permutations 
9. Leet Code OJ 49. Anagrams 
10. Leet Code OJ 67. Add Binary 
11. Leet Code OJ 69. Sqrt(x) 
12. Leet Code OJ 77. Combinations 
13. Leet Code OJ 78. Subsets 
14. Leet Code OJ 79. Word Search 
15. Leet Code OJ 91. Decode Ways [Difficulty: Medium] 
16. Leet Code OJ 102. Binary Tree Level Order Traversal [Difficulty: Easy] 
17. Leet Code OJ 129. Sum Root to Leaf Numbers 
18. Leet Code OJ 131. Palindrome Partitioning
