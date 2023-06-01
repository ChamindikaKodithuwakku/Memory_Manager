class MemoryBlock:

    def __init__(self, start_address, size):
        self.start_address = start_address
        self.process_id = None
        self.size = size
        self.allocated = False
        self.next_node = None

    @staticmethod
    def new_node(start_address, size):
        return MemoryBlock(start_address, size)