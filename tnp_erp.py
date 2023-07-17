def login():
    section=0
    field=0
    user_name=int(input("ENTER USERID :"))
    if(user_name==1234):
        password=int(input("ENTER PASSWORD :"))
        if(password==9000):
            while(section!=5):
                print("SECTION 1:")
                print("FEE INFORMATION:")
                print("1. PAY FEE ONLINE")
                print("2. FEE RECEIPT")
                print("SECTION 2:")
                print("GENERAL INFORMATION:")
                print("1. YOUR PROFILE")
                print("2. QUESTION PAPER")
                print("3. NEWS / NOTICES")
                print("4. SYLLABUS")
                print("SECTION 3:")
                print("ACADEMIC:")
                print("1. ONLINE CLASS RECORDINGS")
                print("2. INTERNAL MARKS")
                print("3. CURRENT REPORT")
                print("SECTION 4:")
                print("COMPANY:")
                print("1. COMPANY CRITERIA")
                print("2. LIST OF COMPANY WE HAVE")
                print("3.LIST OF COMPANY YOU APPLY")
                print("SECTION 5:")
                print("EXIT")
                section=int(input("ENTER SECTION YOU CHOOSE :"))
                if section==1:
                    field=int(input("ENTER FIELD YOU CHOOSE :"))
                    if field ==1:
                        pay_fee()
                    elif field==2:
                        fee_receipt()
                    else:
                        print("INVALID INPUT")
                elif section==2:
                    field=int(input("ENTER FIELD YOU CHOOSE :"))
                    if field==1:
                        profile()
                    elif field==2:
                        paper()
                    elif field==3:
                        news()
                    elif field==4:
                        syllabus()
                    else:
                        print("INVALID INPUT")
                elif section==3:
                    field=int(input("ENTER FIELD YOU CHOOSE :"))
                    if field ==1:
                        online_class()
                    elif field==2:
                        marks()
                    elif field==3:
                        report()
                    else:
                        print("INVALID INPUT")
                elif section==4:
                    field=int(input("ENTER FIELD YOU CHOOSE :"))
                    if field ==1:
                        criteria()
                    elif field==2:
                        company()
                    elif field==3:
                        apply_company()
                    else:
                        print("INVALID INPUT")
                elif section==5:
                    print("THANK YOU FOR COMING")
                else:
                    print("INVALID INPUT")
        else:
            print("INVALID PASSWORD")
    else:
        print("INVALID USER NAME")
def pay_fee():
    root =Tk()
    root.geometry("344x634")
    photo=PhotoImage(file="tnpupi.png")
    ob=Label(image=photo)
    ob.pack()
    root.mainloop()
def fee_receipt():
    pass
def profile():
    con=my.connect(host = "localhost",user = "root", password="Shivam@123", database="tnp_students")
    cur =con.cursor()
    enrollment=input("ENTER YOUR ENROLLMENT NUMBER :")
    name=input("ENTER YOUR NAME :")
    dob=input("ENTER YOUR DATE OF BIRTH :")
    contect=input("ENTER YOUR CONTECT NUMBER :")
    email=input("ENTER YOUR EMAIL ID :")
    caddress=input("ENTER YOUR CURRENT ADDRESS :")
    cpin=input("ENTER YOUR CURRENT PINCODE :")
    paddress=input("ENTER YOUR PERMANENT ADDRESS :")
    ppin=input("ENTER YOUR PERMANENT PINCODE :")
    course=input("ENTER YOUR CURRENT COURSE :")
    branch=input("ENTER YOUR BRANCH :")
    ten=input("ENTER YOUR 10TH PERCENTAGE/C.G.P.A")
    twelve=input("ENTER YOUR 12TH PERCENTAGE/C.G.P.A")
    bachlor=input("ENTER YOUR BACHLOR PERCENTAGE/C.G.P.A")
    blood=input("ENTER YOUR BLOOD GROUP :")
    nationality=input("ENTER YOUR NATIONALITY :")
    fname=input("ENTER YOUR FATHER'S NAME :")
    fcontect=input("ENTER YOUR FATHER'S CONTECT NUMBER :")
    mname=input("ENTER YOUR MOTHER'S NAME :")    
    sql ="insert into student_info(enrollment,name,dob,contect,email,caddress,cpin,paddress,ppin,course,branch,ten,twelve,bachlor,blood,nationality,fname,fcontect,mname)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
    val=(name,city)
    cur.execute(sql,val)
    con.commit()
    print(cur.rowcount,"SAVED SUCCESSFULL")
def paper():
    pass
def news():
    print("PLACEMENT WILL STARTED ON AUGUST")
