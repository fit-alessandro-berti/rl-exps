from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
document_review = Transition('Document Review')
material_testing = Transition('Material Testing')
radiocarbon_date = Transition('Radiocarbon Date')
stylistic_eval = Transition('Stylistic Eval')
database_check = Transition('Database Check')
ownership_audit = Transition('Ownership Audit')
export_verify = Transition('Export Verify')
expert_arbitration = Transition('Expert Arbitration')
conservation_plan = Transition('Conservation Plan')
risk_assessment = Transition('Risk Assessment')
approval_review = Transition('Approval Review')
insurance_setup = Transition('Insurance Setup')
secure_transport = Transition('Secure Transport')
acquisitions_meet = Transition('Acquisitions Meet')
final_documentation = Transition('Final Documentation')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[expert_arbitration])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_check, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[export_verify, skip2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[approval_review, skip3])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    document_review,
    material_testing,
    radiocarbon_date,
    stylistic_eval,
    database_check,
    ownership_audit,
    export_verify,
    expert_arbitration,
    conservation_plan,
    risk_assessment,
    approval_review,
    insurance_setup,
    secure_transport,
    acquisitions_meet,
    final_documentation,
    loop1,
    loop2,
    xor1,
    xor2,
    xor3
])

# Define the dependencies between activities
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(material_testing, stylistic_eval)
root.order.add_edge(radiocarbon_date, database_check)
root.order.add_edge(stylistic_eval, database_check)
root.order.add_edge(database_check, xor1)
root.order.add_edge(ownership_audit, export_verify)
root.order.add_edge(export_verify, xor2)
root.order.add_edge(expert_arbitration, loop1)
root.order.add_edge(loop1, expert_arbitration)
root.order.add_edge(loop1, xor3)
root.order.add_edge(risk_assessment, loop2)
root.order.add_edge(loop2, risk_assessment)
root.order.add_edge(approval_review, xor3)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, acquisitions_meet)
root.order.add_edge(acquisitions_meet, final_documentation)

print(root)