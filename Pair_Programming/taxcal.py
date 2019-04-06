
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('500x200')

class Window(Frame):
   def __init__(self, master=None):
       Frame.__init__(self, master)
       self.master = master
       self.init_window()
             
   
  
    
   def init_window(self):
       def message():
           def select():
               selection = var.get()
               if selection == 1:
                   cal()
               elif selection ==2 :
                   cal1()

           def cal1():
               sf_income = ""
               sp_income = ""
               if sf_ey.get() == "":
                   messagebox.showinfo("Error","Please type in self income.")
                   return;
               else:
                   sf_income = int(sf_ey.get())

               if sp_ey.get() == "":
                   messagebox.showinfo("Error","Please type in spouse income.")
                   return;
               else:
                   sp_income = int(sp_ey.get())

               join_income = int(sf_income)+int(sp_income)
               allowance = 132000
               allowance1= 132000
               allowance2= 264000
               mpf_mc = 0
               mpf_mc1 =0
               join_mc = 0
               result = ""
               # if sf_income > allowance:
               if sf_income / 12 < 7100:
                   mpf_mc = 0
               elif sf_income / 12 > 7100 and sf_income/12 <= 30000:
                    mpf_mc = sf_income * 0.05
               else:
                    mpf_mc = 18000

               print(str(mpf_mc))
               sf_mpf= int(mpf_mc)
               net_char = sf_income-allowance-sf_mpf
               # print(net_char)
               # else :
               #     net_char =0
                   # print(net_char)

               if net_char < 0:
                   net_char =0

               # if sp_income > allowance:

               if sp_income / 12 < 7100:
                   mpf_mc1 = 0
               elif sp_income / 12 <= 30000:
                   mpf_mc1 = sp_income * 0.05
               else:
                   mpf_mc1 = 18000

               sp_mpf = int(mpf_mc1)
               net_char1 = sp_income-allowance1-sp_mpf
               # print(net_char1)
               # else:
               #     net_char1=0
               # print(net_char1)

               if net_char1 < 0:
                   net_char1 = 0

               print(mpf_mc)
               print(mpf_mc1)

               join_mc = mpf_mc+mpf_mc1
               # print(mpf_mc)
               # print(mpf_mc1)
               # print(join_mc)
               join_net_char = join_income - allowance2- join_mc
               # print(join_net_char)

               if join_net_char <0:
                   join_net_char = 0
               # print(join_net_char)
               # return c

               def tax1():
                   join_tax = 0
                   sf_stat = ""
                   sp_stat = ""
                   stat = ""
                   if net_char <= 50000:
                       tax_val1 = net_char*0.02
                   elif net_char <= 100000:
                       tax_val1 = 1000 + (net_char-50000)*0.06
                   elif net_char <= 150000:
                        tax_val1 = 4000 + (net_char-100000)*0.1
                   elif net_char <= 200000:
                        tax_val1 = 9000 + (net_char-150000)*0.14
                   else:
                        tax_val1 = 16000 + (net_char-200000)*0.17

                   tax_val1s = (net_char+allowance) *0.15
                   if tax_val1s < tax_val1:
                       tax_val1 = tax_val1s
                       sf_stat = "*"


                   if net_char1 <= 50000:
                       tax_val2 = net_char1*0.02
                   elif net_char1 <= 100000:
                       tax_val2 = 1000 + (net_char1-50000)*0.06
                   elif net_char1 <= 150000:
                        tax_val2 = 4000 + (net_char1-100000)*0.1
                   elif net_char1 <= 200000:
                        tax_val2 = 9000 + (net_char1-150000)*0.14
                   else:
                        tax_val2 = 16000 + (net_char1-200000)*0.17

                   tax_val2s = (net_char1 + allowance1)*0.15
                   if tax_val2s < tax_val2:
                       tax_val2 = tax_val2s
                       sp_stat = "*"

                   if join_net_char <= 50000:
                       join_tax = join_net_char*0.02
                   elif join_net_char <= 100000:
                       join_tax = 1000 + (join_net_char-50000)*0.06
                   elif join_net_char <= 150000:
                        join_tax = 4000 + (join_net_char-100000)*0.1
                   elif join_net_char <= 200000:
                        join_tax = 9000 + (join_net_char-150000)*0.14
                   else:
                        join_tax = 16000 + (join_net_char-200000)*0.17

                   # print(join_net_char)
                   # print(join_tax)
                   join_taxs = (join_net_char + allowance2) *0.15
                   if join_taxs < join_tax:
                       join_tax = join_taxs
                       stat= "*"

                   joint = int(join_tax)

                   # print(tax_val1)
                   # print(tax_val2)
                   # print(join_tax)

                   totaltax =tax_val1+tax_val2

                   if int(totaltax) < joint:
                       result = "Separate Taxation is recommended."
                   elif totaltax > joint:
                       result = "Joint assessment is recommended."
                   else:
                       result = "Both method have same result."

                   return int(totaltax), int(tax_val1), int(tax_val2), int(joint), str(result), str(sf_stat), str(sp_stat),str(stat)

               tax1()
               messagebox.showinfo("Separate Assessment",'Self Income: '+str(sf_income)+'\n'+'Spouse Income: '+str(sp_income)+'\n'
                                   +"Self Mandatory Contributions: "+str(int(mpf_mc))+'\n'+
                                   "Spouse Mandatory Contributions: "+str(int(mpf_mc1))+'\n'+
                                   "Self Net chargable income: "+str(net_char)+'\n'
                                   +"Spouse Net chargable income: "+str(net_char1)+'\n'
                                   +"Self Tax:  " +str(tax1()[1])+str(tax1()[5])+'\n'
                                   +"Spouse Tax:  " +str(tax1()[2])+str(tax1()[6])+'\n'
                                   +"Total Tax: "+str(tax1()[0]))
               messagebox.showinfo("Joint Assessment",
                                   'Total Income: ' + str(int(join_income)) + '\n' + "MPF Mandatory Contributions: " + str(int(join_mc))
                                   + '\n' + "Net chargable income: " + str(int(join_net_char)) + '\n' + "Total Tax: " + str(tax1()[3])+str(tax1()[7]))
               messagebox.showinfo("Result",tax1()[4])

           def cal():
               sf_mpf = ""
               sf_income = ""
               if sf_ey.get() == "":
                   messagebox.showinfo("Error", "Please type in self income.")
                   return;
               else:
                   sf_income = int(sf_ey.get())

               allowance = 132000
               mpf_mc = 0
               sf_net_char = 0
               # if sf_income > allowance:
               if sf_income / 12 < 7100:
                   mpf_mc = 0
               elif sf_income / 12 <= 30000:
                   mpf_mc = sf_income * 0.05
               else:
                   mpf_mc = 18000

               # print(mpf_mc)
               sf_mpf= int(mpf_mc)
               # print(sf_mpf)
               sf_net_char = sf_income-allowance-sf_mpf

               if sf_net_char < 0:
                   sf_net_char = 0
                   # print(sf_net_char)


               def tax():
                   sf_stat = ""
                   if sf_net_char <= 50000:
                       tax_val = sf_net_char*0.02
                   elif sf_net_char <= 100000:
                       tax_val = 1000 + (sf_net_char-50000)*0.06
                   elif sf_net_char <= 150000:
                        tax_val = 4000 + (sf_net_char-100000)*0.1
                   elif sf_net_char <= 200000:
                        tax_val = 9000 + (sf_net_char-150000)*0.14
                   else:
                        tax_val = 16000 + (sf_net_char-200000)*0.17
                   if tax_val < 0:
                       tax_val = 0

                   tax_vals = (sf_net_char + allowance) * 0.15
                   if tax_vals < tax_val:
                       tax_val = tax_vals
                       sf_stat = "*"


                   # print(tax_val)
                   return  int(tax_val), int(sf_net_char), str(sf_stat)

               tax()
               messagebox.showinfo("Information",'Income:'+str(sf_income)+'\n'+"MPF 'Mandatory Contributions:"+str(sf_mpf)+'\n'+"Net chargable income:"+str(tax()[1])+'\n'+"Tax is " +str(tax()[0])+str(tax()[2]))


           select()



       def clear():
           sf_ey.delete(0, END)
           sf_ey.insert(END,'0')
           sp_ey.delete(0, END)
           sp_ey.insert(END,'0')
       def sel():
           selection=var.get()
           if selection==1:
               sp_ey.config(state='disable')
           else:
               sp_ey.config(state='normal')
               
             
       self.master.title('MPF Page')
       self.pack(fill=BOTH, expand=1)
       self.config(bg='cyan')

       marital_lb = Label(self, text="Marital Status", height=1, width=10, bg="cyan")
       marital_lb.place(x=3, y=10)
       marital_lb.config(font=(15))

       var = IntVar()
       R1= Radiobutton(self, text="Single/Separated/Divorced/Widowed", variable=var, value=1,bg="cyan",command=sel)
       R1.place(x=3,y=30)
       var.set(1)
       R2 = Radiobutton(self, text="Married", variable=var, value=2,bg="cyan",command=sel)
       R2.place(x=250,y=30)

       sf_lb = Label(self, text="Self income (for year)", height=1, width=16, bg="cyan")
       sf_lb.place(x=3, y=60)
       sf_lb.config(font=(15))
       sf_ey = tk.Entry(self, width=20, bd=3)
       sf_ey.place(x=200, y=60)

       sp_lb = Label(self, text="Spouse income (for year)", height=1, width=19, bg="cyan")
       sp_lb.place(x=3, y=90)
       sp_lb.config(font=(15))
       sp_ey = tk.Entry(self, width=20, bd=3)
       sp_ey.place(x=200, y=90)
       sp_ey.config(state='disable')

       submit_bt = Button(self, text="Submit", height=1, width=10,command=message)
       submit_bt.place(x=400, y=130)

       clear_bt = Button(self, text="Clear", height=1, width=10,command=clear)
       clear_bt.place(x=300, y=130)





       

       


       

app = Window(root)
root.mainloop()
