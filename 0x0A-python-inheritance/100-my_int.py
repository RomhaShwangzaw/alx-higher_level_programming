#!/usr/bin/python3
'''A MyInt module'''


class MyInt(int):
    '''A MyInt class that has == and != operators inverted'''

    def __eq__(self, value):
        '''Override == operator with != behavior'''
        return super().__ne__(value)

    def __ne__(self, value):
        '''Override != operator with == behavior'''
        return super().__eq__(value)
