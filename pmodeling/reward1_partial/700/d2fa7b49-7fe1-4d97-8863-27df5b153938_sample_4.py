import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
# Validate the artifact
xor1 = OperatorPOWL(operator=Operator.XOR, children=[historical_review, chemical_test, provenance_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, token_minting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check, insurance_valuation, risk_assessment])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control, transport_setup, final_approval])

root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, xor1, xor2, xor3, xor4])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

print(root)