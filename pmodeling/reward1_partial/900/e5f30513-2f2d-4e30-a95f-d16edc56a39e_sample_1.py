import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake_review = Transition(label='Intake Review')
preliminary_inspect = Transition(label='Preliminary Inspect')
provenance_check = Transition(label='Provenance Check')
archival_research = Transition(label='Archival Research')
material_testing = Transition(label='Material Testing')
radiocarbon_date = Transition(label='Radiocarbon Date')
stylistic_assess = Transition(label='Stylistic Assess')
expert_consult = Transition(label='Expert Consult')
findings_compile = Transition(label='Findings Compile')
internal_review = Transition(label='Internal Review')
client_present = Transition(label='Client Present')
approval_confirm = Transition(label='Approval Confirm')
secure_package = Transition(label='Secure Package')
transport_arrange = Transition(label='Transport Arrange')
chain_custody = Transition(label='Chain Custody')

# Define silent transitions
skip = SilentTransition()

# Define loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_research, material_testing, radiocarbon_date])
xor = OperatorPOWL(operator=Operator.XOR, children=[stylistic_assess, expert_consult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[internal_review, client_present])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[approval_confirm, transport_arrange])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[secure_package, chain_custody])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[intake_review, preliminary_inspect, provenance_check, loop, xor, xor2, xor3, xor4])
root.order.add_edge(intake_review, preliminary_inspect)
root.order.add_edge(preliminary_inspect, provenance_check)
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, secure_package)
root.order.add_edge(secure_package, chain_custody)

# Print the root POWL model
print(root)