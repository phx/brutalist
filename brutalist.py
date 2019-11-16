#!/usr/bin/env python3
##############################################################################
#    Copyright (C) 2019  phx <https://github.com/phx>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
##############################################################################

import sys, re

def show_help():
    print()
    print("Usage: brutalist <[password] | -p [password] | -i [input file]> <[extended options]>\n")
    print("Options:")
    print("       [no params]                             takes input from stdin.")
    print("       [string]                                first argument is used as password.")
    print("       -p | --password                         second argument is used as password.")
    print("       -i | -f | --file [input file]           file is used as input.\n")
    print("Extended Options:")
    print("       -c | --limit-special | --limit-chars    limits special characters to '!@#$%*-+_'")
    print("       -n | --limit-numbers                    only includes common 1 and 2 digit suffixes + special")
    print("       -l | --limit                            limits both 3 digit numbers and special characters")
    print("            --leet                             includes all leet speak combinations (will increase size and time)")
    print()
    sys.exit()

if '--leet' in sys.argv:
    CHARACTERS = {
            r'[Aa]': ['A', 'a', '4', '@'],
            r'[Bb]': ['B', 'b', '3', '13'],
            r'[Cc]': ['C', 'c', '('],
            r'[Dd]': ['D', 'd', '[)'],
            r'[Ee]': ['E', 'e', '3'],
            r'[Ff]': ['F', 'f', '|='],
            r'[Gg]': ['G', 'g', '6'],
            r'[Hh]': ['H', 'h', '|-|'],
            r'[Ii]': ['I', 'i', '1', '|'],
            r'[Jj]': ['J', 'j', '.]'],
            r'[Kk]': ['K', 'k', '|<'],
            r'[Ll]': ['L', 'l', '1', '|'],
            r'[Mm]': ['M', 'm', '|Y|'],
            r'[Nn]': ['N', 'n', '/V'],
            r'[Oo]': ['O', 'o', '0'],
            r'[Pp]': ['P', 'p', '|>'],
            r'[Qq]': ['Q', 'q', '0,'],
            r'[Rr]': ['R', 'r', '|2'],
            r'[Ss]': ['S', 's', '5', '$'],
            r'[Tt]': ['T', 't', '7', '+'],
            r'[Uu]': ['U', 'u', '[_]'],
            r'[Vv]': ['V', 'v'],
            r'[Ww]': ['W', 'w'],
            r'[Xx]': ['X', 'x', '}-{'],
            r'[Yy]': ['Y', 'y', '`/'],
            r'[Zz]': ['Z', 'z', '2']
        }
else:
    CHARACTERS = {
            r'[Aa]': ['A', 'a', '4', '@'],
            r'[Bb]': ['B', 'b', '3'],
            r'[Cc]': ['C', 'c'],
            r'[Dd]': ['D', 'd'],
            r'[Ee]': ['E', 'e', '3'],
            r'[Ff]': ['F', 'f'],
            r'[Gg]': ['G', 'g', '6'],
            r'[Hh]': ['H', 'h'],
            r'[Ii]': ['I', 'i', '1'],
            r'[Jj]': ['J', 'j'],
            r'[Kk]': ['K', 'k'],
            r'[Ll]': ['L', 'l', '1'],
            r'[Mm]': ['M', 'm'],
            r'[Nn]': ['N', 'n'],
            r'[Oo]': ['O', 'o', '0'],
            r'[Pp]': ['P', 'p'],
            r'[Qq]': ['Q', 'q'],
            r'[Rr]': ['R', 'r'],
            r'[Ss]': ['S', 's', '5', '$'],
            r'[Tt]': ['T', 't'],
            r'[Uu]': ['U', 'u'],
            r'[Vv]': ['V', 'v'],
            r'[Ww]': ['W', 'w'],
            r'[Xx]': ['X', 'x'],
            r'[Yy]': ['Y', 'y'],
            r'[Zz]': ['Z', 'z', '2']
        }


def resubs(spass):
    spass = spass.strip()
    for key in CHARACTERS:
        for x in CHARACTERS[key]:
            tmp = re.sub(key, x, spass)
            subappend(tmp)

def subappend(tmp):
    tmp = tmp.strip()
    if tmp not in subs:
        subs.append(tmp)
        resubs(tmp)

