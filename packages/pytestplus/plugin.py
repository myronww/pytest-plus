
import os
import time

from pytestplus import variables

def find_option_by_dest(opt_coll, dest):
    opt = None
    for oitem in opt_coll:
        if oitem.dest == dest:
            opt = oitem
            break
    return opt

def pytest_addoption(parser, pluginmanager):

    parser.addoption("--jobname", dest="jobname", default=variables.JOBNAME, 
        help="A jobname to use for the test reporting.")
    parser.addoption("--output-directory", dest="output_directory", default=variables.DEFAULT_OUTPUT_DIRECTORY,
        help="The output folder template where the test output byproducts should be written.")
    parser.addoption("--jsos-report", dest="jsos_report", default=True,
        help="Flag indicating that a jsos (javascript object stream) test results file should be generated.")
    parser.addoption("--jsos-report-name", dest="jsos_report_name", default="test-results.jsos",
        help="The filename of the jsos (javascript object stream) test results.")

    grp_logging = parser.getgroup("logging")

    opt_logfile = find_option_by_dest(grp_logging.options, "log_file")
    opt_logfile_attrs = opt_logfile.attrs()
    opt_logfile_attrs['help'] = 'The leaf filename of the destination testrun logfile.'
    opt_logfile_attrs['default'] = variables.DEFAULT_LOG_FILENAME

    return

def pytest_configure(config):
    opts = config.option
    variables.JOBNAME = opts.jobname.strip()

    outdir_fill = {
        'jobname': '',
        'start_time': variables.START_TIMESTAMP
    }
    if variables.JOBNAME != '':
        outdir_fill['jobname'] = variables.JOBNAME + os.path.sep

    opts.output_directory = opts.output_directory % outdir_fill
    if not os.path.exists(opts.output_directory):
        os.makedirs(opts.output_directory)

    opts.log_file = os.path.join(opts.output_directory, opts.log_file)
    opts.jsos_report_filename = os.path.join(opts.output_directory, opts.jsos_report_name)
    return

def pytest_runtest_logreport(report):
    return
