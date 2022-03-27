from blockchain import Blockchain
class L2:
    L1 = Blockchain()
    L2_chain = Blockchain()
    def __init__(self):
        while True:
            
            user_input = str(input(': '))
            user_input = user_input.strip(' ')
            if user_input == '/quit':
                break 
            elif user_input == '/add':
                self.add()
            elif '/add_val' in user_input:              #add_val [block-idx] 
                lst = user_input.split(' ')
                self.add_val(lst)
            elif '/view' in user_input:
                lst = user_input.split(' ')
                self.print_network(lst)

                    


    def add(self):
        user_input = int(input('Length of chain: '))
        for i in range(user_input):
            transaction = {'chain': self.L2_chain}
            self.L1.add_block(transaction)

    def add_val(self, lst):
        if len(lst) == 1:
            print("There are not enough parameters")
            return
        val_to_add = None
        for command in range(len(lst)):
            if command == 0:
                pass 
            elif command == 1:
                val = lst[command].strip(' ')
                val_to_add = val
            elif command == 2:
                user_idx = lst[command].strip(' ')
                user_idx = user_idx.strip('[')
                user_idx = user_idx.strip(']')
                user_idx = int(user_idx)
                if user_idx > len(self.L1.chain):
                    print("Index too large")
                    return
                for block_idx in range(len(self.L1.chain)):
                    if block_idx == user_idx:
                        transaction = {'Val': val_to_add}
                        network = self.L1.chain[block_idx].transactions['chain']
                        network.add_block(transaction)
            else:
                continue 
        return True

    def print_network(self, lst):
        if len(lst) == 1:
            print("There are not enough parameters")
            return 
        for network_idx in range(len(lst)):
            if network_idx == 0:
                pass 
            elif network_idx == 1:
                user_idx = lst[network_idx].strip(' ')
                user_idx = user_idx.strip(']')
                user_idx = user_idx.strip('[')
                user_idx = int(user_idx)
                if user_idx > len(self.L1.chain):
                    print("Index too large")
                    return
                for block_idx in range(len(self.L1.chain)):
                    if block_idx == user_idx:
                        des_network = self.L1.chain[block_idx].transactions['chain']
                        des_network.print_blocks()
                    else:
                        continue
            
                        
                    
                    

                
                

        
    

        


            
test = L2()
