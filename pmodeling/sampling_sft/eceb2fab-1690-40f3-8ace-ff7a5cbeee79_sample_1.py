import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
provenance_check = Transition(label='Provenance Check')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
disassembly = Transition(label='Disassembly')
surface_clean = Transition(label='Surface Clean')
stabilize_parts = Transition(label='Stabilize Parts')
structural_repair = Transition(label='Structural Repair')
reconstruction = Transition(label='Reconstruction')
finish_match = Transition(label='Finish Match')
documentation = Transition(label='Documentation')
quality_audit = Transition(label='Quality Audit')
valuation = Transition(label='Valuation')
market_analysis = Transition(label='Market Analysis')
target_outreach = Transition(label='Target Outreach')
client_feedback = Transition(label='Client Feedback')
delivery_prep = Transition(label='Delivery Prep')

# Loop for repeated documentation and feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation, client_feedback])

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    condition_scan,
    material_test,
    disassembly,
    surface_clean,
    stabilize_parts,
    structural_repair,
    reconstruction,
    finish_match,
    loop,
    quality_audit,
    valuation,
    market_analysis,
    target_outreach,
    delivery_prep
])

# Define the control-flow dependencies
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, disassembly)
root.order.add_edge(disassembly, surface_clean)
root.order.add_edge(surface_clean, stabilize_parts)
root.order.add_edge(stabilize_parts, structural_repair)
root.order.add_edge(structural_repair, reconstruction)
root.order.add_edge(reconstruction, finish_match)
root.order.add_edge(finish_match, loop)
root.order.add_edge(loop, quality_audit)
root.order.add_edge(quality_audit, valuation)
root.order.add_edge(valuation, market_analysis)
root.order.add_edge(market_analysis, target_outreach)
root.order.add_edge(target_outreach, delivery_prep)