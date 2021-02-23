t1 = "The Red Cross works to ensure that the blood and platelet donation process is as safe as possible for donors and patients in need. We need to start by confirming some information. RapidPass® may only be completed on the day of your donation. Please acknowledge that you are donating today:"
t2 = "The Red Cross works to ensure, that the blood and platelet process to donate is safe. as possible for donors and patients in needWe need to start by confirming some information. RapidPass may only be completed on the day of your donation. Please acknowledge that you are donating today"

MIN_LENGTH_MATCH = 7


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


# print(findLongestString(t1, t2))


def diff(t1, t2):
    matchingStrings = []
    while len(findLongestString(t1, t2)) > 0:
        longestString = findLongestString(t1, t2)
        matchingStrings.append(longestString)
        t1 = "^".join(t1.split(longestString))
        t2 = "^".join(t2.split(longestString))
        # print(t1)
    return t1, t2, matchingStrings


diffT1, diffT2, matchingStrings = diff(t1, t2)
# diffT1, diffT2 = diffT1.split("^"), diffT2.split("^")

# for i in range(len(max(diffT1, diffT2))):
#     if i < len(diffT1):
#         print(diffT1[i])
#     if i < len(diffT1) and i < len(diffT2):
#         print("...became...")
#     if i < len(diffT1):
#         print(diffT2[i])
print("\nNew in most recent edit....")
for d in diffT1.split("^"):
    if len(d.strip()) > 1:
        print(d.strip())
# for d in diffT2.split("^"):
#     print(d)


# print(matchingStrings)

# if findLongestString(t1, t2) == "":
#     return t1, t2
# else:
#     longestString = findLongestString(t1, t2)
#     matchingStrings.append(longestString)
#     t1 = "^".join(t1.split(longestString))
#     t2 = "^".join(t2.split(longestString))
#     return diff(t1, t2)


# def diff(t1, t2):
#     if len(t1) < MIN_LENGTH_MATCH:
#         commonText.append(t1)
#     else:
#         matchingString = ""
#         i, j = 0, MIN_LENGTH_MATCH
#         while i + j < len(t1):
#             # if len(matchingString) == 0
#             while t1[i : i + j] in t2 or t2[i : i + j] in t1:
#                 if t1[i : i + j] in t2:
#                     matchingString = t1[i : i + j]
#                 else:
#                     matchingString = t2[i : i + j]
#                 j += 1
#             if len(matchingString) > 0:
#                 commonText.append(matchingString)
#                 # differentText1 = t1[:i]
#                 # print(f"t2 = {t2}")
#                 # print(f"commonText = {commonText}")
#                 # print(len(t1.split(commonText[-1])))
#                 [differentText1, t1] = t1.split(matchingString)
#                 [differentText2, t2] = t2.split(matchingString)
#                 changedText.append([differentText1, differentText2])
#                 return diff(t1, t2)
#             i += 1


# diff(t1, t2)
# for cT in changedText:
#     if cT != ["", ""]:
#         print(cT[0], "...became...", cT[1])
# print(commonText)
# print(changedText)


# # text1 = """
# # <!DOCTYPE html>
# # <html lang="en-US">

# #   <head>
# #   <meta charset="utf-8">
# #   <meta http-equiv="X-UA-Compatible" content="IE=edge">
# #   <meta name="viewport" content="width=device-width, initial-scale=1">

# #   <!-- <title>About</title> -->
# #   <title>Scott Larsen - About</title>
# #   <meta name="description" content="Python Developer in LA">


# #   <link rel="stylesheet" href="http://ScottLarsen.com/assets/style.css">

# #   <link rel="canonical" href="http://ScottLarsen.com/">
# #   <link rel="alternate" type="application/rss+xml" title="Scott Larsen" href="http://ScottLarsen.com/feed.xml">

# #   <script async defer src="https://buttons.github.io/buttons.js"></script>

# # </head>

# #   <body class="About">

# #     <header class="border-bottom-thick px-2 clearfix">

