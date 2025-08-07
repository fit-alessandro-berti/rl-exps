import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order structure
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

# Define the order dependencies
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(condition_scan, disassembly)
root.order.add_edge(condition_scan, surface_clean)
root.order.add_edge(material_test, structural_repair)
root.order.add_edge(material_test, reconstruction)
root.order.add_edge(surface_clean, finish_match)
root.order.add_edge(structural_repair, stabilize_parts)
root.order.add_edge(structural_repair, documentation)
root.order.add_edge(reconstruction, stabilize_parts)
root.order.add_edge(reconstruction, documentation)
root.order.add_edge(finish_match, stabilize_parts)
root.order.add_edge(finish_match, documentation)
root.order.add_edge(stabilize_parts, quality_audit)
root.order.add_edge(stabilize_parts, valuation)
root.order.add_edge(stabilize_parts, market_analysis)
root.order.add_edge(stabilize_parts, target_outreach)
root.order.add_edge(stabilize_parts, delivery_prep)
root.order.add_edge(stabilize_parts, client_feedback)
root.order.add_edge(documentation, quality_audit)
root.order.add_edge(documentation, valuation)
root.order.add_edge(documentation, market_analysis)
root.order.add_edge(documentation, target_outreach)
root.order.add_edge(documentation, delivery_prep)
root.order.add_edge(documentation, client_feedback)

# Print the final root model
print(root)