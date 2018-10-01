# Written by: Cameron Napoli
# Problem found on hackerrank.com at:
#     https://www.hackerrank.com/challenges/find-strings/problem

import os
import sys
from itertools import permutations


# NOTE:
# Test cases 4, 5, 6 not passing
# Compressed trie or suffix tree will most likely solve
# this problem within the required time complexity


def genSubstringSet(s):
    return set([s[i:j + 1] for i in range(len(s)) for j in range(i, len(s))])


def genSortedUnion(w):
    unionSet = set()

    # generate substring sets
    for word in w:
        subtringSet = genSubstringSet(word)

        # union substring sets
        unionSet = unionSet.union(subtringSet)

    # sort and return sorted union
    return sorted(unionSet)


def outputFromQuery(sortedUnion, query):
    if query > len(sortedUnion):
        return "INVALID"
    return sortedUnion[query - 1]


def findStrings(w, queries):
    sortedUnion = genSortedUnion(w)
    for query in queries:
        print(outputFromQuery(sortedUnion, query))




if __name__ == '__main__':
    # w = ["aab", "aac"]
    # queries = [3, 8, 23]

    w = [
        "cxxzmhcpmrrbbvskesaoyvejoluqiqnrdrikdhnobnqzksjvdveuzdfpctpbragcazdsglasjqhwwwavadbtnogmcoxvyoekmttrksszcxdbrgpvvcprfgksfmotxbtamxswbkeputygxsfsypdtyowinlbxovbbxsxwtmgjsrkhimkcfxalyqhegmubprhvxopbfakicefmuqkcmmhisgsinvlopzlkptuaqagdashwhldeoqzwdnjzrimkixsbbghjdlnrmxwclizcvgwmviukjcaxvfjuixmbxkuqsbkvduywpkzecxkctwkmiyxqjtbmcmoaitjhqspjlnltvhzumigkztgieccigvgginqpyfboxehqnlymkcyckbsknenkrtwdsmqmckbzvmcqqksklmhvnwjezgjlewfcnwgrychzzwkykvhssmwsvzyondyymobxpwsgsdluraqoordqojqzrilrkdmkxskaccnszhuojbxicxafxrgockziafyojkfuhqayojhebzznfpclovnthfutrqypwjcharjphbodmjlngaybexymhmhfjvroxileqmsnuhmmhhcwblywnxkklmizfkqnleugsuuwiblywxxcnezcrrnpehtgyjnauyciuaosouqfawghharwazsmmnkwofbyvoiehzhnupgwlzwmybjpishdbazemfnhsndpurbaldznkijxnoejzcdfzzxnctiulyhmdywulywtoarvmynqctnhhdlxpvfixntcbbmjmhanovgwzihtstpjkocjryyiychidylwhyxoxpkqbxuypbgqcatheprmzngzjxtxjpknecfaetnxfdcbrklppowhqgmrqflbowqvbsibplmblkcalafnljxjdckvydpnacqndivqadeavxlqgliencdybzvssionzwnolcphkxkapxxbfrlvahreeqoqtisffuxkcvkmfxeamxwwiwnsfuchemzembldkxvngdbrlsqkkqewgmnzrzyfepvgogeysnylnuscrvhfcjiystpwphnjbcejkwjbqdgjqinkkvmqzuvhwpvqsgswncwkdhmjmhjidqodpwbwaqyzqkivblunffuoomqqytnjgzbkypcttsqokhphgiseerzddablsqdvsxchyhipkuuzbksbudnmobwryjezfxosiyqrcffkmouvmjmgyjgezagexduprokrkvfkmtiakzsspgysfsjgjlejkheouukrlutgitdopmzcdwqqnyjhzfpvuuzkzepprtntixrrrkwxpwdgvrrlmpwvcuxdiopvvaivkltahqxwmqkdltcvrpqvabyxtbpjccaioeeyqhooljkzoznvcgmwczzmvwecpsambwumhldxtzydkiwxklbzitlwdgzpujmimftcastohgazijqgjnofnhexlihovyuhkekfjhslffhdiroerkbygyrppjiipgazgnnhrzod",
        "cxxzmhcpmrrbbvskesaoyvejoluqiqnrdrikdhnobnqzksjvdveuzdfpctpbragcazdsglasjqhwwwavadbtnogmcoxvyoekmttrksszcxdbrgpvvcprfgksfmotxbtamxswbkeputygxsfsypdtyowinlbxovbbxsxwtmgjsrkhimkcfxalyqhegmubprhvxopbfakicefmuqkcmmhisgsinvlopzlkptuaqagdashwhldeoqzwdnjzrimkixsbbghjdlnrmxwclizcvgwmviukjcaxvfjuixmbxkuqsbkvduywpkzecxkctwkmiyxqjtbmcmoaitjhqspjlnltvhzumigkztgieccigvgginqpyfboxehqnlymkcyckbsknenkrtwdsmqmckbzvmcqqksklmhvnwjezgjlewfcnwgrychzzwkykvhssmwsvzyondyymobxpwsgsdluraqoordqojqzrilrkdmkxskaccnszhuojbxicxafxrgockziafyojkfuhqayojhebzznfpclovnthfutrqypwjcharjphbodmjlngaybexymhmhfjvroxileqmsnuhmmhhcwblywnxkklmizfkqnleugsuuwiblywxxcnezcrrnpehtgyjnauyciuaosouqfawghharwazsmmnkwofbyvoiehzhnupgwlzwmybjpishdbazemfnhsndpurbaldznkijxnoejzcdfzzxnctiulyhmdywulywtoarvmynqctnhhdlxpvfixntcbbmjmhanovgwzihtstpjkocjryyiychidylwhyxoxpkqbxuypbgqcatheprmzngzjxtxjpknecfaetnxfdcbrklppowhqgmrqflbowqvbsibplmblkcalafnljxjdckvydpnacqndivqadeavxlqgliencdybzvssionzwnolcphkxkapxxbfrlvahreeqoqtisffuxkcvkmfxeamxwwiwnsfuchemzembldkxvngdbrlsqkkqewgmnzrzyfepvgogeysnylnuscrvhfcjiystpwphnjbcejkwjbqdgjqinkkvmqzuvhwpvqsgswncwkdhmjmhjidqodpwbwaqyzqkivblunffuoomqqytnjgzbkypcttsqokhphgiseerzddablsqdvsxchyhipkuuzbksbudnmobwryjezfxosiyqrcffkmouvmjmgyjgezagexduprokrkvfkmtiakzsspgysfsjgjlejkheouukrlutgitdopmzcdwqqnyjhzfpvuuzkzepprtntixrrrkwxpwdgvrrlmpwvcuxdiopvvaivkltahqxwmqkdltcvrpqvabyxtbpjccaioeeyqhooljkzoznvcgmwczzmvwecpsambwumhldxtzydkiwxklbzitlwdgzpujmimftcastohgazijqgjnofnhexlihovyuhkekfjhslffhdiroerkbygyrppjiipgazgnnhrzodo"
    ]
    queries = [200, 4815, 32665]

    findStrings(w, queries)

#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     w_count = int(input())
#
#     w = []
#
#     for _ in range(w_count):
#         w_item = input()
#         w.append(w_item)
#
#     queries_count = int(input())
#
#     queries = []
#
#     for _ in range(queries_count):
#         queries_item = int(input())
#         queries.append(queries_item)
#
#     result = findStrings(w, queries)
#
#     fptr.write('\n'.join(result))
#     fptr.write('\n')
#
#     fptr.close()
