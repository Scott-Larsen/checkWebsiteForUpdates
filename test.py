# # from collections import defaultdict

# def pullFromDict(entry):
#     if entry in d.keys():
#         ret = d[entry].pop()
#         if len(d[entry] == 0):
#                d.delete(entry)
#         return ret
#     return False


# class Solution:
#     def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#         if len(adjacentPairs) <= 1:
#             return adjacentPairs[0]
#         else:
#             res = adjacentPairs.pop()
#             start, end = res[0], res[1]
#             revStart = []
#             d = {}
#             for pair in adjacentPairs:
#                 if pair[0] not in d.keys():
#                     d[pair[0]] = [pair[1]]
#                 else:
#                     d[pair[0]].append(pair[1])

#             while d:
#                 newStart = pullFromDict(start)
#                 if newStart not False:
#                     revStart.append(newStart)
#                     start = revStart[-1]
#                 newEnd = pullFromDict(end)
#                 if newEnd not False:
#                     res.append(newEnd)
#                     end = res[-1]
#             return revStart[::-1] + res


#         if len(adjacentPairs) <= 1:
#             return adjacentPairs[0]
#         else:
#             res = adjacentPairs.pop()
#             start, end = res[0], res[1]
#             while adjacentPairs:
#                 for i in range(len(adjacentPairs) - 1, -1, -1):
#                     if start in adjacentPairs[i]:
#                         new = adjacentPairs.pop(i)
#                         new.remove(start)
#                         start = new[0]
#                         res = [start] + res
#                     elif end in adjacentPairs[i]:
#                         new = adjacentPairs.pop(i)
#                         new.remove(end)
#                         end = new[0]
#                         res.append(end)
#             return res


# if len(adjacentPairs) <= 1:
#     return adjacentPairs
# else:
#     d = defaultdict(list)
#     n = defaultdict(int)
#     for pair in adjacentPairs:
#         d[pair[0]].append(pair)
#         n[pair[0]] += 1
#         d[pair[1]].append(pair)
#         n[pair[1]] += 1
#     smallestKey = [False, False]
#     for key in n.keys():
#         if n[key] < smallestKey[1] or smallestKey[0] == False:
#             smallestKey = [key, n[key]]
#     res = d[smallestKey[0]].pop()
#     notSmallestKey = res[:]
#     notSmallestKey.remove(smallestKey[0])
#     d[notSmallestKey[0]].remove(res)
#     if smallestKey[0] != res[0]:
#         res = [res[1], res[0]]
#     while d:
#         next = d[res[-1]].pop()[:]
#         if d[res[-1]] == []:
#             del d[res[-1]]
#         inverseNext = next[::-1]
#         next.remove(res[-1])
#         d[next[0]].remove(inverseNext[::-1])
#         if d[next[0]] == []:
#             del d[next[0]]
#         res.append(next[0])
#     return res
#
#
#
#
#
#
#
# i = 3
# d = i
# i = 4
# print(d)
# print(divmod(10, 10))

# import random
# import math

# content = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Phasellus sollicitudin condimentum libero,
# sit amet ultrices lacus faucibus nec.
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Cum sociis natoque penatibus et magnis dis parturient montes,
# nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
# venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
# Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
# Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
# Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
# In hac habitasse platea dictumst. Morbi et leo enim.
# Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
# Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


# def fuzzit(content):
#     # Write a random fuzzer for a simulated text viewer application
#     bContent = content.encode()
#     print(bContent)


# print(fuzzit(content))


# def is_luhn_valid(n):
#     ###Your code here.
#     n = str(n)
#     if len(n) % 2 == 0:
#         l = "even"
#     else:
#         l = "odd"
#     res = 0
#     for i in range(len(n)):
#         if l == "even":
#             if i % 2 == 1:
#                 if 2 * int(n[i]) > 9:
#                     res += 2 * int(n[i]) - 9
#                 else:
#                     res += 2 * int(n[i])
#             else:
#                 res += int(n[i])
#         else:
#             if i % 2 == 1:
#                 if 2 * int(n[i]) > 9:
#                     res += 2 * int(n[i]) - 9
#                 else:
#                     res += 2 * int(n[i])
#             else:
#                 res += int(n[i])
#     if res % 10 == 0:
#         return True
#     return False


