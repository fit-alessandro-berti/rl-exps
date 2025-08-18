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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the POWL model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[archival_research, material_testing, radiocarbon_date, stylistic_assess])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[findings_compile, internal_review])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[client_present, skip])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[approval_confirm, secure_package])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[transport_arrange, skip])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[chain_custody, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[intake_review, preliminary_inspect, provenance_check, loop_1, xor_1, loop_2, xor_2, loop_3, xor_3, loop_4])
root.order.add_edge(intake_review, preliminary_inspect)
root.order.add_edge(preliminary_inspect, provenance_check)
root.order.add_edge(provenance_check, loop_1)
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, loop_2)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_2, loop_3)
root.order.add_edge(loop_3, xor_3)
root.order.add_edge(xor_3, loop_4)
root.order.add_edge(loop_4, chain_custody)

print(root)