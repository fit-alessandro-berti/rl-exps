import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        provenance_check: [condition_scan],
        condition_scan: [material_test],
        material_test: [disassembly],
        disassembly: [surface_clean, structural_repair],
        surface_clean: [reconstruction],
        structural_repair: [finish_match],
        reconstruction: [stabilize_parts],
        stabilize_parts: [documentation],
        documentation: [quality_audit],
        quality_audit: [valuation],
        valuation: [market_analysis],
        market_analysis: [target_outreach],
        target_outreach: [delivery_prep],
        delivery_prep: [client_feedback]
    }
)

# Add edges to the order
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, disassembly)
root.order.add_edge(disassembly, surface_clean)
root.order.add_edge(disassembly, structural_repair)
root.order.add_edge(surface_clean, reconstruction)
root.order.add_edge(structural_repair, finish_match)
root.order.add_edge(reconstruction, stabilize_parts)
root.order.add_edge(stabilize_parts, documentation)
root.order.add_edge(documentation, quality_audit)
root.order.add_edge(quality_audit, valuation)
root.order.add_edge(valuation, market_analysis)
root.order.add_edge(market_analysis, target_outreach)
root.order.add_edge(target_outreach, delivery_prep)
root.order.add_edge(delivery_prep, client_feedback)

# Now 'root' is the POWL model for the process