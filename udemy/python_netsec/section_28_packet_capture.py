#! python
"""
Project:    Udemy
Filename:   section_28_packet_capture
Created by: PJC
Created on: September 10, 2016
"""

import logging
import pcapy # Must do in Python 2.7

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():

    network_devices = pcapy.findalldevs()

    logger.info('Network Devices: {0}'.format(network_devices))

if __name__ == '__main__':
    main()