import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
discover_item = Transition(label='Discover Item')
document_find = Transition(label='Document Find')
initial_survey = Transition(label='Initial Survey')
image_capture = Transition(label='Image Capture')
material_testing = Transition(label='Material Testing')
style_compare = Transition(label='Style Compare')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
ownership_verify = Transition(label='Ownership Verify')
legal_review = Transition(label='Legal Review')
risk_assess = Transition(label='Risk Assess')
conservation_plan = Transition(label='Conservation Plan')
certification = Transition(label='Certification')
secure_transfer = Transition(label='Secure Transfer')
dispute_resolve = Transition(label='Dispute Resolve')
final_archive = Transition(label='Final Archive')

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[discover_item, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[document_find, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[image_capture, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[material_testing, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[certification, skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[secure_transfer, skip])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, skip])
xor16 = OperatorPOWL(operator=Operator.XOR, children=[final_archive, skip])

# Define the loop for the risk assessment and conservation plan
loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, conservation_plan])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13, xor14, xor15, xor16, loop])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor14, xor15)
root.order.add_edge(xor15, xor16)
root.order.add_edge(xor16, loop)
root.order.add_edge(loop, xor1)