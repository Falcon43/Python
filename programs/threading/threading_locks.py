import threading
import time
import random




class BankAccount(threading.Thread):

    accountBalance = 100

    def __init__(self,name,moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()


    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name,customer.moneyRequest,time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.accountBalance - customer.moneyRequest >0 :
            BankAccount.accountBalance = BankAccount.accountBalance - customer.moneyRequest
            print("New account balance:  ${}".format(BankAccount.accountBalance))
        else:
            print("Not enough money in account")
            print("Current balance: ${}".format(BankAccount.accountBalance))

        #time.sleep(3)




threadLock = threading.Lock()

joey = BankAccount("Joey",2)
mark = BankAccount("Mark",100)
suse = BankAccount("Suse",50)


joey.start()
mark.start()
suse.start()

joey.join()
mark.join()
suse.join()


print("Execution ends")