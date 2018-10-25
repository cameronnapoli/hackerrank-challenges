// Written by: Cameron Napoli
// Problem found on hackerrank.com at:
//    https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


class IndexSpan {
    private Integer key;
    private Integer index;
    private Integer spanLength;
    public IndexSpan(Integer key, Integer index, Integer spanLength) {
        this.setIndexSpan(key, index, spanLength);
    }
    public void setIndexSpan(Integer key, Integer index, Integer spanLength) {
        this.key = key;
        this.index = index;
        this.spanLength = spanLength;
    }
    public int getKey() {
        return (int)key;
    }
    public int getIndex() {
        return (int)index;
    }
    public int getSpanEnd() {
        return (int)index + (int)spanLength;
    }
}


class MedianStructure {
    // NOTE: values will function as a queue
    private ArrayList<Integer> values;
    private HashMap<Integer, Integer> freq;
    private int trailLen;

    public MedianStructure(int d) {
        values = new ArrayList<Integer>();
        freq = new HashMap<Integer, Integer>();
        trailLen = d;
    }
    public void insert(int v) {
        if (values.size() > trailLen) {
            throw new ArrayIndexOutOfBoundsException("Somehow values got too big! values.size(): "
                    + values.size() + ", trailLen: " + trailLen);
        }

        // Remove element from queue if size gets too big
        if (values.size() == trailLen) {
            int removedKey = values.remove(0);
            freq.put(removedKey, freq.get(removedKey) - 1);
            if (freq.get(removedKey) == 0) {
                freq.remove(removedKey);
            }
        }

        if (freq.get(v) == null) {
            freq.put(v, 1);
        } else {
            freq.put(v, freq.get(v) + 1);
        }
        values.add(v);
    }
    private static float avg(int a, int b) {
        return ((float)a + (float)b) / 2;
    }
    public float getMedian() {
        // Need to modify because the trailing expenditure is only size d
        if (values.size() == 0) {
            throw new ArrayIndexOutOfBoundsException("Attempt to get median on empty structure");
        }

        // Loop through sorted keys of freq to find median
        List<Integer> keys = new ArrayList<Integer>(freq.keySet());
        Collections.sort(keys);

        int index = 0;
        int listSize = values.size();
        IndexSpan prevSpan = new IndexSpan(null, null, null);

        for (int key : keys) {
            // If the search index is on or immediately after the center of the list
            if (index == listSize / 2) {
                if (listSize % 2 != 0) { // odd sized list
                    return key;
                } else { // even sized list
                    return avg(key, prevSpan.getKey());
                }
            }
            else if (index > listSize / 2) {
                if (listSize % 2 != 0) {
                    return prevSpan.getKey();
                } else {
                    // Case if the previous key isn't overlapping the median position
                    if (prevSpan.getSpanEnd() < listSize / 2) {
                        return key;
                    }
                    // Case if the previous key is overlapping the median position
                    else {
                        return prevSpan.getKey();
                    }
                }
            }

            prevSpan.setIndexSpan(key, index, freq.get(key));
            index += freq.get(key);
        }
        return prevSpan.getKey();
    }
}


public class Solution {

    static int activityNotifications(int[] expenditure, int d) {
        MedianStructure medStrct = new MedianStructure(d);
        int totalFraudNotif = 0;

        for (int i = 0; i < d; i++) {
            medStrct.insert(expenditure[i]);
        }

        for (int i = d; i < expenditure.length; i++) {

            if ((float)expenditure[i] >= medStrct.getMedian() * 2) {
                totalFraudNotif += 1;
            }

            medStrct.insert(expenditure[i]);
        }
        return totalFraudNotif;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);
        int d = Integer.parseInt(nd[1]);

        int[] expenditure = new int[n];

        String[] expenditureItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int expenditureItem = Integer.parseInt(expenditureItems[i]);
            expenditure[i] = expenditureItem;
        }

        int result = activityNotifications(expenditure, d);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
        scanner.close();
    }
}
