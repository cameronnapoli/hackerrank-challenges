// Written by: Cameron Napoli
// Problem found on hackerrank.com at:
//    https://www.hackerrank.com/challenges/java-1d-array/problem

import java.util.HashSet;

class Solution {

    private static boolean indexInBounds(int index, int len) {
        if (index < len && index >= 0) {
            return true;
        } return false;
    }

    public static boolean helper(int leap, int[] game, int currIndex, HashSet<Integer> visited) {
        if (visited.contains(currIndex)) {
            return false;
        }
        visited.add(currIndex);

        if (currIndex == game.length - 1 || currIndex + leap >= game.length) {
            return true;
        }

        if (indexInBounds(currIndex + leap, game.length) && game[currIndex + leap] == 0) {
            if (helper(leap, game, currIndex + leap, visited)) {return true;}
        }
        if (indexInBounds(currIndex + 1, game.length) && game[currIndex + 1] == 0) {
            if (helper(leap, game, currIndex + 1, visited)) {return true;}
        }
        if (indexInBounds(currIndex - 1, game.length) && game[currIndex - 1] == 0) {
            if (helper(leap, game, currIndex - 1, visited)) {return true;}
        }
        return false;
    }

    public static boolean canWin(int leap, int[] game) {
        return helper(leap, game, 0, new HashSet<Integer>());
    }
}

public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();

        int leap = 4;
        int[] game = {0, 1, 1, 0, 0, 1, 1, 0, 1};

        boolean r = s.canWin(leap, game);
        if (r) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
