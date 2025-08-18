import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[document_review, material_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, stylistic_eval, database_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, export_verify, expert_arbitration])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[conservation_plan, risk_assessment, approval_review])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[insurance_setup, secure_transport, acquisitions_meet])
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, final_documentation)