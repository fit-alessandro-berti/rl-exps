import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Create the root of the partial order
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

# Optionally, if there are any dependencies between activities, you can add them here
# For example, if 'Material Scan' must happen before 'Expert Review':
# root.order.add_edge(material_scan, expert_review)

# The final result is the 'root' variable