# Practical-DSA
Real-world applications of Data Structures and Algorithms implemented primarily in Python, with performance-critical scripts in C++. Focused on system design context, trade-offs, and the why behind every technical choice.

## Stack.py: An interactive and efficient stack implementation using python
### Key Paradigms & Efficiency Highlights

* **O(1) Dynamic Operations:** Uses Python's built-in dynamic list methods (`append` and `pop`) operating strictly at the end of the array, preventing memory-shifting overhead ($O(N)$) associated with front insertions.
* **Command Pattern via Dispatcher:** Implemented a functional dictionary dispatcher mapping user input commands directly to stack methods, achieving $O(1)$ command routing while avoiding rigid `if-elif-else` control flow blocks.
* **Encapsulated Class Architecture:** Encapsulates internal stack state (`items`, `size`) into a modular, reusable object-oriented class instance equipped with strict capacity bounds checking (`isfull` and `isempty`).
* **Robust Input Sanitization:** Includes defensive error handling using a `try-except` retry loop to validate stack sizing before allocation.