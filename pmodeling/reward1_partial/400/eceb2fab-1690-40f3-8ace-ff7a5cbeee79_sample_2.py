import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
provenance_check_to_condition_scan = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[provenance_check, condition_scan])
condition_scan_to_material_test = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[condition_scan, material_test])
material_test_to_disassembly = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[material_test, disassembly])
disassembly_to_surface_clean = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[disassembly, surface_clean])
surface_clean_to_structural_repair = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[surface_clean, structural_repair])
structural_repair_to_reconstruction = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[structural_repair, reconstruction])
reconstruction_to_finish_match = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[reconstruction, finish_match])
finish_match_to_stabilize_parts = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[finish_match, stabilize_parts])
stabilize_parts_to_documentation = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[stabilize_parts, documentation])
documentation_to_quality_audit = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[documentation, quality_audit])
quality_audit_to_valuation = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[quality_audit, valuation])
valuation_to_market_analysis = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[valuation, market_analysis])
market_analysis_to_target_outreach = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[market_analysis, target_outreach])
target_outreach_to_delivery_prep = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[target_outreach, delivery_prep])
delivery_prep_to_client_feedback = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[delivery_prep, client_feedback])

# Create the root model
root = StrictPartialOrder(nodes=[
    provenance_check,
    condition_scan,
    material_test,
    disassembly,
    surface_clean,
    structural_repair,
    reconstruction,
    finish_match,
    stabilize_parts,
    documentation,
    quality_audit,
    valuation,
    market_analysis,
    target_outreach,
    delivery_prep,
    client_feedback
])

# Define the dependencies
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, disassembly)
root.order.add_edge(disassembly, surface_clean)
root.order.add_edge(surface_clean, structural_repair)
root.order.add_edge(structural_repair, reconstruction)
root.order.add_edge(reconstruction, finish_match)
root.order.add_edge(finish_match, stabilize_parts)
root.order.add_edge(stabilize_parts, documentation)
root.order.add_edge(documentation, quality_audit)
root.order.add_edge(quality_audit, valuation)
root.order.add_edge(valuation, market_analysis)
root.order.add_edge(market_analysis, target_outreach)
root.order.add_edge(target_outreach, delivery_prep)
root.order.add_edge(delivery_prep, client_feedback)

# Print the root model
print(root)