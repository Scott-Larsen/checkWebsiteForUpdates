import requests
import time
import smtplib
import hashlib
from fake_useragent import UserAgent
from os import path
from urllib.request import urlopen

MIN_LENGTH_MATCH = 7

# from difflib import ndiff, SequenceMatcher

# from difflib import Differ
# import difflib

# from bs4 import BeautifulSoup

# sites = {"scott@scottlarsen.com": {"http://scottlarsen.com": 3}}
sites = {
    "scott@scottlarsen.com": {
        "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Vaccine.aspx": 1,
        "https://www.doylestownhealth.org/patients-and-visitors/patient-resources/covid19-resources": 2,
    }
}

ua = UserAgent()
header = {"User-Agent": str(ua.random)}


def downloadText(url):
    from urllib.request import Request, urlopen

    # print("inside downloadText")

    # "http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1"
    req = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    htmlContent = requests.get(url, headers=header)
    # print("htmlContent.text", htmlContent.text)
    return htmlContent.text


def saveText(text, filepath):
    with open(
        filepath,
        "w",
    ) as f:
        f.write(text)
        # f.writelines(text)


def openFile(filepath):
    with open(
        filepath,
        "r",
    ) as f:
        return f.read()
        return f.readlines()  # .splitlines()


# #difflib
# def compareOldAndNew(filepath1, filepath2):
#     text1, text2 = openFile(filepath1), openFile(filepath2)
#     if text1 != text2:
#         percentChange = int((1 - SequenceMatcher(None, "text1", "text2").ratio()) * 100)
#         print(f"\n{percentChange}% change.")
#         # print(f"{10 * SequenceMatcher(None, "text1", "text2").ratio()} has changed.")
#         print("\nMismatches:\n")

#         mismatches = [f"-----{li}" for li in ndiff(text1, text2)]  # if li[0] != " "]
#         for mismatch in mismatches:
#             print(mismatch)
#     else:
#         print("No change")


# def extractLongestString(t1, t2):
#     # print(t1)
#     # print(t2)
#     noChange = False
#     while noChange == False:
#         noChange = True
#         longestSubstring = ""
#         i = 0
#         for i in range(10):  # len(t1) - 1):
#             if len(t1) - i > len(longestSubstring):
#                 j = 1
#                 while i + j < len(t1):  # + 1:
#                     if t1[i : i + j] in t2:
#                         if j > len(longestSubstring) and j > 3:  # and " " t1[i: i + j]:
#                             noChange = False
#                             longestSubstring = t1[i : i + j]
#                             print(longestSubstring[:30], "\n\n\n")
#                             li, lj = i, j
#                     j += 1
#             t1 = t1[:li] + t1[li + lj :]
#             print(len(t1))
#         if noChange == False:
#             print(len(t1))
#         # print(t1)
#         # print(text2)
#     return t1


# def compareOldAndNew(newText, oldText):
#     if newText != oldText:
#         print("Mismatch\n")
#         nt = newText[:]
#         nt = extractLongestString(nt, oldText)
#         print(f"The text has changed {int(len(nt) / len(newText) * 100)}%.")
#     else:
#         print("No change")


def findLongestString(t1, t2):
    i, j = 0, MIN_LENGTH_MATCH
    longestString = ""
    while i + j < len(t1):
        currentString = t1[i : i + j]
        if t1[i : i + j] in t2:
            x = t2.index(t1[i : i + j])
            while i + j < len(t1) and x + j < len(t2) and t1[i + j] == t2[x + j]:
                currentString = t1[i : i + j]
                j += 1
            if j > len(longestString):
                longestString = t1[i : i + j]
            else:
                i += 1
            i = i + j
            j = MIN_LENGTH_MATCH
        else:
            i += 1
    return longestString


def diff(t1, t2):
    matchingStrings = []
    while len(findLongestString(t1, t2)) > 0:
        longestString = findLongestString(t1, t2)
        matchingStrings.append(longestString)
        t1 = "^".join(t1.split(longestString))
        t2 = "^".join(t2.split(longestString))
        # print(t1)
    return t1, t2, matchingStrings


def main():
    for email in sites.keys():
        for url in sites[email].keys():
            # print(downloadText(url))
            filepath = f"/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/checkWebsiteForUpdates/{sites[email][url]}.txt"
            if not path.exists(filepath):
                print(f"\nNo existing record for {url}, downloading now")
                saveText(downloadText(url), filepath)
            else:
                saveText(downloadText(url), "current.txt")
                newText, oldText = openFile("current.txt"), openFile(filepath)
                diffT1, diffT2, matchingStrings = diff(newText, oldText)
                print(f"\nNew in most recent edit of {url}....")
                for d in diffT1.split("^"):
                    if len(d.strip()) > 1:
                        print(d.strip())


if __name__ == "__main__":
    main()