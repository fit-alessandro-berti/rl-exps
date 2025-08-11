import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
skip = SilentTransition()

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[discover_item, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[document_find, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[initial_survey, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[image_capture, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[material_testing, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[certification, xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[secure_transfer, xor13])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, xor14])
xor16 = OperatorPOWL(operator=Operator.XOR, children=[final_archive, xor15])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor16])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor16)

# Print the POWL model
print(root)