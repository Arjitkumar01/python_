# ============================================================
#         PYTHON OOP - 100 PRACTICE QUESTIONS
#   Encapsulation(20) | Abstraction(20) | Polymorphism(20)
#          Inheritance(20) | Mixed(20)
# ============================================================


# ════════════════════════════════════════════════════════════
#   SECTION 1 : ENCAPSULATION  (Q1 – Q20)
# ════════════════════════════════════════════════════════════
# Encapsulation = wrapping data (attributes) and methods
# together inside a class and restricting direct access
# using private (__) or protected (_) members.

# Q1.  Create a class Person with private attributes __name and __age.
#      Add getter methods get_name() and get_age() to access them.
#      Create an object and print both values using getters.



# Q2.  Extend Q1 — add setter methods set_name() and set_age().
#      The setter for age should print an error if age < 0.

# Q3.  Create a class BankAccount with a private attribute __balance.
#      Add methods:
#        deposit(amount)   → adds to balance
#        withdraw(amount)  → deducts if sufficient, else prints error
#        get_balance()     → returns balance
#      Do NOT allow direct access to __balance from outside.

# Q4.  Create a class Student with private __marks (a list).
#      Add:
#        add_mark(m)    → append to __marks
#        get_average()  → return average
#        get_highest()  → return highest mark
#      Access __marks only through these methods.

# Q5.  Create a class Car with private __speed.
#      Add:
#        accelerate(amount)  → increases speed (max 200)
#        brake(amount)       → decreases speed (min 0)
#        get_speed()         → returns current speed
#      Speed should never go below 0 or above 200.

# Q6.  What is the difference between a private attribute (__)
#      and a protected attribute (_)?
#      Write a class Employee to demonstrate both.
#      Show which can be accessed outside the class and which cannot.

# Q7.  Create a class Temperature with private __celsius.
#      Add:
#        set_celsius(value)   → sets value (raise error if < -273.15)
#        get_celsius()        → returns celsius
#        get_fahrenheit()     → returns converted value
#        get_kelvin()         → returns converted value

# Q8.  Create a class Wallet with private __balance and __owner.
#      Add a method transfer(other_wallet, amount) that moves
#      amount from this wallet to another Wallet object.

# Q9.  Create a class SecretBox with a private __secret string.
#      Add a method reveal(password) that returns the secret
#      only if the correct password is passed, else "Access Denied".

# Q10. Create a class Counter with a private __count = 0.
#      Add:
#        increment()   → count += 1
#        decrement()   → count -= 1 (but never below 0)
#        reset()       → count = 0
#        get_count()   → returns count
#      count should never go negative.

# Q11. Demonstrate name mangling in Python.
#      Create a class MyClass with a private attribute __value.
#      Show that __value cannot be accessed as obj.__value but
#      CAN be accessed using obj._MyClass__value.
#      Write a comment explaining why this happens.

# Q12. Create a class ATM with private __pin and __balance.
#      Add a method withdraw(entered_pin, amount) that checks
#      the pin first and only allows withdrawal if pin matches.

# Q13. Create a class Profile with private __email and __password.
#      Add:
#        change_password(old_pass, new_pass) → changes only if old matches
#        get_email()                         → returns email
#        is_valid_login(email, password)     → returns True/False

# Q14. Create a class Inventory with private __items (a dictionary).
#      Add:
#        add_item(name, qty)    → adds/updates item
#        remove_item(name)      → removes item if exists
#        get_quantity(name)     → returns quantity
#        display_all()          → prints all items

# Q15. Create a class Rectangle with private __length and __width.
#      Use @property decorator to create:
#        length   → getter + setter (setter raises error if <= 0)
#        width    → getter + setter (setter raises error if <= 0)
#        area     → read-only property
#        perimeter → read-only property

# Q16. Create a class Ticket with private __seat_number and __is_booked.
#      Add:
#        book()    → marks ticket as booked (error if already booked)
#        cancel()  → marks as not booked (error if not booked)
#        status()  → returns "Booked" or "Available"

# Q17. Create a class PasswordManager with a list of private
#      __passwords. Add:
#        add_password(site, pwd)   → stores password for a site
#        get_password(site, master_key) → returns password only if
#                                         master_key == "admin123"
#        list_sites()              → returns list of site names only

