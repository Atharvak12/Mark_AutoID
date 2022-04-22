class bean():
    id = int
    name = ""
    email = ""
    pwd = ""
    adr = ""

    def setid(self, id):
        self.id = id
    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name

    def setemail(self, email):
        self.email = email
    def getemail(self):
        return self.name

    def setpwd(self, pwd):
        self.pwd = pwd
    def getpwd(self):
        return self.pwd

    def setadr(self, adr):
        self.adr = adr
    def getadr(self):
        return self.adr