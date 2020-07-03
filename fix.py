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
  remediate({'\\s' + attribute + '="[^"]*"': ''}, attribute + " attribute removed")

# finds blank lines
def format():
  fixes = {
    '\n\\s+|(\n){2,}': '\n',
    '\n(?=\\w)': '',
    '(<br />\n){2,}': '',
    '\n(\\s+)?(?=&nbsp;)': '',
    '\n(&nbsp)+' : '',
    '&gt;\\s?(?=</)' : '',
    '(?<=&nbsp;)\n' : '',
    '(?<=\\w)\n' : ''
  }
  remediate(fixes, "removed blank lines and extraneous breaks")

# removes empty headings
def headings():
  remediate({'<h\\d[^>]*>((&nbsp;)+)?</h\\d>' : ''}, "removed empty headings")

# removes redundant span elements
def spans():
  remediate({'</?span[^>]*>':''}, "removed all the span elements")

# make all images decorative
def images():
  with open(filename, "r+") as src:
    markup = src.read()
    images = re.findall('<img[^>]*>', markup)
    for img in images:
      new = re.sub('(\\salt|\\stitle)="[^"]*"', '', img)
      new = new.replace('<img', '<img role="presentation" alt=""')
      markup = markup.replace(img, new)
    src.seek(0)
    src.truncate(0)
    src.write(markup)
    print("images marked as decorative")

#removes repeating nbsp
def nbsp():
    remediate({'(&nbsp;\\s?)+' : '&nbsp;'}, "removed repetitive nbsp")

# removes elements with no text
def empty(elem):
  remediate({'<' + elem + '[^>]*>((&nbsp;)+)?</' + elem + '>' : ''}, "removed empty <" + elem + "> elements")

# adds a <br> into <h3>
def h3br():
  remediate({'<h3>' : '<h3><br>'}, "added <br> to each <h3>")

#removes all <br>
def br():
    remediate({'<br(\\s/)?>' : ''}, "removed all <br> elements")

# remove all attributes from table tag
def tables():
  remediate({'<table[^>]*>' : '<table>'}, "cleared table attributes")

# remove all table elements
def rmtables():
  table = {
    '</?(table|thead|tbody|tfoot|tr|th|td)[^>]*>' : ''
  }
  remediate(table, "removed table elements")

# removes empty table rows
def emptyrows():
  remediate({'<tr>(\n<td[^>]+>&nbsp;</td>)+\n</tr>\n' : ''}, "removed empty table rows")

# replaces <x> with <y>
def swap(x, y):
  remediate({'(?<=(<|/))' + x : y}, "replaced <" + x + "> with <" + y + ">")

def useless(elem):
  remediate({'</?' + elem + '[^>]*>':''}, "removed unecessary <" + elem + ">")

# creates new iframe with inline CSS
def iframes():
  with open(filename, "r+") as file:
    markup = file.read()
    iframes = re.findall('<iframe[^>]*>', markup)
    for iframe in iframes:
      height = re.findall('(?<=height=")\\d+', iframe)
      width = re.findall('(?<=width=")\\d+', iframe)
      src = re.findall('src="[^"]+"', iframe)
      new = '<iframe ' + src[0] + ' style="height: ' + height[0] + 'px; width: ' + width[0] + 'px;">'
      markup = markup.replace(iframe, new)
    file.seek(0)
    file.truncate(0)
    file.write(markup)
    print("iframes recreated")

# calls common
def basic():
  tags()
  headings()
  nbsp()
  h3br()
  empty("p")
  empty("div")
  format()

# function should findall and if exists, msgs and writes otherwise exits  