class Example:
    a = 5  # public
    _b = 6  # protected
    __c = 7  # private
    __d = 8


Example()
print(Example.a)
print(Example._b)
print(Example._Example__c)
print(Example._Example__d)