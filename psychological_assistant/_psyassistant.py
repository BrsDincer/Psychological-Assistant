from src._modelrun import MODELRUN,IGNOREWARNINGOUTPUT
from src._createpassword import RANDOMPASSWORD
from src._classinits import CLASSINIT,PARAMETERS,RESPONSES,RESULTS
from src._speechon import SPEECHON
from src._constant import __ar__,__ex__,__ds__,__th__,__fv__,optlist,lnglist
import gradio as gr
import getopt,sys,os

class PSYCHOLOGICALCOUNSELOR(object):
    def __init__(self)->CLASSINIT:
        IGNOREWARNINGOUTPUT()
        self.__pss = RANDOMPASSWORD()
        self.__pss._GET()
        self.password = self.__pss.password
        self.username = self.__pss.username
    def __str__(self)->str:
        return "PSYCHOLOGICAL COUNSELOR - PROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->CLASSINIT:
        raise TypeError("[DENIED - PERMISSION]")
    def __repr__(self)->str:
        return PSYCHOLOGICALCOUNSELOR.__doc__
    def _RETURNVECTORS(self)->RESPONSES:
        self.__pss._PRINT()
        ix,iw = MODELRUN()._LAUNCH()
        return ix,iw
    
if __name__ == "__main__":
    arglist = sys.argv[1:]
    print("\n[>>] Counselor started by user\n")
    fc = PSYCHOLOGICALCOUNSELOR()
    try:
        arg_,val_ = getopt.getopt(arglist,
                                  optlist,
                                  lnglist)
        for cg_,cv_ in arg_:
            if cg_ in ("-f","--file"):
                print("\n[>>] This process may take a while\nIt is recommended that you do not stop the process\nYou will receive a message at the end of the process\n")
                MODELRUN()._PREMODELPROCESS()
                print("[++] New data processed and ready to use now\n\n")
    except getopt.error as err:
        print(str(err))
    ix,iw = fc._RETURNVECTORS()
    pss = fc.password
    usr = fc.username
    print("The window will open automatically via your default browser\nIf automatic startup does not occur, enter the given address manually\nPlease wait for a while\n\n")
    #
    tx_in = gr.inputs.Textbox(lines=10,
                              label="Client",
                              placeholder="Type here")
    tx_ou = gr.inputs.Textbox(lines=10,
                              label="Counselor - I",
                              placeholder="Thinking")
    tx_wk = gr.inputs.Textbox(lines=10,
                              label="Counselor - II",
                              placeholder="Thinking")
    cc_bx = gr.Checkbox(label="Speech to Counselor - I",
                        info="Do you want to listen to the Counselor-I?")
    ct_bx = gr.Checkbox(label="Speech to Counselor - II",
                        info="Do you want to listen to the Counselor-II?")
    #
    def GETCHAT(init:str,
                spcc:classmethod,
                spct:classmethod,
                mdnd:str="tree_summarize")->RESULTS:
        rsp = ix.query(init,
                        response_mode=mdnd)
        rsp2 = iw.query(init,
                        response_mode=mdnd)
        if spcc:
            tx1_ = "As Counselor One, "+str(rsp.response).lower()
            SPEECHON()._RUN(tx1_)
        if spct:
            tx2_ = "As Counselor Two, "+str(rsp2.response).lower()
            SPEECHON()._RUN(tx2_)
        return rsp.response,rsp2.response
    iface = gr.Interface(fn=GETCHAT,
                         theme=gr.themes.Monochrome(),
                         inputs=[tx_in,cc_bx,ct_bx],
                         outputs=[tx_ou,tx_wk],
                         title="Psychological Counselor",
                         article=__ar__,
                         examples=__ex__,
                         description=__ds__,
                         thumbnail=__th__)
    iface.launch(share=True,
                 auth=(str(usr),str(pss)),
                 auth_message="Welcome to your new client season",
                 max_threads=55,
                 quiet=True,
                 show_api=False,
                 inbrowser=True,
                 server_name="127.0.0.1",
                 favicon_path=__fv__)
    