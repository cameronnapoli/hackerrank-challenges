// https://www.hackerrank.com/challenges/extra-long-factorials/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Solution {

    static BigInteger fact(BigInteger n) {
        if (n.compareTo(BigInteger.valueOf(2)) <= 0) {
            return n;
        }
        return n.multiply(fact(n.subtract(BigInteger.valueOf(1))));
    }

    // Complete the extraLongFactorials function below.
    static void extraLongFactorials(int n) {
        BigInteger fsol = fact(BigInteger.valueOf(n));
        System.out.println(fsol);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        extraLongFactorials(n);

        scanner.close();
    }
}
