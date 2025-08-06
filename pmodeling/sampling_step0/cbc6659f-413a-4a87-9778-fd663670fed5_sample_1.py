from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, expert_review, legal_audit, condition_report, carbon_dating, ownership_verify, historical_match, customs_clearance, risk_assessment, ethics_approval, restoration_plan, final_approval, catalog_entry, exhibit_prep])
xor = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, exhibit_prep])

# Create the root model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)