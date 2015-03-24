#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Print beautiful JSON using Yayson

APACHE LICENSE 2.0
Copyright 2013 Sebastian Dahlgren

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import json
import colorama
import argparse

VERSION = '0.3.1'


def yayson(doc, compact=False, indent=2, sort=False):

    # Parse the JSON
    try:
        doc = json.loads(doc)
    except ValueError:
        sys.stderr.write('Invalid JSON\n')
        sys.exit(1)

    # Set compact / extensive mode
    if compact:
        separators = (',', ':')
    else:
        separators = (', ', ': ')

    dump = json.dumps(
        doc,
        indent=indent,
        sort_keys=sort,
        separators=separators)

    # Print the JSON
    for line in dump.split('\n'):
        try:
            key, value = line.split(':', 1)
            value = value.strip()

            # Handle values
            if value[0] == '{':
                value = colorama.Fore.YELLOW + value
            if value[0] == '[':
                value = colorama.Fore.YELLOW + value
            elif value[0] == '"':
                value = colorama.Fore.MAGENTA + value
            else:
                value = colorama.Fore.CYAN + value
            if value[len(value)-1] == ',':
                value = (
                    colorama.Fore.MAGENTA + value[:len(value)-1] +
                    colorama.Fore.YELLOW + ','
                )

            if compact:
                separator = ':'
            else:
                separator = ': '

            print (colorama.Fore.YELLOW + key + separator + value)
        except ValueError:
            print(colorama.Fore.YELLOW + line)

    print(colorama.Fore.RESET)


def main():
    """ Main function """
    parser = argparse.ArgumentParser(
        description='Yayson produces beautiful JSON')
    parser.add_argument(
        '-i', '--indent',
        type=int,
        default=2,
        help='Number of spaces to indent with (default: 2)')
    parser.add_argument(
        '-c', '--compact',
        action='store_true',
        help=(
            'Print JSON in compact mode, i.e. without '
            'spaces between keys and values'))
    parser.add_argument(
        '-s', '--sort',
        action='store_true',
        help='Turn on key sorting')
    parser.add_argument(
        '--version',
        action='store_true',
        help='Print version information')
    args = parser.parse_args()

    if args.version:
        print('Yayson {0}'.format(VERSION))
        sys.exit(0)

    # Initialize colorama
    colorama.init(autoreset=True)

    # Read the input
    doc = ''
    for line in sys.stdin.readlines():
        doc += line

    yayson(doc, compact=args.compact, indent=args.indent, sort=args.sort)


if __name__ == '__main__':
    main()
    sys.exit(0)