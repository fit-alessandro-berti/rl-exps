import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_review, chemical_test, provenance_audit, expert_panel])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[token_minting, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, risk_assessment])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_control])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[transport_setup, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, final_approval])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(xor1, final_approval)
root.order.add_edge(xor2, final_approval)
root.order.add_edge(xor3, final_approval)
root.order.add_edge(xor4, final_approval)
root.order.add_edge(xor5, final_approval)

# Return the root of the POWL model
return root