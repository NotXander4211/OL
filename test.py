class Fruit:
    def __init__(self, value) -> None:
        self._value = value
    @property #getter
    def orange(self):
        print("Getting value")
        return self._value
    @orange.setter
    def orange(self, nval):
        print(f"Setting val to: {nval}")
        self._value = nval
orange = Fruit("Not an orange")
print(orange.orange)
orange.orange = "An orange"
print(orange.orange)
