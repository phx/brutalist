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
    print("Usage: brutalist <[password] | -i [input file]>\n")
    print("Options:\n")
    print("       [no params]        takes input from stdin.")
    print("       [string]           first argument is used as password.")
    print("       -i [input file]    file is used as input.\n")
    sys.exit()

def resubs(spass):
    spass = spass.strip()
    tmp = re.sub(r'[Aa]', '4', spass)
    subappend(tmp)
    tmp = re.sub(r'[Aa]', '@', spass)
    subappend(tmp)
    tmp = re.sub(r'[Bb]', '3', spass)
    subappend(tmp)
    tmp = re.sub(r'[Bb]', '13', spass)
    subappend(tmp)
    tmp = re.sub(r'[Cc]', '(', spass)
    subappend(tmp)
    tmp = re.sub(r'[Dd]', '[)', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ee]', '3', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ff]', '|=', spass)
    subappend(tmp)
    tmp = re.sub(r'[Gg]', '6', spass)
    subappend(tmp)
    tmp = re.sub(r'[Hh]', '|-|', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ii]', '1', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ii]', '|', spass)
    subappend(tmp)
    tmp = re.sub(r'[Jj]', '.]', spass)
    subappend(tmp)
    tmp = re.sub(r'[Kk]', '|<', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ll]', '1', spass)
    subappend(tmp)
    tmp = re.sub(r'[Mm]', '|Y|', spass)
    subappend(tmp)
    tmp = re.sub(r'[Nn]', '/V', spass)
    subappend(tmp)
    tmp = re.sub(r'[Oo]', '0', spass)
    subappend(tmp)
    tmp = re.sub(r'[Pp]', '|>', spass)
    subappend(tmp)
    tmp = re.sub(r'[Qq]', '0,', spass)
    subappend(tmp)
    tmp = re.sub(r'[Rr]', '|2', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ss]', '5', spass)
    subappend(tmp)
    tmp = re.sub(r'[Ss]', '$', spass)
    subappend(tmp)
    tmp = re.sub(r'[Tt]', '7', spass)
    subappend(tmp)
    tmp = re.sub(r'[Tt]', '+', spass)
    subappend(tmp)
    tmp = re.sub(r'[Uu]', '[_]', spass)
    subappend(tmp)
    tmp = re.sub(r'[Xx]', '}-{', spass)
    subappend(tmp)
    tmp = re.sub(r'[Yy]', '`/', spass)
    subappend(tmp)
    tmp = re.sub(r'[Zz]', '2', spass)
    subappend(tmp)

def subappend(tmp):
    tmp = tmp.strip()
    if tmp not in subs:
        subs.append(tmp)
        resubs(tmp)

