from workflow import Workflow
from workflow.background import run_in_background, is_running
import sys


def main(wf):
    query = wf.args[0]
    if 'desktop' in query:
        cmd = ['/usr/bin/python', wf.workflowfile('destop.py')]
        run_in_background('desktop', cmd)
    if is_running('desktop'):
        running()


def running():
    wf.add_item('Fetching Data')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))