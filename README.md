# Exercise 6.5 Santa's Workshop

We'll practise wrapping gifts in this exercise. Let's create the classes `Gift` and `Package`. The gift has a name and weight, and the package contains gifts.

## Gift-class

Create a `Gift` class, where the objects instantiated from it represent different kinds of gifts. The information that's recorded is the name and weight of the item (kg).

Add the following methods to the class:

- Constructor for which the name and weight of the gift are given as parameters
- Method `def get_name()`, which returns the name of the gift
- Method `def get_weight()`, which returns the weight of the gift
- Method `def __str__()`, which returns a string in the form "name (weight kg)"

The following is an example of the class in use:

```python
def main():
    Gift book = Gift("Harry Potter and the Philosopher's Stone", 2)

    print("Gift's name: " + book.get_name())
    print("Gift's weight: " + book.get_weight())

    print("Gift: " + book)
```
The program's print output should be as follows:

```plaintext
Gift's name: Harry Potter and the Philosopher's Stone
Gift's weight: 2
Gift: Harry Potter and the Philosopher's Stone (2 kg)
```

## Package-class

Create a `Package` class to which gifts can be added, and that keeps track of the total weight of the gifts in the package. The class should contain:

- A parameterless constructor
- Method `def add_gift(self, gift)`, which adds the gift passed as a parameter to the package. The method returns no value.
- Method `def total_weight()`, which returns the total weight of the package's gifts.

It's recommended to store the items in a `list` object.

```python
gifts = []
```

An example use case of the class is as follows:

```python
def main():
    book = Gift("Harry Potter and the Philosopher's Stone", 2)

    Ppackage = Package()
    package.add_gift(book)
    print(package.total_weight())
```

The program's output should be the following:

```plaintext
2
```
