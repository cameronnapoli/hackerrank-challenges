// Written by: Cameron Napoli
// 2018-07-18
// Problem found on hackerrank.com at:
//     https://www.hackerrank.com/challenges/two-two/problem


import java.io.FileNotFoundException;
import java.io.FileReader;
import java.math.BigInteger;
import java.io.File;
import java.util.Scanner;


class Trie {

    // Alphabet size (# of symbols)
    static final int ALPHABET_SIZE = 10;
    static final char ALP_START = '0';
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public class TrieNode {
        TrieNode[] children = new TrieNode[ALPHABET_SIZE];
        boolean isEnd;

        TrieNode() {
            isEnd = false;
            for (int i = 0; i < ALPHABET_SIZE; i++) {
                children[i] = null;
            }
        }
    };

    public void insert(String key) {
        int level;
        int index;

        TrieNode pCrawl = root;

        for (level = 0; level < key.length(); level++) {
            index = key.charAt(level) - ALP_START;

            if (index < 0 || index >= ALPHABET_SIZE) {
                throw new ArrayIndexOutOfBoundsException("Key contains character '"
                        + key.charAt(level) +"' which is not in the alphabet.");
            }

            if (pCrawl.children[index] == null)
                pCrawl.children[index] = new TrieNode();

            pCrawl = pCrawl.children[index];
        }

        pCrawl.isEnd = true; // Mark leaf node
    }

    public int countHits(String subStr) {
        int count = 0;
        TrieNode pCrawl = root;

        for (int level = 0; level < subStr.length(); level++) {
            int index = subStr.charAt(level) - ALP_START;
            if (index < 0 || index >= ALPHABET_SIZE) {
                throw new ArrayIndexOutOfBoundsException("Key contains character '"
                        + subStr.charAt(level) + "' which is not in the alphabet.");
            }

            if (pCrawl.children[index] == null) {
                break;
            }
            if (pCrawl.children[index].isEnd) {
                count++;
            }

            pCrawl = pCrawl.children[index];
        }

        return count;
    }
}


public class Main {
    public static Trie generateTrie(int nLower, int nUpper) {
        Trie ntRoot = new Trie();
        BigInteger two = BigInteger.valueOf(2);
        for (int i = nLower; i <= nUpper; i++) {
            String resStr = two.pow(i).toString();
            System.out.println("resStr.length(): " + resStr.length()); // 242
            ntRoot.insert(resStr);
        }
        return ntRoot;
    }

    public static int twoTwo(String inp) {
        // TODO: Scan string for bad alphabet characters

        Trie ntRoot = generateTrie(0, 800);

        int maxLen = BigInteger.valueOf(2).pow(800).toString().length();

        int count = 0;

        for (int i = 0; i < inp.length(); i++) {
            if (inp.charAt(i) != '0') {
                int end = min(inp.length(), i + maxLen);

                count += ntRoot.countHits(inp.substring(i, end));
            }
        }

        return count;
    }

    public static int min(int a, int b) {
        if (a < b) {
            return a;
        } return b;
    }

    public static void main(String[] args) throws FileNotFoundException {
        long startTime = System.nanoTime();
        String inp = "8192749812";

        File file = new File("C:\\Users\\cnapoli\\Documents\\Code\\hackerrank-challenges\\twotwo_test.txt");
        Scanner sc = new Scanner(file);

        while (sc.hasNextLine()) {
            inp = sc.nextLine();
            System.out.println(inp.substring(0, 50) + " ...");
        }

        int res = twoTwo(inp);
        System.out.println("Result: " + res);
        System.out.println("");

        long endTime   = System.nanoTime();
        long totalTime = endTime - startTime;
        System.out.println(totalTime / 1000000.0 + "ms");
    }
}
