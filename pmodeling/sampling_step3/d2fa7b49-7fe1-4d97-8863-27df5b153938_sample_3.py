import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
preliminary_check = Transition(label='Preliminary Check')
historical_review = Transition(label='Historical Review')
chemical_test = Transition(label='Chemical Test')
provenance_audit = Transition(label='Provenance Audit')
expert_panel = Transition(label='Expert Panel')
token_minting = Transition(label='Token Minting')
legal_review = Transition(label='Legal Review')
compliance_check = Transition(label='Compliance Check')
insurance_valuation = Transition(label='Insurance Valuation')
risk_assessment = Transition(label='Risk Assessment')
packaging_prep = Transition(label='Packaging Prep')
climate_control = Transition(label='Climate Control')
transport_setup = Transition(label='Transport Setup')
final_approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, historical_review, chemical_test, provenance_audit, expert_panel, token_minting, legal_review, compliance_check, insurance_valuation, risk_assessment, packaging_prep, climate_control, transport_setup, final_approval])

# Define the dependencies between the nodes
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, historical_review)
root.order.add_edge(historical_review, chemical_test)
root.order.add_edge(chemical_test, provenance_audit)
root.order.add_edge(provenance_audit, expert_panel)
root.order.add_edge(expert_panel, token_minting)
root.order.add_edge(token_minting, legal_review)
root.order.add_edge(legal_review, compliance_check)
root.order.add_edge(compliance_check, insurance_valuation)
root.order.add_edge(insurance_valuation, risk_assessment)
root.order.add_edge(risk_assessment, packaging_prep)
root.order.add_edge(packaging_prep, climate_control)
root.order.add_edge(climate_control, transport_setup)
root.order.add_edge(transport_setup, final_approval)

print(root)