#!/usr/bin/env python3

import operator

filename = 'Files/shoe-data.txt'

def line_to_dict(one_line):
    # brand, color, size = one_line.strip().split('\t')

    # return {'brand':brand,
    #         'color':color,
    #         'size': size}

    return dict(zip(['brand', 'color', 'size'],
                    one_line.strip().split('\t')))

shoes = [line_to_dict(one_line)
         for one_line in open(filename)]

def by_size(shoe_dict):
    return shoe_dict['size']


def by_brand_and_size(shoe_dict):
    return shoe_dict['brand'], shoe_dict['size']

# sort_key = input("Enter sort key: ")

# def by_user_key(shoe_dict):
#     return shoe_dict[sort_key]

def by_user_key():
    sort_key = input("Enter sort key: ")
    def inner(shoe_dict):
        return shoe_dict[sort_key]
    return inner

sort_keys = input("Enter sort key: ").split()
for one_shoe in sorted(shoes, key=operator.itemgetter(*sort_keys)):
    print(one_shoe)
    

# (1) Sort shoes by size (smallest to largest)
