import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Visual_Inspect = Transition(label='Visual Inspect')
Document_Gather = Transition(label='Document Gather')
Material_Test = Transition(label='Material Test')
Pigment_Analyze = Transition(label='Pigment Analyze')
Style_Compare = Transition(label='Style Compare')
Provenance_Trace = Transition(label='Provenance Trace')
Data_Crosscheck = Transition(label='Data Crosscheck')
Infrared_Scan = Transition(label='Infrared Scan')
Xray_Fluoresce = Transition(label='Xray Fluoresce')
Expert_Consult = Transition(label='Expert Consult')
Forgery_Detect = Transition(label='Forgery Detect')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Final_Approval = Transition(label='Final Approval')
Archive_Store = Transition(label='Archive Store')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Infrared_Scan, Xray_Fluoresce])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Style_Compare, Expert_Consult])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Data_Crosscheck, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Forgery_Detect, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Report_Draft, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Review, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Final_Approval, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Archive_Store, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, skip)
root.order.add_edge(xor6, skip)

# Print the final POWL model
print(root)