import pm4py
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

# Define nodes for each activity
document_review_node = Transition(label='Document Review')
material_testing_node = Transition(label='Material Testing')
radiocarbon_date_node = Transition(label='Radiocarbon Date')
stylistic_eval_node = Transition(label='Stylistic Eval')
database_check_node = Transition(label='Database Check')
ownership_audit_node = Transition(label='Ownership Audit')
export_verify_node = Transition(label='Export Verify')
expert_arbitration_node = Transition(label='Expert Arbitration')
conservation_plan_node = Transition(label='Conservation Plan')
risk_assessment_node = Transition(label='Risk Assessment')
approval_review_node = Transition(label='Approval Review')
insurance_setup_node = Transition(label='Insurance Setup')
secure_transport_node = Transition(label='Secure Transport')
acquisitions_meet_node = Transition(label='Acquisitions Meet')
final_documentation_node = Transition(label='Final Documentation')

# Define partial order
root = StrictPartialOrder(nodes=[
    document_review_node,
    material_testing_node,
    radiocarbon_date_node,
    stylistic_eval_node,
    database_check_node,
    ownership_audit_node,
    export_verify_node,
    expert_arbitration_node,
    conservation_plan_node,
    risk_assessment_node,
    approval_review_node,
    insurance_setup_node,
    secure_transport_node,
    acquisitions_meet_node,
    final_documentation_node
])

# Define edges for partial order
root.order.add_edge(document_review_node, material_testing_node)
root.order.add_edge(document_review_node, radiocarbon_date_node)
root.order.add_edge(document_review_node, stylistic_eval_node)
root.order.add_edge(document_review_node, database_check_node)
root.order.add_edge(document_review_node, ownership_audit_node)
root.order.add_edge(document_review_node, export_verify_node)
root.order.add_edge(document_review_node, expert_arbitration_node)
root.order.add_edge(document_review_node, conservation_plan_node)
root.order.add_edge(document_review_node, risk_assessment_node)
root.order.add_edge(document_review_node, approval_review_node)
root.order.add_edge(document_review_node, insurance_setup_node)
root.order.add_edge(document_review_node, secure_transport_node)
root.order.add_edge(document_review_node, acquisitions_meet_node)
root.order.add_edge(document_review_node, final_documentation_node)

root.order.add_edge(material_testing_node, radiocarbon_date_node)
root.order.add_edge(material_testing_node, stylistic_eval_node)
root.order.add_edge(material_testing_node, database_check_node)
root.order.add_edge(material_testing_node, ownership_audit_node)
root.order.add_edge(material_testing_node, export_verify_node)
root.order.add_edge(material_testing_node, expert_arbitration_node)
root.order.add_edge(material_testing_node, conservation_plan_node)
root.order.add_edge(material_testing_node, risk_assessment_node)
root.order.add_edge(material_testing_node, approval_review_node)
root.order.add_edge(material_testing_node, insurance_setup_node)
root.order.add_edge(material_testing_node, secure_transport_node)
root.order.add_edge(material_testing_node, acquisitions_meet_node)
root.order.add_edge(material_testing_node, final_documentation_node)

root.order.add_edge(radiocarbon_date_node, stylistic_eval_node)
root.order.add_edge(radiocarbon_date_node, database_check_node)
root.order.add_edge(radiocarbon_date_node, ownership_audit_node)
root.order.add_edge(radiocarbon_date_node, export_verify_node)
root.order.add_edge(radiocarbon_date_node, expert_arbitration_node)
root.order.add_edge(radiocarbon_date_node, conservation_plan_node)
root.order.add_edge(radiocarbon_date_node, risk_assessment_node)
root.order.add_edge(radiocarbon_date_node, approval_review_node)
root.order.add_edge(radiocarbon_date_node, insurance_setup_node)
root.order.add_edge(radiocarbon_date_node, secure_transport_node)
root.order.add_edge(radiocarbon_date_node, acquisitions_meet_node)
root.order.add_edge(radiocarbon_date_node, final_documentation_node)