# Q18. Create a class Circle using @property:
#      - radius (getter + setter, raise ValueError if < 0)
#      - diameter (read-only → 2 * radius)
#      - area (read-only → π * r²)
#      Show that changing radius automatically updates area and diameter.

# Q19. Create a class Employee with protected _name and _salary
#      (single underscore). Create a subclass Manager that accesses
#      and modifies _salary directly.
#      Discuss: why is it only a convention and not enforced?

# Q20. Create a class LoggedAccess where every time a private
#      attribute __value is read or written through getters/setters,
#      it prints a log message like:
#        "Reading value: 42"
#        "Writing value: 99"


# ════════════════════════════════════════════════════════════
#   SECTION 2 : ABSTRACTION  (Q21 – Q40)
# ════════════════════════════════════════════════════════════
# Abstraction = hiding complex implementation details and
# showing only the essential features.
# In Python, use the abc module (Abstract Base Classes).

# Q21. Import ABC and abstractmethod from the abc module.
#      Create an abstract class Shape with an abstract method area().
#      Create two subclasses: Square and Triangle that implement area().
#      Create objects of both and print their areas.

# Q22. Create an abstract class Animal with abstract methods:
#        speak()  → should print the animal's sound
#        move()   → should print how it moves
#      Create subclasses: Dog, Bird, Fish — each implementing both.

# Q23. Try to create an object of an abstract class directly.
#      Write the code and show the error in a comment.
#      Explain WHY Python raises this error.

# Q24. Create an abstract class Vehicle with:
#        abstract method: start_engine()
#        abstract method: stop_engine()
#        concrete method: status() → prints "Vehicle is ready"
#      Create subclasses Car and Bike that implement the abstract methods.

# Q25. Create an abstract class Payment with abstract method process(amount).
#      Add a concrete method receipt(amount) that prints a receipt.
#      Create subclasses: CreditCard, UPI, Cash.
#      Each should implement process() and can also call receipt().

# Q26. Create an abstract class DatabaseConnector with:
#        abstract method: connect()
#        abstract method: disconnect()
#        abstract method: execute(query)
#        concrete method: log(msg) → prints "[LOG]: msg"
#      Create a subclass MySQLConnector that implements all abstract methods.

# Q27. Create an abstract class Notification with abstract method send().
#      Create subclasses: EmailNotification, SMSNotification, PushNotification.
#      Write a function notify_all(notifications, message) that calls
#      send() on each notification object in the list.

# Q28. Create an abstract class FileHandler with:
#        abstract methods: open_file(), close_file(), read_file()
#      Create subclasses: TextFileHandler and CSVFileHandler.
#      Each should print what it does without actual file I/O.

# Q29. Create an abstract class Sorter with abstract method sort(arr).
#      Create subclasses:
#        BubbleSorter   → implements bubble sort
#        SelectionSorter → implements selection sort
#      Both return the sorted array.

# Q30. Demonstrate that a class with even ONE unimplemented abstract
#      method cannot be instantiated.
#      Write a class PartialImpl that inherits from Shape (Q21)
#      but only implements area(), NOT perimeter().
#      Try creating an object and show the result.

# Q31. Create an abstract class Logger with:
#        abstract method: log(message)
#      Create subclasses:
#        ConsoleLogger  → prints to console
#        FileLogger     → "writes" to a file (just print the action)
#      Write a function run_app(logger) that takes any logger and logs 3 messages.

# Q32. Create an abstract class Robot with abstract methods:
#        walk(), talk(), charge()
#      Create two types: HomeRobot and IndustrialRobot.
#      Each implements the methods differently.

# Q33. Create an abstract class Converter with abstract method convert(value).
#      Create subclasses:
#        KmToMiles    → multiplies by 0.621
#        CelsiusToF   → formula (v * 9/5) + 32
#        KgToPounds   → multiplies by 2.205

# Q34. Create an abstract class Game with:
#        abstract methods: start(), play(), end()
#        concrete method: run() → calls start(), play(), end() in order
#      Create subclasses: Chess and Cricket.
#      Call run() on both and see the sequence.

