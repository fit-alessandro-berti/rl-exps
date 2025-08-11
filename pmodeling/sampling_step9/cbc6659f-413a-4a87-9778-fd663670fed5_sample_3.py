import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_audit, condition_report, carbon_dating])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify, historical_match, customs_clearance, risk_assessment])
ethics_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_approval, restoration_plan])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, catalog_entry, exhibit_prep])

root = StrictPartialOrder(nodes=[provenance_loop, material_loop, ownership_loop, ethics_loop, final_loop])
root.order.add_edge(provenance_loop, material_loop)
root.order.add_edge(material_loop, ownership_loop)
root.order.add_edge(ownership_loop, ethics_loop)
root.order.add_edge(ethics_loop, final_loop)

# Save the final result in the variable 'root'