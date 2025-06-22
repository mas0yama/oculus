import splinter

# browser = splinter.Browser(headless= True)
#
# browser.visit('https://splinter.readthedocs.io')
# browser.driver.save_full_page_screenshot("/home/hajimurad/screenhot.png")

from src.core.core import Session

session = Session(None, "/home/hajimurad/Dev/oculus/inp", "/home/hajimurad/Dev/oculus/out")
session.run()