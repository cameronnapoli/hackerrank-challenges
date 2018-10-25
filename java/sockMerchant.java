// Written by: Cameron Napoli
// 2018-07-18
// Problem found on hackerrank.com at:
//     https://www.hackerrank.com/challenges/sock-merchant/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Main {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < ar.length; i++) {
            if (! map.containsKey(ar[i]) ) {
                map.put(ar[i], 1);
            } else {
                map.put(ar[i], 1+map.get(ar[i]));
            }
        }

        int total = 0;

        for (Map.Entry<Integer, Integer> item : map.entrySet()) {
            Integer value = item.getValue();
            System.out.println(item.getKey() + " => " + item.getValue());
            total += value - (value % 2);
        }

        return total / 2;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
