from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
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

# Define nodes
loop_artifact_intake = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, preliminary_check])
xor_token_minting_legal_review = OperatorPOWL(operator=Operator.XOR, children=[token_minting, legal_review])
xor_compliance_check_insurance_valuation = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_valuation])
xor_risk_assessment_climate_control = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, climate_control])
xor_transport_setup_final_approval = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, final_approval])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop_artifact_intake, xor_token_minting_legal_review, xor_compliance_check_insurance_valuation, xor_risk_assessment_climate_control, xor_transport_setup_final_approval])
root.order.add_edge(loop_artifact_intake, xor_token_minting_legal_review)
root.order.add_edge(xor_token_minting_legal_review, xor_compliance_check_insurance_valuation)
root.order.add_edge(xor_compliance_check_insurance_valuation, xor_risk_assessment_climate_control)
root.order.add_edge(xor_risk_assessment_climate_control, xor_transport_setup_final_approval)

print(root)