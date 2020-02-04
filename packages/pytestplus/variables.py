
import os
import time

DEFAULT_OUTPUT_DIRECTORY = os.path.expanduser("~/testresults/%(jobname)s%(start_time)s")
DEFAULT_LOG_FILENAME = "testrun.log"

START_TIME = time.time()
START_TIMESTAMP = time.strftime("%Y-%m-%dT%H%M.%S", time.gmtime(time.time()))
JOBNAME = ""
OUTPUT_DIRECTORY = DEFAULT_OUTPUT_DIRECTORY % { 'jobname': '', 'start_time': START_TIMESTAMP}