# Q35. Create an abstract class Authenticator with abstract method authenticate(user, pwd).
#      Create subclasses:
#        BasicAuthenticator   → checks user == "admin" and pwd == "1234"
#        TokenAuthenticator   → checks if token starts with "Bearer "
#      Return True/False from both.

# Q36. Create an abstract class Shape3D with abstract methods:
#        volume(), surface_area()
#      Create subclasses: Sphere, Cube, Cylinder.
#      Use math module for calculations.

# Q37. Create an abstract class Iterator with abstract methods:
#        has_next() → returns True/False
#        next()     → returns next element
#      Create a NumberIterator(start, end) that iterates from start to end.

# Q38. Create an abstract class TaxCalculator with abstract method calculate_tax(income).
#      Create subclasses:
#        IndividualTax  → 10% if income < 500000 else 20%
#        CorporateTax   → flat 30%
#      Print the tax amount for a given income.

# Q39. Create an abstract class Validator with abstract method validate(value).
#      Create subclasses:
#        EmailValidator  → checks if "@" and "." in value
#        AgeValidator    → checks if 0 < value < 120
#        PhoneValidator  → checks if value is 10 digits (all numbers)

# Q40. Create an abstract class ReportGenerator with abstract method generate(data).
#      Create subclasses: PDFReport, ExcelReport, HTMLReport.
#      Each should print how it would generate the report with the given data.


# ════════════════════════════════════════════════════════════
#   SECTION 3 : POLYMORPHISM  (Q41 – Q60)
# ════════════════════════════════════════════════════════════
# Polymorphism = "many forms" — the same method name behaves
# differently based on the object calling it.
# Types: Method Overriding, Duck Typing, Operator Overloading

# Q41. Create a base class Animal with method speak().
#      Create subclasses Dog, Cat, Cow — each overrides speak().
#      Create a list with one of each and call speak() in a loop.
#      This demonstrates RUNTIME polymorphism.

# Q42. Create a function make_sound(animal) that calls animal.speak().
#      Pass Dog, Cat, and Cow objects to it.
#      This demonstrates DUCK TYPING — no inheritance needed.

# Q43. Create a class Calculator with multiple versions of add():
#      Python doesn't support method overloading directly.
#      Use default arguments to simulate it:
#        add(a, b=0, c=0) → returns a + b + c
#      Show it works with 1, 2, and 3 arguments.

# Q44. Create a class Vector with:
#        __add__(other)  → Vector + Vector
#        __sub__(other)  → Vector - Vector
#        __mul__(other)  → Vector * scalar (number)
#        __str__()       → "Vector(x, y)"
#      This demonstrates OPERATOR OVERLOADING.

# Q45. Create a class Fraction with:
#        __add__, __sub__, __mul__, __truediv__
#        __eq__  → equality check
#        __str__ → "num/den"
#      Test all operations.

# Q46. Create a class Book with __len__() returning number of pages,
#      __str__() returning "Title by Author",
#      __eq__() returning True if both title and author match.
#      Test len(), print(), and == operator on Book objects.

# Q47. Create a class Temperature with __lt__, __gt__, __eq__
#      based on celsius value.
#      Sort a list of Temperature objects using sorted().

# Q48. Create a base class Employee with method get_salary().
#      Create subclasses:
#        FullTime(salary)           → returns salary
#        PartTime(hourly, hours)    → returns hourly * hours
#        Freelancer(rate, projects) → returns rate * projects
#      Demonstrate polymorphism by calling get_salary() on all.

# Q49. Create classes Square, Rectangle, Triangle — none inheriting
#      from each other. Each has an area() method.
#      Write a function total_area(shapes) that sums all areas.
#      This is pure DUCK TYPING polymorphism.

# Q50. Create a class Matrix with:
#        __add__   → matrix addition
#        __mul__   → matrix * scalar
#        __str__   → formatted grid
#      Test adding two matrices and multiplying by a scalar.

# Q51. Create a class StringWrapper that wraps a string and overloads:
#        __add__   → concatenate two StringWrappers
#        __mul__   → repeat the string n times
#        __len__   → length of the string
#        __contains__ → check if substring exists (in operator)

# Q52. Create a class Animal with speak() returning "...".
#      Create Dog, Cat overriding speak().
#      Now create a class AnimalFactory with a static method
#      get_animal(type) that returns the correct object.
#      Call speak() on the returned object.

