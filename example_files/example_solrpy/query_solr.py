#! python3
"""
Project:    Sandbox
Filename:   query_solr
Created by: PJC
Created on: September 08, 2016
"""

import argparse
import logging
import pysolr

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():

    args = argparse.ArgumentParser('Perform a SOLR search against c375ragtsdev1.  The following fields can be searched:'
                                   '  id, title_texts, document_number_texts, or _version_.')
    args.add_argument('-r',
                      type=int,
                      help='Set the number of results to return',
                      required=False)
    args.add_argument('-s',
                      type=str,
                      help='Set the field and string to search for, e.g. title_texts:"api".',
                      required=False)
    args.add_argument('-fq',
                      type=list,
                      help="Add any desired filter queries that will narrow the returned results.  This is added as a "
                           "list, e.g.['type:Product', 'subscriptions_im:3']",
                      required=False)

    cmdargs = args.parse_args()

    if cmdargs.r is None:

        results_returned = 10

    else:

        results_returned = cmdargs.r

    if cmdargs.s is None:

        # Search term is in format of field:search_term
        search_term = '*:*'

    else:

        search_term = cmdargs.s

    filter_queries = cmdargs.fq
    filter_queries = ['type:Product', 'subscriptions_im:3', 'current_b:true', 'base_b:true']

    solr_url = 'http://c375ragtsdev1.int.thomsonreuters.com:8983/solr/enterprise_full_text/'

    try:

        # Create SOLR connection
        solr_conn = pysolr.Solr(solr_url, timeout=10)

        # Perform search with provided search variables
        logger.info('SOLR Searching...')
        results = solr_conn.search(search_term, fq=filter_queries, rows=1000000)
        logger.info('SOLR Search Succeeded')

    except Exception as e:

        logger.warn('SOLR Search Failed')
        logger.exception(e)
        quit()

    logger.info("Total results:  {0}.\n".format(len(results)))

    # Display the ID and Title of each returned result
    for result in results:

        logger.info('{0}: Title is "{1}"'.format(result['id'],result['title_texts']))






if __name__ == '__main__':
    main()