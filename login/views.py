from django.shortcuts import render,redirect

# Create your views here.
from signup.models import stocks
import mysql.connector
from signup.models import transaction

login_check=False
con=mysql.connector.connect(host="localhost", user="root", passwd="root",database="stocksonline")

mycursor=con.cursor()


def login_1(request):
    global username
    global login_check
    con=mysql.connector.connect(host="localhost", user="root", passwd="root",database="stocksonline")

    mycursor=con.cursor()
    sql="select username,password from signup_signup"
    mycursor.execute(sql)
    a=mycursor.fetchall()
    print(a)
    
    usr=[]
    pwd=[]
    #login_check=False
    for i in a:
        usr.append(i[0])
        pwd.append(i[1])
    l=len(usr)
    
    
    
    if request.method=="POST":
        global username
        d=request.POST["username"]
        password=request.POST["password"]
        for i in range(l):
            if usr[i]==d:
                if pwd[i]==password:
                    #global username
                    username=d
                    #global login_check
                    login_check=True
                    #request.session['lc']=True
                    print(login_check)
                    '''global l1
                    global l2
                    global dl'''
                    sql18="select som from signup_signup where username='{}'".format(username)
                    mycursor.execute(sql18)
                    a=mycursor.fetchall()
                    balance=a[0][0]
                    text="Welcome, "+username+",You have "+str(balance)+" in your account!"
                    l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
                    l2=transaction.objects.filter(seller=username).filter(status='y').values('amount','stock','shares')
                    dl=[]
                    if con.is_connected:
                        print('yes')
                    sql15="select name from signup_stocks"
                    mycursor.execute(sql15)
                    n=mycursor.fetchall()
                    l=len(n)
                    for i in range(l):
                        sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
                        sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
                        mycursor.execute(sql8)
                        a=mycursor.fetchall()
                        mycursor.execute(sql9)
                        b=mycursor.fetchall()
                        if a==[(None,)]:
                            bought=0
                        else:
                            bought=float(a[0][0])
                        if b==[(None,)]:
                            sold=0
                        else:
                            sold=float(b[0][0])
                        net=bought-sold
                        if net>0:
                            sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage from signup_stocks where name='{}'".format(n[i][0])
                            mycursor.execute(sql16)
                            g=mycursor.fetchall()
                            de=list(g[0])
                            d=de+[net]
                            print(d)
                            dl.append(d)                 
                    return render(request, "myhome.html",{'a':text,'l1':l1,'l2':l2,'l3':dl})
                    #return redirect("../myhome")

                '''else:
                    login_check=False
                    return render(request, "login.html")'''
        else:
            login_check=False
            return render(request,"login.html",{'a':'Incorrect- please try again'})
    else:
        return render(request, "login.html",{'a':''})

        #usr = login.Objects.all()
        #print(usr)
print(login_check)



def myhome(request):
   
   if login_check==True:
        con=mysql.connector.connect(host="localhost", user="root", passwd="root",database="stocksonline")
        mycursor=con.cursor()
        sql18="select som from signup_signup where username='{}'".format(username)
        mycursor.execute(sql18)
        a=mycursor.fetchall()
        balance=a[0][0]

        text="Welcome, "+username+" !, You have "+str(balance)+" in your account!"
        l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
        l2=transaction.objects.filter(seller=username).values('amount','stock','shares')
        dl=[]
        if con.is_connected:
            print('yes')
        sql15="select name from signup_stocks"
        mycursor.execute(sql15)
        n=mycursor.fetchall()
        l=len(n)
        for i in range(l):
            sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
            sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
            mycursor.execute(sql8)
            a=mycursor.fetchall()
            mycursor.execute(sql9)
            b=mycursor.fetchall()
            if a==[(None,)]:
                bought=0
            else:
                bought=float(a[0][0])
            if b==[(None,)]:
                sold=0
            else:
                sold=float(b[0][0])
            net=bought-sold
            if net>0:
                sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage,signup_transaction.shares from signup_stocks inner join signup_transaction on signup_stocks.name=signup_transaction.stock where name='{}'".format(n[i][0])
                mycursor.execute(sql16)
                g=mycursor.fetchall()
                de=list(g[0])
                d=de+[net]
                print(d)
                dl.append(d)
        return render(request, 'myhome.html',{'a':text,'l1':l1,'l2':l2,'l3':dl})
   else:
       return render(request,'login.html',{'a':''})    

        
