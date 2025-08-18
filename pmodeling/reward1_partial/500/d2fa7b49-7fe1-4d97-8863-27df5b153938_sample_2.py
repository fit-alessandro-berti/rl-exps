import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process steps
artifact_intake_to_preliminary_check = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, preliminary_check])
preliminary_check_to_historical_review = OperatorPOWL(operator=Operator.XOR, children=[preliminary_check, historical_review])
historical_review_to_chemical_test = OperatorPOWL(operator=Operator.XOR, children=[historical_review, chemical_test])
chemical_test_to_provenance_audit = OperatorPOWL(operator=Operator.XOR, children=[chemical_test, provenance_audit])
provenance_audit_to_expert_panel = OperatorPOWL(operator=Operator.XOR, children=[provenance_audit, expert_panel])
expert_panel_to_token_minting = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, token_minting])
token_minting_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[token_minting, legal_review])
legal_review_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
compliance_check_to_insurance_valuation = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_valuation])
insurance_valuation_to_risk_assessment = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
risk_assessment_to_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, packaging_prep])
packaging_prep_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])
climate_control_to_transport_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_control, transport_setup])
transport_setup_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, final_approval])

# Create the root model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    preliminary_check,
    historical_review,
    chemical_test,
    provenance_audit,
    expert_panel,
    token_minting,
    legal_review,
    compliance_check,
    insurance_valuation,
    risk_assessment,
    packaging_prep,
    climate_control,
    transport_setup,
    final_approval
])
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