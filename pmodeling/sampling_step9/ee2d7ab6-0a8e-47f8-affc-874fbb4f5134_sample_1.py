import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Client_Consult = Transition(label='Client Consult')
Spec_Gathering = Transition(label='Spec Gathering')
Supplier_Sourcing = Transition(label='Supplier Sourcing')
Design_Review = Transition(label='Design Review')
Simulation_Test = Transition(label='Simulation Test')
Proto_Assembly = Transition(label='Proto Assembly')
Quality_Check = Transition(label='Quality Check')
Firmware_Flash = Transition(label='Firmware Flash')
Sensor_Install = Transition(label='Sensor Install')
Final_Testing = Transition(label='Final Testing')
Brand_Packaging = Transition(label='Brand Packaging')
Shipping_Prep = Transition(label='Shipping Prep')
Delivery_Schedule = Transition(label='Delivery Schedule')
Client_Training = Transition(label='Client Training')
Diagnostics_Setup = Transition(label='Diagnostics Setup')
skip = SilentTransition()

# Define the exclusive choice between prototype assembly and quality check
xor = OperatorPOWL(operator=Operator.XOR, children=[Proto_Assembly, Quality_Check])

# Define the loop for firmware flash, sensor install, and final testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[Firmware_Flash, Sensor_Install, Final_Testing])

# Define the partial order model
root = StrictPartialOrder(nodes=[Client_Consult, Spec_Gathering, Supplier_Sourcing, Design_Review, Simulation_Test, xor, loop, Brand_Packaging, Shipping_Prep, Delivery_Schedule, Client_Training, Diagnostics_Setup])
root.order.add_edge(Client_Consult, Spec_Gathering)
root.order.add_edge(Spec_Gathering, Supplier_Sourcing)
root.order.add_edge(Supplier_Sourcing, Design_Review)
root.order.add_edge(Design_Review, Simulation_Test)
root.order.add_edge(Simulation_Test, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, Brand_Packaging)
root.order.add_edge(Brand_Packaging, Shipping_Prep)
root.order.add_edge(Shipping_Prep, Delivery_Schedule)
root.order.add_edge(Delivery_Schedule, Client_Training)
root.order.add_edge(Client_Training, Diagnostics_Setup)