def syllabus():
    print("TREANING AND PLACEMENT PROGRAM")
    print("VERBAL ABILITY :")
    print("1. ARTICLES")
    print("2. NARRATION")
    print("3. NOUN")
    print("4. PRONOUN")
    print("5. VERB")
    print("6. TENSES ")
    print("7. ADVERB")
    print("8. ADJECTIVE")
    print("9. PREPOSITION")
    print("10. SBJECT VERB AGREEMENT")
    print("11. VOCABULARY")
    print("12. ANALOGY")
    print("13. READING COMPREHENSIONS")
    print("14. PARAJUMBLES")
    print("15. CRITICAL REASONING")
    print("16. FIJ")
    print("17. ESSAY WRITING")
    print("QUANTATATIVE APPTITUDE :")
    print("1.  NUMBER SYSTEM")
    print("2.  HCF-LCM")
    print("3.  AVERAGE AND AGES")
    print("4.  PERCENTAGE")
    print("5.  PROFIT AND LOSS")
    print("6.  SIMPLE INTREST AND COMPOUND INTREST")
    print("7.  RATIO AND PROPORTION")
    print("8.  MIXTURE AND ALLIGATIONS")
    print("9.  DATA INTERPRETATION")
    print("10. TIME AND WORK")
    print("11. TIME, SPEED AND DISTANCE")
    print("12. MENSURATION")
    print("13. SET THEORY")
    print("14. PERMUTATION AND COMBINATION")
    print("15. PROBABILITY")
    print("16. LOGARITHM")
    print("LOGICAL REASONING :")
    print("1.  CODING DECODING")
    print("2.  BLOOD RELATIONS")
    print("3.  DIRECTION SENSE")
    print("4.  SITTING ARRANGEMENT")
    print("5.  CUBE AND DICE")
    print("6.  CLOCKS AND CAKENDAR")
    print("7.  DATA SUFFICIENCY")
    print("8.  SYLLOGISM")
    print("9.  VENN DIAGRAM")
    print("10. ODD MAN OUT(SERISES)")
def online_class():
    print("WATCH VIDEOS FOR THIS LINK :")
    print("https://www.youtube.com/c/Youthmasters")

def marks():
    pass
def report():   
    pass
def criteria():
    print("OVERALL CRITERIA TO APPLY ANY COMPANY :")
    print("1. NO BACKLOGS")
    print("2. ABOVE 60% MARKS FOR OVERALL (10TH TO HIGHEST DEGREE)")
    print("3. 24 MONTHS EDUCATION GAP WILL CONSIDER")
    print("4. AT LEAST ONE PROJECT")
def company():
    print("COMPANY WE HAVE :")
    print("1.  Amazon")
    print("2.  GOOGLE")
    print("3.  MICROSOFT")
    print("4.  ORACLE")
    print("5.  INFOSYS")
    print("6.  TCS")
    print("7.  WIPRO")
    print("8.  HCL")
    print("9.  TECH MAHINDRA")
    print("10. MIND TREE")
    print("11. COGNIZENT")
    print("12. CISCO") 
def apply_company():
    name=input("ENTER YOUR NAME :")
    enroll=input("ENTER YOUR ENROLLMENT NUMBER :")
    ten=float(input("ENTER YOUR 10TH PERCENTAGE :"))
    twelve=float(input("ENTER YOUR 12TH PERCENTAGE :"))
    gap=int(input("ENTER YOUR OVERALL YEAR GAP"))
    print("DO YOU PRE-GRADUATION/BACHLOR DEGREE :")
    print("1.YES")
    print("2.NO")
    ch=int(input("ENTER YOUR CHOICE :"))
    if ch==1:
        grad=float(input("ENTER YOUR PRE-GRADUATION PERCENTAGE/BACHLOR :"))

    print("DO YOU POST-GRADUATION/MASTER DEGREE :")
    print("1.YES")
    print("2.NO")
    ch=int(input("ENTER YOUR CHOICE :"))
    if ch==1:
        pgrad=float(input("ENTER YOUR POST-GRADUATION PERCENTAGE/MASTER :"))

    if ten>=60.00 and twelve>=60.00 and grad>=60.00 and pgrad>=60.00 and gap==0:
        print("YOU HAVE TO APPLY THIS COMPANIES:")
        print("1.  GOOGLE")
        print("2.  AMAZON")
        print("3.  MICROSOFT")
        print("4.  ORACLE")
        print("5.  INFOSYS")
        print("6.  TCS")
        print("7.  WIPRO")
        print("8.  HCL")
        print("9.  TECH MAHINDRA")
        print("10. MIND TREE")
        print("11. COGNIZENT")
        print("12. CISCO")
    elif ten>=40.00 and twelve>=60.00 and grad>=60.00 and pgrad>=60.00 and gap<3:
        print("1.  INFOSYS")
        print("2.  TCS")
        print("3.  WIPRO")
        print("4.  HCL")
        print("5.  TECH MAHINDRA")
        print("6.  MIND TREE")
        print("7.  COGNIZENT")
        print("8.  CISCO")
    elif ten>=60.00 and twelve>=40.00 and grad>=60.00 and pgrad>=60.00 and gap<5:
        print("3.  WIPRO")
        print("4.  HCL")
        print("5.  TECH MAHINDRA")
        print("6.  MIND TREE")
        print("7.  COGNIZENT")
        print("8.  CISCO")
    elif ten>=60.00 and twelve>=60.00 and grad>=40.00 and pgrad>=60.00 and gap>=0:
        print("4.  HCL")
        print("5.  TECH MAHINDRA")
        print("6.  MIND TREE")
        print("8.  CISCO")
    elif ten>=60.00 and twelve>=60.00 and grad>=60.00 and pgrad>=40.00 and gap>=0:
        print("4.  HCL")
        print("5.  TECH MAHINDRA")
        print("6.  MIND TREE")
    elif ten<60.00 and twelve<60.00 and grad<60.00 and pgrad<60.00 and gap>=0:
        print("5.  TECH MAHINDRA")
        print("6.  MIND TREE")
    else:
        print(" WE DON'T HAVE ANY COMPANY FOR YOU TRY OPEN CAMPUS")
        
                                
import mysql.connector as my
from tkinter import*
print("\t\t*************************************************************************")
print("\n\n\t\t\t\t ----: WELCOME TO TREANING AND PLACEMENT ERP :----")
print("\n\n\t\t*********************************************************************")
login()
        
                        
                        
                            
                    
