import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
assess = Transition(label='Assess Artifact')
verify = Transition(label='Verify Provenance')
analyze = Transition(label='Analyze Condition')
plan = Transition(label='Plan Conservation')
clean = Transition(label='Clean Surface')
stabilize = Transition(label='Stabilize Structure')
source = Transition(label='Source Materials')
fabricate = Transition(label='Fabricate Parts')
repairs = Transition(label='Perform Repairs')
patina = Transition(label='Apply Patina')
colors = Transition(label='Match Colors')
document = Transition(label='Document Process')
review = Transition(label='Review Quality')
approve = Transition(label='Obtain Approval')
package = Transition(label='Package Securely')
transport = Transition(label='Arrange Transport')
skip = SilentTransition()

# Loop for optional fabrication and sourcing
fabricate_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fabricate, skip]
)
source_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[source, skip]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    assess,
    verify,
    analyze,
    plan,
    clean,
    stabilize,
    source_loop,
    fabricate_loop,
    repairs,
    patina,
    colors,
    document,
    review,
    approve,
    package,
    transport
])

# Define the control-flow dependencies
root.order.add_edge(assess, verify)
root.order.add_edge(verify, analyze)
root.order.add_edge(analyze, plan)

# After planning, perform cleaning and stabilization in parallel
root.order.add_edge(plan, clean)
root.order.add_edge(plan, stabilize)

# After cleaning and stabilization, either fabricate or source parts (exclusive choice)
root.order.add_edge(clean, fabricate_loop)
root.order.add_edge(stabilize, source_loop)

# Both fabricate and source can lead to repairs
for child in [fabricate_loop, source_loop]:
    root.order.add_edge(child, repairs)

# Repairs can lead to either patina or color matching
root.order.add_edge(repairs, patina)
root.order.add_edge(repairs, colors)

# Both patina and color matching can lead to documentation
root.order.add_edge(patina, document)
root.order.add_edge(colors, document)

# After documentation, there are two paths: quality review and approval, then transport, or just transport
root.order.add_edge(document, review)
root.order.add_edge(document, approve)
root.order.add_edge(review, transport)
root.order.add_edge(approve, transport)

# Finally, transport must happen
root.order.add_edge(transport, skip)  # skip is a placeholder for end of process