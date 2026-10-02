## Reflection

1. Where would Multiply belong?

Multiply would belong in calculation.py with the other calculation classes. I would register it in the operations dictionary in cli.py so the calculator recognizes the multiply command. I would also update the help message to include multiply and add tests for multiplication in test_calculation.py.
History would not need any multiplication logic because its job is only to store, return, and remove calculation objects. It does not need to know how each calculation works.

2. Email and Text Notifications

Email and text-message notification objects could share a send() method:
notification.send(message)

Each type would implement send() differently, but the rest of the program could use the same send() contract without needing to know how the message is delivered.

3. What Transfers to Another Language?

Design concepts such as classes, inheritance, abstraction, polymorphism, separation of responsibilities, and testing would transfer to another programming language.

I would still need to learn that language's syntax, type system, package structure, exception handling, testing tools, and runtime rules.