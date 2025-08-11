import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Opportunity_Scan, Idea_Workshop])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Concept_Merge, Resource_Align])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Feasibility_Test])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Feedback_Gather])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Design_Adapt, Compliance_Check])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Scaling_Plan, IP_Management])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Market_Sync, Partner_Review])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Exit_Strategy, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)