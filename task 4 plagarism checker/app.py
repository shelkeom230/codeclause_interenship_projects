import tkinter as tk
from tkinter import Text, Scrollbar, messagebox
import difflib

class PlagiarismChecker:
    def __init__(self, root):
        self.root = root
        root.title("Plagiarism Checker by Omkar Shelke || codeclause")
        
        root.configure(bg='#11f211')

        heading_label=tk.Label(root,text='Plagarism checker by Omkar Shelke',font=('Times New Roman',25,'bold'),bg='#11f211')
        heading_label.pack(pady=20)
        
        self.text1 = Text(root, wrap='word', width=50, height=15)
        self.text1.pack(side=tk.LEFT, padx=5, pady=5)

        scrollbar = Scrollbar(root, command=self.text1.yview)
        scrollbar.pack(side=tk.LEFT, fill='y')

        self.text1.config(yscrollcommand=scrollbar.set)

        self.text2 = Text(root, wrap='word', width=50, height=15)
        self.text2.pack(side=tk.LEFT, padx=5, pady=5)

        compare_button = tk.Button(root, text="Check Plagiarism", command=self.check_plagiarism)
        compare_button.pack(side=tk.TOP, pady=8)

        clear_button=tk.Button(root,text='clear input',command=self.clear_input)
        clear_button.pack(side=tk.TOP,pady=11)
        
        exit_btn=tk.Button(root,text='exit',command=self.exit_app)
        exit_btn.pack(side=tk.TOP,pady=14)
        
    def check_plagiarism(self):
        text1_content = self.text1.get("1.0", "end-1c")
        text2_content = self.text2.get("1.0", "end-1c")

        similarity_ratio = self.calculate_similarity(text1_content, text2_content)
        
        if similarity_ratio>=95.00:
            messagebox.showinfo("Plagiarism Result", f"Similarity Ratio: {similarity_ratio}% plagarism detected.")
        else:
            messagebox.showinfo("Plagarism result",f"Similarity Ratio: {similarity_ratio}% No plagarism detected.")

    def calculate_similarity(self, text1, text2):
        matcher = difflib.SequenceMatcher(None, text1, text2)
        similarity_ratio = matcher.ratio() * 100
        return round(similarity_ratio, 2)

    def clear_input(self):
        self.text1.delete("1.0",tk.END)
        self.text2.delete("1.0",tk.END)
        
    def exit_app(self):
        root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    plagiarism_checker = PlagiarismChecker(root)
    root.mainloop()

# I have made use of difflib to check for the similarity
# let's run the program 