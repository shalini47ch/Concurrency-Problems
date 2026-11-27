'''
Implement a ReadersPreferenceRW class using Python threading locks and semaphores.

Requirements:
1. Multiple readers can access the shared resource simultaneously.
2. Only one writer can access it at a time.
3. Readers and writers cannot access it simultaneously.
4. The first reader blocks writers.
5. The last reader releases the resource for writers.
6. Readers get priority over writers.

'''
#this is reader's preference reader writer pattern
class ReadersPreferenceRW:
   def __init__(self):
     self.readercount=0
     self.readercountlock=threading.Lock()
     self.resourceaccess=threading.Semaphore(1)

   def reader_acquire(self):
      with self.readercountlock:
         self.readercount+=1
        if(self.readercount==1):
           self.resourceaccess.acquire()

  #now similarly create a helper function to perform reader release
  def reader_release(self):
     with self.readercountlock:
       self.readercount-=1
       if(self.readercount==0):
         self.resourceacesss.release()

#now we need two more helpers one is writer acquire and one is writer release
 def writer_acquire(self):
    self.resourceaccess.acquire()

 def writer_release(self):
    self.resourceaccess.release()
        





     
