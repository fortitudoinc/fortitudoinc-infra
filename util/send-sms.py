#!/usr/bin/env python3
"""
Usage: ./send-sms.py phonenumber msg
"""

import boto3
import sys

def usage():
    print('Usage: {} phonenumber msg'.format(sys.argv[0]))
    print('\tImportant! Phone number parameter must include country code!')


def main():
    sns = boto3.client('sns')

    # Testing on US number indicates that long messages (greater than 140 characters) should be automatically broken up
    resp = sns.publish(
        PhoneNumber=sys.argv[1],
        Message=sys.argv[2],
        Subject='Fortitudo Telemedicine Message'
    )

    print(resp)

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        usage()
    else:
        main()