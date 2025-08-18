from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops and choices
loop_ownership = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, export_verify])
xor_arbitration = OperatorPOWL(operator=Operator.XOR, children=[expert_arbitration, skip])
xor_approval = OperatorPOWL(operator=Operator.XOR, children=[approval_review, skip])

# Define partial order
root = StrictPartialOrder(nodes=[document_review, material_testing, radiocarbon_date, stylistic_eval, database_check, loop_ownership, xor_arbitration, conservation_plan, risk_assessment, xor_approval, insurance_setup, secure_transport, acquisitions_meet, final_documentation])

# Define dependencies
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(material_testing, stylistic_eval)
root.order.add_edge(radiocarbon_date, database_check)
root.order.add_edge(stylistic_eval, database_check)
root.order.add_edge(database_check, loop_ownership)
root.order.add_edge(loop_ownership, xor_arbitration)
root.order.add_edge(xor_arbitration, conservation_plan)
root.order.add_edge(conservation_plan, risk_assessment)
root.order.add_edge(risk_assessment, xor_approval)
root.order.add_edge(xor_approval, insurance_setup)
root.order.add_edge(insurance_setup, secure_transport)
root.order.add_edge(secure_transport, acquisitions_meet)
root.order.add_edge(acquisitions_meet, final_documentation)

# Print the final POWL model
print(root)