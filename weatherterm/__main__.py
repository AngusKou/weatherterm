import sys
from argparse import ArgumentParser

from weatherterm.core import parser_loader
from weatherterm.core import ForecastType
from weatherterm.core import Unit
from weatherterm.core import SetUnitAction


def _validate_forecast_args(args):
    if args.forecast_option is None:
        err_msg = 'One of these arguments must be used:'
        print(f'{argparser.prog}:error:{err_msg}', file=sys.stderr)
        sys.exit()


# get all parsers available
parsers = parser_loader.load('./weatherterm/parsers')

argparser = ArgumentParser(prog='weatherterm', description='weather info')

required = argparser.add_argument_group('required arguments')
required.add_argument('-p', '--parser', choices=parsers.keys(), required=True, dest='parser',
                      help='specify which parser is going to be used')

unit_values = [name.title() for name, value in Unit.__members__.items()]

argparser.add_argument('-u', '--unit', choices=unit_values, action=SetUnitAction, required=False, dest='unit',
                       help='Specify the unit')
argparser.add_argument('-a', '--areacode', required=True, dest='area_code', help='code area to check')
argparser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
argparser.add_argument('-td', '--today', dest='forecast_option', action='store_const', const=ForecastType.TODAY,
                       help='show the weather forecast')

args = argparser.parse_args()
_validate_forecast_args(args)

cls = parsers[args.parser]

parser = cls()
results = parser.run(args)

for result in results:
    print(results)
