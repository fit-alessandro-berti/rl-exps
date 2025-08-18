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

# Define the partial order
root = StrictPartialOrder(nodes=[
    document_review, material_testing, radiocarbon_date, stylistic_eval,
    database_check, ownership_audit, export_verify, expert_arbitration,
    conservation_plan, risk_assessment, approval_review, insurance_setup,
    secure_transport, acquisitions_meet, final_documentation
])

# Define the partial order dependencies
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(material_testing, stylistic_eval)
root.order.add_edge(stylistic_eval, database_check)
root.order.add_edge(ownership_audit, export_verify)
root.order.add_edge(expert_arbitration, conservation_plan)
root.order.add_edge(risk_assessment, approval_review)
root.order.add_edge(insurance_setup, secure_transport)
root.order.add_edge(acquisitions_meet, final_documentation)

print(root)