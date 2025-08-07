import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names as described
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

# Define the partial order model
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

# Define the dependencies between the activities
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

# The final POWL model is now defined in the 'root' variable.