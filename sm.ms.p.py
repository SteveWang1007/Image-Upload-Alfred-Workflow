from workflow import Workflow, ICON_INFO
from workflow.background import run_in_background, is_running

def main(wf):
    query = wf.args[0]
    if 'desktop' in query:
        run_in_background('desktop',)


if __name__ == '__main__':
    wf = Workflow()
    wf.run(main)