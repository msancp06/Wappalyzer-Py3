# Author: Manuel Sanchez
# Github: https://github.com/msancp06
# Important: This code is intended to be used in unix enviroments, windows will not work due to signals.

import signal
import subprocess

def raise_timeout(signum, frame):
        raise TimeoutError
    
def wappalyzer_report(url, timeout=60):
    '''
        Generates the report from the wappalyzer app installed in localhost by npm.
        
        Parameters
        ----------
        url: str
            The URL to be analized.
        timeout : int
            Timeout in seconds.

        Returns
        -------
        json_report : json 
            The report of the website analysis.
    '''

    json_report = {}
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(timeout) #Set timeout

    try:
        json_report = subprocess.check_output(['wappalyzer', url]).decode("utf-8")
    except TimeoutError:
        print("Wappalyzer got timeout") #Use your favorite logger system
    except Exception as e:
        print("Wappalyzer got a problem:{}".format(e))

    signal.alarm(0) #Disable timeout

    return json_report