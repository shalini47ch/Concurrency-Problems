'''
Leetcode 1115
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.




'''

class FooBar:
    def __init__(self, n):
        #we will use the concept of semaphore and then acquire foo and relase the bar and in the other case acquire bar and release foo so it will be printed alternately
        self.n = n
        self.foosemaphore=threading.Semaphore(1) #this will go first
        self.barsemaphore=threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foosemaphore.acquire()
            printFoo()
            self.barsemaphore.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            #now here lets do for barsemaphore
            self.barsemaphore.acquire()
            printBar()
            self.foosemaphore.release()
