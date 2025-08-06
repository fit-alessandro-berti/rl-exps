import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
Opportunity_Scan = Transition(label='Opportunity Scan')
Idea_Workshop = Transition(label='Idea Workshop')
Concept_Merge = Transition(label='Concept Merge')
Resource_Align = Transition(label='Resource Align')
Prototype_Build = Transition(label='Prototype Build')
Feasibility_Test = Transition(label='Feasibility Test')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Gather = Transition(label='Feedback Gather')
Design_Adapt = Transition(label='Design Adapt')
Compliance_Check = Transition(label='Compliance Check')
Scaling_Plan = Transition(label='Scaling Plan')
IP_Management = Transition(label='IP Management')
Market_Sync = Transition(label='Market Sync')
Partner_Review = Transition(label='Partner Review')
Exit_Strategy = Transition(label='Exit Strategy')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Idea_Workshop, Opportunity_Scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Resource_Align, Compliance_Check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Design_Adapt, Scaling_Plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[IP_Management, Market_Sync])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Partner_Review, Exit_Strategy])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Pilot_Launch])

# Define the partial order
root.nodes = [loop, xor1, xor2, xor3, xor4, xor5]

# Define the order
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)

# Print the root
print(root)