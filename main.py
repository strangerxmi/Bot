from gingerit.gingerit import GingerIt
from datetime import datetime


#ENTER AND CORRECT TEXT
praser = GingerIt()
qtn = input('Enter........ ')
analyseqtn = praser.parse(qtn)
print(f'You : {qtn}')
print('')
finalqtn = analyseqtn['result'].lower()
print('Understanding : ' + finalqtn)

#PROCESS
now = datetime.now()
dt =  now.strftime("%b-%d-%Y %H:%M:%S").upper()
# Append-adds at last
file1 = open("records.txt", "a")  # append mode
file1.write("\n")
file1.writelines(finalqtn + f' ...({dt})...')
file1.close()


