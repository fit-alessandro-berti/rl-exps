import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
assess = Transition(label='Assess Artifact')
verify = Transition(label='Verify Provenance')
cond = Transition(label='Analyze Condition')
plan = Transition(label='Plan Conservation')
clean = Transition(label='Clean Surface')
stabilize = Transition(label='Stabilize Structure')
source = Transition(label='Source Materials')
fabricate = Transition(label='Fabricate Parts')
repair = Transition(label='Perform Repairs')
patina = Transition(label='Apply Patina')
colors = Transition(label='Match Colors')
doc = Transition(label='Document Process')
quality = Transition(label='Review Quality')
approval = Transition(label='Obtain Approval')
package = Transition(label='Package Securely')
transport = Transition(label='Arrange Transport')

# Loop for repeated cleaning and stabilization
clean_stab_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[clean, stabilize]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    assess,
    verify,
    cond,
    plan,
    clean_stab_loop,
    source,
    fabricate,
    repair,
    patina,
    colors,
    doc,
    quality,
    approval,
    package,
    transport
])

# Define the control-flow dependencies
root.order.add_edge(assess, verify)
root.order.add_edge(verify, cond)
root.order.add_edge(cond, plan)
root.order.add_edge(plan, clean_stab_loop)
root.order.add_edge(clean_stab_loop, source)
root.order.add_edge(source, fabricate)
root.order.add_edge(fabricate, repair)
root.order.add_edge(repair, patina)
root.order.add_edge(patina, colors)
root.order.add_edge(colors, doc)
root.order.add_edge(doc, quality)
root.order.add_edge(quality, approval)
root.order.add_edge(approval, package)
root.order.add_edge(package, transport)