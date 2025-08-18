import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
doc_review = Transition(label='Document Review')
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
    doc_review,
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
    final_documentation
])

# Define the dependencies
root.order.add_edge(doc_review, material_testing)
root.order.add_edge(doc_review, radiocarbon_date)
root.order.add_edge(doc_review, stylistic_eval)
root.order.add_edge(doc_review, database_check)
root.order.add_edge(doc_review, ownership_audit)
root.order.add_edge(doc_review, export_verify)
root.order.add_edge(doc_review, expert_arbitration)
root.order.add_edge(material_testing, conservation_plan)
root.order.add_edge(material_testing, risk_assessment)
root.order.add_edge(material_testing, approval_review)
root.order.add_edge(radiocarbon_date, conservation_plan)
root.order.add_edge(radiocarbon_date, risk_assessment)
root.order.add_edge(radiocarbon_date, approval_review)
root.order.add_edge(stylistic_eval, conservation_plan)
root.order.add_edge(stylistic_eval, risk_assessment)
root.order.add_edge(stylistic_eval, approval_review)
root.order.add_edge(database_check, conservation_plan)
root.order.add_edge(database_check, risk_assessment)
root.order.add_edge(database_check, approval_review)
root.order.add_edge(ownership_audit, conservation_plan)
root.order.add_edge(ownership_audit, risk_assessment)
root.order.add_edge(ownership_audit, approval_review)
root.order.add_edge(export_verify, conservation_plan)
root.order.add_edge(export_verify, risk_assessment)
root.order.add_edge(export_verify, approval_review)
root.order.add_edge(expert_arbitration, conservation_plan)
root.order.add_edge(expert_arbitration, risk_assessment)
root.order.add_edge(expert_arbitration, approval_review)
root.order.add_edge(conservation_plan, insurance_setup)
root.order.add_edge(conservation_plan, secure_transport)
root.order.add_edge(conservation_plan, acquisitions_meet)
root.order.add_edge(risk_assessment, insurance_setup)
root.order.add_edge(risk_assessment, secure_transport)
root.order.add_edge(risk_assessment, acquisitions_meet)
root.order.add_edge(approval_review, insurance_setup)
root.order.add_edge(approval_review, secure_transport)
root.order.add_edge(approval_review, acquisitions_meet)
root.order.add_edge(insurance_setup, final_documentation)
root.order.add_edge(secure_transport, final_documentation)
root.order.add_edge(acquisitions_meet, final_documentation)

# Print the root
print(root)