# print(is_luhn_valid(125))

# import math

# # for i in range(3, 39):
# #     print(i, math.sqrt(i), int(math.sqrt(i)))


# def isPrime(number):
#     if number == 2:
#         return True
#     if number <= 1 or (number % 2) == 0:
#         return False
#     for check in range(3, int(math.sqrt(number)) + 1):
#         print(number % check)  # if (number % check) == 0:
#         #     return False
#     return True


# for i in range(1, 34, 2):
#     print(i, isPrime(i))

# for check in range(3, int(math.sqrt(number))):
#     print(math.sqrt(num), int(math.sqrt(num)))

# def solution(n):
#     #     current = 1
#     #     perfect = []
#     #     while n > current:
#     #         perfect.append(current)
#     #         n -= current
#     #         current += 1
#     #     current += n
#     #     print(perfect)

#     # print(solution(10))

#     if n <= 4:
#         return 1
#     else:
#         solutions = []
#         potentials = []
#         halfRange = n / 2
#         if isinstance(halfRange, float):
#             halfRange = int(halfRange + 0.5)
#         for i in range(1, halfRange):
#             potentials.append([i])
#         while potentials:
#             current = potentials.pop()
#             for j in range(current[-1] + 1, n - sum(current) + 1):
#                 potential = current + [j]
#                 if sum(potential) == n:
#                     solutions.append(potential)
#                     print(potential)
#                 else:
#                     potentials.append(potential)
#         return len(solutions)


# print(solution(15))
# # for x in range(4, 201):
# #     print(solution(x))


# # CORRECT SPECIFICATION:
# #
# # the Queue class provides a fized-size FIFO queue of integers
# #
# # the constructor takes a single parameter: an integer >0 that
# # is the maximum number of elements the queue can hold
# #
# # empty() returns True iff the queue holds no elements
# #
# # full() returns True iff the queue cannot hold any more elements
# #
# # enqueue(i) attempts to put the integer i into the queue; it returns
# # True if successful and False if the queue is full
# #
# # dequeue() removes an integer from the queue and returns it,
# # or else returns None if the queue is empty

# import array

# class Queue:
#     def __init__(self,size_max):
#         assert size_max > 0
#         self.max = size_max
#         self.head = 0
#         self.tail = 0
#         self.size = 0
#         self.data = array.array('i', range(size_max))

#     def empty(self):
#         return self.size == 0

#     def full(self):
#         return self.size == self.max

#     def enqueue(self,x):
#         if self.size == self.max:
#             return False
#         self.data[self.tail] = x
#         self.size += 1
#         self.tail += 1
#         if self.tail == self.max:
#             self.tail = 0
#         return True

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         x = self.data[self.head]
#         self.size -= 1
#         self.head += 1
#         if self.head == self.max:
#             self.head = 0
#         return x


# def test1():
#     q = Queue(3)
#     res = q.empty()
#     if not res:
#         print "test1 NOT OK"
#         return
#     res = q.enqueue(10)
#     if not res:
#         print "test1 NOT OK"
#         return
#     res = q.enqueue(11)
#     if not res:
#         print "test1 NOT OK"
#         return
#     x = q.dequeue()
#     if x != 10:
#         print "test1 NOT OK"
#         return
#     x = q.dequeue()
#     if x != 11:
#         print "test1 NOT OK"
#         return
#     res = q.empty()
#     if not res:
#         print "test1 NOT OK"
#         return
#     print "test1 OK"

# def test2():
#     q = Queue(1)
#     res = q.enqueue(2)
#     if q.enqueue(5):
#         print("test2 not OK")
#     print("test2 OK")

# def test3():
#     q = Queue(2)
#     res = q.enqueue(1)
#     res = q.enqueue(2)
#     res = q.enqueue(3)
#     if res:
#         print("test3 not OK")
#     prin("test3 OK")


# test1()
# test2()
# test3()


# toSolve = [1]
# for j in range(len(toSolve) - 1, -1, -1):
# print(j)


# # s = "abba"
# # print(s.split())

# # endPosition = [18, 20, 25, 29, 41, 45, 50, 52]
# # moves = []
# # for x in endPosition:
# #     moves.append(x - 35)
# # print(moves)

