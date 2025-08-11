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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[Ship_Drone, SilentTransition()])

loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Draft, Vendor_Select, Component_Order, Parts_Inspect, Frame_Build, Wiring_Setup, Software_Load, Flight_Sim, Quality_Test, Feedback_Review, Adjust_Design, Compliance_Check, Packaging_Prep, Final_Demo])
root = StrictPartialOrder(nodes=[loop, xor])

root.order.add_edge(loop, xor)

# Print the POWL model
print(root)