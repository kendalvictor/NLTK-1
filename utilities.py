import re

def regex(name):
    tag = '<' + name + '>'
    close = '</' + name + '>'
    regex = '(' + tag + ')' + '(.*)(' + close + ')'
    return re.compile(regex, re.S|re.M)