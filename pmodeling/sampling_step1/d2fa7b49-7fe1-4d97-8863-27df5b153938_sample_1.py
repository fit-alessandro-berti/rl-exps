import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[token_minting, expert_panel])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[provenance_audit, chemical_test])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[historical_review, preliminary_check])

# Define the partial order
root = StrictPartialOrder(nodes=[
    xor,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    artifact_intake
])

# Define the order dependencies
root.order.add_edge(artifact_intake, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor)
root.order.add_edge(xor, final_approval)

# Print the final POWL model
print(root)