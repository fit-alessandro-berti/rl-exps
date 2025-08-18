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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[token_minting, legal_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, insurance_valuation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, packaging_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, transport_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, None])  # 'None' represents an empty set of children

# Define the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, preliminary_check, historical_review, chemical_test, provenance_audit, expert_panel, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, historical_review)
root.order.add_edge(historical_review, chemical_test)
root.order.add_edge(chemical_test, provenance_audit)
root.order.add_edge(provenance_audit, expert_panel)
root.order.add_edge(expert_panel, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, final_approval)