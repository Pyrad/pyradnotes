# C++ Concurrency in Action

***Practical Multithreading***

***Anthony Williams***


## Note

## About the book

## Resources

## Words

granularity

## Usage

## Names

## Brief Contents

- **1. Hello, world of concurrency in C++!**
- **2. Managing threads**
- **3. Sharing data between threads**
- **4. Synchronizing concurrent operations**
- **5. The C++ memory model and operations on atomic types**
- **6. Designing lock-based concurrent data structures**
- **7. Designing lock-free concurrent data structures**
- **8. Designing concurrent code**
- **9. Advanced thread management**
- **10. Testing and debugging multithreaded applications**

## Contents

- **1. Hello, world of concurrency in C++!**
	- What is concurrency?
		- Concurrency in computer systems
		- Approaches to concurrency
	- Why use concurrency?
		- Using cocurrency for separation of concerns
		- Using concurrency for performance
		- When not to use concurrency
	- Concurrency and multithreading in C++
		- History of multithreading in C++
		- Concurrency support in the new standard
		- Efficiency in the C++ Thread Library
		- Platform-specific facilities
	- Getting started
		- Hello, Concurrent World
	- Summary
- **2. Managing threads**
	- Basic thread management
		- Launching a thread
		- Waiting for a thread to complete
		- Waiting in exceptional circumstances
		- Running threads in the background
	- Passing arguments to a thread function
	- Transferring ownership of a thread
	- Choosing the number of threads at runtime
	- Identifying threads
	- Summary
- **3. Sharing data between threads**
	- Problems with sharing data between threads
		- Race conditions
		- Avoiding problematic race conditions
	- Protecting shared data with mutexes
		- Using mutexes in C++
		- Structuring code for protecting shared data
		- Spotting race conditions inherent in interfaces
		- Deadlock: the problem and a solution
		- Further guidelines for avoiding deadlock
		- Flexible locking with `std::unique_lock`
		- Transferring mutex ownership between scopes
		- Locking at an appropriate granularity
	- Alternative facilities for protecting shared data
		- Protecting shared data during initialization
		- Protecting rarely updated data structures
		- Recursive locking
	- Summary
- **4. Synchronizing concurrent operations**
	- Waiting for an event or other condition
		- Waiting for a condition with condition variables
		- Building with a thread-safe queue with condition variables
	- Waiting for one-off events with features
		- Returning values from background tasks
		- Associating a task with a future
		- Making `(std::)promises`
		- Saving an exception for the future
		- Waiting for multiple threads
	- Waiting with a time limit
		- Clocks
		- Durations
		- Time points
		- Functions that accept timeouts
	- Using synchronization of operations to simplify code
		- Functional programming with futures
		- Synchronizing operations with message passing
	- Summary
- **5. The C++ memory model and operations on atomic types**
	- Memory model basics
		- Objects andd memory locations
		- Objects, memory locations and concurrency
		- Modification orders
	- Atomic operations and types in C++
		- The standard atomic types
		- Operations on `std::atomic_flag`
		- Operations on `std::atomic<bool>`
		- Operations on `std::atomic<T*>` : pointer arithmetic
		- Operations on standard atomic integral types
		- The `std::atomic<>` primary class template
		- Free functions for atomic operations
	- Summary
- **6. Designing lock-based concurrent data structures**
	- What does it mean to design for concurrency?
		- Guidelines for designing data structures for concurrency
	- Lock-based concurrency data structures
		- A thread-safe stack using locks
		- A thread-safe queue using locks and condition variables
		- A thread-safe queue using fine-grained locks and condition variables
	- Designing more complex lock-based data structures
		- Writing a thread-safe lookup table using locks
		- Writing a thread-safe list using locks
	- Summary
- **7. Designing lock-free concurrent data structures**
	- Definitions and consequences
		- Types of non-blocking data structures
		- Lock-free data structures
		- Wait-free data structures
		- The pros and cons of lock-free data structures
	- Examples of lock-free data structures
		- Writing a thread-safe stack without locks
		- Stopping those pesky leaks: managing memory in lock-free data structures
		- Detecting nodes that can't be reclaimed using hazard pointers
		- Detecting nodes in use with reference counting
		- Applying the memory model to the lock-free stack
		- Waiting for a thread-safe queue without locks
	- Guidelines for writing lock-free data structures
		- Guideline: use `std::memory_order_seq_cst` for prototyping
		- Guideline: use a lock-free memory reclamation scheme
		- Guideline: watch out for the ABA problem
		- Guideline: identify busy-wait loops and help the other thread
	- Summary
- **8. Designing concurrent code**
	- Techniques for dividing work between threads
		- Dividing data between threads before processing begins
		- Dividing data recursively
		- Dividing data by task types
	- Factors affecting the performance of concurrent code
		- How many processors?
		- Data contention and cache ping-pong
		- False sharing
		- How close is your data?
		- Oversubscription and execessive task switching
	- Designing data structures for multithreaded performance
		- Dividing array elements for complex operations
		- Data access patterns in other data structures
	- Additional consideration when designing for concurrency
		- Exception safety in parallel algorithms
		- Scalability and Amdahl's law
		- Hiding latency with multiple threads
		- Improving responsiveness with concurrency
	- Design concurrent code in practice
		- A parallel implemenation of `std::for_each`
		- A parallel implemenation of `std::find`
		- A parallel implemenation of `std::partial_sum`
	- Summary
- **9. Advanced thread management**
	- Thread pools
		- The simplest thread pool
		- Waiting for tasks submitted to a thread pool
		- Tasks that wait for other tasks
		- Avoiding contention on the work queue
		- Work stealing
	- Interrupting threads
		- Launching and interrupting another thread
		- Detecting that a thread has been interrupted
		- Interrupting a condition variable wait
		- Interrupting a wait on `std::condition_varaible_any`
		- Interrupting other blocking calls
		- Handling interruptions
		- Interrupting background tasks on application exit
	- Summary
- **10. Testing and debugging multithreaded applications**
	- Types of concurrency-related bugs
		- Unwanted blocking
		- Race conditions
	- Techniques for locating concurrency-related bugs
		- Reviewing code to locate potential bugs
		- Locating concurrency-related bugs by testing
		- Designing for testability
		- Multithreaded testing techniques
		- Structuring multithreaded test code
		- Testing the performance of multithreaded code
	- Summary

## Preface






















