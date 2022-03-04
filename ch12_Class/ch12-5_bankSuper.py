class Banks():
    def __init__(self,name):
        self.__bankname="Taipei"
        self.__name=name
        self.__balance=0
        self.bankname='Taipei Bank'
        self.__rate=30
        self.__service_charge=0.01
    def save_money(self,money):
        self.__balance+=money
        print("存款",money,'完成')
    def withdraw_money(self,money):
        self.__balance-=money 
        print("提款",money,'完成')  
    def get_money(self):
        print(self.__name.title(),'目前餘額: ',self.__balance)  
        return self.__balance
    def usa_to_taiwan(self,usa):
        self.result= self.__cal_rate(usa)
        return self.result
    def __cal_rate(self,usa):
        return int(usa*self.__rate*(1-self.__service_charge))  
    
class Shilin_Bank(Banks):
    def __init__(self,name):
        self.bankname='Shilin_Bank'
class Beitou_Bank(Banks):
    def __init__(self,name):
        self.bankname='Beitou_Bank'
yin=Banks('yin')
usDollors=100
ling=Shilin_Bank('ling')
print(ling.bankname)
chia=Beitou_Bank('Chia')
print(chia.bankname)

#
#print('A:存款5000元',yin.save_money(5000),yin.get_money())
#print('B:提款3000元',yin.withdraw_money(3000),yin.get_money())
#print('C:存款1500元',yin.save_money(1500),yin.get_money())
#print('D',usDollors,'美金可兌換',yin.usa_to_taiwan(usDollors))
#print('E:',yin.get_money())


        
