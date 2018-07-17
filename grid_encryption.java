// Written by: Cameron Napoli
// 2018-07-17
// Problem found on hackerrank.com at:
//     https://www.hackerrank.com/challenges/encryption/problem

package com.company;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.lang.Math;


class Grid {
    private char[][] g;
    Grid(String s, int nRows, int nCols) {
        g = new char[nRows][nCols];
        // Load s into grid
        int si = 0;
        for (int i = 0; i < nRows; i++) {
            for (int j = 0; j < nCols; j++) {
                if (si > s.length()-1) {
                    g[i][j] = '\0';
                } else {
                    g[i][j] = s.charAt(si);
                } si++;
            }
        }
    }
    public String encryptFromGrid() {
        // Read by cols not by rows
        String res = "";
        for (int j = 0; j < numCols(); j++) {
            if (j != 0) {
                res += " ";
            }
            for (int i = 0; i < numRows(); i++) {
                if (g[i][j] != '\0') {
                    res += g[i][j];
                }
            }
        }
        return res;
    }
    private int numRows() {
        return g.length;
    }
    private int numCols() {
        return g[0].length;
    }
    @Override
    public String toString() {
        String res = "";
        for (int i = 0; i < g.length; i++) {
            for (int j = 0; j < g[i].length; j++) {
                res += g[i][j] + " ";
            } res += "\n";
        } return res;
    }
}


public class Main {

    public static String removeSpaces(String s) {
        return s.replaceAll(" ", "");
    }

    public static String encryption(String s) {
        s = removeSpaces(s);
        int L = s.length();

        int nRows = (int)Math.floor(Math.sqrt(L));
        int nCols = (int)Math.ceil(Math.sqrt(L));

        // Make sure cols * rows >= length of s
        if (nRows * nCols < s.length()) {
            if (nRows < nCols) { nRows++; }
            else               { nCols++; }
        }

        Grid g = new Grid(s, nRows, nCols);

        System.out.println(g);

        return g.encryptFromGrid();
    }

    public static void main(String[] args) {
        String s = "if man was meant to stay on the ground god would have given us roots";

        String result = encryption(s);
        System.out.println(result);
    }
}
