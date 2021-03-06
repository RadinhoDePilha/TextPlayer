import argparse

parser =argparse.ArgumentParser(
    prog= 'text-displayer' ,
    description="Display a pdf word by word for your fast reading",
    )

parser.add_argument(
    'pdf_file',
    help='The path of the file that you want to read',
    )

parser.add_argument(
    '-p', '--page',
    required=False,
    action='store',
    help='The page that you wanna start',
    default=0,
    type= int,


)

parser.add_argument(
    '-cm', '--clipboard-mode',
    required=False,
    help='Use this to use the Clipboard Mode (EXPERIMENTAL)',
    dest='clipmode',
    default=0
)

args = parser.parse_args()

print(args)
