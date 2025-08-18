from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ]
)

# Define the control-flow operators
# Provenance Check -> Material Scan
root.order.add_edge(provenance_check, material_scan)
# Material Scan -> Expert Review
root.order.add_edge(material_scan, expert_review)
# Expert Review -> Legal Audit
root.order.add_edge(expert_review, legal_audit)
# Legal Audit -> Condition Report
root.order.add_edge(legal_audit, condition_report)
# Condition Report -> Carbon Dating
root.order.add_edge(condition_report, carbon_dating)
# Carbon Dating -> Ownership Verify
root.order.add_edge(carbon_dating, ownership_verify)
# Ownership Verify -> Historical Match
root.order.add_edge(ownership_verify, historical_match)
# Historical Match -> Customs Clearance
root.order.add_edge(historical_match, customs_clearance)
# Customs Clearance -> Risk Assessment
root.order.add_edge(customs_clearance, risk_assessment)
# Risk Assessment -> Ethics Approval
root.order.add_edge(risk_assessment, ethics_approval)
# Ethics Approval -> Restoration Plan
root.order.add_edge(ethics_approval, restoration_plan)
# Restoration Plan -> Final Approval
root.order.add_edge(restoration_plan, final_approval)
# Final Approval -> Catalog Entry
root.order.add_edge(final_approval, catalog_entry)
# Catalog Entry -> Exhibit Prep
root.order.add_edge(catalog_entry, exhibit_prep)

print(root)