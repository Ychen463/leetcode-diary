/**
 * @param {number[]} nums
 * @return {boolean}
 */
 /**
 题目描述
给定一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

解题思路
这个问题可以通过贪心算法来解决。贪心算法的核心思想是在每一步都做出在当前看来最好的选择。对于跳跃游戏来说，我们可以追踪当前能够到达的最远位置，然后遍历数组来更新这个最远位置。如果在遍历过程中能够到达数组的末尾，那么就返回 true。

初始化：最远可以到达的位置 maxReach 设置为 0。
遍历数组：对于数组中的每个元素，我们检查是否能从当前位置继续往前走（即当前位置 i 是否在 maxReach 范围内）。如果可以，我们更新 maxReach 为 max(maxReach, i + nums[i])，即当前位置加上在当前位置可以跳的最远距离。
检查能否到达终点：如果在某次遍历中 maxReach 已经大于或等于最后一个位置的索引，那么就表示我们可以到达数组的末尾。
 */
var canJump = function(nums) {
    let maxReach = 0; // 初始化最远可以到达的位置
    for (let i = 0; i < nums.length; i++) {
        if (i > maxReach) {
            // 如果当前位置超过了之前计算的最远可以到达的位置，表示无法到达当前位置
            return false;
        }
        // 更新最远可以到达的位置
        maxReach = Math.max(maxReach, i + nums[i]);
        if (maxReach >= nums.length - 1) {
            // 如果最远可以到达的位置已经达到或超过了数组的末尾，表示可以到达
            return true;
        }
    }
    return false;
};