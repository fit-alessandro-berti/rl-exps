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

# Define the workflow
xor = OperatorPOWL(operator=Operator.XOR, children=[
    radiocarbon_date,
    material_testing,
    database_check,
    ownership_audit,
    export_verify,
    expert_arbitration,
    risk_assessment
])

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    stylistic_eval,
    conservation_plan,
    approval_review,
    insurance_setup,
    secure_transport,
    acquisitions_meet
])

root = StrictPartialOrder(nodes=[xor, loop])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, final_documentation)