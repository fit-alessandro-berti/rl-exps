import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake      = Transition(label='Artifact Intake')
preliminary_check    = Transition(label='Preliminary Check')
historical_review    = Transition(label='Historical Review')
chemical_test        = Transition(label='Chemical Test')
provenance_audit     = Transition(label='Provenance Audit')
expert_panel         = Transition(label='Expert Panel')
token_minting        = Transition(label='Token Minting')
legal_review         = Transition(label='Legal Review')
compliance_check     = Transition(label='Compliance Check')
insurance_valuation  = Transition(label='Insurance Valuation')
risk_assessment      = Transition(label='Risk Assessment')
packaging_prep       = Transition(label='Packaging Prep')
climate_control      = Transition(label='Climate Control')
transport_setup      = Transition(label='Transport Setup')
final_approval       = Transition(label='Final Approval')

# Build the loop for expert validation (historical -> chemical -> provenance)
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_review, chemical_test, provenance_audit])

# Build the choice for optional insurance valuation (can be skipped)
insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[insurance_valuation, Transition(label=''))]

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    preliminary_check,
    expert_loop,
    expert_panel,
    token_minting,
    legal_review,
    compliance_check,
    insurance_xor,
    risk_assessment,
    packaging_prep,
    climate_control,
    transport_setup,
    final_approval
])

# Define the control-flow edges
root.order.add_edge(artifact_intake, preliminary_check)
root.order.add_edge(preliminary_check, expert_loop)
root.order.add_edge(expert_loop, expert_panel)
root.order.add_edge(expert_panel, token_minting)
root.order.add_edge(token_minting, legal_review)
root.order.add_edge(legal_review, compliance_check)
root.order.add_edge(compliance_check, insurance_xor)
root.order.add_edge(insurance_xor, risk_assessment)
root.order.add_edge(risk_assessment, packaging_prep)
root.order.add_edge(packaging_prep, climate_control)
root.order.add_edge(climate_control, transport_setup)
root.order.add_edge(transport_setup, final_approval)