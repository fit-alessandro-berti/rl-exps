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

# Define silent transitions for concurrency
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    document_review,
    material_testing,
    radiocarbon_date,
    stylistic_eval,
    database_check,
    ownership_audit,
    export_verify,
    expert_arbitration
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    conservation_plan,
    skip
])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    risk_assessment,
    skip
])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[
    approval_review,
    skip
])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[
    insurance_setup,
    skip
])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[
    secure_transport,
    skip
])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[
    acquisitions_meet,
    skip
])

xor7 = OperatorPOWL(operator=Operator.XOR, children=[
    final_documentation,
    skip
])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)

print(root)