# Q53. Create a class Shape with method draw() → "Drawing shape".
#      Create Circle, Rectangle, Triangle overriding draw().
#      Write a function render_all(shapes) that calls draw() on each.
#      Add a new class Pentagon without changing render_all().
#      This shows how polymorphism makes code OPEN for extension.

# Q54. Demonstrate polymorphism with built-in functions:
#      - len()    works on str, list, tuple, dict
#      - str()    works on int, float, list, custom class
#      - +        works on int, float, str, list
#      Write examples for each and explain in comments.

# Q55. Create a class Person and override __str__ and __repr__.
#      Show the difference:
#        str(obj)  → user-friendly string
#        repr(obj) → developer-friendly string
#      Place objects in a list and print the list (uses __repr__).

# Q56. Create a class SmartList that wraps a list and overloads:
#        __add__      → merge two SmartLists
#        __contains__ → check if item exists
#        __getitem__  → access by index
#        __len__      → number of items
#        __str__      → formatted string

# Q57. Create classes Plugin1, Plugin2, Plugin3 — all with a
#      method run(data). Write a class PluginManager that stores
#      a list of plugins and calls run(data) on each.
#      Add a new Plugin4 without changing PluginManager.

# Q58. Create a class Animal with method describe() that uses
#      self.__class__.__name__ to print the class name dynamically.
#      Inherit Dog and Cat from Animal (don't override describe()).
#      Show that d.describe() prints "Dog" and c.describe() prints "Cat".

# Q59. Create a class Number that overloads:
#        __add__, __sub__, __mul__, __floordiv__, __mod__
#        __pow__    → ** operator
#        __abs__    → abs() function
#        __neg__    → unary minus (-obj)
#      Test all operators.

# Q60. Create two completely unrelated classes Parrot and Airplane.
#      Both have a method fly().
#      Write a function lift_off(obj) that calls obj.fly().
#      Pass both objects to it and show it works.
#      Write a comment explaining duck typing: "If it flies like a duck..."


# ════════════════════════════════════════════════════════════
#   SECTION 4 : INHERITANCE  (Q61 – Q80)
# ════════════════════════════════════════════════════════════
# Inheritance = a class (child) derives attributes and methods
# from another class (parent), promoting code reuse.

# Q61. Create a base class Animal with attributes name and sound,
#      and a method speak() → prints "<name> says <sound>".
#      Create subclasses Dog and Cat with appropriate sounds.
#      Create objects of both and call speak().

# Q62. Create a class Vehicle with attributes make, model, year
#      and method description() → returns a formatted string.
#      Create a subclass Car with extra attribute num_doors.
#      Override description() to include num_doors.
#      Use super() to call the parent method inside.

# Q63. Create a class Person with __init__(name, age) and method greet().
#      Create a subclass Student with extra attribute student_id.
#      Use super().__init__() to initialize name and age.
#      Add method study() → prints "student_id is studying".

# Q64. Create a class Shape with method area() → returns 0.
#      Create subclasses Circle, Rectangle, Triangle — each overrides area().
#      Write a function largest_area(shapes) that returns the shape
#      with the maximum area from a list.

# Q65. Create a class Employee with name and salary.
#      Create a subclass Manager with an extra attribute department.
#      Create a subclass Director that inherits from Manager and
#      adds a budget attribute.
#      This is MULTI-LEVEL inheritance. Print all attributes.

# Q66. Create classes Flyable and Swimmable with methods fly() and swim().
#      Create a class Duck that inherits from BOTH (multiple inheritance).
#      Also add method quack().
#      This is MULTIPLE inheritance.

# Q67. Demonstrate Python's MRO (Method Resolution Order):
#      Create class A with method hello() → "Hello from A".
#      Create B(A) and C(A), both override hello().
#      Create D(B, C).
#      Call D().hello() and print D.__mro__ to see the order.

# Q68. Create a base class BankAccount with:
#        __init__(owner, balance)
#        deposit(amount)
#        withdraw(amount)
#        get_balance()
#      Create subclasses:
#        SavingsAccount → adds interest_rate, method add_interest()
#        CurrentAccount → adds overdraft_limit, allows going negative