def themarket(request):
    print("here",login_check)
    if login_check==True:
        #con=mysql.connector.connect(host="localhost", user="root", passwd="root",database="stocksonline")
        #mycursor=con.cursor()
        sql1="select * from signup_stocks"
        #mycursor.execute(sql1)
        #a=mycursor.fetchall()
        #name=[]
        #comp=[]
        #price=[]
        #change=[]
        #volatility=[]
        a=stocks.objects.all()

        #n=len(a)
        '''for i in a:
            name.append(i[0])
            comp.append(i[1])
            price.append(i[2])
            change.append(i[3])
            volatility.append(i[4])'''
        return render(request, 'themarket.html',{'a':a}) 

    else:
        return render(request,'login.html',{'a':''}) 

def settings(request):
   if login_check==True:
	    return render(request, 'settings.html')
   else:
        return render(request,'login.html',{'a':''}) 

 
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
mycursor=con.cursor()

def buy_direct(request):
    con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
    mycursor=con.cursor()
    if login_check ==True:
        if request.method=="POST":
            con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
            mycursor=con.cursor()
            stock=request.POST["option"]
            num_of=request.POST["num"]
            num_of=int(num_of)
            sql3="select * from signup_stocks"
            mycursor.execute(sql3)
            t=mycursor.fetchall()
            n=len(t)
            for i in range(n):
                if t[i][1]==stock:
                    vall=t[i][2]
                    val=float(vall)
            sql4="select * from signup_signup"
            mycursor.execute(sql4)
            w=mycursor.fetchall()

            p=len(w)
            for i in range(p):
                if w[i][0]==username:
                    baln=w[i][4]
                    bal=float(baln)
                #sql2="insert into signup_transaction values("username,","None,","stock,","val*num_of*1.3,","True")"
            if val*num_of*1.3 > bal:
                
                disp="Insufficient Funds to complete transaction!"
                #sql2="insert into signup_transaction values("username,","None,","stock,","val*num_of*1.3,","T")"
                return render(request,'buy.html',{'a':disp})
            else:
                new_bal=bal-(val*num_of*1.3)
                disp="You have "+str(new_bal) + " money left in your StocksOnline wallet."
                sql2='insert into signup_transaction(buyer,seller,amount,status,stock,shares) values ("{}","{}","{}","{}","{}","{}")'.format(username,None,val*num_of*1.3,'y',stock,num_of)
                sql5='update signup_signup set som = {} where username = "{}"'.format(new_bal,username)
                mycursor.execute(sql5)
                mycursor.execute(sql2)
                con.commit()
                con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
                mycursor=con.cursor()
                l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
                l2=transaction.objects.filter(seller=username).values('amount','stock','shares')
                dl=[]
                if con.is_connected:
                    print('yes')
                sql15="select name from signup_stocks"
                mycursor.execute(sql15)
                n=mycursor.fetchall()
                l=len(n)
                for i in range(l):
                    sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
                    sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
                    mycursor.execute(sql8)
                    a=mycursor.fetchall()
                    mycursor.execute(sql9)
                    b=mycursor.fetchall()
                    if a==[(None,)]:
                        bought=0
                    else:
                        bought=float(a[0][0])
                    if b==[(None,)]:
                        sold=0
                    else:
                        sold=float(b[0][0])
                    net=bought-sold
                    if net>0:
                        sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage from signup_stocks where name='{}'".format(n[i][0])
                        mycursor.execute(sql16)
                        g=mycursor.fetchall()
                        de=list(g[0])
                        d=de+[net]
                        print(d)
                        dl.append(d)
                
                return render(request,'myhome.html',{'a':disp,'l1':l1,'l2':l2,'l3':dl})
        else:
            return render(request,'buy.html')
    else:
        return render(request,'login.html')

