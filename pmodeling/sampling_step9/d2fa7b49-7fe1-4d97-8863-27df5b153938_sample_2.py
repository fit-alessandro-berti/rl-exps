import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define sub-processes
artifact_validation = OperatorPOWL(operator=Operator.XOR, children=[historical_review, chemical_test, provenance_audit, expert_panel])
blockchain_token_minting = OperatorPOWL(operator=Operator.XOR, children=[token_minting, skip])
compliance_checks = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
insurance_valuation_check = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, skip])
risk_assessment_check = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])
packaging_prep_climate_control = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])
transport_setup_final_approval = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, final_approval])

# Define main process
root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, artifact_validation, blockchain_token_minting, compliance_checks, insurance_valuation_check, risk_assessment_check, packaging_prep_climate_control, transport_setup_final_approval])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, artifact_validation)
root.order.add_edge(artifact_validation, blockchain_token_minting)
root.order.add_edge(blockchain_token_minting, compliance_checks)
root.order.add_edge(compliance_checks, insurance_valuation_check)
root.order.add_edge(insurance_valuation_check, risk_assessment_check)
root.order.add_edge(risk_assessment_check, packaging_prep_climate_control)
root.order.add_edge(packaging_prep_climate_control, transport_setup_final_approval)

print(root)