
class Person:
    # weak private
    # we want to tuse the variabel internnally and not externally.
    _name="no name"
    def setName(self,name):
        self._name=name
        print(f"name is set to {self._name}")
    # strong private
    def _think(self):
        print("Thinking to myself")
    def work(self):
        self._think()

class Child(Person):
    def testDouble(self):
        self._think()
