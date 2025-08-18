import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Wear_Analysis = Transition(label='Wear Analysis')
Image_Capture = Transition(label='Image Capture')
Pattern_Match = Transition(label='Pattern Match')
Ownership_Verify = Transition(label='Ownership Verify')
Ethics_Review = Transition(label='Ethics Review')
Carbon_Dating = Transition(label='Carbon Dating')
Restoration_Eval = Transition(label='Restoration Eval')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Archive_Data = Transition(label='Archive Data')
Exhibit_Approve = Transition(label='Exhibit Approve')
Condition_Monitor = Transition(label='Condition Monitor')
Final_Certification = Transition(label='Final Certification')

# Define silent transitions
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check, Material_Scan, Wear_Analysis, Image_Capture, Pattern_Match, Ownership_Verify, Ethics_Review, Carbon_Dating, Restoration_Eval])
xor = OperatorPOWL(operator=Operator.XOR, children=[Report_Draft, Stakeholder_Review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Archive_Data, Exhibit_Approve])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Condition_Monitor, Final_Certification])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)