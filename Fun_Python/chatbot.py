'''ZUBENTAHI FISRT CHATBOT CODE'''
from duckduckgo_search import DDGS
import GetDate
import tkinter as tk
from tkinter import messagebox
import googleSearch as gs
import mysql.connector
import _mysql_connector

#c_question = input("Question to chatbot: ")
#print(get_chatbot_response(c_question))

class Chatbot_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SkylaH CHATBOT GUI")
        self.root.geometry("700x300")  # Set window size
        self.root.configure(bg="lightgray")  # Set background color

        self.Title_label = tk.Label(root, text="Welcome to my Chatbot", font=("italy", 16, "bold"), fg="darkcyan", bg="lightgray")
        self.Title_label.pack(padx=10, pady=10)

        frame = tk.Frame(root)
        frame.pack()

        self.q_label = tk.Label(frame, text="Ask me a Question:", font=("arial",12, "bold"))
        self.q_label.grid(row=0, column=0, padx=5, pady=5)

        self.question_field = tk.Entry(frame, borderwidth=2, width=30)
        self.question_field.grid(row=0, column=1, padx=5, pady=5)

        self.button = tk.Button(frame, text="GET Answer➡️", font=("arial", 10, "bold"), bg="white", command=self.get_search_answer)
        self.button.grid(row=2, column=0, padx=5, pady=5)

        self.answer_label = tk.Label(frame, font=("arial", 12, "bold"), wraplength=375, justify="left")
        self.answer_label.grid(row=2, column=1, padx=5, pady=5)

        '''FUNCTION TO PROCESS RESULT FROM THE WRITTEN QUESTIONS AND ANSWERS'''
        
        self.question_and_answers ={
            "what's the weather today": "I can't tell you the weather yet, but I can learn to do that!",
            "What's the date today": GetDate.get_current_date(),
            "What's time  now": GetDate.get_current_time(),
            "How many province in SA": "9 Provinces",
            "1+1": "2"
        }

    #FUNCTION FOR CHAT_ RESPONSE
    def  get_chatbot_response(self):
        user_input = self.question_field.get()
        if user_input in self.question_and_answers:
            answer = self.question_and_answers[user_input]
            self.answer_label.configure(text=answer)
            return print(answer)
        if user_input == "":
            self.answer_label.configure(text="PLEASE WRITE SOMETHING")
        else:
            return messagebox.showinfo("infor", "Sorry I don't understand")

    def get_search_answer(self):
        query = self.question_field.get()

        if query=="":
            return self.answer_label.config(text="Please provide question ")
    # Check if the query is a math equation
        try:
            result = eval(query)  # Evaluate the math expression safely
            self.answer_label.configure(text=f"The result of {query} is: {result}")
            return print(f"The result of {query} is: {result}")
        except:
        # If it's not a math equation, perform a normal search
            results = DDGS().text(query, max_results=1)
            for result in results:
                self.answer_label.configure(text=result["body"])
                return print(result["body"])  # Extract the actual answer text

            return self.answer_label.configure(text="No relevant answer found.")

root = tk.Tk()
cb_app = Chatbot_GUI(root)
root.mainloop()