def get_subs(ch, char):
    spass = before + char + after
    spass = spass.strip()
    subs.append(re.sub(r'[Aa]', '4', spass))
    subs.append(re.sub(r'[Aa]', '@', spass))
    subs.append(re.sub(r'[Bb]', '3', spass))
    subs.append(re.sub(r'[Bb]', '13', spass))
    subs.append(re.sub(r'[Cc]', '(', spass))
    subs.append(re.sub(r'[Dd]', '[)', spass))
    subs.append(re.sub(r'[Ee]', '3', spass))
    subs.append(re.sub(r'[Ff]', '|=', spass))
    subs.append(re.sub(r'[Gg]', '6', spass))
    subs.append(re.sub(r'[Hh]', '|-|', spass))
    subs.append(re.sub(r'[Ii]', '1', spass))
    subs.append(re.sub(r'[Ii]', '|', spass))
    subs.append(re.sub(r'[Jj]', '.]', spass))
    subs.append(re.sub(r'[Kk]', '|<', spass))
    subs.append(re.sub(r'[Ll]', '1', spass))
    subs.append(re.sub(r'[Mm]', '|Y|', spass))
    subs.append(re.sub(r'[Nn]', '/V', spass))
    subs.append(re.sub(r'[Oo]', '0', spass))
    subs.append(re.sub(r'[Pp]', '|>', spass))
    subs.append(re.sub(r'[Qq]', '0,', spass))
    subs.append(re.sub(r'[Rr]', '|2', spass))
    subs.append(re.sub(r'[Ss]', '5', spass))
    subs.append(re.sub(r'[Ss]', '$', spass))
    subs.append(re.sub(r'[Tt]', '7', spass))
    subs.append(re.sub(r'[Tt]', '+', spass))
    subs.append(re.sub(r'[Uu]', '[_]', spass))
    subs.append(re.sub(r'[Xx]', '}-{', spass))
    subs.append(re.sub(r'[Yy]', '`/', spass))
    subs.append(re.sub(r'[Zz]', '2', spass))
    c = char.lower()
    for sc in range(len(spass)):
        b = spass[:sc]
        a = spass[sc+1:]
        if ch == sc:
            if c == 'a':
                subs.append(b + '4' + a)
                subs.append(b + '@' + a)
            if c == 'b':
                subs.append(b + '3' + a)
                subs.append(b + '13' + a)
            if c == 'c':
                subs.append(b + '(' + a)
            if c == 'd':
                subs.append(b + '[)' + a)
            if c == 'e':
                subs.append(b + '3' + a)
            if c == 'f':
                subs.append(b + '|=' + a)
            if c == 'g':
                subs.append(b + '6' + a)
            if c == 'h':
                subs.append(b + '|-|' + a)
            if c == 'i':
                subs.append(b + '|' + a)
                subs.append(b + '1' + a)
            if c == 'l':
                subs.append(b + 'l' + a)
            if c == 'm':
                subs.append(b + '|Y|' + a)
            if c == 'n':
                subs.append(b + '/V' + a)
            if c == 'o':
                subs.append(b + '0' + a)
            if c == 'p':
                subs.append(b + '|>' + a)
            if c == 'q':
                subs.append(b + '0,' + a)
            if c == 'r':
                subs.append(b + '|2' + a)
            if c == 's':
                subs.append(b + '5' + a)
                subs.append(b + '$' + a)
            if c == 't':
                subs.append(b + '7' + a)
                subs.append(b + '+' + a)
            if c == 'u':
                subs.append(b + '[_]' + a)
            if c == 'x':
                subs.append(b + '}-{' + a)
            if c == 'y':
                subs.append(b + '`/' + a)
            if c == 'z':
                subs.append(b + '2' + a)


if __name__ == '__main__':

    password_list = []

    if 'help' in sys.argv:
        show_help()
    if '-help' in sys.argv:
        show_help()
    if '--help' in sys.argv:
        show_help()
    if '-h' in sys.argv:
        show_help()
    if len(sys.argv) == 1:
        try:
            passwords = [x for x in sys.stdin.readlines()]
            for password in passwords:
                password_list.append(password.strip())
        except:
            show_help
    elif len(sys.argv) == 2:
        try:
            password_list.append(sys.argv[1].strip())
            # password = sys.argv[1].strip()
        except:
            show_help
    elif len(sys.argv) == 3:
        try:
            password_file = sys.argv[3]
            with open(password_file, r) as fp:
                for line in fp:
                    password_list.append(line.strip())
        except:
            show_help
    
    passwords = set(password_list)

    subs = []

    for password in passwords:    
        resubs(password)
        
        # switch to upper
        up = password.upper()
        resubs(up)
        for ch in range(len(up)):
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
        for ch in range(len(lp)):
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
        special_characters = '!@#$%^&*+-_.;~()[]'

        for ch in range(len(numbers)):
            if 9 > ch >= 0:    
                number_suffixes.append(numbers[ch-1:ch+2])
        number_suffixes.remove('')

        for sub in unique_subs:
            print(sub)
        for sub in unique_subs:
            for num in numbers:
                print(sub + num)
                print(sub + num + num)
        for sub in unique_subs:
            for suf in number_suffixes:
                print(sub + suf)
                for c in special_characters:
                    print(sub + suf + c)
        for sub in unique_subs:
            for c in special_characters:
                print(sub + c)
                for num in numbers:
                    print(sub + num + c)
                    print(sub + num + num + c)

