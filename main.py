import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sao_check as ps4
import pc as PC


def from_pc_to_ps4():
    pc_path = filedialog.askopenfilename(title='Choose your PC save', initialfile='SaveData.sav')
    if not pc_path:
        return
    pc_data = open(pc_path, 'rb').read()
    pc_data_decrypted = PC.decrypt_file(pc_data)
    ps4_data = ps4.patch_save_pc(pc_data_decrypted)
    out_path = filedialog.asksaveasfilename(title='Save your New PS4 save', initialfile='ue4savegame.ps4.sav')
    if not out_path:
        return
    with open(out_path, 'wb') as f:
        f.write(ps4_data)
    messagebox.showinfo('Success', 'Save transferred to PS4 format!')


def from_ps4_to_pc():
    ps4_path = filedialog.askopenfilename(title='Choose your PS4 save', initialfile='ue4savegame.ps4.sav')
    if not ps4_path:
        return
    ps4_data = open(ps4_path, 'rb').read()
    pc_data = PC.encrypt_file(ps4_data)
    out_path = filedialog.asksaveasfilename(title='Save your New PC save', initialfile='SaveData.sav')
    if not out_path:
        return
    with open(out_path, 'wb') as f:
        f.write(pc_data)
    messagebox.showinfo('Success', 'Save transferred to PC format!')


root = tk.Tk()
root.title('Save Converter')
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

# Tab 1: PC → PS4
tab1 = ttk.Frame(notebook, padding=20)
notebook.add(tab1, text='PC → PS4')
ttk.Button(tab1, text='Convert PC Save to PS4', command=from_pc_to_ps4).pack()

# Tab 2: PS4 → PC
tab2 = ttk.Frame(notebook, padding=20)
notebook.add(tab2, text='PS4 → PC')
ttk.Button(tab2, text='Convert PS4 Save to PC', command=from_ps4_to_pc).pack()

root.mainloop()