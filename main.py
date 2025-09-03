from oculus.core import Oculus
import argparse

print(r"""
                 ,,             
                 ||             
 /'\\  _-_ \\ \\ || \\ \\  _-_, 
|| || ||   || || || || || ||_.  
|| || ||   || || || || ||  ~ || 
\\,/  \\,/ \\/\\ \\ \\/\\ ,-_-  
""")

parser = argparse.ArgumentParser(description="oculus - take a screenshot of urls")
parser.add_argument('-i', '--input', type=str, default="", help="Absolute path to directory with input files")
parser.add_argument('-o', '--output', type=str, default="", help='Absolute path to directory with output files')
parser.add_argument('-ua', '--user-agent', default="", type=str, help="Absolute path to file with user-agents")
parser.add_argument('-rpa', '--req-per-ua', default=5, type=int, help="Amount of requests per user-agent")
parser.add_argument('-d', '--driver-name', default="", type=str, help='Custom drivername')
parser.add_argument('-gb', '--gobuster', default="", type=str, help='Parse gobuster output instead of wordlist')
parser.add_argument('-u', '--url', default="", type=str, help="Url to parse")
parser.add_argument('-wl', '--wordlist', default="", type=str, help="Wordlists")
args = parser.parse_args()
print(args)

# session = Oculus(args.driver_name, args.input, args.output)
# session.config(args.user_agent, args.req_per_ua)
#
# session.run()
#
# from oculus import utils
#
# # dirbrute.parse_gobuster_dir_output("./gobusterout")
#

if args.input == '' and args.gobuster == '':
    print("No input files nor gobuster")
    exit(0)

if args.input != '' and args.gobuster != '':
    print("Choose either --gobuster or --input")
    exit(0)

if args.output == '':
    print("Set --output")
    exit(0)

# if args.url == '':
#     print("Set --url")
#     exit(0)

if args.user_agent == '':
    args.user_agent = None

if args.gobuster == '':
    args.gobuster = None


# Base url нужен чтобы брутить
# Если есть input, то base url ебали в рот

# ёпта.
# в inputs сайты которые надо пробрутить
# бейз юрл тут к пизде рукав не пришей
# я плохой разраб
# удаляюсь
# input_dir + wordlists
# base_url + gobuster

oculus = Oculus(input_dir=args.input, output_dir=args.output, wordlist_path=args.wordlist, base_url=None,
                gobuster_path=args.gobuster)

oculus.config(args.user_agent, args.req_per_ua)

oculus.brute_dirs(5)
#oculus.run()
