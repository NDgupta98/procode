import itertools
from textwrap import wrap
opc_mne={'MOVR':1,'ADDR':2,'SUBR':3,'MULR':4,'DIVR':5,'ANDR':6,'ORR':7,'A':8,'S':9,'M':10,'D':11,'AND':12,'OR':13,'LOAD':14,'STORE':15,'DCR':16,'INC':17,'HALT':20}
size_opc={'MOVR':1,'ADDR':1,'SUBR':1,'MULR':1,'DIVR':1,'ANDR':1,'ORR':1,'A':2,'S':2,'M':2,'D':2,'AND':2,'OR':2,'LOAD':3,'STORE':3,'DCR':1,'INC':1,'HALT':1}
ins=[]
r=[]
op=[]
siz=[]
raddr=0
n=int(input("Enter the no. of lines in ALP instruction "))

for i in range(n):
	inst=input("Enter instruction ")
	ins.append(inst)
ins=[z.upper() for z in ins]
for i in range(n):
	x=ins[i]
	if " " in x:
		a,b=x.split()
		if a in size_opc:
			opcode=opc_mne.get(a)
			s=size_opc.get(a)
			siz.append(raddr)
			raddr+=s
			if len(str(b)) == 2:
				op.append(str(opcode) + "," +b)
			else:
				d=wrap(b,2)
				op.append(str(opcode) + "," +d[0]+","+d[1])

	else:
		if x in size_opc:
			opcode=opc_mne.get(x)
			s=size_opc.get(x)
			op.append(opcode)
			siz.append(raddr)
			raddr+=s

print("Relational address\tInstruction\t \t   Machine code")
for (a,b,c) in zip(siz,ins,op):
	print(a,"\t\t\t",b,"\t\t\t",c)