# #   <nav class="topnav">
# #     <a class="align-left align-middle link-primary text-accent title" href="/">Scott Larsen</a><br class="brNoDisplay">
# #     <div class="topnav-right">
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/">About</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/projects">Projects</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="https://github.com/Scott-Larsen">GitHub</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="https://www.linkedin.com/in/ScottRLarsen">LinkedIn</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="/static/Scott-Larsen-Resume.pdf">Resume</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/blog">Blog</a>
# #     </div>
# #   </nav>
# # </header>


# #     <div>
# #       <article class="container mx-auto px-2 mt2 mb4">
# #   <header>
# #     <h1 class="h0 py-4 mt-3">About</h1>
# #   </header>
# #   <div class="col-4 sm-width-full border-top-thin">
# #   </div>
# #   <div class="prose mb-4 py-4">
# #     <p><img class="profilePhoto" alt="Scott Larsen Portrait" src="https://avatars1.githubusercontent.com/u/25908816?s=460&amp;v=4" /></p>

# # <p>Hi 👋, I’m Scott, a 🐍 Python Developer with HTML5, CSS3 and a bit of Javascript experience looking for my first developer role.  I would be happy to relocate, especially once the Covid pandemic has wound down.  I have experience in building websites with Flask, scraping data using Beautiful Soup and Selenium and querying GraphQL/ APIs.  Because of my background in photography I have dabbled in and would love to delve deeper into learning from and manipulating images and video with OpenCV and computer vision.</p>

# # <h3 id="contact-me">Contact me</h3>

# # <p><a href="/cdn-cgi/l/email-protection#4112222e35350112222e35350d203332242f6f222e2c"><span class="__cf_email__" data-cfemail="3764545843437764545843437b56454452591954585a">[email&#160;protected]</span></a></p>

# #   </div>
# # </article>

# #     </div>

# #     <div class="border-top-thin clearfix mt-2 mt-lg-4">
# #   <div class="container mx-auto px-2">
# #     <!-- <p class="col-8 sm-width-full left py-2 mb-0">This project is maintained by <a class="text-accent" href="https://github.com/Scott-Larsen">Scott-Larsen</a></p> -->
# #     <ul class="list-reset right clearfix sm-width-full py-2 mb-2 mb-lg-0">
# #       <li class="inline-block mr-1">
# #         <!-- <a href="https://twitter.com/share" class="twitter-share-button" data-hashtags="Scott Larsen">Tweet</a> <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
# #       </li>
# #       <li class="inline-block">
# #         <a class="github-button" href="https://github.com/Scott-Larsen/" data-icon="octicon-star" data-count-href="Scott-Larsen//stargazers" data-count-api="/repos/Scott-Larsen/#stargazers_count" data-count-aria-label="# stargazers on GitHub" aria-label="Star Scott-Larsen/ on GitHub">Star</a> -->
# #       </li>
# #     </ul>
# #   </div>
# # </div>


# #   <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body>

# # </html>

# # """


# # text2 = """
# # <!DOCTYPE html>
# # <html lang="en-US">

# #   <head>
# #   <meta charset="utf-8">
# #   <meta http-equiv="X-UA-Compatible" content="IE=edge">
# #   <meta name="viewport" content="width=device-width, initial-scale=1">

# #   <!-- <title>About</title> -->
# #   <title>Scott Larsen - About</title>
# #   <meta name="description" content="Python Developer in LA">


# #   <link rel="stylesheet" href="http://ScottLarsen.com/assets/style.css">

# #   <link rel="canonical" href="http://ScottLarsen.com/">
# #   <link rel="alternate" type="application/rss+xml" title="Scott Larsen" href="http://ScottLarsen.com/feed.xml">

# #   <script async defer src="https://buttons.github.io/buttons.js"></script>

# # </head>

# #   <body class="About">

# #     <header class="border-bottom-thick px-2 clearfix">

