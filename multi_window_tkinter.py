from tkinter import *
from tkinter import ttk
import uuid
import json

global my_data_list
global currentRowIndex

my_data_list    = []


root = Tk()
root.title('List of Friends')
root.geometry("1278x720")
root.configure(bg='LightBlue')


input_frame = LabelFrame(root,text='Info',bg="lightgray",font=('Consolas',14))
input_frame.grid(row=0,column=0,rowspan=5,columnspan=4)


l1 = Label(input_frame,           anchor="w",           width=24,
           height=1,              relief="ridge",       text="ID",          
           font=('Consolas',14)   ).grid(row=1, column=0)

l2 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="First Name",       
           font=('Consolas',14)   ).grid(row=2, column=0)

l3 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="Last Name", 
           font=('Consolas',14)   ).grid(row=3, column=0) 


l4 = Label(input_frame,           anchor="w",           width=24, 
           height=1,              relief="ridge",       text="Cell Phone", 
           font=('Consolas',14)   ).grid(row=4, column=0)



id_value = StringVar()
id_value.set(uuid.uuid4())

crm_id=Label(input_frame,           anchor="w",                 height=1,
           relief="ridge",          textvariable=id_value,      font=('Consolas',14))
crm_id.grid(row=1, column=1)

crm_fn      =Entry(input_frame,width=30,borderwidth=2,fg="black",font=('Consolas',14))
crm_fn.grid(row=2, column=1,columnspan=2)

crm_ln      =Entry(input_frame,width=30,borderwidth=2,fg="black",font=('Consolas',14))
crm_ln.grid(row=3, column=1,columnspan=2)

crm_cellphone=Entry(input_frame,width=30,borderwidth=2,fg="black",font=('Consolas',14))
crm_cellphone.grid(row=4, column=1,columnspan=2)








trv =ttk.Treeview(root, columns=(1,2,3,4),show="headings",height="16")
trv.grid(row=11,column=0, rowspan=16,columnspan=4)

trv.heading(1,text="ID", anchor="center")
trv.heading(2,text="First Name", anchor="center")
trv.heading(3,text="Last Name", anchor="center")
trv.heading(4,text="Cell Phone", anchor="center")

trv.column("#1",anchor="w",width=270, stretch=True)
trv.column("#2",anchor="w", width=140, stretch=False)
trv.column("#3",anchor="w", width=140, stretch=False)
trv.column("#4",anchor="w", width=140, stretch=False)








# --review=s
def load_json_from_file():
    global my_data_list
    with open("c:\\tmp\\amigos.json","r") as file_handler:
	    my_data_list = json.load(file_handler)
    file_handler.close
    print('file has been read and closed')


# --review=s
def save_json_to_file():
    global my_data_list
    with open("c:\\tmp\\amigos.json", "w") as file_handler:
        json.dump(my_data_list, file_handler, indent=4)
    file_handler.close
    print('file has been written to and closed')



# --review=s
def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)
    

# --review=s
def load_trv_with_json():
    global my_data_list

    remove_all_data_from_trv()

    rowIndex=1

    for key in my_data_list:
	    guid_value = key["id"]
	    first_name = key["first_name"]
	    last_name = key["last_name"]
	    cell_phone = key["cell_phone"]

	    trv.insert('',index='end',iid=rowIndex,text="",
                        values=(guid_value,first_name, last_name, cell_phone))    
	    rowIndex=rowIndex+1


# --review=Y
def clear_all_fields():
    crm_fn.delete(0,END)
    crm_ln.delete(0,END)
    crm_cellphone.delete(0,END)
    crm_id.configure(text="")
    crm_fn.focus_set()
    id_value.set(uuid.uuid4())
    change_background_color("#FFFFFF")
    

# --review=Y
def find_row_in_my_data_list(guid_value):
    global my_data_list
    row     = 0
    found   = False

    for rec in my_data_list:
        if rec["id"] == guid_value:
            found = True
            break
        row = row+1

    if(found==True):
        return(row)

    return(-1)


