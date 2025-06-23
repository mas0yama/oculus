import splinter

from src.core.core import Session

session = Session(None, "ABSPATH", "ABSPATH")
session.config('ABSPATH', 1)


session.run()