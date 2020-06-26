#!/usr/bin/env python

####
## progress bar ##
###


_author_ = 'David Poslt'
_email_  = 'david.poslt@gmail.com'

from time import sleep

def symbol(s):
    symbol = s
    return symbol

def progress(symbol):
    wait = sleep(2)

    for i in range(1,11):
        print(i, end='\t')
        sleep(1)
    print('\n')

progress(symbol('#'))

