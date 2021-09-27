
class Person:
    # weak private
    # we want to tuse the variabel internnally and not externally.
    _name="no name"
    def setName(self,name):
        self._name=name
        print(f"name is set to {self._name}")