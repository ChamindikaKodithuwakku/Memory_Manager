from Memory_Controller import MemoryBlock

class MemoryManager:
    def __init__(self):
        self.initial_node()

    def initial_node(self):
        self.total_memory = 2560
        self.os_size = 400
        self.free_memory = self.total_memory - self.os_size

        self.memory_list = MemoryBlock.new_node(0,self.free_memory)

    def allocate_memory(self,process_id,size):
        current_node = self.memory_list
        previous_node = None
        while current_node :
            if current_node.allocated == False and current_node.size >= size:
                allocated_node = MemoryBlock(current_node.start_address,size)
                allocated_node.allocated = True
                allocated_node.process_id = process_id
                allocated_node.next_node = current_node.next_node
                current_node.size = current_node.size - size
                #current_block.start_address = current_block.start_address + size
                current_node.next_node = allocated_node

                self.free_memory = self.free_memory - size
                print(f"Process {process_id} allocated {size}k of memory.")
                return 1        
            
            previous_node = current_node
            current_node = current_node.next_node
        
        print(f"Memory space not enough to allocate this Process {process_id}.")
        return 0

    def release_memory(self,process_id):
        current_node = self.memory_list
        previous_node = None
        while current_node:
            if current_node.allocated == True and current_node.process_id == process_id:
                current_node.allocated = False
                current_node.process_id = None
                self.free_memory = self.free_memory + current_node.size

                print(f"Process {process_id} relesed memory.")
                return 1
        
            previous_node = current_node
            current_node = current_node.next_node

            
        print(f"Process {process_id} is not allocated any memory.")
        return 0

    def print_memory_snapshot(self):
        current_node = self.memory_list
        memory_snapshot = "Memory Snapshot:\n"
        while current_node:
            if current_node.allocated == True:
                status = "Allocated"
            else:
                status = "Free"
            memory_snapshot += f"Address: {current_node.process_id},  Size: {current_node.size}k,  status: {status}\n"
            print(f"Address: {current_node.process_id}, Size: {current_node.size}k, status: {status}\n")
            current_node = current_node.next_node

        memory_snapshot += f"Total Memory: {self.total_memory}k\n"
        print(f"Total Memory: {self.total_memory}k\n")
        memory_snapshot += f"Free Memory: {self.free_memory}k\n"
        print(f"Free Memory: {self.free_memory}k\n")
        return memory_snapshot
   