root.order.add_edge(stylistic_eval_node, database_check_node)
root.order.add_edge(stylistic_eval_node, ownership_audit_node)
root.order.add_edge(stylistic_eval_node, export_verify_node)
root.order.add_edge(stylistic_eval_node, expert_arbitration_node)
root.order.add_edge(stylistic_eval_node, conservation_plan_node)
root.order.add_edge(stylistic_eval_node, risk_assessment_node)
root.order.add_edge(stylistic_eval_node, approval_review_node)
root.order.add_edge(stylistic_eval_node, insurance_setup_node)
root.order.add_edge(stylistic_eval_node, secure_transport_node)
root.order.add_edge(stylistic_eval_node, acquisitions_meet_node)
root.order.add_edge(stylistic_eval_node, final_documentation_node)

root.order.add_edge(database_check_node, ownership_audit_node)
root.order.add_edge(database_check_node, export_verify_node)
root.order.add_edge(database_check_node, expert_arbitration_node)
root.order.add_edge(database_check_node, conservation_plan_node)
root.order.add_edge(database_check_node, risk_assessment_node)
root.order.add_edge(database_check_node, approval_review_node)
root.order.add_edge(database_check_node, insurance_setup_node)
root.order.add_edge(database_check_node, secure_transport_node)
root.order.add_edge(database_check_node, acquisitions_meet_node)
root.order.add_edge(database_check_node, final_documentation_node)

root.order.add_edge(ownership_audit_node, export_verify_node)
root.order.add_edge(ownership_audit_node, expert_arbitration_node)
root.order.add_edge(ownership_audit_node, conservation_plan_node)
root.order.add_edge(ownership_audit_node, risk_assessment_node)
root.order.add_edge(ownership_audit_node, approval_review_node)
root.order.add_edge(ownership_audit_node, insurance_setup_node)
root.order.add_edge(ownership_audit_node, secure_transport_node)
root.order.add_edge(ownership_audit_node, acquisitions_meet_node)
root.order.add_edge(ownership_audit_node, final_documentation_node)

root.order.add_edge(export_verify_node, expert_arbitration_node)
root.order.add_edge(export_verify_node, conservation_plan_node)
root.order.add_edge(export_verify_node, risk_assessment_node)
root.order.add_edge(export_verify_node, approval_review_node)
root.order.add_edge(export_verify_node, insurance_setup_node)
root.order.add_edge(export_verify_node, secure_transport_node)
root.order.add_edge(export_verify_node, acquisitions_meet_node)
root.order.add_edge(export_verify_node, final_documentation_node)

root.order.add_edge(expert_arbitration_node, conservation_plan_node)
root.order.add_edge(expert_arbitration_node, risk_assessment_node)
root.order.add_edge(expert_arbitration_node, approval_review_node)
root.order.add_edge(expert_arbitration_node, insurance_setup_node)
root.order.add_edge(expert_arbitration_node, secure_transport_node)
root.order.add_edge(expert_arbitration_node, acquisitions_meet_node)
root.order.add_edge(expert_arbitration_node, final_documentation_node)

root.order.add_edge(conservation_plan_node, risk_assessment_node)
root.order.add_edge(conservation_plan_node, approval_review_node)
root.order.add_edge(conservation_plan_node, insurance_setup_node)
root.order.add_edge(conservation_plan_node, secure_transport_node)
root.order.add_edge(conservation_plan_node, acquisitions_meet_node)
root.order.add_edge(conservation_plan_node, final_documentation_node)

root.order.add_edge(risk_assessment_node, approval_review_node)
root.order.add_edge(risk_assessment_node, insurance_setup_node)
root.order.add_edge(risk_assessment_node, secure_transport_node)
root.order.add_edge(risk_assessment_node, acquisitions_meet_node)
root.order.add_edge(risk_assessment_node, final_documentation_node)

root.order.add_edge(approval_review_node, insurance_setup_node)
root.order.add_edge(approval_review_node, secure_transport_node)
root.order.add_edge(approval_review_node, acquisitions_meet_node)
root.order.add_edge(approval_review_node, final_documentation_node)

root.order.add_edge(insurance_setup_node, secure_transport_node)
root.order.add_edge(insurance_setup_node, acquisitions_meet_node)
root.order.add_edge(insurance_setup_node, final_documentation_node)

root.order.add_edge(secure_transport_node, acquisitions_meet_node)
root.order.add_edge(secure_transport_node, final_documentation_node)

root.order.add_edge(acquisitions_meet_node, final_documentation_node)

print(root)