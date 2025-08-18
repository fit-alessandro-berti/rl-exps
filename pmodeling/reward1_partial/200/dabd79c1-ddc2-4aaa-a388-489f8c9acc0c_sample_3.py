import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[database_check, ownership_audit, export_verify, expert_arbitration])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, approval_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, material_testing])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, insurance_setup])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[final_documentation, acquisitions_meet])

# Define the partial order
root = StrictPartialOrder(nodes=[document_review, loop, xor_1, xor_2, conservation_plan, xor_3, xor_4])
root.order.add_edge(document_review, loop)
root.order.add_edge(loop, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, conservation_plan)
root.order.add_edge(conservation_plan, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, final_documentation)