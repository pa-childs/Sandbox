#! python3
"""
Project:    Sandbox
Filename:   paramiko_test
Created by: PJC
Created on: August 22, 2016
"""

import logging
import paramiko

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Setup for connection to SSH
REVIEW_ENV = 'c375ragtsdev1.int.thomsonreuters.com'
USERNAME = 'techstreet'
PASSWORD = '!techstreet'


# Open SSH Connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(REVIEW_ENV, username=USERNAME, password=PASSWORD)
logger.info('SSH Connection Opened\n')

# List directory
test_command = 'ls -la'
logger.info('Running: {0}'.format(test_command))

stdin, stdout, stderr = ssh.exec_command(test_command)
output = stdout.readlines()
err_msg = stderr.readlines()

if not output:

    logger.info('STDERR: {0}\n'.format(str(err_msg)))

else:

    logger.info('Output:\n {0}\n'.format(str(output)))


# Change directory
target_path = '/data/techstreet/instances/jason/PDF_ROOT/pdfs'
test_command = 'cd {0}; pwd'.format(target_path)
logger.info('Running: {0}'.format(test_command))

stdin, stdout, stderr = ssh.exec_command(test_command)
output = stdout.readlines()
err_msg = stderr.readlines()

if not output:

    logger.info('STDERR: {0}\n'.format(str(err_msg)))

else:

    logger.info('Output:\n {0}\n'.format(str(output)))

# Change directory
test_command = 'find {0} -name "{1}"'.format(target_path, 'AHP-Ginkgo.pdf')
logger.info('Running: {0}'.format(test_command))

stdin, stdout, stderr = ssh.exec_command(test_command)
output = stdout.readlines()
err_msg = stderr.readlines()

if not output:

    logger.info('STDERR: {0}\n'.format(str(err_msg)))

else:

    logger.info('Output:\n {0}\n'.format(str(output)))

ssh.close()
logger.info('SSH Connection Closed\n')
