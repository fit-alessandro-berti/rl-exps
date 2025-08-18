import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow
artifact_intake_to_preliminary_check = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, preliminary_check])
preliminary_check_to_expert_panel = OperatorPOWL(operator=Operator.XOR, children=[preliminary_check, expert_panel])
expert_panel_to_token_minting = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, token_minting])
token_minting_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[token_minting, legal_review])
legal_review_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
compliance_check_to_insurance_valuation = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_valuation])
insurance_valuation_to_risk_assessment = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
risk_assessment_to_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, packaging_prep])
packaging_prep_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])
climate_control_to_transport_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_control, transport_setup])
transport_setup_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, final_approval])

# Define the loop
artifact_intake_to_preliminary_check_to_expert_panel_to_token_minting_to_legal_review_to_compliance_check_to_insurance_valuation_to_risk_assessment_to_packaging_prep_to_climate_control_to_transport_setup_to_final_approval = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake_to_preliminary_check, preliminary_check_to_expert_panel, expert_panel_to_token_minting, token_minting_to_legal_review, legal_review_to_compliance_check, compliance_check_to_insurance_valuation, insurance_valuation_to_risk_assessment, risk_assessment_to_packaging_prep, packaging_prep_to_climate_control, climate_control_to_transport_setup, transport_setup_to_final_approval])

# Define the root
root = StrictPartialOrder(nodes=[artifact_intake_to_preliminary_check_to_expert_panel_to_token_minting_to_legal_review_to_compliance_check_to_insurance_valuation_to_risk_assessment_to_packaging_prep_to_climate_control_to_transport_setup_to_final_approval])
root.order.add_edge(artifact_intake_to_preliminary_check_to_expert_panel_to_token_minting_to_legal_review_to_compliance_check_to_insurance_valuation_to_risk_assessment_to_packaging_prep_to_climate_control_to_transport_setup_to_final_approval, final_approval)

# Print the root
print(root)