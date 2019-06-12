import subprocess as sp
import os
import junit_xml
import shutil
import glob

XUNIT_BIN_NAME = 'xunit-viewer'

if __name__ == "__main__":
    bin_runner_path = os.environ['TEST_BIN_PATH']
    results_folderpath = os.environ['TEST_RESULTS_PATH']
    junit_results_filepath = os.path.join(results_folderpath, "results.xml")
    html_results_filepath = os.path.join(results_folderpath, "results.html")

    # results folder

    if not os.path.isdir(results_folderpath):
        os.mkdir(results_folderpath)

    files = glob.glob(results_folderpath+os.path.sep+"*")
    for f in files:
        os.remove(f)

    # execute

    result = sp.run([bin_runner_path, '--log_format=JUNIT', '--log_level=all',
            '--run_test=liba_suite/trivial_suite', f'--log_sink={junit_results_filepath}'])

    print(f"Test runner completed with exit code: {result.returncode}")

    result = sp.run([XUNIT_BIN_NAME,
            f'--results={results_folderpath}', f'--output={html_results_filepath}'], shell=True)

