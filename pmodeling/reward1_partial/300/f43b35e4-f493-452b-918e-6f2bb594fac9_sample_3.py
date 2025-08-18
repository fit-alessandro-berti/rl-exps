import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Client_Brief = Transition(label='Client Brief')
Design_Draft = Transition(label='Design Draft')
Part_Sourcing = Transition(label='Part Sourcing')
Component_Fabric = Transition(label='Component Fabric')
Circuit_Assembly = Transition(label='Circuit Assembly')
Software_Upload = Transition(label='Software Upload')
Initial_Testing = Transition(label='Initial Testing')
Flight_Calibrate = Transition(label='Flight Calibrate')
Payload_Mount = Transition(label='Payload Mount')
Stress_Testing = Transition(label='Stress Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Quality_Check = Transition(label='Quality Check')
Certification = Transition(label='Certification')
Packaging = Transition(label='Packaging')
Delivery_Plan = Transition(label='Delivery Plan')
Post_Support = Transition(label='Post Support')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        Client_Brief,
        Design_Draft,
        Part_Sourcing,
        Component_Fabric,
        Circuit_Assembly,
        Software_Upload,
        Initial_Testing,
        Flight_Calibrate,
        Payload_Mount,
        Stress_Testing,
        Feedback_Loop,
        Quality_Check,
        Certification,
        Packaging,
        Delivery_Plan,
        Post_Support
    ]
)

# Define the dependencies between the nodes
root.order.add_edge(Client_Brief, Design_Draft)
root.order.add_edge(Design_Draft, Part_Sourcing)
root.order.add_edge(Part_Sourcing, Component_Fabric)
root.order.add_edge(Component_Fabric, Circuit_Assembly)
root.order.add_edge(Circuit_Assembly, Software_Upload)
root.order.add_edge(Software_Upload, Initial_Testing)
root.order.add_edge(Initial_Testing, Flight_Calibrate)
root.order.add_edge(Flight_Calibrate, Payload_Mount)
root.order.add_edge(Payload_Mount, Stress_Testing)
root.order.add_edge(Stress_Testing, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Quality_Check)
root.order.add_edge(Quality_Check, Certification)
root.order.add_edge(Certification, Packaging)
root.order.add_edge(Packaging, Delivery_Plan)
root.order.add_edge(Delivery_Plan, Post_Support)

# Return the root of the POWL model
return root