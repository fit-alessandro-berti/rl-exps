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

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_review, chemical_test, provenance_audit, expert_panel])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[token_minting, SilentTransition()])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, compliance_check, insurance_valuation, risk_assessment])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, climate_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, SilentTransition()])
root = StrictPartialOrder(nodes=[artifact_intake, loop1, xor1, loop2, loop3, xor2, final_approval])
root.order.add_edge(artifact_intake, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor2, final_approval)

# Print the POWL model
print(root)