# Q69. Create a class Animal with method eat() and sleep().
#      Create a subclass Mammal that adds breathe().
#      Create a subclass Dog that adds bark().
#      Show that a Dog object can call eat(), sleep(), breathe(), bark().

# Q70. Create a class Library with a list of books.
#      Add methods: add_book(), remove_book(), list_books().
#      Create a subclass DigitalLibrary that also has e_books list.
#      Override list_books() to show both physical and digital books.
#      Use super() to print physical books first.

# Q71. Create a class Appliance with attributes brand and power_watts.
#      Add method power_consumption(hours) → returns watts * hours / 1000 (kWh).
#      Create subclasses: WashingMachine, Refrigerator, AirConditioner.
#      Each adds its own attribute and overrides power_consumption() if needed.

# Q72. Create a class Person with method introduce().
#      Create a subclass Teacher with subject attribute.
#      Create another subclass Principal that inherits from Teacher
#      and adds school_name. Override introduce() at each level using super().

# Q73. Demonstrate method overriding completely:
#      Create class Parent with methods greet(), farewell(), and info().
#      In Child, override only greet().
#      Show that Child uses its own greet() but inherits farewell() and info().

# Q74. Create a class Collection with __init__(items=[]) and methods:
#        add(item), remove(item), contains(item), size()
#      Create subclasses UniqueCollection (no duplicates) and
#      SortedCollection (always sorted). Override add() in both.

# Q75. Create a class Game with methods start(), pause(), resume(), end().
#      Create subclasses: VideoGame and BoardGame.
#      VideoGame adds save_progress() and load_progress().
#      BoardGame adds roll_dice() and move_piece().

# Q76. Create a class Food with attributes name, calories, price.
#      Create subclasses: Vegetarian and NonVegetarian.
#      Add a class method create_combo(food1, food2) that returns a
#      new Food object with combined name, calories, and price.

# Q77. Create a class Node and a class LinkedList using inheritance:
#      BaseList → defines interface (abstract-like)
#      LinkedList inherits BaseList and implements:
#        append(), prepend(), delete(), display()

# Q78. Create a class EventHandler with method handle(event).
#      Create subclasses: ClickHandler, KeyboardHandler, TouchHandler.
#      Each handles a specific event type.
#      Write a function dispatch(handler, event) that calls handle().

# Q79. Create a class Product with attributes name, price, quantity.
#      Create subclasses: PhysicalProduct (adds weight, shipping_cost())
#      and DigitalProduct (adds file_size, download_url).
#      Override a method get_details() in both.

# Q80. Create a class Animal with a class variable count = 0 that
#      increments every time an Animal or subclass object is created.
#      Create subclasses Dog and Cat.
#      Show that Animal.count tracks ALL objects (Animal + Dog + Cat).


# ════════════════════════════════════════════════════════════
#   SECTION 5 : MIXED OOP QUESTIONS  (Q81 – Q100)
# ════════════════════════════════════════════════════════════
# These questions combine multiple OOP concepts together.

# Q81. Create a class Vehicle (encapsulation: private __speed).
#      Create subclass Car (inheritance).
#      Create subclass ElectricCar (multi-level).
#      Each adds a method. Show encapsulation by using getters/setters.

# Q82. Create an abstract class Shape (abstraction).
#      Create Circle and Rectangle (inheritance + abstraction).
#      Overload + operator to merge two shapes into a combined area object.
#      (polymorphism + operator overloading)

# Q83. Create a class Animal with speak() (polymorphism).
#      Use encapsulation to store __sound privately.
#      The speak() method uses the private sound via a getter.
#      Create Dog and Cat that set their sounds in __init__.

# Q84. Create a class Person with @property name and age (encapsulation).
#      Create a subclass Employee (inheritance) with @property salary.
#      Create a subclass Manager (multi-level) with @property bonus.
#      Use super() at each level.

# Q85. Create an abstract class Sorter (abstraction) with abstract
#      method sort(arr). Create BubbleSorter and MergeSorter (inheritance).
#      Write a function run_sort(sorter, arr) (duck typing / polymorphism).
#      Each sorter should return the sorted array.