# #   <nav class="topnav">
# #     <a class="align-left align-middle link-primary text-accent title" href="/">Scott Larsen</a><br class="brNoDisplay">
# #     <div class="topnav-right">
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/">About</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/projects">Projects</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="https://github.com/Scott-Larsen">GitHub</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="https://www.linkedin.com/in/ScottRLarsen">LinkedIn</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" target="_blank" rel="noopener" href="/static/Scott-Larsen-Resume.pdf">Resume</a>
# #       <a class="align-middle link-primary mr-2 mr-lg-0 ml-lg-2" href="/blog">Blog</a>
# #     </div>
# #   </nav>
# # </header>


# #     <div>
# #       <article class="container mx-auto px-2 mt2 mb4">
# #   <header>
# #     <h1 class="h0 py-4 mt-3">About</h1>
# #   </header>
# #   <div class="col-4 sm-width-full border-top-thin">
# #   </div>
# #   <div class="prose mb-4 py-4">
# #     <p><img class="profilePhoto" alt="Scott Larsen Portrait" src="https://avatars1.githubusercontent.com/u/25908816?s=460&amp;v=4" /></p>

# # <p>Hi 👋, I’m Scott, a 🐍 Python Developer with HTML5, CSS3 and a bit of Javascript experience looking for my first developer role.  I would be happy to relocate, especially once the Covid pandemic has wound down.  I have experience in building websites with Flask, scraping data using Beautiful Soup and Selenium and querying GraphQL/ APIs.  Because of my background in photography I have dabbled in and would love to delve deeper into learning from and manipulating images and video with OpenCV and computer vision.</p>

# # <h3 id="contact-me">Contact me</h3>

# # <p><a href="/cdn-cgi/l/email-protection#2a7949455e5e6a7949455e5e664b58594f4404494547"><span class="__cf_email__" data-cfemail="81d2e2eef5f5c1d2e2eef5f5cde0f3f2e4efafe2eeec">[email&#160;protected]</span></a></p>

# #   </div>
# # </article>

# #     </div>

# #     <div class="border-top-thin clearfix mt-2 mt-lg-4">
# #   <div class="container mx-auto px-2">
# #     <!-- <p class="col-8 sm-width-full left py-2 mb-0">This project is maintained by <a class="text-accent" href="https://github.com/Scott-Larsen">Scott-Larsen</a></p> -->
# #     <ul class="list-reset right clearfix sm-width-full py-2 mb-2 mb-lg-0">
# #       <li class="inline-block mr-1">
# #         <!-- <a href="https://twitter.com/share" class="twitter-share-button" data-hashtags="Scott Larsen">Tweet</a> <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
# #       </li>
# #       <li class="inline-block">
# #         <a class="github-button" href="https://github.com/Scott-Larsen/" data-icon="octicon-star" data-count-href="Scott-Larsen//stargazers" data-count-api="/repos/Scott-Larsen/#stargazers_count" data-count-aria-label="# stargazers on GitHub" aria-label="Star Scott-Larsen/ on GitHub">Star</a> -->
# #       </li>
# #     </ul>
# #   </div>
# # </div>


# #   <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body>

# # </html>

# # """


# def extractLongestString(t1, t2):
#     noChange = False
#     while noChange == False:
#         noChange = True
#         longestSubstring = ""
#         i = 0
#         for i in range(len(t1) - 1):
#             if len(t1) > len(longestSubstring):
#                 j = 1
#                 while i + j < len(t1) + 1:
#                     if t1[i : i + j] in t2:
#                         if j > len(longestSubstring) and j > 3:  # and " " t1[i: i + j]:
#                             noChange = False
#                             longestSubstring = t1[i : i + j]
#                             # print(longestSubstring)
#                             li, lj = i, j
#                     j += 1
#         if noChange == False:
#             t1 = t1[:li] + t1[li + lj :]
#             # print(t1)
#         print(t1)
#         print(text2)
#     return t1


# def compareOldAndNew(newText, oldText):
#     if newText != oldText:
#         print("Mismatch\n")
#         nt = newText[:]
#         nt = extractLongestString(nt, oldText)
#         print(f"The text has changed {int(len(nt) / len(newText) * 100)}%.")
#     else:
#         print("No change")


# text1, text2 = openFile(filepath1), openFile(filepath2)
# compareOldAndNew(text1, text2)