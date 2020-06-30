# Asks user for a filename and then applies fixes
import codecs
import re

def depreciated():
  tags = {
    "</?u>": "",
    "<b>": "<strong>",
    "</b>": "</strong>",
    "<i>": "<em>",
    "</i>": "</em>"
  }
  try:
    filename = input("Enter source\n (filename.ext): ")
    with codecs.open(filename, "r+", "utf-8") as src:
      fixes = src.read()
      for old, new in tags.items():
        fixes = re.sub(old, new, fixes)
      src.seek(0)
      src.write(fixes)
      print("Depreciated tags removed or updated")
  except:
    print("something went wrong")  
  finally:
    src.close()