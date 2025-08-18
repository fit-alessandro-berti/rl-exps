from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[token_minting, expert_panel, historical_review, chemical_test, provenance_audit])

root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, loop, xor])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, loop)
root.order.add_edge(loop, xor)

print(root)