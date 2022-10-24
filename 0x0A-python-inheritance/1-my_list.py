#!/usr/bin/python3
'''My List module'''


class MyList(list):
    '''MyList Class that inherits from list'''

    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''
        print(sorted(self))
