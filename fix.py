# Functions to assist with repetitious tasks in HTML remediation
from bs4 import BeautifulSoup
import re

filename = "source.html"

# assigns new source file
def source():
  global filename
  filename = input("Enter source\n (filename.ext): ")
  print("source file changed to" + filename)

# recieves list of changes to make
# opens file and writes changes
def remediate(fixlist, msg):
  try:
    with open(filename, "r+") as src:
      markup = src.read()
      for find, replace in fixlist.items():
        markup = re.sub(find, replace, markup)
      src.seek(0)
      src.truncate(0)
      src.write(markup)
      print(msg)
  except:
    print("something went wrong")   

# updates tags
def tags():
  fix = {
    '</?u>': '',
    '<b>': '<strong>',
    '</b>': '</strong>',
    '<i>': '<em>',
    '</i>': '</em>'
  }
  remediate(fix, "<u> <b> <i> tags fixed")

# finds attribute and value
def attr(attribute):
  remediate({'\\s' + attribute + '="[^"]+"': ''}, attribute + " attribute removed")

# finds blank lines
def format():
  remediate({'\n\\s+|\n{2,}': '\n'}, "removed blank lines")



format()  