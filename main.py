import os, json

class InerhitBlockData:

    def __init__(self, from_connection, is_open_port=True):
        self.con = [from_connection]
        self.isPortOpen = [is_open_port]
        self.block_inherited = None # nothing is in the block yet
    
    def _append_connection_(self, new_con_name, portOpen = True):
        self.con.append(new_con_name)
        self.isPortOpen.append(portOpen)

    def _inherit_(self, block, connection_name, formsOf = 12):

        if connection_name in self.con:
            index = -1
            for i in range(len(self.con)):

                if self.con[i] == connection_name:
                    index = i
                    break

            if self.isPortOpen[index] == True:
                inherited_mini_blocks = []
                #current_block_index = 0
                block = str(block)
                block_index = 0
                current_byte = 0
                last_index = 0
                i = 0

                while i <= len(block):
                    if current_byte >= formsOf:
                        x = last_index
                        while x <= formsOf:

                            inherited_mini_blocks.append(block[x])

                            if x == current_byte: break
                            x+=1
                            
                        #current_block_index += 1
                        current_byte = 0

                        last_index = x

                    block_index += 1
                    current_byte += 8
                    i+=1
                
                self.block_inherited = inherited_mini_blocks
                return self.block_inherited
            else: print('Cannot take block from closed port\n')
        
    def IsOpenPort(self, connection_name): 
        
        index = 0
        for i in range(len(self.con)):

            if self.con[i] == connection_name:
                index = i
                break
        return self.isPortOpen[index]


class SetupConnection():

    def __init__(self, connection_name, open_connection = True, openPort = True):

        self.con_name = connection_name
        self.con_status = open_connection
        self.OpenPort = openPort
    
    def _init_connection_(self, withBlock = 'Empty String'):

        if self.con_status:
            SEND = InerhitBlockData(self.con_name, self.con_status)

            while self.con_status == True and SEND.IsOpenPort(self.con_name) == True:

                print(SEND._inherit_(withBlock,self.con_name,8))

                break

CON = SetupConnection('Myport')
CON._init_connection_()