// https://www.hackerrank.com/challenges/permutation-equation/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the permutationEquation function below.
    static int[] permutationEquation(int[] p) {
        int result[] = new int[p.length];

        // 1 index loop to frame the problem towards the question
        for (int i = 1; i <= p.length; i++) {
            int p_ind1 = 1;

            // first find where i appears in p
            for (int j = 1; j <= p.length; j++) {
                if (p[j-1] == i) {
                    p_ind1 = j;
                }
            }

            int p_ind2 = 1;
            // find where that index appears in p
            for (int j = 1; j <= p.length; j++) {
                if (p[j-1] == p_ind1) {
                    p_ind2 = j;
                }
            }

            result[i-1] = p_ind2;
        }

        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] p = new int[n];

        String[] pItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int pItem = Integer.parseInt(pItems[i]);
            p[i] = pItem;
        }

        int[] result = permutationEquation(p);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

