import Bean
from Bean import *
import MarkDao
from MarkDao import *


def testCreate():
    mb = bean()
    # mb.setid(2)
    mb.setname("Atharva")
    mb.setemail("atharva@gmail.com")
    mb.setpwd("pass1234")
    mb.setadr("indore")
    md = markDao()
    md.add(mb)
    print(":ADD")
# testCreate()

def testRead():
    mb = bean()
    mb.setid(3)
    md =  markDao()
    md.search_single(mb)
    print("Select")
# testRead()

def testRead_all():
    md = markDao()
    md.search_all()
# testRead_all()

def testUpdate():
    mb = bean()
    mb.setname("Atharvakabra")
    mb.setid(1)
    mb.setemail("atharva@gmail.com")
    mb.setpwd("pass1234")
    mb.setadr("indore")
    md = markDao()
    md.update(mb)
    print("updated")
# testUpdate()

def testDelete():
    mb = bean()
    mb.setid(2)
    md = markDao()
    md.delete(mb)
    print("deleted")
# testDelete()

