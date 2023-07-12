
class Patient:
  id = 0
  def __init__(self,name,age,blood):
      self.id = Patient.id
      self.name = name
      self.age = age
      self.blood = blood
      self.prev = None
      self.next = None
      Patient.id += 1

class WRM:
  def __init__(self):
    self.head = Patient(None,None,None)
    self.head.prev = self.head
    self.head.next = self.head
  def RegisterPatient(self,name,age,blood):
    if type(name) != str or type(age) != int or type(blood) != str:
      print(f"registration for {name} was Unsuccessful")
    elif ( 0 > age > 200) or blood not in ["A+","A-","B+","B-","AB+","AB-","O+","O-"]:
      print(f"registration for {name} was Unsuccessful")
    else:
      new_node = Patient(name,age,blood)
      new_node.next = self.head
      new_node.prev = self.head.prev
      self.head.prev.next = new_node
      self.head.prev = new_node

  def ShowAllPatient(self):
    n = self.head.next
    while n != self.head:
      print(f"ID: {n.id}, Name: {n.name}")
      n = n.next

  def ServePatient(self):
    if self.head.next == self.head:
      print("No patient to serve")
    else:
      n = self.head.next
      print(f"{n.name} is being served")
      n = n.next
      done = n.prev
      n.prev = n.prev.prev
      n.prev.next = n
      done.prev = None
      done.next = None

  def CanDoctorGoHome(self):
    if self.head.next == self.head:
      print("YES! Doctor can go home")
    else:
      print("NO! Doctor cannot go home")

  def CancelAll(self):
    if self.head.next == self.head:
      print("Canceling was Unsuccessful")
    else:
      self.head.prev.next = None
      self.head.prev = self.head
      self.head.next = self.head
      print("Canceling was Successful")

New_hospital = WRM()
p1 = New_hospital.RegisterPatient("a",0,"A+")
p2 = New_hospital.RegisterPatient("d",25,"B+")
p3 = New_hospital.RegisterPatient("p",30,"AB-")
p4 = New_hospital.RegisterPatient("c",50,"O+")
p5 = New_hospital.RegisterPatient("f",70,"O-")
p6 = New_hospital.RegisterPatient(1,70,"O-")
p7 = New_hospital.RegisterPatient("g",70,2)
p8 = New_hospital.RegisterPatient("k","s","O")
p9 = New_hospital.RegisterPatient("l",-20,"s")
p10 = New_hospital.RegisterPatient("m",0,"O-")
p11 = New_hospital.RegisterPatient("n",800,"O-")


New_hospital.ShowAllPatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CancelAll()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()

p1 = New_hospital.RegisterPatient("a",0,"A+")
p2 = New_hospital.RegisterPatient("d",25,"B+")
p3 = New_hospital.RegisterPatient("p",30,"AB-")
p4 = New_hospital.RegisterPatient("c",50,"O+")
p5 = New_hospital.RegisterPatient("f",70,"O-")
New_hospital.CanDoctorGoHome()

New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.ServePatient()
New_hospital.CanDoctorGoHome()
New_hospital.CancelAll()