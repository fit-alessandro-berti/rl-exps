import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define POWL models
historical_exclusive = OperatorPOWL(operator=Operator.XOR, children=[historical_review, chemical_test])
provenance_exclusive = OperatorPOWL(operator=Operator.XOR, children=[provenance_audit, expert_panel])
legal_compliance = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
insurance_risk = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
climate_control_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_control, transport_setup])

# Define partial order
root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, historical_exclusive, provenance_exclusive, token_minting, legal_compliance, insurance_risk, climate_control_setup, final_approval])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, historical_exclusive)
root.order.add_edge(preliminary_check, provenance_exclusive)
root.order.add_edge(historical_exclusive, token_minting)
root.order.add_edge(provenance_exclusive, token_minting)
root.order.add_edge(token_minting, legal_compliance)
root.order.add_edge(token_minting, insurance_risk)
root.order.add_edge(legal_compliance, climate_control_setup)
root.order.add_edge(insurance_risk, climate_control_setup)
root.order.add_edge(climate_control_setup, final_approval)

# Print the root POWL model
print(root)