# Q86. Implement the Strategy Pattern using OOP:
#      Abstract class DiscountStrategy with abstract method apply(price).
#      Create: NoDiscount, PercentageDiscount(percent), FlatDiscount(amount).
#      Create class Shop with a method set_strategy(strategy) and
#      get_final_price(price) that applies the strategy.

# Q87. Implement the Template Method Pattern:
#      Abstract class DataMigration with:
#        template method: migrate() → calls extract(), transform(), load()
#        abstract methods: extract(), transform(), load()
#      Create subclasses: CSVMigration, JSONMigration.

# Q88. Create a class Stack (encapsulation: private __items list).
#      Overload operators (polymorphism):
#        +  → merge two stacks
#        len() → size of stack
#        in  → check if item is in stack
#        str() → string representation
#      Add push(), pop(), peek() methods.

# Q89. Create a Singleton class DatabaseConnection (only one instance).
#      Override __new__(). Add methods: connect(), query(sql), disconnect().
#      Show that two variables point to the same object.
#      This combines encapsulation (private _instance) + special methods.

# Q90. Create an abstract class Iterator (abstraction) with
#      abstract methods __iter__() and __next__().
#      Create EvenIterator(start, end) and OddIterator(start, end).
#      Use them in a for loop to print even/odd numbers in a range.

# Q91. Create a class Product (encapsulation: private __price).
#      Create a subclass DiscountedProduct (inheritance) that overrides
#      get_price() to apply a discount percentage.
#      Create a subclass PremiumProduct with extra features.
#      Print prices of all three using polymorphism in a loop.

# Q92. Create a class Logger (abstract) with abstract method log(msg).
#      Create ConsoleLogger, FileLogger, DatabaseLogger.
#      Create a class Application that accepts a logger in __init__
#      and uses it. Swap loggers at runtime — this is DEPENDENCY INJECTION.

# Q93. Create a class Event with encapsulated private __attendees list.
#      Create a subclass OnlineEvent with __meeting_link.
#      Create a subclass OfflineEvent with __venue.
#      Both override a method get_details() (polymorphism).
#      Use @property for all private attributes.

# Q94. Create a class Number with overloaded comparison operators:
#        __lt__, __le__, __gt__, __ge__, __eq__, __ne__
#      Use @functools.total_ordering to reduce boilerplate (only define
#      __eq__ and __lt__, the rest are auto-generated).

# Q95. Implement the Observer Pattern:
#      Class Subject with: subscribe(observer), unsubscribe(observer), notify(data)
#      Abstract class Observer with abstract method update(data).
#      Create EmailObserver, SMSObserver, LogObserver.
#      When Subject.notify() is called, all observers get updated.

# Q96. Create a class Matrix (encapsulation: private __data).
#      Overload (polymorphism):
#        +  → matrix addition
#        *  → matrix multiplication
#        [] → __getitem__ to access element by (row, col)
#        str → formatted grid
#      Create a subclass SquareMatrix (inheritance) with method determinant().

# Q97. Create a class Animal abstract class with abstract speak().
#      Create Dog (domestic=True), Wolf (domestic=False).
#      Override __str__ to show name + domestic status.
#      Create a class Zoo with:
#        add_animal(animal)
#        __iter__  → iterate over animals
#        __len__   → number of animals
#        __str__   → list all animals

# Q98. Create a class Graph using encapsulation (private __adj_list).
#      Add methods: add_vertex, add_edge, get_neighbors.
#      Create a subclass WeightedGraph (inheritance) that stores
#      edge weights. Override add_edge(u, v, weight).
#      Add method shortest_path_cost(u, v) using a greedy approach.

# Q99. Create a class Config (Singleton pattern) that stores
#      application settings in a private __settings dict.
#      Add methods: set(key, value), get(key), get_all().
#      Demonstrate that all parts of the program share the same config.

# Q100. Design a mini Library Management System using all 4 OOP pillars:
#       - Encapsulation : Book class with private __title, __isbn, __available
#       - Abstraction   : Abstract class LibraryItem with abstract methods
#                         checkout() and return_item()
#       - Inheritance   : Book and Magazine inherit from LibraryItem
#       - Polymorphism  : Both implement checkout() and return_item()
#                         differently. A function process(item) calls
#                         checkout() on any LibraryItem.
#       Add a Library class that manages a list of LibraryItems.
