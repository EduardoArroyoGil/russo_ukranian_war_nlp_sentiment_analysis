import etls_main as etls_main

import datetime
import logging
import time


if __name__ == '__main__':

    # ct stores current time
    ct = str(datetime.datetime.now())[:19]

    # setting logging method
    logging.basicConfig(filename=f'logs/info_{ct}.txt', level=logging.DEBUG)

    # starting time to measure timings
    start_time = time.time()

    # calling out etls_main python script
    etls_main

    logging.debug("--- %s minutes ---" % round((time.time() - start_time) / 60, 2))

