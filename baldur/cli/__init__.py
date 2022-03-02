import argparse
from functools import reduce
from baldur.cli.partners.control_mobile import commands as cmobile_commands

CLI_COMMANDS_FOR_PARTNER = [
    {
        "partner": "control_mobile", 
        "commands": cmobile_commands
    }
]

def get_commands():
    parser = argparse.ArgumentParser(description="Balur - A Python package for integration with api of control-mobile app")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    parser.add_argument("-E", "--environment", help="Choice environment", choices=["dev", "prod"], default="dev")

    parser.add_argument("-F", "--return-file", help="File to return the result", required=True)
    
    parser.add_argument("-P", "--partner", help="Choice partner to execute the command", choices=["control_mobile"], required=True)

    reduce(lambda r, a: a['commands'](r), filter(lambda f: f['partner'] in ['rv'], CLI_COMMANDS_FOR_PARTNER), parser)

    return parser.parse_args()