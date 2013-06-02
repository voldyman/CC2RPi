from collections import namedtuple

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
