from blockchain import Blockchain
class L2:
    L1 = Blockchain()
    L2_chain = Blockchain()
    def __init__(self):
        while True:
            try:
                user_input = str(input(': '))
                if user_input == '/quit':
                    break 
                elif user_input == '/add':
                    self.add()
                
                
            
            except:
                pass
                

    def add(self):
        user_input = int(input('Length of chain: '))
        for i in range(user_input):
            transaction = {'chain': self.L2_chain}
            self.L1.add_block(transaction)
        


            
test = L2()
