emp =  {  'id01' :  { 'name' : 'Dev', 'phone' : '08056771173'},
          'id02' :{ 'name' : 'Raj', 'phone' : '01176791193'},
          'id03' :  { 'name' : 'Ami', 'phone' : '08056774473'},
          'id04' :{ 'name' : 'Anita', 'phone' : '011767976193'},
          'id05' :  { 'name' : 'Sam', 'phone' : '08056771173'},
          'id06' :{ 'name' : 'Reena', 'phone' : '02276791193'},
          'id07' :  { 'name' : 'Akul', 'phone' : '08056774473'},
          'id08' :{ 'name' : 'Amar', 'phone' : '011767976193'}}
m=[ emp['name']  for emp in emp.values() if emp['phone'][:3]=='080' ]
print(m)


print()
print()

cities = { '080':'Bengaluru', '044':'Chennai', '040':'Hyderabad', '011':'Delhi', '022':'Mumbai' }
m={ cities[ emp['phone'][:3] ]  for emp in emp.values() }
print(m)
