"""
Copyright 2025 mas0yama [oyamamas]

"""
import splinter
from oculus.loggers import *
import time
import os

import requests


class Oculus:
    def __init__(self, drivername: str = None, input_dir="./inp", output_dir="./out", wordlist_path=None, base_url = ""):

        self.browser = None
        self.outdir = None
        self.inpdir = None

        self.__current_path = os.getcwd()
        self.__user_agents = []
        self.__cur_ua = ""
        self.__requests_per_ua = 5
        self.__req_per_ua_counter = 0

        self.__browser_config = ()

        self.__explored = {}
        self.__wordlist_path = wordlist_path
        self.__base_url = base_url

        log_debug("sessin init", f"{self.__current_path}")
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

        if wordlist_path is not None:
            if not os.path.exists(wordlist_path):
                log_fatal("Session initiliazation", f"Could not find worldlist file {wordlist_path}")

    def config(self, ua_filename=None, requsts_per_ua=5, driver=None, **kwargs):
        # TODO EXTENSIONS
        _use_ua = False
        _custom_driver = False
        if ua_filename is not None:
            if not os.path.exists(ua_filename):
                log_fatal("Session config %", "Could not find user-agents file. Using default.")
                return

            with open(ua_filename, "rt") as f:
                self.__user_agents = f.read().split('\n')
            self.__cur_ua = self.__user_agents[0]

        self.__browser_config = splinter.Config(extensions=None, fullscreen=False, headless=True, incognito=False,
                                                user_agent=self.__cur_ua)
        self.__requests_per_ua = requsts_per_ua

        if driver is not None:
            self.browser = splinter.Browser(driver, config=self.__browser_config)
        else:
            self.browser = splinter.Browser(config=self.__browser_config)

        log_info("Session config %", f"Setting user-agents file {ua_filename}, requests per us  {requsts_per_ua}")

    def __screenshot(self, url):
        if self.__user_agents:
            if self.__req_per_ua_counter >= self.__requests_per_ua:
                self.__req_per_ua_counter = 0
                cur_ua_index = self.__user_agents.index(self.__cur_ua)
                self.__cur_ua = self.__user_agents[(cur_ua_index + 1) % len(self.__user_agents)]
        path = f"{self.outdir}/{url.split("://")[-1].split("/")[0]}.png"
        log_info("Screenshotting %", f"Screenshoting {url}")
        log_info("Screenshotin %",
                 f"Using User-Agent {self.__cur_ua} {self.__req_per_ua_counter + 1}/{self.__requests_per_ua}")
        self.browser.visit(url)
        log_info("Saving %", f"{path}")
        self.browser.driver.save_full_page_screenshot(path)
        self.__req_per_ua_counter += 1

    def brute_dirs(self, queue_len=10):
        wordlist_file = None
        cur_offset = 0
        path_queue = []
        try:
            wordlist_file = open(self.__wordlist_path, "rt")
        except Exception as e:
            log_fatal("Brute dirs", str(e))
            return

        wordlist_file.seek(0, os.SEEK_END)
        while cur_offset != wordlist_file.tell():
            path_queue = []

            # Collect queue to check path existence
            for _ in range(queue_len):
                wordlist_file.seek(0, os.SEEK_END)
                if cur_offset == wordlist_file.tell():
                    break

                wordlist_file.seek(cur_offset)
                path_queue.append(wordlist_file.readline())
                cur_offset = wordlist_file.tell()

            for path in path_queue:
                path = f"{self.__base_url}{path.rstrip()}"
                response = requests.get(path)
                if response.status_code != 404:
                    self.__explored[path] = response.status_code
                    log_info("Busting dirs %", f"Explored {response.status_code} {path}")
                    log_info("Busting dirs ", "Screenshoting...")
                    self.__screenshot(path)

            wordlist_file.seek(0, os.SEEK_END)

        pass

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
                self.__screenshot(url)
