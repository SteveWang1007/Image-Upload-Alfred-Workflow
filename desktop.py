from workflow import workflow
import sys


def desktop(wf):
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    currentFileList = os.listdir("/Users/mac/Desktop/")
    for elem in currentFileList:
        if image(elem):
            wf.add_item(title=elem,
                        subtitle='Press Enter to Upload this image',
                        arg=elem,
                        valid=False,
                        autocomplete=elem)
    wf.send_feedback()


if __name__ == '__main__':
    wf = workflow()
    sys.exit(wf.run(main))