def for_sale(request):
    if login_check==True:
        if request.method=="POST":
            con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
            mycursor=con.cursor()
            stock=request.POST["option"]
            num_of=request.POST["num"]
            num=int(num_of)
            sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,stock)
            sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,stock)
            mycursor.execute(sql8)
            a=mycursor.fetchall()
            mycursor.execute(sql9)
            b=mycursor.fetchall()
            if a==[(None,)]:
                bought=0
            else:
                bought=float(a[0][0])
            if b==[(None,)]:
                sold=0
            else:
                sold=float(b[0][0])
            net=bought-sold
            print(net)
            sql10="select last from signup_stocks where name='{}'".format(stock)
            mycursor.execute(sql10)
            c=mycursor.fetchall()
            if c==[(None,)]:
                val=0
            else:
                val=float(c[0][0])

            if net >= num:
                add=val*num*1.3   
                sql7='insert into signup_transaction(buyer,seller,amount,status,stock,shares) values ("{}","{}","{}","{}","{}","{}")'.format(None,username,add,'y',stock,num)
                mycursor.execute(sql7)
                con.commit()
                sql4="select * from signup_signup"
                mycursor.execute(sql4)
                w=mycursor.fetchall()
                p=len(w)
                for i in range(p):
                    if w[i][0]==username:
                        bal_1=w[i][4]
                bal=float(bal_1)
                newbal=bal+add
                sql11="update signup_signup set som = {} where username='{}'".format(newbal,username)
                mycursor.execute(sql11)
                con.commit()
                con.close()
                con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
                mycursor=con.cursor()                
                a="Sold!"
                l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
                l2=transaction.objects.filter(seller=username).values('amount','stock','shares')
                dl=[]
                if con.is_connected:
                    print('yes')
                sql15="select name from signup_stocks"
                mycursor.execute(sql15)
                n=mycursor.fetchall()
                l=len(n)
                for i in range(l):
                    sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
                    sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
                    mycursor.execute(sql8)
                    a=mycursor.fetchall()
                    mycursor.execute(sql9)
                    b=mycursor.fetchall()
                    if a==[(None,)]:
                        bought=0
                    else:
                        bought=float(a[0][0])
                    if b==[(None,)]:
                        sold=0
                    else:
                        sold=float(b[0][0])
                    net=bought-sold
                    if net>0:
                        sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage from signup_stocks where name='{}'".format(n[i][0])
                        mycursor.execute(sql16)
                        g=mycursor.fetchall()
                        de=list(g[0])
                        d=de+[net]
                        print(d)
                        dl.append(d)
                sql19="select som from signup_signup where username='{}'".format(username)
                mycursor.execute(sql19)
                d=mycursor.fetchall()
                num=d[0][0]
                a="Sold! You now have "+str(num)+" money in your account."                
                return render(request,'myhome.html',{'a':a,'l1':l1,'l2':l2,'l3':dl})
            else:


                return render(request,'listing.html',{'a':'You do not have sufficient amount of this stock to sell..'})
        else:
            return render(request,'listing.html')
    else:
        return render(request,'login.html')


