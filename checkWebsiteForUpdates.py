import requests
from fake_useragent import UserAgent
from os import path

from sendEMail import sendEMail
from config import FROM_EMAIL

TESTING = False
MIN_LENGTH_MATCH = 7
CHANGE_THRESHOLD = 1

if not TESTING:
    sites = {
        FROM_EMAIL: {
            "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Vaccine.aspx": 1,
            "https://www.doylestownhealth.org/patients-and-visitors/patient-resources/covid19-resources": 2,
        }
    }
else:
    sites = {
        FROM_EMAIL: {
            "http://www.ScottLarsen.com": 3,
        }
    }

ua = UserAgent()
header = {"User-Agent": str(ua.random)}


def downloadText(url):
    from urllib.request import Request

    req = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    htmlContent = requests.get(url, headers=header)
    return htmlContent.text


def saveText(text, filepath):
    with open(
        filepath,
        "w",
    ) as f:
        f.write(text)


def openFile(filepath):
    with open(
        filepath,
        "r",
    ) as f:
        return f.read()
        return f.readlines()


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
        if detectGibberish(longestString) == False:
            matchingStrings.append(longestString)
            t1 = "^".join(t1.split(longestString))
            t2 = "^".join(t2.split(longestString))
        else:
            t1 = "".join(t1.split(longestString))
            t2 = "".join(t2.split(longestString))
    return t1, t2, matchingStrings


def detectGibberish(str):
    if len(str) < 3:
        return True
    elif len(str) > 13 and " " not in str.strip():
        return True
    elif (
        " " not in str.strip()
        and sum([1 for char in str[1:] if char.isupper()]) > len(str) / 8
    ):
        return True
    return False


def main():
    for email in sites.keys():
        body = []
        for url in sites[email].keys():
            filepath = f"/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/checkWebsiteForUpdates/{sites[email][url]}.txt"
            if not path.exists(filepath):
                print(f"\nNo existing record for {url}, downloading now")
                saveText(downloadText(url), filepath)
            else:
                if not TESTING:
                    oldText = openFile(filepath)
                else:
                    tempFilepath = f"{filepath[:-4]}Archive.txt"
                    oldText = openFile(tempFilepath)
                saveText(downloadText(url), filepath)
                newText = openFile(filepath)
                diffT1, diffT2, matchingStrings = diff(newText, oldText)
                diffT1 = [
                    x
                    for x in diffT1.split("^")
                    if len(x.strip()) > 1 and not detectGibberish(x)
                ]
                percentChange = (
                    len("".join(diffT1)) / len("".join(matchingStrings))
                ) * 100
                if percentChange > CHANGE_THRESHOLD:
                    body.append(f"\n{int(percentChange)}% change on {url}.")
                    for d in diffT1:
                        if len(d.strip()) > 1 and not detectGibberish(d):
                            body.append(d.strip())

        if len(body) > 0:
            print("Queueing e-mail")
            sendEMail("\n".join(body), email)


if __name__ == "__main__":
    main()