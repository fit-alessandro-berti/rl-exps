import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
intake       = Transition(label='Artifact Intake')
vis_inspect  = Transition(label='Visual Inspection')
material     = Transition(label='Material Testing')
radiocarbon  = Transition(label='Radiocarbon Dating')
provenance   = Transition(label='Provenance Check')
archive      = Transition(label='Archive Research')
expert       = Transition(label='Expert Review')
style        = Transition(label='Style Analysis')
craft        = Transition(label='Craftsmanship Eval')
condition    = Transition(label='Condition Check')
restoration  = Transition(label='Restoration Plan')
forgery      = Transition(label='Forgery Risk')
legal        = Transition(label='Legal Review')
report       = Transition(label='Report Drafting')
catalog      = Transition(label='Catalog Entry')

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, vis_inspect, material, radiocarbon, provenance, archive,
    expert, style, craft, condition, restoration, forgery, legal,
    report, catalog
])

# Define the control-flow dependencies
root.order.add_edge(intake,   vis_inspect)
root.order.add_edge(vis_inspect, material)
root.order.add_edge(material, radiocarbon)
root.order.add_edge(radiocarbon, provenance)
root.order.add_edge(provenance, archive)
root.order.add_edge(archive, expert)
root.order.add_edge(expert, style)
root.order.add_edge(expert, craft)
root.order.add_edge(style, condition)
root.order.add_edge(craft, condition)
root.order.add_edge(condition, restoration)
root.order.add_edge(condition, forgery)
root.order.add_edge(condition, legal)
root.order.add_edge(restoration, report)
root.order.add_edge(forgery, report)
root.order.add_edge(legal, report)
root.order.add_edge(report, catalog)

print(root)