import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order nodes
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, expert_review, legal_audit, condition_report, carbon_dating, ownership_verify, historical_match, customs_clearance, risk_assessment, ethics_approval, restoration_plan, final_approval, catalog_entry])
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, catalog_entry, exhibit_prep])

# Define the exclusive choice nodes
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
final_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval_loop, skip])

# Define the root node
root = StrictPartialOrder(nodes=[provenance_xor, final_approval_xor])
root.order.add_edge(provenance_xor, final_approval_xor)

# Print the final result
print(root)