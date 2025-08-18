from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
provenance_check = Transition(label='Provenance Check')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
disassembly = Transition(label='Disassembly')
surface_clean = Transition(label='Surface Clean')
structural_repair = Transition(label='Structural Repair')
reconstruction = Transition(label='Reconstruction')
finish_match = Transition(label='Finish Match')
stabilize_parts = Transition(label='Stabilize Parts')
documentation = Transition(label='Documentation')
quality_audit = Transition(label='Quality Audit')
valuation = Transition(label='Valuation')
market_analysis = Transition(label='Market Analysis')
target_outreach = Transition(label='Target Outreach')
delivery_prep = Transition(label='Delivery Prep')
client_feedback = Transition(label='Client Feedback')

# Define loops and exclusive choices
provenance_and_condition = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, condition_scan])
material_test_and_disassembly = OperatorPOWL(operator=Operator.XOR, children=[material_test, disassembly])
surface_clean_and_structural_repair = OperatorPOWL(operator=Operator.XOR, children=[surface_clean, structural_repair])
reconstruction_and_finish_match = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, finish_match])
stabilize_parts_and_documentation = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, documentation])
quality_audit_and_valuation = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, valuation])
market_analysis_and_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])
delivery_prep_and_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define partial order
root = StrictPartialOrder(nodes=[
    provenance_and_condition,
    material_test_and_disassembly,
    surface_clean_and_structural_repair,
    reconstruction_and_finish_match,
    stabilize_parts_and_documentation,
    quality_audit_and_valuation,
    market_analysis_and_target_outreach,
    delivery_prep_and_client_feedback
])
root.order.add_edge(provenance_and_condition, material_test_and_disassembly)
root.order.add_edge(material_test_and_disassembly, surface_clean_and_structural_repair)
root.order.add_edge(surface_clean_and_structural_repair, reconstruction_and_finish_match)
root.order.add_edge(reconstruction_and_finish_match, stabilize_parts_and_documentation)
root.order.add_edge(stabilize_parts_and_documentation, quality_audit_and_valuation)
root.order.add_edge(quality_audit_and_valuation, market_analysis_and_target_outreach)
root.order.add_edge(market_analysis_and_target_outreach, delivery_prep_and_client_feedback)

# Print the root POWL model
print(root)