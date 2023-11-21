import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import font 

class MailSender:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Sender by Omkar Shelke || codeclause")
        self.root.geometry("400x400")
        
        self.heading_label = tk.Label(root, text="Mail Sender by Omkar Shelke", font=("Arial", 16, "bold"), bg="lightblue")
        self.heading_label.pack(pady=10)
        
        
        self.from_label = tk.Label(root, text="From:")
        self.from_label.pack()

        self.from_entry = tk.Entry(root, width=40)
        self.from_entry.pack()

        self.to_label = tk.Label(root, text="To:")
        self.to_label.pack()

        self.to_entry = tk.Entry(root, width=40)
        self.to_entry.pack()

        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(root, width=40)
        self.subject_entry.pack()

        self.message_label = tk.Label(root, text="Message:")
        self.message_label.pack()

        self.message_text = tk.Text(root, width=40, height=5)
        self.message_text.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_email)
        self.send_button.pack()

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_fields)
        self.clear_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def send_email(self):
        sender_email = self.from_entry.get()
        recipient_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        if not (sender_email and recipient_email and subject and message):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            app_password = "ctpi moys bbit qqjw"  # Replace with your generated app password
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()

            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def clear_fields(self):
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)
    
    def set_font(self):
        font_string = "Calibri 20"
        new_font = font.Font(family="Calibri", size=20)
        
        self.text_widget.config(font=new_font)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='lightblue')
    mail_sender = MailSender(root)
    root.mainloop()

# I made use of smtplib library and gmai service 
# let's run the program