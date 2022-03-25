from blockchain import Blockchain
class L2:
    L1 = Blockchain()
    L2 = Blockchain()
    def __init__(self):
        while True:
            try:
                user_input = str(input(': '))
                if user_input == '/quit':
                    break 
                elif user_input == '/add':
                    self.add()
                user_input = int(user_input)
                
            
            except:
                pass
            
    
            