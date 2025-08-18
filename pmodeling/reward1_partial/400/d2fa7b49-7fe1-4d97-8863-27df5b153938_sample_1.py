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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[token_minting, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, insurance_valuation, risk_assessment])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    preliminary_check,
    historical_review,
    chemical_test,
    provenance_audit,
    expert_panel,
    xor,
    loop,
    packaging_prep,
    climate_control,
    transport_setup,
    final_approval
])

# Add dependencies
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, historical_review)
root.order.add_edge(historical_review, chemical_test)
root.order.add_edge(chemical_test, provenance_audit)
root.order.add_edge(provenance_audit, expert_panel)
root.order.add_edge(expert_panel, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, packaging_prep)
root.order.add_edge(packaging_prep, climate_control)
root.order.add_edge(climate_control, transport_setup)
root.order.add_edge(transport_setup, final_approval)

# Print the POWL model
print(root)