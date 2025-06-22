import splinter
from src.loggers import *
import time
import os


class Session:
    def __init__(self, drivername: str = None, input_dir="./inp", output_dir="./out", user_agent = None):

        self.browser = None
        self.outdir = None
        self.inpdir = None
        self.current_path = os.getcwd()

        log_debug("sessin init", f"{self.current_path}")
        if not os.path.isdir(input_dir):
            log_fatal("Session initialization", "Could not find input directory.")
            raise NotADirectoryError

        self.inpdir = input_dir

        if os.path.isdir(output_dir):
            _ = time.time()
            log_info("Session  initialization", f"Output dir exists. Creating new dir_{_}")
            os.mkdir(f"{output_dir}{_}")
            self.outdir = f"{output_dir}{_}"

        if not os.path.isdir(output_dir):
            log_info("Session initialization", f"Creating new output dir {output_dir}")
            os.mkdir(f"{output_dir}")
            self.outdir = f"{output_dir}"
            log_info("Setting outdir", f"{self.outdir}")

        if drivername is not None:
            self.browser = splinter.Browser(drivername)
        else:
            self.browser = splinter.Browser(headless=True)

    def run(self):
        for input_file in os.listdir(self.inpdir):
            urls = []
            log_info("Running %", f"Reading input file {input_file}")
            with open(f"{self.inpdir}/{input_file}", "rt") as f:
                urls = f.read().strip().split('\n')
            if not urls:
                log_info("Running %", f"File {input_file} is empty. Going next")
                break

            for url in urls:

                if url is None:
                    continue
                path = f"{self.outdir}/{url.split("://")[-1]}.png"
                log_info("Screenshotting %", f"Screenshoting {url}")
                self.browser.visit(url)
                log_info("Saving %", f"{path}")
                self.browser.driver.save_full_page_screenshot(path)
                #self.browser.quit()