def change_details(request):
    if login_check==True:
        if request.method=="POST":
            con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
            mycursor=con.cursor()
            top_up=request.POST['amount']
            add=int(top_up)
            sql4="select * from signup_signup"
            mycursor.execute(sql4)
            w=mycursor.fetchall()
            p=len(w)
            for i in range(p):
                if w[i][0]==username:
                    bal_1=w[i][4]
            bal=int(bal_1)
            newbal=bal+add
            sql11="update signup_signup set som = {} where username='{}'".format(newbal,username)
            mycursor.execute(sql11)
            con.commit()
            con.close()
            con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
            mycursor=con.cursor()
            l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
            l2=transaction.objects.filter(seller=username).values('amount','stock','shares')
            dl=[]
            if con.is_connected:
                print('yes')
            sql15="select name from signup_stocks"
            mycursor.execute(sql15)
            n=mycursor.fetchall()
            l=len(n)
            for i in range(l):
                sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
                sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
                mycursor.execute(sql8)
                a=mycursor.fetchall()
                mycursor.execute(sql9)
                b=mycursor.fetchall()
                if a==[(None,)]:
                    bought=0
                else:
                    bought=float(a[0][0])
                if b==[(None,)]:
                    sold=0
                else:
                    sold=float(b[0][0])
                net=bought-sold
                if net>0:
                    sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage from signup_stocks where name='{}'".format(n[i][0])
                    mycursor.execute(sql16)
                    g=mycursor.fetchall()
                    de=list(g[0])
                    d=de+[net]
                    print(d)
                    dl.append(d)
            sql20="select som from signup_signup where username='{}'".format(username)
            mycursor.execute(sql20)
            b=mycursor.fetchall()
            num=b[0][0]

            a='Money deposited! You now have '+str(num)+' money in your account.'
            return render(request,'myhome.html',{'a':a,'l1':l1,'l2':l2,'l3':dl})
        else:
            return render(request,'topup.html')
    else:
        return render(request,'login.html')

def change_passwd(request):
    if login_check==True:
        if request.method=='POST':
            oldpd=request.POST['old']
            newpd=request.POST['password']
            sql13="select password from signup_signup where username='{}'".format(username)
            mycursor.execute(sql13)
            print(newpd)
            e=mycursor.fetchall()
            older=e[0][0]
            if oldpd==older:
                sql12="update signup_signup set password = '{}' where username = '{}'".format(newpd,username)
                mycursor.execute(sql12)
                con.commit()
                con.close()
            con.close()
            con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stocksonline")
            mycursor=con.cursor()
            l1=transaction.objects.filter(buyer=username).values('amount','stock','shares')
            l2=transaction.objects.filter(seller=username).values('amount','stock','shares')
            dl=[]
            if con.is_connected:
                print('yes')
            sql15="select name from signup_stocks"
            mycursor.execute(sql15)
            n=mycursor.fetchall()
            l=len(n)
            for i in range(l):
                sql8="select sum(shares) from signup_transaction where buyer='{}' and stock='{}'".format(username,n[i][0])
                sql9="select sum(shares) from signup_transaction where seller='{}' and stock='{}'".format(username,n[i][0])
                mycursor.execute(sql8)
                a=mycursor.fetchall()
                mycursor.execute(sql9)
                b=mycursor.fetchall()
                if a==[(None,)]:
                    bought=0
                else:
                    bought=float(a[0][0])
                if b==[(None,)]:
                    sold=0
                else:
                    sold=float(b[0][0])
                net=bought-sold
                if net>0:
                    sql16="select signup_stocks.symbol,signup_stocks.name,signup_stocks.last,signup_stocks.change,signup_stocks.change_percentage from signup_stocks where name='{}'".format(n[i][0])
                    mycursor.execute(sql16)
                    g=mycursor.fetchall()
                    de=list(g[0])
                    d=de+[net]
                    print(d)
                    dl.append(d)
               
                return render(request,'myhome.html',{'a':'Password changed!','l1':l1,'l2':l2,'l3':dl})
            else:
                return render(request,'changepasswd.html')
        else:
            return render(request,'changepasswd.html')
    else:
        return render(request,'login.html')

def logout(request):
    global login_check
    if login_check==True:

        login_check=False
        return render(request,'stocks.html')
    else:
        return render(request,'login.html')

def about(request):
    return render(request,'about.html')


