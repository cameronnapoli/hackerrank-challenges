// Written by: Cameron Napoli
// 2018-11-05
// Problem found on leetcode at:
//     https://leetcode.com/problems/max-increase-to-keep-city-skyline/

import java.lang.Math;

class Solution {
    private int[] maxOfColumns(int[][] grid) {
        int[] res = new int[grid[0].length];
        for (int c = 0; c < grid[0].length; c++) {
            int currMax = 0;
            for (int r = 0; r < grid.length; r++) {
                if (grid[r][c] > currMax) {
                    currMax = grid[r][c];
                }
            }
            res[c] = currMax;
        }
        return res;
    }

    private int[] maxOfRows(int[][] grid) {
        int[] res = new int[grid.length];
        for (int r = 0; r < grid.length; r++) {
            int currMax = 0;
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] > currMax) {
                    currMax = grid[r][c];
                }
            }
            res[r] = currMax;
        }
        return res;
    }

    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] maxColumns = maxOfColumns(grid);
        int[] maxRows = maxOfRows(grid);

        int amtIncrease = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                amtIncrease += Math.min(maxColumns[c], maxRows[r]) - grid[r][c];
            }
        }
        return amtIncrease;
    }
}