# # [-17, -15, -10, -6, 6, 10, 15, 17]

# #     -17     -15
# # -10             -6
# #         0
# # 6               10
# #     15      17


# # import requests
# # import time
# # import smtplib
# # import hashlib
# # from fake_useragent import UserAgent
# # from os import path
# # from urllib.request import urlopen
# # from time import sleep

# # ua = UserAgent()
# # header = {"User-Agent": str(ua.random)}

# # # url = "http://scottlarsen.com"
# # # url = "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Vaccine.aspx"
# # # url = "https://www.doylestownhealth.org/about/news/health-news-and-blog/information-on-coronavirus-covid-19"
# # # filepath = "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/checkWebsiteForUpdates/test.html"

# # # htmlContent = requests.get(url, headers=header)
# # # text = "".join(htmlContent.text.split())

# # # sleep(10)

# # # newHtmlContent = requests.get(url, headers=header)
# # # textFromFile = "".join(newHtmlContent.text.split())

# # # with open(
# # #     filepath,
# # #     "w",
# # # ) as f:
# # #     f.writelines(text)

# # # with open(
# # #     filepath,
# # #     "r",
# # # ) as f:
# # #     textFromFile = f.read()  # .splitlines()

# # # if text == textFromFile:
# # #     print("Matching!")
# # # else:
# # #     print("Mismatch!")
# # #     print(text, textFromFile)

# # # print(text)  # , textFromFile)

# # # # from difflib import Differ
# # # # import difflib

# # # # from bs4 import BeautifulSoup

# # # sites = {"scott@scottlarsen.com": {"http://scottlarsen.com": 3}}
# # sites = {
# #     "scott@scottlarsen.com": {
# #         "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Vaccine.aspx": 1
# #     }
# # }
# # #         ,
# # #         "https://www.doylestownhealth.org/patients-and-visitors/patient-resources/covid19-resources": 2,
# # #     }
# # # }

# # ua = UserAgent()
# # header = {"User-Agent": str(ua.random)}


# # # def stripText(text):
# # #     # return hashlib.hash256(text.encode("utf-8")).hexdigest()
# # #     interval = len(text) // 100
# # #     res = []
# # #     for i in range(0, len(text), interval):
# # #         # print(text[i])
# # #         if text[i].isalpha():  # not in ["\n", "\r", " "]:
# # #             res.append(text[i])
# # #     # print(res)
# # #     return "".join(res)


# # def stripText(text):
# #     return "".join(text.strip())


# # def downloadText(url):
# #     # from urllib.request import Request, urlopen

# #     # req = Request(
# #     #     "http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1",
# #     #     headers={"User-Agent": "Mozilla/5.0"},
# #     # )
# #     # response = urlopen(req).read()

# #     # response = urlopen(url).read()
# #     # print(response)
# #     # return response
# #     htmlContent = requests.get(url, headers=header)
# #     return htmlContent.text


# # def saveText(text, filepath):
# #     # text = stripText(text)
# #     print(text[0])
# #     with open(
# #         filepath,
# #         "w",
# #     ) as f:
# #         f.writelines(text)


# # def compareOldAndNew(url, filepath):
# #     with open(
# #         filepath,
# #         "r",
# #     ) as f:
# #         hashFromFile = f.read().splitlines()

# #     # htmlContent = requests.get(url, headers=header)
# #     currentSHA = stripText(downloadText(url))
# #     hashFromFile = stripText(hashFromFile[0])
# #     if currentSHA != hashFromFile:
# #         print("Mismatch\n")
# #         print(hashFromFile[:200])
# #         print("\n\n\n")
# #         print(currentSHA[:500])
# #     else:
# #         print("No change")
# #         # print(currentSHA, hashFromFile[0])


# # def main():
# #     for email in sites.keys():
# #         for url in sites[email].keys():
# #             # print(downloadText(url))
# #             filepath = f"/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/checkWebsiteForUpdates/{sites[email][url]}.html"
# #             if not path.exists(filepath):
# #                 print(f"No existing record for {url}, downloading now")
# #                 saveText(downloadText(url), filepath)
# #             else:
# #                 compareOldAndNew(url, filepath)


# # if __name__ == "__main__":
# #     main()
