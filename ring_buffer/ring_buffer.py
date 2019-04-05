class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # pass
    # start with storage[current], change to new item
    # if current is greater than capacity
    # remove first item and replace with new item
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
    else:
      self.current = 0
      self.append(item)

    

  def get(self):
    # pass
    our_list = []
    for item in self.storage:
      if item is not None:
        our_list.append(item)
    return our_list