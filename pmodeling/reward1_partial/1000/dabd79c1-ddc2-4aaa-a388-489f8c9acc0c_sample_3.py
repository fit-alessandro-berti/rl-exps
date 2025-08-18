import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop_document_review = OperatorPOWL(operator=Operator.LOOP, children=[document_review, material_testing, radiocarbon_date, stylistic_eval, database_check, ownership_audit, export_verify, expert_arbitration])
xor_concurrent = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, insurance_setup, secure_transport, acquisitions_meet])
xor_concurrent_2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, final_documentation])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_document_review, xor_concurrent, xor_concurrent_2])
root.order.add_edge(loop_document_review, xor_concurrent)
root.order.add_edge(loop_document_review, xor_concurrent_2)