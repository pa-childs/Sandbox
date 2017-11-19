#! python3
"""
Project:    Udemy
Filename:   section_28_create_raw_packets
Created by: PJC
Created on: September 11, 2016
"""

import logging
from scapy.all import *


# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():
    frame = Ether(dst='15:16:89:fa:dd:09'/IP(dst='9.16.5.4')/TCP()/'This is my payload')

    logger.info(frame)
    sendp(frame)

if __name__ == '__main__':
    main()
