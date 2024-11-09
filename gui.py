from analysis import stats_analysis
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

window = Tk()
df = stats_analysis()
now = datetime.now()
date = now.date()

window.geometry("1140x730")
window.resizable(False, False)
window.config(bg="#1C1C1C")
window.title("NBA Stats Scraper: 2024-2025 NBA Preseason Stats")
icon = PhotoImage(file="icons/icon-logo.png")
window.iconphoto(True, icon)
text_widget = ""

def on_enter(e):
  e.widget['background'] = '#1D428A'  # Lighter blue for hover
  e.widget['foreground'] = 'white'

def on_leave(e):
  e.widget['background'] = '#0C2340'  # Original blue color
  e.widget['foreground'] = 'white'

def on_enter_red(e):
  e.widget['background'] = '#E04A5A'  # Lighter blue for hover
  e.widget['foreground'] = 'white'

def on_leave_red(e):
  e.widget['background'] = '#C8102E'  # Original red color
  e.widget['foreground'] = 'white'

def main():
  global button_df, button_info, button_offensive, button_defensive, label, display_date, all_rights

  for widget in window.winfo_children():
        widget.place_forget()

  if text_widget:
    text_widget.place_forget()
  
  display_date = Label(text=f"Date: {date}", background="#1C1C1C", fg="white")
  display_date.pack(side=TOP, anchor="ne")

  label = Label(text="2024-2025 NBA Season Prediction", bg="#1C1C1C", font = ('Helvetica', 30, 'bold'), fg="white")
  label.place(x=320, y=160)

  nba_logo = Image.open("icons/nba-logo.png")
  resized_image = nba_logo.resize((80, 170), Image.LANCZOS)
  nba_logo_tk = ImageTk.PhotoImage(resized_image)

  # Create a label with the resized PhotoImage
  image_label = Label(window, image=nba_logo_tk, background="#1C1C1C")
  image_label.image = nba_logo_tk 
  image_label.place(x=190,y=100)  # Ensure this is properly packed or placed in the layout

  button_df = Button(text="Scraped Data", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=overall_stats, cursor="hand2", activebackground="#C8102E")
  button_df.bind("<Enter>", on_enter)
  button_df.bind("<Leave>", on_leave)
  button_df.place(x=380, y=270)

  button_info = Button(text="About", padx=45, pady=11, font=("Helvetica", 12), bg="#0C2340", fg="white", cursor="hand2", activebackground="#C8102E", command=about)
  button_info.bind("<Enter>", on_enter)
  button_info.bind("<Leave>", on_leave)
  button_info.place(x=625, y=269)

  button_offensive = Button(text="Offensive Ratings", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=offensive_ratings, cursor="hand2", activebackground="#C8102E")
  button_offensive.bind("<Enter>", on_enter)
  button_offensive.bind("<Leave>", on_leave)
  button_offensive.place(x=368, y=370)

  button_defensive = Button(text="Defensive Ratings", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=defensive_ratings, cursor="hand2", activebackground="#C8102E")
  button_defensive.bind("<Enter>", on_enter)
  button_defensive.bind("<Leave>", on_leave)
  button_defensive.place(x=608, y=370)

  button_save_overall_data = Button(text="Save Overall Data", padx=15, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=save_all_stats, cursor="hand2", activebackground="#C8102E")
  button_save_overall_data.bind("<Enter>", on_enter)
  button_save_overall_data.bind("<Leave>", on_leave)
  button_save_overall_data.place(x=490, y=470)

  all_rights = Label(text="©2024 All Rights Reserved  |  v1.0.0", background="#1C1C1C", fg="white")
  all_rights.pack(side=BOTTOM, anchor="se")