def get_subs(ch, char):
    spass = before + char + after
    spass = spass.strip()
    for key in CHARACTERS:
        for x in CHARACTERS[key]:
            subs.append(re.sub(key, x, spass))

    lower_char = char.lower()
    if '--leet' in sys.argv:
        for sc in range(len(spass)):
            b = spass[:sc]
            a = spass[sc+1:]
            if ch == sc:
                if lower_char == 'a':
                    subs.append(b + '4' + a)
                    subs.append(b + '@' + a)
                    resubs(b + '4' + a)
                    resubs(b + '@' + a)
                if lower_char == 'b':
                    subs.append(b + '3' + a)
                    subs.append(b + '13' + a)
                    resubs(b + '3' + a)
                    resubs(b + '13' + a)
                if lower_char == 'c':
                    subs.append(b + '(' + a)
                    resubs(b + '(' + a)
                if lower_char == 'd':
                    subs.append(b + '[)' + a)
                    resubs(b + '[)' + a)
                if lower_char == 'e':
                    subs.append(b + '3' + a)
                    resubs(b + '3' + a)
                if lower_char == 'f':
                    subs.append(b + '|=' + a)
                    resubs(b + '|=' + a)
                if lower_char == 'g':
                    subs.append(b + '6' + a)
                    resubs(b + '6' + a)
                if lower_char == 'h':
                    subs.append(b + '|-|' + a)
                    resubs(b + '|-|' + a)
                if lower_char == 'i':
                    subs.append(b + '|' + a)
                    subs.append(b + '1' + a)
                    resubs(b + '|' + a)
                    resubs(b + '1' + a)
                if lower_char == 'l':
                    subs.append(b + '1' + a)
                    resubs(b + '1' + a)
                    subs.append(b + '|' + a)
                    resubs(b + '|' + a)
                if lower_char == 'm':
                    subs.append(b + '|Y|' + a)
                    resubs(b + '|Y|' + a)
                if lower_char == 'n':
                    subs.append(b + '/V' + a)
                    resubs(b + '/V' + a)
                if lower_char == 'o':
                    subs.append(b + '0' + a)
                    resubs(b + '0' + a)
                if lower_char == 'p':
                    subs.append(b + '|>' + a)
                    resubs(b + '|>' + a)
                if lower_char == 'q':
                    subs.append(b + '0,' + a)
                    resubs(b + '0,' + a)
                if lower_char == 'r':
                    subs.append(b + '|2' + a)
                    resubs(b + '|2' + a)
                if lower_char == 's':
                    subs.append(b + '5' + a)
                    subs.append(b + '$' + a)
                    resubs(b + '5' + a)
                    resubs(b + '$' + a)
                if lower_char == 't':
                    subs.append(b + '7' + a)
                    subs.append(b + '+' + a)
                    resubs(b + '7' + a)
                    resubs(b + '+' + a)
                if lower_char == 'u':
                    subs.append(b + '[_]' + a)
                    resubs(b + '[_]' + a)
                if lower_char == 'x':
                    subs.append(b + '}-{' + a)
                    resubs(b + '}-{' + a)
                if lower_char == 'y':
                    subs.append(b + '`/' + a)
                    resubs(b + '`/' + a)
                if lower_char == 'z':
                    subs.append(b + '2' + a)
                    resubs(b + '2' + a)
    else:
        for sc in range(len(spass)):
            b = spass[:sc]
            a = spass[sc+1:]
            if ch == sc:
                if lower_char == 'a':
                    subs.append(b + '@' + a)
                    resubs(b + '@' + a)
                if lower_char == 'b':
                    subs.append(b + '3' + a)
                    resubs(b + '3' + a)
                if lower_char == 'e':
                    subs.append(b + '3' + a)
                    resubs(b + '3' + a)
                if lower_char == 'g':
                    subs.append(b + '6' + a)
                    resubs(b + '6' + a)
                if lower_char == 'i':
                    subs.append(b + '1' + a)
                    resubs(b + '1' + a)
                if lower_char == 'l':
                    subs.append(b + '1' + a)
                    resubs(b + '1' + a)
                if lower_char == 'o':
                    subs.append(b + '0' + a)
                    resubs(b + '0' + a)
                if lower_char == 'q':
                    subs.append(b + '0,' + a)
                    resubs(b + '0,' + a)
                if lower_char == 's':
                    subs.append(b + '5' + a)
                    subs.append(b + '$' + a)
                    resubs(b + '5' + a)
                    resubs(b + '$' + a)
                if lower_char == 'z':
                    subs.append(b + '2' + a)
                    resubs(b + '2' + a)

