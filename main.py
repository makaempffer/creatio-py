def run():
    comp = Component()
    comp2 = Component()
    comp.set_linked_component(comp2)
    comp.set_data("This is comp data!")
    print(comp.data)
    print("this is comp2 data ->", comp2.data)
    comp.pass_data_to_linked()
    print("This is comp2 data after pass ->", comp2.data)
    comp.update_linked_state()




class Component:
    def __init__(self):
        self.state = False
        self.data = None
        self.linked_component: Component = None

    def set_linked_component(self, component):
        self.linked_component = component
        print("[LINK] -> Link set.")

    def set_data (self, data):
        self.data = data

    def set_state(self, new_state):
        self.state = new_state
    
    def switch_state(self):
        self.state = not self.state
    
    def get_data(self):
        print(self.data)

    def get_state(self):
        print(self.state)

    def pass_data_to_linked(self):
        self.linked_component.set_data(self.data)
        print("[LINK] -> Data passed.")

    def update_linked_state(self):
        if self.linked_component == None:
            return
        self.linked_component.switch_state()
        print("[LINK] -> Linked state updated.")

if __name__ == "__main__":
    run()
    
