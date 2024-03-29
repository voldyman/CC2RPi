from collections import namedtuple
'''
    BEGIN LICENSE

    Copyright (C) 2013 Inventrom <contactus@inventrom.com>
    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU Lesser General Public License version 3, as published
    by the Free Software Foundation.

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranties of
    MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
    PURPOSE.  See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program.  If not, see <http://www.gnu.org/licenses/>

    END LICENSE
'''


Command = namedtuple('Command', 'cmd sender receiver text')

def parse(line):
    '''
    commands structure: @<cmd> <sender> <to> :<text>
    '''

    first_split = line.split(':', 1)

    if not len(first_split) == 2:
        return None

    data = first_split[0].split()
    text = first_split[1]

    if not data[0].startswith('@'):
        return None

    if data[0] == '@MSG':
        if not len(data) == 3:
            return None
        data.append(text)
        return Command._make(data)
    else:
        return None
