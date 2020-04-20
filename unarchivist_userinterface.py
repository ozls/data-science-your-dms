#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# LIBRARIES
# =============================================================================

import tkinter as t
from tkinter import filedialog, ttk

# =============================================================================
# FUNCTION
# =============================================================================

def ziptocsv():

    global zip_path
    global csv_path
    global prog
    global done

    from zipfile import ZipFile
    import pandas as pd
    import json

    done.configure(text="")
    d = pd.DataFrame([])

    with ZipFile(zip_path) as theZip:

        fileNames = theZip.namelist()
        fileNames = [fn for fn in fileNames if fn.endswith('json')]

        n = len(fileNames)
        i = -1

        for fileName in fileNames:

            i = i+1
            p = i*100/n

            prog["value"] = p
            prog.update()

            with theZip.open(fileName) as f:
                dic = json.load(f)
                df = pd.DataFrame(dic["messages"])
                df["title"] = dic["title"]
                df["type"] = dic["thread_type"]
                d = pd.concat([d, df])

    d = d.loc[:,("title", "type", "sender_name", "content", "timestamp_ms")]
    for c in ["sender_name", "content", "title"]:
        d[c] = [str(i).encode("latin1").decode("utf8") for i in d[c]]

    d.to_csv(csv_path, sep = ";")

    done.configure(text = "\nAll done !")

# =============================================================================
# INTERFACE
# =============================================================================

w = t.Tk()
w.title("FB Messenger Unarchiver")
w.geometry("640x480")

welcometxt = """
Welcome. This is a simple program to help you extract your messages from a Facebook archive. We assume you have successfully downloaded a ZIP Facebook archive containly only your messages, in the JSON format. Media quality doesn't matter as only text messages are extracted. You may choose "Low quality" for a faster download.
"""

welcome = t.Label(w, text = welcometxt, wraplength=600, justify="left")
welcome.grid(row=0, column=1, columnspan = 2)

# ZIP --------------------------------------------------------------------------

def choosezip():

    global zip_path

    ft = (("ZIP files","*.zip"),("all files","*.*"))
    zip_path = filedialog.askopenfilename(filetypes=ft)
    viewzip.configure(text = zip_path)

pickzip = t.Button(w, text = "Choose ZIP location", width = 20, height = 1, command = choosezip, anchor = "s")
pickzip.grid(row=1, column=1)

zip_path = "No path specified for the ZIP file containing your archives."
viewzip = t.Label(w, text=zip_path, justify="left")
viewzip.grid(row=1, column=2)

# CSV --------------------------------------------------------------------------

def choosecsv():

    global csv_path

    csv_path = filedialog.askdirectory()
    viewcsv.configure(text = csv_path)

pickcsv = t.Button(w, text = "Choose CSV location", width = 20, height = 1, command = choosecsv)
pickcsv.grid(row=2, column=1)

csv_path = "No path specified for the CSV file where your archives will be exported."
viewcsv = t.Label(w, text=csv_path, justify="left")
viewcsv.grid(row=2, column=2)

# EXTRACTING -------------------------------------------------------------------

extract = t.Button(w, text = "Extract messages", width = 20, height = 1, command = ziptocsv)
extract.grid(row=3, column=1)

# DONE -------------------------------------------------------------------------

prog = ttk.Progressbar(orient = "horizontal", maximum = 100, mode = 'determinate', length=360)
prog.grid(row=3, column=2)

done = t.Label(w, text="")
done.grid(row=4, column=1)

w.mainloop()