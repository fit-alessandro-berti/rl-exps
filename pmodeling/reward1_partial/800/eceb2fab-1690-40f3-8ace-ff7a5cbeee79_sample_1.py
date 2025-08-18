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

# Define the loop for the restoration phases
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    disassembly, surface_clean, structural_repair, reconstruction, finish_match, stabilize_parts, documentation
])

# Define the exclusive choice for the quality validation and market analysis
quality_and_market = OperatorPOWL(operator=Operator.XOR, children=[
    quality_audit, market_analysis
])

# Define the root process
root = StrictPartialOrder(nodes=[restoration_loop, quality_and_market, target_outreach, delivery_prep, client_feedback])
root.order.add_edge(restoration_loop, quality_and_market)
root.order.add_edge(quality_and_market, target_outreach)
root.order.add_edge(target_outreach, delivery_prep)
root.order.add_edge(delivery_prep, client_feedback)

# Return the root process
print(root)