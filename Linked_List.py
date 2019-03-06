class Linked_List:

   class __Node:
   
      def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      #pas
         self.val = val
         self.__next = None
         self.__previous = None

   def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    #pass
   
      self.__size = 0
      self.__header = self.__Node(None)
      self.__trailer = self.__Node(None)
      self.__header.__next = self.__trailer
      self.__trailer.__previous = self.__header
      self.__header.__previous = None
      self.__trailer.__next = None

   def __len__(self):
    # return the number of value-containing nodes in
    # this list.
    # TODO replace pass with your implementation
    #pass
   
      return self.__size

   def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    #pass
   
      if (self.__trailer is self.__header.__next):
         NewNode = Linked_List.__Node(val)
         NewNode.__previous = self.__trailer.__previous #self.__header
         NewNode.__next = self.__trailer
         self.__trailer.__previous.__next = NewNode
         self.__trailer.__previous = NewNode
      #self.__size += 1
      else:
         NewNode = Linked_List.__Node(val)
         NewNode.__next = self.__trailer
         NewNode.__previous = self.__trailer.__previous
         self.__trailer.__previous.__next = NewNode
         self.__trailer.__previous = NewNode
      self.__size += 1

   def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the
    # specified index. If the index is not a valid
    # position within the list, raise an IndexError
    # exception. This method cannot be used to add an
    # item at the tail position.
    # TODO replace pass with your implementation
    #pass
   
            
   #      elif (index < 0 or index >= self.__size):
      if (index <0 or index >= self.__size):
         raise IndexError
         
      elif (index == 0):
         NewNode = Linked_List.__Node(val)
         NewNode.__previous = self.__trailer.__previous #self.__header
      #        NewNode.__previous = self.__header
         NewNode.__next = self.__header.__next
         self.__header.__next.__previous = NewNode
         self.__header.__next = NewNode
         self.__size += 1
      
      
      else:
         current = self.__header.__next
         cycle = 0
         while(index != cycle):
            current = current.__next
            cycle += 1
         NewNode = Linked_List.__Node(val)
         NewNode.__next = current
         NewNode.__previous = current.__previous
         current.__previous.__next = NewNode
         current.__previous = NewNode
         self.__size += 1

   def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    #pass
   
      if (index >= self.__size or index < 0 or self.__size == 0): #index >=
         raise IndexError
    #cur=self.__header.__next
    #cycle=0
    #while(cycle != index):
    #    cur=cur.__next
    #    cycle+=1
    #value=cur.val
    #cur.__previous.__next=cur.__next
    #cur.__next.__previous=cur.__previous
    #cur.__next=None
    #cur.__previous=None
    #self.__size-=1
    #return value
   
      current = self.__header.__next
      for i in range(0, index):
         current = current.__next
      current.__previous.__next = current.__next
      current.__next.__previous = current.__previous
      self.__size -= 1
      return current.val

    #self.__previous.__next = self.__current.__next
    #self.__next.__previous = self.__current.__previous
    #self.__size -= 1
    #return self.__current.val

    #value = current.val
    #current.__previous.__next = current.__next
    #current.__next.__previous = current.__previous
    #current.__next = None
    #current.__previous = None
    #self.__size -= 1
    #return value

   def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation
    #pass
   
      if (index >= self.__size or index < 0):
         raise IndexError
      elif (index == 0):
         return self.__header.__next.val
      self.__current = self.__header.__next
      for i in range(0, index):
         self.__current = self.__current.__next
      return self.__current.val


   def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    #pass
   
      if (self.__size > 1):
         current = self.__header.__next
         current.__next.__previous = self.__header #top = header
         self.__header.__next = current.__next
         current.__previous = self.__trailer.__previous
         current.__next = self.__trailer
         self.__trailer.__previous.__next = current
         self.__trailer.__previous = current

   def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    #pass
   
      if (self.__size == 0):
         string = '[ ]'
      else:
         current = self.__header.__next
         string = '[ '
         for i in range(0, self.__size):
            if (i == 0):
               string = string + str(current.val) #str = str + str(cur.val)
            else:
               string = string + ', ' + str(current.val)
            current = current.__next
         string += ' ]' #string = string + ' ]'
      return string

   def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
   
      self.__current = self.__header.__next
      return self

   def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    #pass
   
      if (self.__current == self.__size or self.__current == self.__trailer):
         raise StopIteration
      product = self.__current
      self.__current = self.__current.__next
      return product.val

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  #pass


   print('')
   a = Linked_List()

   print('Test for Empty List')
   print(a)

   try:
      print(a.get_element_at(0))
   except IndexError:
      print('PASSED')

   a.rotate_left()
   print(a)

   try:
      print(a.remove_element_at(0))
   except IndexError:
      print('PASSED')

   try:
      a.remove_element_at(3,12) #2 10
   except:
      IndexError
      print('PASSED')

   try:
      a.get_element_at(3,12)
   except:
      IndexError
      print('PASSED')
   try:
      a.get_element_at(6,10)
   except:
      IndexError
      print('PASSED')

   try:
      a.remove_element_at(4,16)
   except:
      IndexError
      print('PASSED')
   try:
      a.get_element_at(2,10)
   except:
      IndexError
      print('PASSED')

   print(len(a))
   print('')


   print('Test for One Element')
   a.append_element(1)
   print(a)
   print(a.get_element_at(0))
   a.remove_element_at(0)
   print(a)
   a.insert_element_at(1,0)
   print(a)

   try:
      a.insert_element_at(1,-1)
   except:
      IndexError
      print('PASSED')
   print(a)

   try:
      a.insert_element_at(3,12)
   except:
      IndexError
      print('PASSED')

   try:
      a.remove_element_at(12)
   except:
      IndexError
      print('PASSED')

   try:
      a.insert_element_at(3,10)
   except:
      IndexError
      print('PASSED')

   try:
      a.remove_element_at(3,9)
   except:
      IndexError
      print('PASSED')
   try:
      a.insert_element_at(2,10)
   except:
      IndexError
      print('PASSED')
   try:
      a.remove_element_at(2,10)
   except:
      IndexError
      print('Passed')      
   print(len(a))
   print('')


   print('Test for Multiple Elements')

   a.append_element(3)
   print(a)

   a.insert_element_at(7,1)
   print(a)

   print(a.get_element_at(2))
   a.insert_element_at(-3,0)
   print(a)
   a.insert_element_at(9,0)
   print(a)
   a.rotate_left()
   print(a)
   print(a.remove_element_at(1))

   try:
      a.get_element_at(9)
   except:
      IndexError
      print('PASSED')

   try:
      a.get_element_at(-4)
   except:
      IndexError
      print('PASSED')

   try:
      a.remove_element_at(12)
   except:
      IndexError
      print('PASSED')
   try:
      a.get_element_at(13)
   except:
      IndexError
      print('PASSED')
   print(len(a))