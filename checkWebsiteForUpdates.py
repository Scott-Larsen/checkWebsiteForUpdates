import requests
import time
import smtplib
import hashlib
from fake_useragent import UserAgent
from os import path
from urllib.request import urlopen

# from difflib import Differ
# import difflib

# from bs4 import BeautifulSoup

sites = {"scott@scottlarsen.com": {"http://scottlarsen.com": 3}}
#         "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Vaccine.aspx": 1
#     }
# }
#         ,
#         "https://www.doylestownhealth.org/patients-and-visitors/patient-resources/covid19-resources": 2,
#     }
# }

ua = UserAgent()
header = {"User-Agent": str(ua.random)}


def hashText(text):
    # return hashlib.hash256(text.encode("utf-8")).hexdigest()
    interval = len(text) // 100
    res = []
    for i in range(0, len(text), interval):
        # print(text[i])
        if text[i].isalpha():  # not in ["\n", "\r", " "]:
            res.append(text[i])
    # print(res)
    return "".join(res)


def downloadText(url):
    from urllib.request import Request, urlopen

    req = Request(
        "http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response = urlopen(req).read()

    # response = urlopen(url).read()
    print(response)
    return response
    # htmlContent = requests.get(url, headers=header)
    # return htmlContent.text


def saveText(text, filepath):
    with open(
        filepath,
        "w",
    ) as f:
        f.writelines(hashText(text))


def compareOldAndNew(url, filepath):
    with open(
        filepath,
        "r",
    ) as f:
        hashFromFile = f.read().splitlines()

    # htmlContent = requests.get(url, headers=header)
    currentSHA = hashText(downloadText(url))
    if currentSHA != hashFromFile[0].rstrip():
        print("Mismatch\n")
        print(hashFromFile[0])
        print(currentSHA)
    else:
        print("No change")
        print(currentSHA, hashFromFile[0])


def main():
    for email in sites.keys():
        for url in sites[email].keys():
            # print(downloadText(url))
            filepath = f"/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/checkWebsiteForUpdates/{sites[email][url]}.html"
            if not path.exists(filepath):
                print(f"No existing record for {url}, downloading now")
                saveText(downloadText(url), filepath)
            # else:
            #     compareOldAndNew(url, filepath)


if __name__ == "__main__":
    main()

    # print("".join(text))
    # text = f.read().rstrip("\n\r")
    # print("".join(text)[-1000:])
    # print(htmlContent.text.strip(" ").strip("\n").strip("\r")[-1000:])

    # if "".join(text) == htmlContent.text.rstrip("\n\r"):
    #     print("Yes!")
    # for line in text:
    #     print(line)
    # print("".join(zip(f.read().strip()[:1000], htmlContent.text.strip()[:1000])))
    # for line in htmlContent.text:
    #     print(line, "\n")
    # print(htmlContent.text)

    # for line in zip(
    #     f.read().strip().rstrip()[:1000], htmlContent.text.strip().rstrip()[:1000]
    # ):
    #     print(line)

    # print("".join(f.read().splitlines())[:1000], htmlContent.text.strip()[:1000])

    #         import difflib
    # from difflib_data import *
    # import difflib

    # d = difflib.Differ()
    # diff = d.compare(f.read()[:1000], htmlContent.text[:1000])
    # for line in diff:
    #     print(line)
    # print(diff)
    # # print("".join(diff))

    # # print(f.read().strip()[:1000])
    # # print(htmlContent.text.strip()[:1000])

    # if "".join(f.read().splitlines())[:1000] != htmlContent.text.strip()[:1000]:
    #     # if htmlContent.text.strip()[:1000] != f.read().strip()[:1000]:
    #     print("Changes!")
    # #     # sendEmail(url)