def save_all_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_overall_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'ORB', 'RPG', 'PF']].to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_offensive_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'PPG', 'EFG%', 'TS%', 'APG', 'TO Ratio', 'Off Ratings']].sort_values(by="Off Ratings", ascending=False).to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_defensive_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'DRB', 'SPG', 'BPG', 'TOV', 'Def Ratings']].sort_values(by="Def Ratings", ascending=False).to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def overall_stats():

    for widget in window.winfo_children():
      widget.place_forget()

    if text_widget:
      text_widget.place_forget()
    
    display_date.pack_forget()
    all_rights.pack_forget()

    label.config(text="2024-2025 NBA Pre-Season Stats", font=("Arial", 25, 'bold'))
    label.place(x=315, y=50)

    global frame
    frame = Frame(window)
    frame.place(x=100, y=120)

    # Create a Text widget
    table = tk.Text(frame, height=30, width=113, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table.config(yscrollcommand=scrollbar.set)

    # Insert column headers
    table.insert(tk.END, f"{'Team':<15} | {'GP':<1} | {'MPG':<4} | {'FGM':<4} | {'FGA':<4} | {'FG%':<4} | {'3PM':<4} | {'3PA':<5} | {'3P%':<4} | {'FTM':<4} | {'FTA':<4} | {'FT%':<4} | {'ORB':<4} | {'RPG':<4} | {'PF':<8}\n")
    table.insert(tk.END, "-" * 112 + "\n")  # Separator line

    # Insert teams and stats into the Text widget
    for index, row in df.iterrows():
        table.insert(tk.END, f"{row['Team']:<15} | {row['GP']:<2} | {row['MPG']:<3} | {row['FGM']:<3} | {row['FGA']:<3} | {row['FG%']:<3} | {row['3PM']:<4} | {row['3PA']:<3}  | {row['3P%']:<3} | {row['FTM']:<3} | {row['FTA']:<3} | {row['FT%']:<3} | {row['ORB']:<4} | {row['RPG']:<3} | {row['PF']:<7}\n")
    
    home_button = Button(text="Home", padx=15, pady=2, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
    home_button.bind("<Enter>", on_enter)
    home_button.bind("<Leave>", on_leave)
    home_button.place(x=470, y=670)

    save_button = Button(text="Save", padx=15, pady=2, font=("Helvetica", 11), bg="#0C2340", fg="white", command=save_overall_stats, cursor="hand2", activebackground="#C8102E")
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    save_button.place(x=610, y=670)


def offensive_ratings():
  for widget in window.winfo_children():
      widget.place_forget()

  if text_widget:
    text_widget.place_forget()

  display_date.pack_forget()
  all_rights.pack_forget()

  label.config(text="2024-2025 NBA Top Offensive Teams", font=("Arial", 25, 'bold'))
  label.place(x=283, y=50)

  off_chart = Image.open("icons/Offensive-Chart.png")

  resized_image = off_chart.resize((450, 453), Image.LANCZOS)

  off_chart_tk = ImageTk.PhotoImage(resized_image)

  # Create a label with the resized PhotoImage
  image_label = Label(window, image=off_chart_tk)
  image_label.image = off_chart_tk 
  image_label.place(x=35,y=125)  # Ensure this is properly packed or placed in the layout

  global frame
  frame = Frame(window)
  frame.place(x=500, y=125)

  # Create a Text widget
  table = tk.Text(frame, height=26, width=68, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
  table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  scrollbar = tk.Scrollbar(frame, command=table.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

  table.config(yscrollcommand=scrollbar.set)

  # Insert column headers
  table.insert(tk.END, f"{'Team':<15} | {'PPG':<5} | {'EFG%':<4} | {'TS%':<4} | {'APG':<4} | {'TO Ratio':<4} | {'Off Ratings':<4}\n")
  table.insert(tk.END, "-" * 69 + "\n")  # Separator line

  sorted_df = df.sort_values(by="Off Ratings", ascending=False)

  # Insert teams and stats into the Text widget
  for index, row in sorted_df.iterrows():
      table.insert(tk.END, f"{row['Team']:<15} | {row['PPG']:<5} | {row['EFG%']:<3} | {row['TS%']:<3} | {row['APG']:<3} | {row['TO Ratio']:<8} | {row['Off Ratings']:<3}\n")

  home_button = Button(text="Home", padx=20, pady=3, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
  home_button.bind("<Enter>", on_enter)
  home_button.bind("<Leave>", on_leave)
  home_button.place(x=515, y=670)

  save_button = Button(text="Save Data", padx=10, pady=3, font=("Helvetica", 10), bg="#C8102E", fg="white", command=save_offensive_stats, cursor="hand2", activebackground="#0C2340", activeforeground="white")
  save_button.bind("<Enter>", on_enter_red)
  save_button.bind("<Leave>", on_leave_red)
  save_button.place(x=750, y=595)


def defensive_ratings():
  for widget in window.winfo_children():
      widget.place_forget()

  if text_widget:
    text_widget.place_forget()
  
  display_date.pack_forget()
  all_rights.pack_forget()

  label.config(text="2024-2025 NBA Top Defensive Teams", font=("Arial", 25, 'bold'))
  label.place(x=283, y=50)

  off_chart = Image.open("icons/Defensive-Chart.png")

  resized_image = off_chart.resize((450, 453), Image.LANCZOS)

  off_chart_tk = ImageTk.PhotoImage(resized_image)

  # Create a label with the resized PhotoImage
  image_label = Label(window, image=off_chart_tk)
  image_label.image = off_chart_tk 
  image_label.place(x=35,y=125)  # Ensure this is properly packed or placed in the layout

  global frame
  frame = Frame(window)
  frame.place(x=500, y=125)

  # Create a Text widget
  table = tk.Text(frame, height=26, width=68, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
  table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  scrollbar = tk.Scrollbar(frame, command=table.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

  table.config(yscrollcommand=scrollbar.set)

  # Insert column headers
  table.insert(tk.END, f"{'Team':<15} | {'DRB':<5} | {'SPG':<4} | {'BPG':<4} | {'TOV':<4} | {'Def Ratings':<4}\n")
  table.insert(tk.END, "-" * 69 + "\n")  # Separator line

  sorted_df = df.sort_values(by="Def Ratings", ascending=False)

  # Insert teams and stats into the Text widget
  for index, row in sorted_df.iterrows():
      table.insert(tk.END, f"{row['Team']:<15} | {row['DRB']:<5} | {row['SPG']:<4} | {row['BPG']:<3} | {row['TOV']:<5} | {row['Def Ratings']:<3}\n")

  home_button = Button(text="Home", padx=20, pady=3, font=("Helvetica", 12), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
  home_button.bind("<Enter>", on_enter)
  home_button.bind("<Leave>", on_leave)
  home_button.place(x=515, y=670)

  save_button = Button(text="Save Data", padx=10, pady=3, font=("Helvetica", 10), bg="#C8102E", fg="white", command=save_defensive_stats, cursor="hand2", activebackground="#0C2340", activeforeground="white")
  save_button.bind("<Enter>", on_enter_red)
  save_button.bind("<Leave>", on_leave_red)
  save_button.place(x=750, y=595)

def about():

  global text_widget

  for widget in window.winfo_children():
      widget.place_forget()
  
  display_date.pack_forget()
  all_rights.pack_forget()

  label.config(text="About", font=("Arial", 40, 'bold'))
  label.place(x=470, y=80)

  text_widget = tk.Text(window, wrap="word", width=90, height=17, font=("Helvetica", 15), bg="#1C1C1C", fg="white", padx=30, pady=30)
  text_widget.place(x=45 , y=170)

  paragraph = """Welcome to NBA Stats Scraper! Here, you will find pre-season statistics that highlight the top teams in offense and defense for the on going NBA Season, along with overall insights into the games of each basketball teams.\n\nWe used web scraping techniques to collect all the needed data and imported the Pandas library to manage and analyze it effectively. With this method, we make sure that the predictions from the collected data are accurate for predicting the NBA Season games.\n\nWe will provide and show you all the important data to help you understand which teams are strong contenders this season. Get ready for an exciting ride as we uncover the challenges and surprises of the upcoming NBA Season!\n\nDeveloper:\nMartinez, Joanna Mae\nEnriquez, Andreiy\nZamora, Kurt\nOlmedo, Mark Nathan\nPalatino, Raymond Charles"""
  text_widget.insert("1.0", paragraph)

  # Make the Text widget read-only
  text_widget.config(state="disabled")

  home_button = Button(text="Home", padx=20, pady=3, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
  home_button.bind("<Enter>", on_enter)
  home_button.bind("<Leave>", on_leave)
  home_button.place(x=515, y=660)

main()
window.mainloop()
