import splinter

from src.core.core import Session

session = Session(None, "", "")
session.config('', 1)

session.run()