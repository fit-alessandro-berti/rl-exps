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

# Define loops and XORs as per the process description
multi_disciplinary_validation = OperatorPOWL(operator=Operator.XOR, children=[historical_review, chemical_test, provenance_audit, expert_panel])
blockchain_minting = OperatorPOWL(operator=Operator.LOOP, children=[token_minting])
jurisdictional_compliance = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, compliance_check])
insurance_valuation_and_risk = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
packaging_and_climate_control = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, multi_disciplinary_validation, blockchain_minting, jurisdictional_compliance, insurance_valuation_and_risk, packaging_and_climate_control, transport_setup, final_approval])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, multi_disciplinary_validation)
root.order.add_edge(multi_disciplinary_validation, blockchain_minting)
root.order.add_edge(blockchain_minting, jurisdictional_compliance)
root.order.add_edge(jurisdictional_compliance, insurance_valuation_and_risk)
root.order.add_edge(insurance_valuation_and_risk, packaging_and_climate_control)
root.order.add_edge(packaging_and_climate_control, transport_setup)
root.order.add_edge(transport_setup, final_approval)

# Print the root POWL model
print(root)