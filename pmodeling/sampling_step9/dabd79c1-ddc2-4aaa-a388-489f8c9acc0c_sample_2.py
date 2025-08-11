import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
document_review = Transition(label='Document Review')
material_testing = Transition(label='Material Testing')
radiocarbon_date = Transition(label='Radiocarbon Date')
stylistic_eval = Transition(label='Stylistic Eval')
database_check = Transition(label='Database Check')
ownership_audit = Transition(label='Ownership Audit')
export_verify = Transition(label='Export Verify')
expert_arbitration = Transition(label='Expert Arbitration')
conservation_plan = Transition(label='Conservation Plan')
risk_assessment = Transition(label='Risk Assessment')
approval_review = Transition(label='Approval Review')
insurance_setup = Transition(label='Insurance Setup')
secure_transport = Transition(label='Secure Transport')
acquisitions_meet = Transition(label='Acquisitions Meet')
final_documentation = Transition(label='Final Documentation')

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, material_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, export_verify])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[acquisitions_meet, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_documentation, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop2, xor6)

# Print the POWL model
print(root)