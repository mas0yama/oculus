from oculus.core import Oculus

# parser = argparse.ArgumentParser(description="oculus - take a screenshot of urls")
# parser.add_argument('-i', '--input', type=str, default="", help="Absolute path to directory with input files")
# parser.add_argument('-o', '--output', type=str, default="", help='Absolute path to directory with output files')
# parser.add_argument('-ua', '--user-agent', default="", type=str, help="Absolute path to file with user-agents")
# parser.add_argument('-rpa', '--req-per-ua', default=5, type=int, help="Amount of requests per user-agent")
# parser.add_argument('-d', '--driver-name', default="", type=str, help='Custom drivername')
#
# args = parser.parse_args()
# print(args)
# session = Session(args.driver_name, args.input, args.output)
# session.config(args.user_agent, args.req_per_ua)
#
# session.run()


from oculus import utils

# dirbrute.parse_gobuster_dir_output("./gobusterout")

session = Oculus(input_dir=, output_dir=, wordlist_path=, base_url="https://example.com/")
session.config()
session.brute_dirs(5)