if __name__ == '__main__':

    for help in ['help', '-help', '--help', '-h']:
        if help in sys.argv:
            show_help()

    password_list = []

    # If only 1 argument that doesn't match options, use argument as password:
    if len(sys.argv) == 2:
        for opt in ['-p', '--password', '-i', '--input', '-f', '--file', '-c', '--limit-special', '--limit-chars', '-n', '--limit-numbers', '-l', '--limit', '--leet']:
            if opt in sys.argv:
                flag = True
        if flag != True:
            password_list.append(sys.argv[1].strip())
    elif len(sys.argv) >= 3:
        # Check for -p|--password argument:
        for param in ['-p', '--password']:
            if param == sys.argv[1]:
                password_list.append(sys.argv[2].strip())
        # Check for file input:
        for param in ['-i', '-f', '--file']:
            if sys.argv[1] == '-i':
                password_file = sys.argv[2]
                with open(password_file, r) as fp:
                    for line in fp:
                        password_list.append(line.strip())
    else:
        try:
            passwords = [x for x in sys.stdin.readlines()]
            for password in passwords:
                password_list.append(password.strip())
        except:
            show_help()

    # Character limits:
    special_characters = '!@#$%^&*+-=_.;~()[]'
    for limit in ['l', '-c', '--limit-special', '--limit-chars', '--limit']:
        if limit in sys.argv:
            special_characters='!@#$%*-+_'

    passwords = set(password_list)

    subs = []

    for password in passwords:
        resubs(password)

        # switch to upper
        up = password.upper()
        resubs(up)
        for ch, _ in enumerate(up):
            before = up[:ch]
            char = up[ch]
            after = up[ch+1:]
            uchar = up[ch].replace(char, char.lower())
            subs.append(before + uchar + after)
            subs.append(before.upper() + uchar + after.upper())
            subs.append(before.lower() + uchar + after.lower())
            subs.append(before.upper() + uchar + after.lower())
            subs.append(before.lower() + uchar + after.upper())
            resubs(before + uchar + after)
            resubs(before.upper() + uchar + after.upper())
            resubs(before.lower() + uchar + after.lower())
            resubs(before.upper() + uchar + after.lower())
            resubs(before.lower() + uchar + after.upper())
            get_subs(ch, uchar)

        # switch to lower
        lp = password.lower()
        resubs(lp)
        for ch, _ in enumerate(lp):
            before = lp[:ch]
            char = lp[ch]
            after = lp[ch+1:]
            lchar = lp[ch].replace(char, char.upper())
            subs.append(before + lchar + after)
            subs.append(before.upper() + lchar + after.upper())
            subs.append(before.lower() + lchar + after.lower())
            subs.append(before.upper() + lchar + after.lower())
            subs.append(before.lower() + lchar + after.upper())
            resubs(before + lchar + after)
            resubs(before.upper() + lchar + after.upper())
            resubs(before.lower() + lchar + after.lower())
            resubs(before.upper() + lchar + after.lower())
            resubs(before.lower() + lchar + after.upper())
            get_subs(ch, lchar)

        unique_subs = set(subs)

        number_suffixes = []
        numbers = '0123456789'

        for ch, _ in enumerate(numbers):
            if 9 > ch >= 0:
                number_suffixes.append(numbers[ch-1:ch+2])
        number_suffixes.remove('')

        combos = []
        for sub in unique_subs:
            combos.append(sub)
        for sub in unique_subs:
            for num in numbers:
                combos.append(sub + num)
                combos.append(sub + num + num)
        for sub in unique_subs:
            for suf in number_suffixes:
                combos.append(sub + suf)
                for c in special_characters:
                    combos.append(sub + suf + c)
        for sub in unique_subs:
            for c in special_characters:
                combos.append(sub + c)
                for num in numbers:
                    combos.append(sub + num + c)
                    combos.append(sub + num + num + c)

        for opt in ['-n', '--limit-numbers', '-l', '--limit']:
            if opt in sys.argv:
                limit = True
        if limit != True:
            three_digit_suffixes = ["{0:03}".format(i) for i in range(1000)]
            for sub in unique_subs:
                for suf3 in three_digit_suffixes:
                    combos.append(sub + suf3)
                    for c in special_characters:
                        combos.append(sub + suf3 + c)

        unique_combos = list(set(combos))
        for password in unique_combos:
            print(password)
