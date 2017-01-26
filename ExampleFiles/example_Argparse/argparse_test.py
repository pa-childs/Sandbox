#! python3
"""
Project:    Sandbox
Filename:   argparse_test
Created by: PJC
Created on: July 23, 2016
"""

import argparse


def main():
    args = argparse.ArgumentParser('This is an example of how to pass arguments to a Python script.')
    args.add_argument('-n', type=str, help='The name of the person.', required=True)
    args.add_argument('-a', type=int, help='The age of the person', required=True)
    args.add_argument('-p', type=str, help='The type of pet they have', required=False)

    cmdargs = args.parse_args()

    name = cmdargs.n
    age = cmdargs.a
    pet = cmdargs.p

    if pet:

        print("My name is {0}.  I am {1} years old.  I have a {2}.".format(name, age, pet))

    else:

        print("My name is {0}.  I am {1} years old.  I don't have a pet.".format(name, age))


if __name__ == '__main__':
    main()
