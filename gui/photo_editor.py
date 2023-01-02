import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


root = tk.Tk()
root.title("Basic GUI Layout")
root.maxsize(900, 600)
root.config(background="skyblue")

# create left and right frames
left_frame = tk.Frame(root, width=200, height=400, bg="grey")
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(root, width=650, height=400, bg="grey")
right_frame.grid(row=0, column=1, padx=10, pady=5)

# create frames and labels in the left_frame
tk.Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = tk.PhotoImage(file="gui/8899da2f65fb5a3731ca6c7c29901f11.gif")
original_image = image.subsample(3,3)  # resize image using subsample
tk.Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# display the iamge in right_frame
tk.Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5) 

# create tool bar frame
tool_bar = tk.Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# example labels that serve as placeholders for other widgets
tk.Label(tool_bar, text="Tools", relief="raised").grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
tk.Label(tool_bar, text="Filters", relief="raised").grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
tk.Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
tk.Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
tk.Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
tk.Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
tk.Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

root.mainloop()