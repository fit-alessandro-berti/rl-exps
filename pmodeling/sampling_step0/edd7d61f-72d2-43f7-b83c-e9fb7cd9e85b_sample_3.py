import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Chemical_Test = Transition(label='Chemical Test')
Imaging_Capture = Transition(label='Imaging Capture')
Expert_Consult = Transition(label='Expert Consult')
Historical_Match = Transition(label='Historical Match')
Forgery_Detect = Transition(label='Forgery Detect')
Documentation_Verify = Transition(label='Documentation Verify')
Cross_Border_Check = Transition(label='Cross-Border Check')
Condition_Assess = Transition(label='Condition Assess')
Value_Estimate = Transition(label='Value Estimate')
Report_Draft = Transition(label='Report Draft')
Report_Review = Transition(label='Report Review')
Client_Approval = Transition(label='Client Approval')
Certification_Issue = Transition(label='Certification Issue')
Archive_Record = Transition(label='Archive Record')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Historical_Match, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Condition_Assess, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Value_Estimate, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Documentation_Verify, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Cross_Border_Check, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Imaging_Capture, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Chemical_Test, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Forgery_Detect, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Consult, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Provenance_Check, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Material_Scan, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Initial_Review, skip])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12])

# Define the root
root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop1, xor7)
root.order.add_edge(loop1, xor8)
root.order.add_edge(loop1, xor9)
root.order.add_edge(loop1, xor10)
root.order.add_edge(loop1, xor11)
root.order.add_edge(loop1, xor12)

# Print the root
print(root)