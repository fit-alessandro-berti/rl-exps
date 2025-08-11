import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define exclusive choice for Idea Workshop
xor = OperatorPOWL(operator=Operator.XOR, children=[Concept_Merge, skip])

# Define loop for Resource Align, Prototype Build, Feasibility Test, Pilot Launch, Feedback Gather, Design Adapt, Compliance Check, Scaling Plan, IP Management, Market Sync, Partner Review
loop = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Align, Prototype_Build, Feasibility_Test, Pilot_Launch, Feedback_Gather, Design_Adapt, Compliance_Check, Scaling_Plan, IP_Management, Market_Sync, Partner_Review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)