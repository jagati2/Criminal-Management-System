from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1920x1080+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar () 
        self.var_name=StringVar() 
        self.var_nickname=StringVar() 
        self.var_arrest_date=StringVar() 
        self.var_date_of_crime=StringVar() 
        self.var_address=StringVar() 
        self.var_age=StringVar() 
        self.var_occupation=StringVar() 
        self.var_birthMark=StringVar() 
        self.var_crime_type=StringVar () 
        self.var_father_name=StringVar() 
        self.var_gender=StringVar() 
       

        lb_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lb_title.place(x=0,y=0,width=1400,height=40)
    


        # Img_Frame
        img_frame=Frame (self.root, bd=2, relief=RIDGE, bg= 'white')
        img_frame. place(x=0,y=40,width=1400, height=130)
        img1=Image.open( 'Images/cops2.jpg')
        img1=img1.resize((450,160), Image.LANCZOS)

        self. photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label (img_frame, image=self.photo1)
        self.img_1. place(x=0,y=0, width=450, height=160)


        # Img_2
        
        img2=Image.open( 'Images/cops1.jpg')
        img2=img2.resize((450,160), Image.LANCZOS)

        self. photo2=ImageTk.PhotoImage(img2)
        self.img_2=Label (img_frame, image=self.photo2)
        self.img_2. place(x=450,y=0, width=450, height=160)

        #img3
        img3=Image.open( 'Images/cops3.jpg')
        img3=img3.resize((450,160), Image.LANCZOS)

        self. photo3=ImageTk.PhotoImage(img3)
        self.img_3=Label (img_frame, image=self.photo3)
        self.img_3.place(x=900,y=0, width=450, height=160)

       

        #MainFrame

        Main_frame=Frame (self.root, bd=2, relief=RIDGE, bg= 'white')
        Main_frame.place(x=3,y=160, width=1300, height=520)
        

        #upper frame

        upper_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='green', bg= 'white')
        upper_frame. place(x=10,y=10, width=1280,height=300)

        #lower frame

        down_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='blue', bg= 'white')
        down_frame. place(x=10,y=250, width=1300,height=200)

        search_frame=LabelFrame(down_frame, bd=2, relief=RIDGE,text='Search Record',font=('times new roman',11,'bold'),fg='red', bg= 'white')
        search_frame. place(x=0,y=0, width=1270,height=50)

        
        search_by=Label(search_frame, font=("arial", 8, "bold"), text="Search by: ", bg="red") 
        search_by.grid(row=0,column=0, sticky=W, padx=1)


        search_txt=ttk.Entry(search_frame, width=18, font=("arial",9,"bold")) 
        search_txt.grid(row=0, column=2, sticky=W, padx=1) 
        # search button 
        btn_search=Button (search_frame,command=self.search_data, text='Search', font=("arial", 9,"bold"), width=14,bg='blue') 
        btn_search.grid(row=0, column=3,padx=1, pady=5) 
        # all button 
        btn_all=Button(search_frame,command=self.fetch_data, text= 'Show All', font=("arial", 9, "bold"), width=14, bg='blue') 
        btn_all.grid(row=0, column=4, padx=1, pady=4)

        table_frame=Frame (down_frame, bd=2,relief=RIDGE) 
        table_frame.place(x=0,y=50,width=1250,height=120) 
        # Scroll bar 
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL) 
        self.criminal_table=ttk.Treeview(table_frame, column=("1","2","3","4","5","6","7","8","9","10","11","12","13"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.criminal_table.xview) 
        scroll_y.config(command=self.criminal_table.yview) 

        self.criminal_table.heading("1", text='CaseId')
        self.criminal_table.heading ("2", text="CrimeNo") 
        self.criminal_table.heading("3", text="Criminal Name") 
        self.criminal_table.heading ("4",text="NickName") 
        self.criminal_table.heading("5",text="ArrestDate") 
        self.criminal_table.heading("6", text="CrimeOfDate") 
        self.criminal_table.heading("7", text="Address") 
        self.criminal_table.heading("8", text="Age") 
        self.criminal_table.heading ("9", text="Occupation") 
        self.criminal_table.heading ("10",text="Birth Mark") 
        self.criminal_table.heading("11",text="Crime Type") 
        self.criminal_table.heading("12", text="Father Name")
        self.criminal_table.heading("13", text="Gender") 


        self.criminal_table['show']='headings'
        self.criminal_table.column("1",width=100) 
        self.criminal_table.column("2",width=100) 
        self.criminal_table.column("3",width=100) 
        self.criminal_table.column("4",width=100) 
        self.criminal_table.column("5",width=100) 
        self.criminal_table.column("6",width=100) 
        self.criminal_table.column("7",width=100) 
        self.criminal_table.column("8",width=100) 
        self.criminal_table.column("9",width=100) 
        self.criminal_table.column("10",width=100) 
        self.criminal_table.column("11",width=100) 
        self.criminal_table.column("12",width=100) 
        self.criminal_table.column("13",width=100) 
        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

        self.var_com_search=StringVar()
        self.var_search=StringVar()
        combo_search_box=ttk.Combobox (search_frame, font=("arial",9, "bold"),width=16,state='readonly') 
        combo_search_box['value']=('Select Option', 'Case_id','Criminal_no') 
        combo_search_box.current(0) 
        combo_search_box.grid(row=0,column=1, sticky=W, padx=1)

          #bcakground right side image 
        img_crime=Image.open('images/xyz.jpg') 
        img_crime=img_crime.resize((470, 245), Image.LANCZOS) 
        self.photocrime=ImageTk.PhotoImage(img_crime) 
        self.img_crime=Label(upper_frame, image=self.photocrime) 
        self.img_crime.place(x=800, y=0,width=470,height=245)


        #labesl entry
        #case id
        caseid= Label (upper_frame,text='CASE ID:',font=('arial',9,'bold'), bg= 'white')
        caseid.grid (row=0,column=0,padx=1,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id, width=22, font=('arial', 9, 'bold'))
        caseentry.grid(row=0,column=1,padx=1,sticky=W)
        
        #CRIMINAL NO
        label_criminalNo= Label (upper_frame,text='Criminal NO:',font=('arial',9,'bold'), bg= 'white')
        label_criminalNo.grid (row=0,column=2,padx=1,sticky=W,pady=7)

        txt_criminalNo=ttk.Entry(upper_frame,textvariable=self.var_criminal_no, width=22, font=('arial', 9, 'bold'))
        txt_criminalNo.grid(row=0,column=3,padx=1,pady=7)
        
    
        # Criminal Name 
        lbl_Name=Label(upper_frame, font=("arial", 9, "bold"), text="Criminal Name : ",bg="white") 
        lbl_Name.grid(row=1, column=0, sticky=W, padx=1, pady=7) 
        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=("arial" ,9,"bold")) 
        txt_Name.grid(row=1, column=1, sticky=W, padx=1, pady=7) 
        # NickName 
        lbl_nickname=Label (upper_frame, font=("arial", 9, "bold"), text="NickName : ",bg="white") 
        lbl_nickname.grid(row=1, column=2, padx=1,sticky=W,pady=7) 

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22, font=("arial" ,9,"bold"))  
        txt_nickname.grid(row=1,column=3, padx=1, pady=7) 
        # Arrest Date 
        lbl_arrestDate=Label(upper_frame, font=("arial", 9, "bold"), text="Arrest Date : ",bg="white") 
        lbl_arrestDate.grid (row=2, column=0, sticky=W, padx=1, pady=7) 
        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font=("arial" ,9,"bold")) 
        txt_arrestDate.grid (row=2, column=1, padx=1, pady=7) 
        # Date of Crime 
        lbl_dateOfCrime=Label (upper_frame, font=("arial", 9, "bold"), text="Date of Crime : ",bg="white") 
        lbl_dateOfCrime.grid(row=2, column=2,sticky=W, padx=1,pady=7) 
        txt_dateOfCrime=ttk. Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=("arial" ,9,"bold")) 
        txt_dateOfCrime.grid(row=2, column=3, sticky=W, padx=1, pady=7) 

        # Address 
        lbl_address=Label (upper_frame, font=("arial", 9, "bold"), text="Address : ", bg="white") 
        lbl_address.grid(row=3,column=0,sticky=W, padx=1, pady=7) 
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial" ,9,"bold")) 
        txt_address.grid (row=3, column=1, padx=1, pady=7) 
        # Age 
        lbl_age=Label(upper_frame, font=("arial", 9, "bold"), text="Age : ", bg="white")  
        lbl_age.grid(row=3, column=2, sticky=W, padx=1, pady=7) 
        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age, font=("arial" ,9,"bold")) 
        txt_age.grid(row=3, column=3, padx=1,pady=7) 
        # occupution 
        lbl_occupution=Label(upper_frame, font=("arial", 9, "bold"), text="Occupation : ",bg="white" )
                            
        lbl_occupution.grid(row=4, column=0, sticky=W, padx=1,pady=7)
        txt_occupution=ttk. Entry(upper_frame,textvariable=self.var_occupation, width=22, font=("arial", 9, "bold")) 
        txt_occupution.grid(row=4, column=1, padx=1, pady=7) 
        #birthMark 
        lbl_birthmark=Label (upper_frame, font=("arial", 9, "bold"), text="Birth Mark : ",bg="white" ) 
        lbl_birthmark.grid (row=4, column=2, sticky=W, padx=1, pady=7) 
        txt_birthmark=ttk. Entry(upper_frame,textvariable=self.var_birthMark, width=22, font=("arial", 9, "bold")) 
        txt_birthmark.grid (row=4, column=3, sticky=W, padx=1, pady=7) 
       # Crime Type 
        lbl_crimeType=Label (upper_frame, font=("arial", 9, "bold"), text="Crime Type : ",bg="white" ) 
        lbl_crimeType.grid(row=0, column=4, sticky=W, padx=1, pady=7)
        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font=("arial", 9, "bold"))
        txt_crimeType.grid (row=0, column=5, padx=1, pady=7) 


        # Father Name 
        lbl_fatherName=Label(upper_frame, font=("arial", 9, "bold"), text="Father's Name : ",bg="white" ) 
        lbl_fatherName.grid(row=1,column=4, sticky=W, padx=1,pady=7) 
        txt_fatherName=ttk. Entry(upper_frame,textvariable=self.var_father_name,width=22, font=("arial",9,"bold")) 
        txt_fatherName.grid(row=1,column=5, padx=1, pady=7)

        # gender 
        lbl_gender=Label(upper_frame, font=("arial", 9, "bold"), text="Gender : ", bg="white") 
        lbl_gender.grid(row=2,column=4,sticky=W, padx=1, pady=7) 
       
        # Rdio Button gender 
        radio_frame_gender=Frame (upper_frame, bd=2,relief=RIDGE, bg='white') 
        radio_frame_gender.place(x=600,y=80,width=140, height=30)
        male=Radiobutton(radio_frame_gender,variable=self.var_gender, text="Male",value='male',font=("arial", 8, "bold"),bg='white')
        male.grid(row=0, column=0, pady=1, padx=1, sticky=W) 
        self.var_gender.set('male')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender, text="Female",value='female',font=("arial", 8, "bold"),bg='white')
        female.grid(row=0, column=1, pady=1, padx=1, sticky=W) 

    

       

    

        # Buttons 
        button_frame=Frame (upper_frame, bd=2, relief=RIDGE, bg="white") 
        button_frame.place(x=5, y=170,width=620,height=45) 
        
        # add button 
        btn_add=Button(button_frame, command=self.add_data,text="Record Save", font=("arial", 10, "bold"), width=14,bg='blue',fg='white' )
        btn_add.grid(row=0, column=0, padx=2,pady=4 )

          # update button 
        btn_update=Button(button_frame,command=self.update_data,text="Update", font=("arial", 10, "bold"), width=14,bg='blue',fg='white' )
        btn_update.grid(row=0, column=1, padx=2,pady=4 )

          # delete button 
        btn_delete=Button(button_frame,command=self.delete_data, text="Delete", font=("arial", 10, "bold"), width=14,bg='blue',fg='white' )
        btn_delete.grid(row=0, column=2, padx=2,pady=4 )

          # clear button 
        btn_clear=Button(button_frame,command=self.clear_data, text="Clear", font=("arial", 10, "bold"), width=14,bg='blue',fg='white' )
        btn_clear.grid(row=0, column=3, padx=2,pady=4 )


    # Add function
    def add_data(self):
      if self.var_case_id.get() =="":
        messagebox.showerror('Error', 'All Fields are required')
      else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Test@123',
                                           database='criminal_management')
            my_cursor = conn.cursor()

            # Add the missing %s in the SQL query parameters
            my_cursor.execute(
                'INSERT INTO criminal1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get()
                    
                ))

            conn.commit()
            self.fetch_data()
            self.clear_data()
            conn.close()
            messagebox.showinfo('Success', 'Criminal record has been added')
        except Exception as es:
            messagebox.showerror('Error', f'Due to {str(es)}')


    # fetch data 
    def fetch_data(self) : 
        conn=mysql.connector.connect (host='localhost',username='root',password='Test@123',database='criminal_management') 
        my_cursor=conn.cursor() 
        my_cursor.execute('select * from criminal1')
        data=my_cursor.fetchall() 
        if len(data)!=0 : 
          self.criminal_table.delete(*self.criminal_table.get_children()) 
          for i in data : 
            self.criminal_table.insert('', END, values=i) 
            conn.commit() 
        conn.close()

    # get cursor 
    def get_cursor(self,event="") : 
      cursur_row=self.criminal_table.focus() 
      content=self.criminal_table.item(cursur_row) 
      data=content ['values']
      
      self.var_case_id.set(data[0]) 
      self.var_criminal_no.set(data[1]) 
      self.var_name.set(data[2]) 
      self.var_nickname.set(data[3]) 
      self.var_arrest_date.set (data[4]) 
      self.var_date_of_crime.set (data[5]) 
      self.var_address.set(data[6]) 
      self.var_age.set(data[7]) 
      self.var_occupation.set(data[8]) 
      self.var_birthMark.set(data[9]) 
      self.var_crime_type.set(data[10]) 
      self.var_father_name.set(data[11]) 
      self.var_gender.set(data[12])
    #update function
    def update_data(self) : 
       if self.var_case_id.get()=="":
          messagebox.showerror('Error', 'All Fields are required') 
       else : 
          try : 
            update=messagebox.askyesno('Update', 'Are you sure you want to update ')
            if update>0 : 
                conn=mysql.connector.connect(host='localhost', username='root', password="Test@123",database='criminal_management')  
                my_cursor=conn.cursor() 
                my_cursor.execute('update criminal1 set Criminal_no=%s,Criminal_name=%s , Nick_name=%s, arrest_date=%s, dateOfcrime= %s, address =%s, age=%s, occupation=%s, BirthMark=%s, crimeType=%s, fatherName=%s, gender= %s where Case_id=%s',(
                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                         self.var_criminal_no.get(), 
                                                                                                                                                                                                                                                         self.var_name.get(), 
                                                                                                                                                                                                                                                         self.var_nickname.get(),
                                                                                                                                                                                                                                                         self.var_arrest_date.get(), 
                                                                                                                                                                                                                                                         self.var_date_of_crime.get(), 
                                                                                                                                                                                                                                                         self.var_address.get(), 
                                                                                                                                                                                                                                                         self.var_age.get(), 
                                                                                                                                                                                                                                                         self.var_occupation.get(), 
                                                                                                                                                                                                                                                         self.var_birthMark.get(), 
                                                                                                                                                                                                                                                         self.var_crime_type.get(), 
                                                                                                                                                                                                                                                         self.var_father_name.get(), 
                                                                                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                                                                                         self.var_case_id.get() 
                                                                                                                                                                                                                                                        ))           


            else : 
              if not update:
                 return 
            conn.commit() 
            self.fetch_data() 
            self.clear_data()
            conn.close()  
            messagebox.showinfo('success','Record successfully updated')                                                                                                                                                                                                                                           
          except Exception as es:
                  Message.showerror('Error',f'Due to{str(es)}')       

    def delete_data(self):
       if self.var_case_id.get()=="" : 
        messagebox.showerror('Error', 'All Fields are required') 
       else: 
           try: 
              Delete=messagebox.askyesno('Delete', 'Are you sure you want to delete this record') 
              if Delete>0 : 
                 conn=mysql.connector.connect(host='localhost', username='root', password="Test@123",database='criminal_management')  
                 my_cursor=conn.cursor() 
                 sql='delete from criminal1 where Case_id=%s'
                 value=(self.var_case_id.get(),)   
                 my_cursor.execute(sql,value)                                                                             
              else:
                 if not Delete:
                    return
              conn.commit()
              self.fetch_data()
              self.clear_data()
              conn.close()
              messagebox.showinfo('success','Record successfully deleted')                                                                                                                                                                                                                                           
           except Exception as es:
                  Message.showerror('Error',f'Due to{str(es)}')


    # clear
    def clear_data(self) : 
       self.var_case_id.set("") 
       self.var_criminal_no.set("") 
       self.var_name.set("") 
       self.var_nickname.set("") 
       self.var_arrest_date.set("") 
       self.var_date_of_crime.set("")
       self.var_address.set("")
       self.var_age.set("")
       self.var_occupation.set("")
       self.var_birthMark.set("")
       self.var_crime_type.set("")
       self.var_father_name.set("") 
       self.var_gender.set("") 

       #search             
    def search_data(self):
       if self.var_com_search.get()=="":
          messagebox.showerror('Error','All fields are required')
       else:
          try:
             conn=mysql.connector.connect(host='localhost', username='root', password="Test@123",database='criminal_management')  
             my_cursor=conn.cursor()
             my_cursor.execute('select * from criminal1 where'+str(self.var_com_search.get())+"LIKE'%"+str(self.var_search()+"%'"))   
             rows=my_cursor.fetchall()
             if len(rows)!=0 : 
              self.criminal_table.delete(*self.criminal_table.get_children()) 
              for i in rows : 
                self.criminal_table.insert("",END, values=i) 
             conn.commit() 
             conn.close()
          except Exception as es:
                  Message.showerror('Error',f'Due to{str(es)}')


if __name__== "__main__":        
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
