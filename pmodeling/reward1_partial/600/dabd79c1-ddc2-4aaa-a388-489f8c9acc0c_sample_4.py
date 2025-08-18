from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
    final_documentation
])

# Define the dependencies between activities
root.order.add_edge(document_review, material_testing)
root.order.add_edge(document_review, radiocarbon_date)
root.order.add_edge(document_review, stylistic_eval)
root.order.add_edge(document_review, database_check)
root.order.add_edge(document_review, ownership_audit)
root.order.add_edge(document_review, export_verify)
root.order.add_edge(document_review, expert_arbitration)
root.order.add_edge(document_review, conservation_plan)
root.order.add_edge(document_review, risk_assessment)
root.order.add_edge(document_review, approval_review)
root.order.add_edge(document_review, insurance_setup)
root.order.add_edge(document_review, secure_transport)
root.order.add_edge(document_review, acquisitions_meet)
root.order.add_edge(document_review, final_documentation)

root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(material_testing, stylistic_eval)
root.order.add_edge(material_testing, database_check)
root.order.add_edge(material_testing, ownership_audit)
root.order.add_edge(material_testing, export_verify)
root.order.add_edge(material_testing, expert_arbitration)
root.order.add_edge(material_testing, conservation_plan)
root.order.add_edge(material_testing, risk_assessment)
root.order.add_edge(material_testing, approval_review)
root.order.add_edge(material_testing, insurance_setup)
root.order.add_edge(material_testing, secure_transport)
root.order.add_edge(material_testing, acquisitions_meet)
root.order.add_edge(material_testing, final_documentation)

root.order.add_edge(radiocarbon_date, stylistic_eval)
root.order.add_edge(radiocarbon_date, database_check)
root.order.add_edge(radiocarbon_date, ownership_audit)
root.order.add_edge(radiocarbon_date, export_verify)
root.order.add_edge(radiocarbon_date, expert_arbitration)
root.order.add_edge(radiocarbon_date, conservation_plan)
root.order.add_edge(radiocarbon_date, risk_assessment)
root.order.add_edge(radiocarbon_date, approval_review)
root.order.add_edge(radiocarbon_date, insurance_setup)
root.order.add_edge(radiocarbon_date, secure_transport)
root.order.add_edge(radiocarbon_date, acquisitions_meet)
root.order.add_edge(radiocarbon_date, final_documentation)

root.order.add_edge(stylistic_eval, database_check)
root.order.add_edge(stylistic_eval, ownership_audit)
root.order.add_edge(stylistic_eval, export_verify)
root.order.add_edge(stylistic_eval, expert_arbitration)
root.order.add_edge(stylistic_eval, conservation_plan)
root.order.add_edge(stylistic_eval, risk_assessment)
root.order.add_edge(stylistic_eval, approval_review)
root.order.add_edge(stylistic_eval, insurance_setup)
root.order.add_edge(stylistic_eval, secure_transport)
root.order.add_edge(stylistic_eval, acquisitions_meet)
root.order.add_edge(stylistic_eval, final_documentation)

root.order.add_edge(database_check, ownership_audit)
root.order.add_edge(database_check, export_verify)
root.order.add_edge(database_check, expert_arbitration)
root.order.add_edge(database_check, conservation_plan)
root.order.add_edge(database_check, risk_assessment)
root.order.add_edge(database_check, approval_review)
root.order.add_edge(database_check, insurance_setup)
root.order.add_edge(database_check, secure_transport)
root.order.add_edge(database_check, acquisitions_meet)
root.order.add_edge(database_check, final_documentation)

root.order.add_edge(ownership_audit, export_verify)
root.order.add_edge(ownership_audit, expert_arbitration)
root.order.add_edge(ownership_audit, conservation_plan)
root.order.add_edge(ownership_audit, risk_assessment)
root.order.add_edge(ownership_audit, approval_review)
root.order.add_edge(ownership_audit, insurance_setup)
root.order.add_edge(ownership_audit, secure_transport)
root.order.add_edge(ownership_audit, acquisitions_meet)
root.order.add_edge(ownership_audit, final_documentation)

root.order.add_edge(export_verify, expert_arbitration)
root.order.add_edge(export_verify, conservation_plan)
root.order.add_edge(export_verify, risk_assessment)
root.order.add_edge(export_verify, approval_review)
root.order.add_edge(export_verify, insurance_setup)
root.order.add_edge(export_verify, secure_transport)
root.order.add_edge(export_verify, acquisitions_meet)
root.order.add_edge(export_verify, final_documentation)

root.order.add_edge(expert_arbitration, conservation_plan)
root.order.add_edge(expert_arbitration, risk_assessment)
root.order.add_edge(expert_arbitration, approval_review)
root.order.add_edge(expert_arbitration, insurance_setup)
root.order.add_edge(expert_arbitration, secure_transport)
root.order.add_edge(expert_arbitration, acquisitions_meet)
root.order.add_edge(expert_arbitration, final_documentation)

root.order.add_edge(conservation_plan, risk_assessment)
root.order.add_edge(conservation_plan, approval_review)
root.order.add_edge(conservation_plan, insurance_setup)
root.order.add_edge(conservation_plan, secure_transport)
root.order.add_edge(conservation_plan, acquisitions_meet)
root.order.add_edge(conservation_plan, final_documentation)

root.order.add_edge(risk_assessment, approval_review)
root.order.add_edge(risk_assessment, insurance_setup)
root.order.add_edge(risk_assessment, secure_transport)
root.order.add_edge(risk_assessment, acquisitions_meet)
root.order.add_edge(risk_assessment, final_documentation)

root.order.add_edge(approval_review, insurance_setup)
root.order.add_edge(approval_review, secure_transport)
root.order.add_edge(approval_review, acquisitions_meet)
root.order.add_edge(approval_review, final_documentation)

root.order.add_edge(insurance_setup, secure_transport)
root.order.add_edge(insurance_setup, acquisitions_meet)
root.order.add_edge(insurance_setup, final_documentation)

root.order.add_edge(secure_transport, acquisitions_meet)
root.order.add_edge(secure_transport, final_documentation)

root.order.add_edge(acquisitions_meet, final_documentation)

# Print the POWL model
print(root)