from tkinter import *
from codeforces import api
def get_info(handles):
    x = api.call('user.info', handles=handles)
    return x[0]
def clicked():
    t.delete(1.0, END)
    req1 = ["Handle", "Current Rating", "Max Rating", "Current Rank", "Max Rank"]
    try:
        handles = textbox.get()
        dict1 = get_info(handles)
        req = ['handle','rating','maxRating','rank','maxRank']
        for i in range(len(req)):
            try:
                val = dict1[req[i]]
                f = '-'*60
                string = "  "+req1[i]+"\t\t\t"+str(val)+'\n'+f+"\n"
                t.insert(INSERT, string)
            except:
                string = "  " + req1[i] + "\t\t\t" + "N/A" + '\n' + f + "\n"
                t.insert(INSERT, string)
    except:
        for i in range(len(req1)):
            f = '-' * 60
            string = "  " + req1[i] + "\t\t\t" + "N/A" + '\n' + f + "\n"
            t.insert(INSERT, string)

if __name__ == "__main__":
    root = Tk()
    root.geometry("495x495+700+300")
    l = Label(root, text='Handle : ').place(x=105,y=70)
    t = Text(height=14,width=61)
    t.place(x=0,y=250)
    textbox = Entry(root)
    textbox.place(x=175,y=70)
    s =Button(root, text = "Submit",command=clicked)
    s.place(x=250,y=120,anchor=CENTER)

    root.mainloop()