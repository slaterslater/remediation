# Automate repetitious tasks in HTML remediation
import codecs
import re

filename = "source.html"

def source():
  global filename
  filename = input("Enter source\n (filename.ext): ")
  print("source file changed to" + filename)

def remediate(fixlist):
  try:
    with codecs.open(filename, "r+", "utf-8") as src:
      markup = src.read()
      for old_tags, new_tags in fixlist.items():
        markup = re.sub(old_tags, new_tags, markup)
      src.seek(0)
      src.write(markup)
      print("Depreciated tags removed or updated")
  except:
    print("something went wrong")   

def tags():
  fixlist = {
    "</?u>": "",
    "<b>": "<strong>",
    "</b>": "</strong>",
    "<i>": "<em>",
    "</i>": "</em>"
  }
  remediate(fixlist)