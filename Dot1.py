# GUI for T2S Converter

import tkinter as tk
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing

root = tk.Tk()
root.geometry("400x240")
root.title("T2S Converter Amazon Polly")
textExample = tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mg_con = boto3.session.Session(profile_name='Gurusaran')
    client = aws_mg_con.client(service_name='polly',region_name='us-east-1')  
    result = textExample.get("1.0","end")
    print(result)
    response = client.synthesize_speech(VoiceId='Ruth',OutputFormat='mp3',Text=result,Engine='neural')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output = os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)

    else:
        print("Could not find the stream")
        sys.exit(-1)
    if sys.platform == 'win32':
        os.startfile(output)       

btnread = tk.Button(root,height=2,width=9,text="Read",command=getText)
btnread.pack()

root.mainloop()