# --review=Y
def change_background_color(new_color):
    crm_fn.config(bg=new_color)
    crm_ln.config(bg=new_color)
    crm_cellphone.config(bg=new_color)
 

# --review=Y
def change_enabled_state(state):

    if state == 'Edit':
        btnUpdate["state"]="normal"
        btnDelete["state"]="normal"
        btnAdd["state"]="disabled"
    elif state=='Cancel':
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="disabled"
    else:
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="normal"


# --review=Y
def load_edit_field_with_row_data(_tuple):
    if len(_tuple)==0:
        return;

    id_value.set(_tuple[0]);
    crm_fn.delete(0,END)
    crm_fn.insert(0,_tuple[1])
    crm_ln.delete(0,END)
    crm_ln.insert(0,_tuple[2])
    crm_cellphone.delete(0,END)
    crm_cellphone.insert(0,_tuple[3])


# --review=Y
def cancel():
    clear_all_fields()
    change_enabled_state('New')


# --review=Y
def print_all_entries():
    global my_data_list

    for rec in my_data_list:
        print(rec)

    crm_fn.focus_set();



# --review=Y
def add_entry():
    guid_value = id_value.get()
    first_name = crm_fn.get()
    last_name = crm_ln.get()
    cell_phone = crm_cellphone.get()

    if len(first_name)==0:
        change_background_color("#FFB2AE")
        return

    process_request('_INSERT_',guid_value,first_name,last_name,cell_phone)


# --review=Y
def update_entry():
    guid_value = id_value.get()
    first_name = crm_fn.get()
    last_name = crm_ln.get()
    cell_phone = crm_cellphone.get()

    if len(first_name)==0:
        change_background_color("#FFB2AE")
        return

    process_request('_UPDATE_',guid_value,first_name,last_name,cell_phone)



# --review=Y
def delete_entry():
    guid_value = id_value.get()
    process_request('_DELETE_',guid_value,None,None,None)
 


# --review=Y
def process_request(command_type,guid_value,first_name,last_name, cell_phone):
    global my_data_list

    if command_type == "_UPDATE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            dict = {"id":guid_value, "first_name":first_name, 
                    "last_name":last_name, "cell_phone":cell_phone}
            my_data_list[row]=dict

    elif command_type == "_INSERT_":
        dict = {"id":guid_value, "first_name":first_name, 
                "last_name":last_name, "cell_phone":cell_phone}
        my_data_list.append(dict)

    elif command_type == "_DELETE_":
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            del my_data_list[row];

    save_json_to_file();
    load_trv_with_json();
    clear_all_fields();


# --review=Y
def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex,'values'))
    load_edit_field_with_row_data(lastTuple)

    change_enabled_state('Edit')


# --review=Y
trv.bind("<ButtonRelease>",MouseButtonUpCallBack)


# --review=
ButtonFrame = LabelFrame(root,text='',bg="lightgray",font=('Consolas',14))
ButtonFrame.grid(row=5,column=0,columnspan=6)

##save=Button(root,text="Save",padx=20,pady=10,command=Save)
btnShow=Button(ButtonFrame,text="Print",padx=20,pady=10,command=print_all_entries)
btnShow.pack(side=LEFT)

btnAdd=Button(ButtonFrame,text="Add",padx=20,pady=10,command=add_entry)
btnAdd.pack(side=LEFT)

btnUpdate=Button(ButtonFrame,text="Update",padx=20,pady=10,command=update_entry)
btnUpdate.pack(side=LEFT)

btnDelete=Button(ButtonFrame,text="Delete",padx=20,pady=10,command=delete_entry)
btnDelete.pack(side=LEFT)


btnClear=Button(ButtonFrame,text="Cancel",padx=18,pady=10,command=cancel)
btnClear.pack(side=LEFT)

btnExit=Button(ButtonFrame,text="Exit",padx=20,pady=10,command=root.quit)
btnExit.pack(side=LEFT)


# --review=Y
load_json_from_file()
load_trv_with_json()

crm_fn.focus_set();
root.mainloop()