from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
legal_audit = Transition(label='Legal Audit')
condition_report = Transition(label='Condition Report')
carbon_dating = Transition(label='Carbon Dating')
ownership_verify = Transition(label='Ownership Verify')
historical_match = Transition(label='Historical Match')
customs_clearance = Transition(label='Customs Clearance')
risk_assessment = Transition(label='Risk Assessment')
ethics_approval = Transition(label='Ethics Approval')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
exhibit_prep = Transition(label='Exhibit Prep')

# Define the workflow
provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
material_scan_to_expert_review = OperatorPOWL(operator=Operator.XOR, children=[material_scan, expert_review])
expert_review_to_legal_audit = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_audit])
legal_audit_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, condition_report])
condition_report_to_carbon_dating = OperatorPOWL(operator=Operator.XOR, children=[condition_report, carbon_dating])
carbon_dating_to_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, ownership_verify])
ownership_verify_to_historical_match = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, historical_match])
historical_match_to_customs_clearance = OperatorPOWL(operator=Operator.XOR, children=[historical_match, customs_clearance])
customs_clearance_to_risk_assessment = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, risk_assessment])
risk_assessment_to_ethics_approval = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, ethics_approval])
ethics_approval_to_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[ethics_approval, restoration_plan])
restoration_plan_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, final_approval])
final_approval_to_catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[final_approval, catalog_entry])
catalog_entry_to_exhibit_prep = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, exhibit_prep])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    expert_review,
    legal_audit,
    condition_report,
    carbon_dating,
    ownership_verify,
    historical_match,
    customs_clearance,
    risk_assessment,
    ethics_approval,
    restoration_plan,
    final_approval,
    catalog_entry,
    exhibit_prep
])

# Define the order of activities
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, expert_review)
root.order.add_edge(expert_review, legal_audit)
root.order.add_edge(legal_audit, condition_report)
root.order.add_edge(condition_report, carbon_dating)
root.order.add_edge(carbon_dating, ownership_verify)
root.order.add_edge(ownership_verify, historical_match)
root.order.add_edge(historical_match, customs_clearance)
root.order.add_edge(customs_clearance, risk_assessment)
root.order.add_edge(risk_assessment, ethics_approval)
root.order.add_edge(ethics_approval, restoration_plan)
root.order.add_edge(restoration_plan, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_prep)

# Print the root POWL model
print(root)