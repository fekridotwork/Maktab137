class Publisher:

    def __init__(self):
        self.observers = []   
        self.state = None     

    def add_observer(self, observer):
        self.observers.append(observer)
        print(f"Observer with the name of \"{observer.name}\" added.")

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            print(f"\nObserver \"{observer.name}\" removed.")
        else:
            print(f"Observer \"{observer.name}\" not found!")

    def change_state(self, new_value):
        print(f"\nPublisher state changed to: {new_value}\n")
        self.state = new_value
        self.notify_all()

    def notify_all(self):
        print(f"Notifying {len(self.observers)} observers.")
        for obs in self.observers:
            obs.update(self.state)


class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, new_value):
        print(f"Observer received new value: {new_value}")




publisher = Publisher()
matin = Observer("َMatin")
amirali = Observer("Amirali")

publisher.add_observer(matin)
publisher.add_observer(amirali)

publisher.change_state(5)
publisher.remove_observer(amirali)
publisher.change_state(10)
