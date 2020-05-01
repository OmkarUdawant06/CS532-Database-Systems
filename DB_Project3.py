#!/usr/bin/env python
import pandas as pd
import pymongo
import json
import os
import subprocess as sub
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sys
import collections
import numpy as np
import matplotlib.pyplot as plt
from bson.son import SON
import pprint
from fpdf import FPDF
import seaborn as sns
import json
from datetime import date, datetime, timedelta
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("MongoDB Application")
        self.minsize(640,400)
        self.configure(background = "#A9A9A9")
        self.photo = tk.PhotoImage(file = "/Users/tod/Downloads/icon1.png")
        self.iconphoto(False,self.photo)
        self.labelFrame = ttk.LabelFrame(self, text = "------MongoDB Project Assignment------")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.button_find_file()
        self.button_exit()
        self.button_query1()
        self.button_query2()
        self.button_query3()
        self.button_query4()
        self.button_query5()
        self.button_query6()
        self.button_query7()
        self.button_query8()
        
    def button_find_file(self):
        self.button = ttk.Button(self.labelFrame, text = "Import a File", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
        
    def button_exit(self):
        self.button = ttk.Button(self.labelFrame, text = "Exit", command = self.close_window)
        self.button.grid(column = 1, row = 4)
        
    def close_window(self):
        self.destroy()
        
    def button_query1(self):
        self.button = ttk.Button(self.labelFrame, text = "Query1", command = self.new_window1)
        self.button.grid(column = 3, row = 1)
        
    def button_query2(self):
        self.button = ttk.Button(self.labelFrame, text = "Query2", command = self.new_window2)
        self.button.grid(column = 3, row = 2)
        
    def button_query3(self):
        self.button = ttk.Button(self.labelFrame, text = "Query3", command = self.new_window3)
        self.button.grid(column = 3, row = 3)
        
    def button_query4(self):
        self.button = ttk.Button(self.labelFrame, text = "Query4", command = self.new_window4)
        self.button.grid(column = 3, row = 4)
        
    def button_query5(self):
        self.button = ttk.Button(self.labelFrame, text = "Query5", command = self.new_window5)
        self.button.grid(column = 4, row = 1)
        
    def button_query6(self):
        self.button = ttk.Button(self.labelFrame, text = "Query6", command = self.new_window6)
        self.button.grid(column = 4, row = 2)
        
    def button_query7(self):
        self.button = ttk.Button(self.labelFrame, text = "Query7", command = self.new_window7)
        self.button.grid(column = 4, row = 3)
        
    def button_query8(self):
        self.button = ttk.Button(self.labelFrame, text = "Query8", command = self.new_window8)
        self.button.grid(column = 4, row = 4)
        
        
    def connection_db(self):
        self.mng_client = pymongo.MongoClient('localhost', 27017)
        self.mng_db = self.mng_client['airlines'] # Replace mongo db name
        self.collection_name = 'data' # Replace mongo db collection name
        self.db_cm = self.mng_db[self.collection_name]
        
    def query1(self):
        self.connection_db()
        self.count = 0
        self.window.label1.destroy()
        self.textarea.destroy()
        
        self.var1 = str(self.combobox_a.get())
        self.var2 = str(self.n.get())
        self.var3 = str(self.combobox_b.get())
        if self.var1 == None:
            self.x = ()
            self.x = self.db_cm.find({"user_timezone":self.var2, "name":self.var3})
        else:
            self.x = ()
            self.x = self.db_cm.find({"airline_sentiment":self.var1, "name":self.var3})
       
        self.window.label1 = ttk.Label(self.window, text = "Following is the list of Airlines "+self.var3+" has ratted "+self.var1)
        self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)
            
        self.x = self.db_cm.find({"name":self.var3}, {"airline":1})
        self.listnew = list()
        self.count_no = 0    
        for doc in self.x:
                self.listnew.append(doc["airline"])
        
        for i, j in enumerate(self.listnew[:-1]):
            if j  == self.listnew[i+1]: 
                self.count_no = self.count_no +1
        self.count_no = self.count_no +1
        
        self.textarea = tk.Text(self.window)
        
        if self.count_no > 1:
                self.textarea.insert(END, str(self.listnew[0]) + '\t' + str(self.count_no))
        else:
            for x in self.listnew:
                self.textarea.insert(END, x + '\n')
        
        self.textarea.grid(column = 0, row = 7, padx = 10, pady = 10)
                
        
   
    def new_window1(self):
        self.window = tk.Toplevel(root)
        self.window.title("Frequency of Flights depending on sentiments: Positive / Negative / Neutral and Flyers")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        
        self.window.label1 = ttk.Label()
        self.textarea = tk.Text()
        
        self.window.label = ttk.Label(self.window, text = "Customize query below:")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Type of Comment:")
        self.window.label.grid(column = 0, row = 2, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Select Flyer Name:")
        self.window.label.grid(column = 0, row = 3, padx = 20, pady = 20)
        
        
        self.window.label = ttk.Label(self.window, text = "Select Timezone:")
        self.window.label.grid(column = 0, row = 4, padx = 20, pady = 20)
        
        self.dropdown_commenttype()
        
        self.buttonCommit = tk.Button(self.window, text="Show", command = self.query1)
        self.buttonCommit.grid(column = 1, row = 5)
    
    
    
    def query2(self):
        #db.Airlines.find({"airline_sentiment":"negative","airline":"Virgin America"},{negativereason:1, _id:0})
        self.connection_db()
        self.count = 0
        
        self.textarea.destroy()
        self.window.label1.destroy()
        self.x = ()
        self.air12 = list()
        #self.var1 = str(self.combobox_a.get())
        self.airline_var = str(self.airline_name.get())
        self.x = self.db_cm.find({"airline_sentiment":"negative","airline":self.airline_var},{"_id":0, "negativereason":1})
        for doc in self.x:
            self.air12.append(doc["negativereason"])
        
        self.window.label1 = ttk.Label(self.window, text = "Following are the negative comments for Airlines "+self.airline_var)
        self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)
          
        self.textarea = tk.Text(self.window)
        for x in self.air12:
            self.textarea.insert(END, x + '\n')
            self.textarea.grid(column = 0, row = 7, padx = 10, pady = 10)
        
        
    def new_window2(self):
        self.window = tk.Toplevel(root)
        self.window.title("List of Reasons for Negative Reactions")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "Customize query below:")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Select Airlines:")
        self.window.label.grid(column = 0, row = 2, padx = 20, pady = 20)
        
        
        self.airlines()
        
        self.buttonCommit = tk.Button(self.window, text="Show", command = self.query2)
        self.buttonCommit.grid(column = 1, row = 3)
     
    def airlines(self):
        self.connection_db()
        self.airline_name = tk.StringVar()
        self.air12 = list()
        
        self.air_names = self.db_cm.find({},{"airline":1, "_id":0})
        for doc in self.air_names:
            self.air12.append(doc["airline"])
        
        #remove same values from list
        self.air12 = [i for i in self.air12 if i] 
        
        self.sort1_airline_name = set(self.air12)
        self.unique_airline_name = (list(self.sort1_airline_name))
        
        self.air12 = list()
        
        for x in self.unique_airline_name: 
            self.air12.append(x)
            
        self.air12.sort()
        self.air_combo = ttk.Combobox(self.window, values=list(self.air12), textvariable = self.airline_name, state='readonly')
        self.air_combo.grid(column = 1, row = 2, padx = 20, pady = 20)
        
    def query3(self):
        #db.data.aggregate([{$match: {airline_sentiment : "negative", airline: "United"}},
        #{$group:{_id: { Airline: "United", NegativeReason:'$negativereason'}, Negative_Count:{$sum:1}}},
        #{ $sort: { Negative_Count: -1 } },{$limit:1} ])
        self.connection_db()
        self.count = 0
        
        self.textarea.destroy()
        self.window.label1.destroy()
        self.x = ()
        
        self.air12 = list()
        self.air13 = list()
        self.airline_var = str(self.airline_name.get())
        self.pipe = [{"$match": {"airline_sentiment" : "negative", "airline": self.airline_var}},
        {"$group":{"_id": { "Airline": self.airline_var, "NegativeReason":"$negativereason"}, "Negative_Count":{"$sum":1}}},
        { "$sort": { "Negative_Count": -1 } }]
        self.x = list(self.db_cm.aggregate(pipeline=self.pipe))
        for doc in self.x:
            self.air13.append(doc)
    
        self.window.label1 = ttk.Label(self.window, text = "Following is the count of negative comments that "+self.airline_var+" Airlines received from all flyers")
        self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)
        
        self.textarea = tk.Text(self.window, wrap="word")
        
        for x in self.air13:
            self.textarea.insert(END, str(x)+'\n')
        self.textarea.grid(column = 0, row = 7, padx = 10, pady = 10)
          
        
    def new_window3(self):
        self.window = tk.Toplevel(root)
        self.window.title("Frequency of most common reason for receiving the negative comment from Flyer (Highest to Lowest Frequency)")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "Customize query below:")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Select Airlines:")
        self.window.label.grid(column = 0, row = 2, padx = 20, pady = 20)
        
        self.airlines()
        
        self.buttonCommit = tk.Button(self.window, text="Show", command = self.query3)
        self.buttonCommit.grid(column = 1, row = 3)
        
        
    def query4(self):
       #db.data.aggregate([{$match: {airline_sentiment : "negative"}},
        #{$group:{_id: {Airline:'$airline'},Negative_Count:{$sum:1}}},
        #{ $sort: { Negative_Count: -1 } }])
        self.connection_db()
        
        self.textarea.destroy()
        self.window.label1.destroy()
        self.x = ()
        
        self.air13 = list()
        self.pipe = [{"$match": {"airline_sentiment" : "negative"}},
        {"$group":{"_id": {"Airline":'$airline'},"Negative_Count":{"$sum":1}}},
        { "$sort": { "Negative_Count": -1 } }]
        self.x = list(self.db_cm.aggregate(pipeline=self.pipe))
        for doc in self.x:
            self.air13.append(doc)
    
        self.window.label1 = ttk.Label(self.window, text = "Following is the list of Airlines sorted from Highest to Lowest negative comments from all flyers")
        self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)
        
        self.textarea = tk.Text(self.window, wrap="word")
        
        for x in self.air13:
            self.textarea.insert(END, str(x)+'\n')
        self.textarea.grid(column = 0, row = 7, padx = 10, pady = 10)
          
        
    def new_window4(self):
        self.window = tk.Toplevel(root)
        self.window.title("Maximum count of Negative reviews from the Flyer for all Airlines")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "--- Click  Show button --->")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.buttonCommit = tk.Button(self.window, text="Show Output", command = self.query4)
        self.buttonCommit.grid(column = 1, row = 3)
        
    def query5_pie(self):
        self.connection_db()
        self.data = pd.DataFrame(list(self.db_cm.find()))
        self.skip = 0

        self.nums = 14640
        self.pipeline = [
            {"$match": {"airline" : { "$nin": [ "null", "" , "Atlantic Time (Canada)"] }}},
            { "$group": { "_id":'$airline', "count": { "$sum": 1 }}},
            { "$project": {"count": 1,"percentage": {"$concat": [ { "$substr": [ { "$multiply": [ { "$divide": [ "$count", {"$literal": self.nums }] }, 100 ] }, 0,4] }, "", "%" ]}}},
            { "$sort": { "count": -1 } },
            { "$project": {"percentage" : 1}}]
        #pprint.pprint(list(self.db_cm.aggregate(self.pipeline)))

        #Pie chart of tweets frequency for each airline
        self.labels = ['United','US Airways','American','Southwest','Delta','Virgin America']
        self.percentage = [0.256, 0.195, 0.185, 0.162, 0.149, 0.0338]
        self.colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#33ccff', '#ff6600']
        self.fig1, self.ax1 = plt.subplots(figsize=(6.5, 6))
        self.ax1.pie(self.percentage, colors=self.colors, labels=self.labels, autopct='%1.1f%%', startangle=90)

        self.centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        self.fig = plt.gcf()
        self.fig.gca().add_artist(self.centre_circle)

        self.ax1.axis('equal')  
        plt.tight_layout()
        plt.title('Tweets Frequency by Airline', fontsize=18)
        #plt.figure(num='Pie Chart')
        plt.show()
        
    def query5_bar(self):
        self.connection_db()
        self.data = pd.DataFrame(list(self.db_cm.find({},{"_id":0,"airline":1, "negativereason":1})))

        #Visualize negaive reasons per airline
        self.colors = sns.color_palette('husl',10)
        pd.crosstab(self.data.airline, self.data.negativereason).plot(kind='bar',color=self.colors,figsize=(8,8),stacked=True)
        plt.title('The Reasons Customers React Negatively to Each Airline in Frequency', fontsize=18)
        plt.xlabel('Airline')
        plt.ylabel('Frequency')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=0)
        #plt.figure(num='Bar Graph')
        plt.show()
        #matplotlib.pyplot.title(label, fontdict=None, loc='center', pad=None, **kwargs)
    
    def new_window5(self):
        self.window = tk.Toplevel(root)
        self.window.title("Graphical representation of Airlines")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "--- Select Bar Graph / Pie Chart to display --->")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.buttonCommit = tk.Button(self.window, text="Show Pie Chart", command = self.query5_pie)
        self.buttonCommit.grid(column = 0, row = 3)
        
        self.buttonCommit = tk.Button(self.window, text="Show Bar Graph", command = self.query5_bar)
        self.buttonCommit.grid(column = 2, row = 3)
        
    def query6(self):
        self.connection_db()
        self.today = date.today()
        self.future = datetime.now()
        self.textarea.destroy()
        self.window.label1.destroy()
        self.x = ()
        self.x_airline_name = {}
        self.tweet = list()
        self.days_after = str((date.today()+timedelta(days=7)).strftime("%m/%d/%y"))
        
        self.airline_var = str(self.airline_name.get())
        
        self.pipe = [{"$match": {"airline" : self.airline_var, "airline_sentiment" : "negative"}},
                   {"$group":{"_id": {"NegativeReason":'$negativereason', "TweetCreated":'$tweet_created'},
                   "Negative_Count":{"$sum":1}}},{ "$sort": { "Negative_Count": -1 } }  ]
        self.x = list(self.db_cm.aggregate(pipeline = self.pipe)) 
        
        for doc in self.x:	
            self.x_airline_name.update(doc)
        
        
        self.prob=0
        self.chances=0
        if self.airline_var == "American":
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 2759
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
        elif self.airline_var == "Delta":
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 2222
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
        elif self.airline_var == "Southwest": 
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 2420
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
        elif self.airline_var == "US Airways":
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 2913
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
        elif self.airline_var == "United":
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 3822
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
        else:
            self.late_flight = self.db_cm.count_documents({"airline": self.airline_var, "negativereason": 'Late Flight'})
            self.total_negative = 504
            self.chances = (self.late_flight/self.total_negative)*100
            self.prob = (1-(self.late_flight/self.total_negative))*100
            
        self.window.label1 = ttk.Label(self.window, text = "The Chances that "+self.airline_var+" Airlines compared to other negative reasons will have Flight delays in next week: "+self.days_after+" is "+str(round(self.chances,2))+'%')
        self.window.label1.grid(column = 0, row = 5, padx = 20, pady = 20)    
        
        #self.window.label1 = ttk.Label(self.window, text = "The Probability that "+self.airline_var+" Airlines compared to other negative reasons will have Flight delays in next week: "+self.days_after+" is "+str(round(self.prob,2))+'%')
        #self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)    
        
        
        
    def new_window6(self):
        self.window = tk.Toplevel(root)
        self.window.title("Predict Delays in Airlines")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "--- Select Airlines and Predict future delays in Airlines --->")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Select Airlines:")
        self.window.label.grid(column = 0, row = 2, padx = 20, pady = 20)
        
        self.airlines()
        
        self.buttonCommit = tk.Button(self.window, text="Predict Future Delays", command = self.query6)
        self.buttonCommit.grid(column = 1, row = 3)
     
    def popupmsg(self,msg):
        self.popup = tk.Tk()
        self.NORM_FONT= ("Verdana", 10)
        self.popup.wm_title("Report GeneratedSuccessfully!")
        self.label = ttk.Label(self.popup, text=msg, font=self.NORM_FONT)
        self.label.grid(column = 1, row = 1)
        self.B1 = ttk.Button(self.popup, text="Okay", command = self.popup.destroy)
        self.B1.grid(column = 1, row = 2)
        self.popup.mainloop()
        
    
    def query7(self): 
        for i,j in self.x_airline_name.items():
            if str(j) is "True":
                self.pdf = FPDF()
                FPDF(orientation='P', unit='pt', format='A4')
                self.pdf.add_page()
                self.pdf.set_font("Arial", size=12)
                self.pdf.cell(200, 10, txt=i+" Airline needs Improvement!", ln=1, align="C")
                self.pdf.cell(200, 10, txt="Your airlines have received many negative comments.", ln=2, align="L")
                self.pdf.cell(200, 10, txt="Please improve services inorder to provide better experience for your customers!", ln=2, align="L")
                self.pdf.output("Airlines_"+i+".pdf")
        self.popupmsg("Query Successful!")
        
    def new_window7(self):
        self.window = tk.Toplevel(root)
        self.window.title("Generate Report for suggesting improvement")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        self.connection_db()
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.x_airline_name = {}
        self.x_status = list()
        
        self.pipe = [{"$match": {"airline_sentiment" : "negative"}},
        {"$group":{"_id":'$airline',"Negative_Count":{"$sum":1}}},
        {"$project": {"Negative_Count":{ "$gt": ['$Negative_Count',1000] } }}]
        self.x = list(self.db_cm.aggregate(pipeline = self.pipe))
        for doc in self.x:	
            self.x_airline_name.update( {doc["_id"] : doc["Negative_Count"]} )
        
        self.window.label = ttk.Label(self.window, text = "--- Click  Generate Report button --->")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.buttonCommit = tk.Button(self.window, text="Generate Report", command = self.query7)
        self.buttonCommit.grid(column = 1, row = 3)
        
    def query8(self): 
        self.connection_db()
        
        self.textarea.destroy()
        self.window.label1.destroy()
        
        #airlines name
        self.airline_var = str(self.airline_name.get())
        self.x_airline_name = {}
        
        self.add_feedback = self.db_cm.update_many({},{"$set": {"feedback" : ""}},True)
        self.map_feedback = self.db_cm.update_many({"airline_sentiment":"positive"},{"$set": {"feedback" : "good"}},True)
        
        #aggregate([{$match: {feedback : good}},{$group:{_id:$airline,text:$text}}])
        
        self.pipe = [{"$match": {"feedback" : "good"}},{"$group":{"_id":'$airline',"text":{"$push":'$text'}}}]
        self.x = list(self.db_cm.aggregate(pipeline = self.pipe))
        for doc in self.x:	
            self.x_airline_name.update( {doc["_id"] : doc["text"]} )
          
        self.window.label1 = ttk.Label(self.window, text = "Following is the list of Feedback for "+self.airline_var+" Airlines")
        self.window.label1.grid(column = 0, row = 6, padx = 20, pady = 20)
        
        self.textarea = tk.Text(self.window, wrap="word")
        
        for k,v in self.x_airline_name.items():
            if k == self.airline_var:
                for x in v:
                    self.textarea.insert(END, str(x)+'\n')
        
        self.textarea.grid(column = 0, row = 7, padx = 10, pady = 10)
        self.drop_feedback = self.db_cm.update_many({},{"$unset": {"feedback" : ""}},True)
        
        
    def new_window8(self):
        self.window = tk.Toplevel(root)
        self.window.title("Feedback Section for Positive Comments")
        self.window.minsize(640,400)
        self.window.configure(background = "#A9A9A9")
        
        self.textarea = tk.Text()
        self.window.label1 = ttk.Label()
        
        self.window.label = ttk.Label(self.window, text = "--- Generate Feedback Below --->")
        self.window.label.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.window.label = ttk.Label(self.window, text = "Select Airlines:")
        self.window.label.grid(column = 0, row = 2, padx = 20, pady = 20)
        
        self.airlines()
        
        self.buttonCommit = tk.Button(self.window, text="Generate Feedback", command = self.query8)
        self.buttonCommit.grid(column = 1, row = 3)
        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetypes = (("csv files","*.csv"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.import_content()
        if self.flag == True :
            ttk.Label(text = "File imported in Mondo DB successfully!").grid(column = 0,row = 5)
        else:
            ttk.Label(text = "Some error occured!").grid(column = 0,row = 5)
    
    def import_content(self):
        self.flag = False
        self.connection_db()
        cdir = os.path.dirname(__file__)
        file_res = os.path.join(cdir, self.filename)
        data = pd.read_csv(file_res)
        data_json = json.loads(data.to_json(orient='records'))
        self.db_cm.drop()
        self.db_cm.insert_many(data_json)
        self.flag = True;
        
    def dropdown_commenttype(self):
        self.connection_db()
        self.option_name_negative = tk.StringVar()
        self.option_name_positive = tk.StringVar()
        self.option_name_neutral = tk.StringVar()
        self.option_comment = tk.StringVar()
        self.option_timezone = tk.StringVar()
        self.name_var = tk.StringVar()
        self.sentiment_var = tk.StringVar()
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        self.last_county = tk.StringVar(self)
        self.area = tk.StringVar(self)
        self.country = tk.StringVar(self)
        self.choice_name_negative = list()
        self.choice_name_positive = list()
        self.choice_name_neutral = list()
        self.choices1 = list()
        self.ch12 = list()
        
        self.names = self.db_cm.find({"airline_sentiment":"negative"},{"_id":0, "name":1})
        for doc in self.names:
            self.choice_name_negative.append(doc["name"])
        
        self.sort1_flyer_name = set(self.choice_name_negative)
        self.unique_flyer_name = (list(self.sort1_flyer_name))
        
        self.choice_name_negative = list()
        
        for x in self.unique_flyer_name: 
            self.choice_name_negative.append(x)
            
        self.choice_name_negative.sort()
        
        #---------------------------------------------------------------------------------------
        
        self.names1 = self.db_cm.find({"airline_sentiment":"positive"},{"_id":0, "name":1})
        for doc in self.names1:
            self.choice_name_positive.append(doc["name"])
        
        self.sort1_flyer_name1 = set(self.choice_name_positive)
        self.unique_flyer_name1 = (list(self.sort1_flyer_name1))
        
        self.choice_name_positive = list()
        
        for x in self.unique_flyer_name1: 
            self.choice_name_positive.append(x)
        
        self.choice_name_positive.sort()
        
        #---------------------------------------------------------------------------------------
        
        self.names2 = self.db_cm.find({"airline_sentiment":"neutral"},{"_id":0, "name":1})
        for doc in self.names2:
            self.choice_name_neutral.append(doc["name"])
        
        self.sort1_flyer_name2 = set(self.choice_name_neutral)
        self.unique_flyer_name2 = (list(self.sort1_flyer_name2))
        
        self.choice_name_neutral = list()
        
        for x in self.unique_flyer_name2: 
            self.choice_name_neutral.append(x)
        
        self.choice_name_neutral.sort()
        
        #---------------------------------------------------------------------------------------
        
        self.choices2 = {'positive':self.choice_name_negative,'negative':self.choice_name_positive,'neutral':self.choice_name_neutral}
        
        self.variable10 = tk.StringVar(self)
        self.variable20 = tk.StringVar(self)
        
        self.variable_b.trace('w', self.fun2)
        self.variable_a.trace('w', self.update_options)
        
        
        self.combobox_a = ttk.Combobox(self.window, values=list(self.choices2.keys()), textvariable = self.variable10, state='readonly')
        self.combobox_a.bind("<<ComboboxSelected>>", self.fun)
        self.combobox_a.current(0)
        
        if list(self.choices2.keys()) == "positive":
            self.combobox_b = ttk.Combobox(self.window, values=self.choices2['positive'], textvariable = self.variable20, state='readonly')
        elif list(self.choices2.keys()) == "negative":
            self.combobox_b = ttk.Combobox(self.window, values=self.choices2['negative'], textvariable = self.variable20, state='readonly')
        else:
            self.combobox_b = ttk.Combobox(self.window, values=self.choices2['neutral'], textvariable = self.variable20, state='readonly')
        
        self.combobox_b.bind("<<ComboboxSelected>>", self.fun2)
        self.combobox_b.current(0)
        
        self.combobox_a.grid(column = 1, row = 2, padx = 20, pady = 20)
        self.combobox_b.grid(column = 1, row = 3, padx = 20, pady = 20)
        
        self.button_search = ttk.Button(self.window, text = "Search timezone", command = self.time)
        self.button_search.grid(column = 2, row = 3)
        #---------------------------------------------------------------------------------------
        #"airline_sentiment":"negative","user_timezone":"Pacific Time (US & Canada)","name":"GunsNDip"
     
    def time(self):   
        self.n = tk.StringVar() 
        self.window.label1.destroy()
        self.textarea.destroy()
        self.choices1 = ttk.Combobox(self.window, width = 27, textvariable = self.n)
        
        self.names3 = self.db_cm.find({"airline_sentiment":self.variable10.get(),"name":self.variable20.get()},{"_id":0,"user_timezone":1})
        for doc in self.names3:
            self.ch12.append(doc["user_timezone"])
            
        self.ch12 = [i for i in self.ch12 if i] 
        self.sort1_timezone = set(self.ch12)
        self.unique_list_timezone = (list(self.sort1_timezone))
        self.ch12 = list()
        
        for x in self.unique_list_timezone: 
            self.ch12.append(x)
        
        self.choices1['values'] = (self.ch12)
        self.choices1.grid(column = 1, row = 4, padx = 20, pady = 20)
    
    
    def fun(self,*args):
        #print("changed 1-st combobox value to: " + self.combobox_a.get())
        if self.last_county != self.combobox_a.get():
            self.combobox_b['values'] = self.choices2[self.combobox_a.get()]
            self.combobox_b.current(0)
        self.last_county = self.area = self.combobox_a.get()
        
        return self.variable_a.get()

    def fun2(self, *args):
        #print("changed 2-nd combobox value to" + self.combobox_b.get())
        self.country = self.combobox_b.get()
        return self.variable_b.get()

    def update_options(self, *args):
        countries = self.choices2[self.variable_a.get()]
        self.variable_b.set(countries[0])
        menu = self.combobox_b['menu']
        menu.delete(0, 'end')
        

if __name__ == '__main__':
    root = Root()
    root.iconbitmap('/Users/tod/Downloads/iconnew.ico')
    root.mainloop()