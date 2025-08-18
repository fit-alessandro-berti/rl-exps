from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the loop for material analysis and expert consultations
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, expert_review])

# Define the exclusive choice for legal compliance checks
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, customs_clearance])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[provenance_check, loop, xor, condition_report, carbon_dating, ownership_verify, historical_match, risk_assessment, ethics_approval, restoration_plan, final_approval, catalog_entry, exhibit_prep])
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, condition_report)
root.order.add_edge(condition_report, carbon_dating)
root.order.add_edge(carbon_dating, ownership_verify)
root.order.add_edge(ownership_verify, historical_match)
root.order.add_edge(historical_match, risk_assessment)
root.order.add_edge(risk_assessment, ethics_approval)
root.order.add_edge(ethics_approval, restoration_plan)
root.order.add_edge(restoration_plan, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_prep)

# Return the root of the POWL model
return root