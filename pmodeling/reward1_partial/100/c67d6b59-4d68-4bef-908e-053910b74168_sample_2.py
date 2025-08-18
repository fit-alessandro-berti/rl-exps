import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Client_Meet = Transition(label='Client Meet')
Design_Draft = Transition(label='Design Draft')
Vendor_Select = Transition(label='Vendor Select')
Component_Order = Transition(label='Component Order')
Parts_Inspect = Transition(label='Parts Inspect')
Frame_Build = Transition(label='Frame Build')
Wiring_Setup = Transition(label='Wiring Setup')
Software_Load = Transition(label='Software Load')
Flight_Sim = Transition(label='Flight Sim')
Quality_Test = Transition(label='Quality Test')
Feedback_Review = Transition(label='Feedback Review')
Adjust_Design = Transition(label='Adjust Design')
Compliance_Check = Transition(label='Compliance Check')
Packaging_Prep = Transition(label='Packaging Prep')
Final_Demo = Transition(label='Final Demo')
Ship_Drone = Transition(label='Ship Drone')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Client_Meet,
    Design_Draft,
    Vendor_Select,
    Component_Order,
    Parts_Inspect,
    Frame_Build,
    Wiring_Setup,
    Software_Load,
    Flight_Sim,
    Quality_Test,
    Feedback_Review,
    Adjust_Design,
    Compliance_Check,
    Packaging_Prep,
    Final_Demo,
    Ship_Drone
])

# Add dependencies
root.order.add_edge(Client_Meet, Design_Draft)
root.order.add_edge(Client_Meet, Vendor_Select)
root.order.add_edge(Design_Draft, Component_Order)
root.order.add_edge(Design_Draft, Vendor_Select)
root.order.add_edge(Component_Order, Parts_Inspect)
root.order.add_edge(Parts_Inspect, Frame_Build)
root.order.add_edge(Frame_Build, Wiring_Setup)
root.order.add_edge(Wiring_Setup, Software_Load)
root.order.add_edge(Software_Load, Flight_Sim)
root.order.add_edge(Flight_Sim, Quality_Test)
root.order.add_edge(Quality_Test, Feedback_Review)
root.order.add_edge(Feedback_Review, Adjust_Design)
root.order.add_edge(Adjust_Design, Quality_Test)
root.order.add_edge(Quality_Test, Compliance_Check)
root.order.add_edge(Compliance_Check, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Final_Demo)
root.order.add_edge(Final_Demo, Ship_Drone)

# Print the root
print(root)