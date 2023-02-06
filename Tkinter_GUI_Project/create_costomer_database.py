import mysql.connector as mysql
db=mysql.connect(host='localhost',user='root',passwd='',database='aacompany')
cur=db.cursor()
'''
try:
    cur.execute(" create database AAcompany ")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("create table customer(cid int(5) primary key,cname varchar(50) not null,city varchar(50),mobile bigint(15),gender varchar(10) not null) ")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("create table product(pid int(7) primary key,pname varchar(50) unique not null,prise float(15) not null,qty bigint(15)) ")
    print('success')
except:
   print('invalid sql qurey')


try:
    cur.execute("create table transaction(tid int(5) primary key auto_increment,cid int(5)not null,pid int(5)not null,qty bigint(15) not null,constraint cid_fk foreign key(cid) references customer(cid),constraint pid_fk foreign key(pid) references product(pid))")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("create table login(uid int(5) primary key auto_increment,username varchar(50) not null unique,password varchar(50) not null,fname varchar(25) not null,sname varchar(25) not null,question varchar(150),answer varchar(50))")
    print('success')
except:
   print('invalid sql qurey')


try:
    cur.execute("alter table transaction add (pid5 int(5),qty5 bigint(15),constraint pid5_fk foreign key(pid5) references product(pid))")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("alter table transaction add (dis1 float(10),dis2 float(10),dis3 float(10),dis4 float(10),dis5 float(10))")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("create table trans(tid int(5) not null,cid int(5)not null,pid bigint(10)not null,pname varchar(50) not null,prise float(10) not null,qty bigint(15) not null,disc int(5) not null,amount float(15),constraint cid_fk foreign key(cid) references customer(cid),constraint pid_fk foreign key(pid) references product(pid),constraint pname_fk foreign key(pname) references product(pname),constraint prise_fk foreign key(prise) references product(prise))")
    print('success')
except:
   print('invalid sql qurey')

try:
    cur.execute("create table trans(tid int(5) not null,cid int(5)not null,pid bigint(10)not null,pname varchar(50) not null,prise float(10) not null,qty bigint(15) not null,disc int(5) not null,amount float(15) not null)")
    print('success')
except:
   print('invalid sql qurey')


db.commit()
db.close()
print('------')
'''
