from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Supplier Vetting')
design = Transition(label='Design Review')
prototype = Transition(label='Prototype Build')
audit = Transition(label='Quality Audit')
scheduling = Transition(label='Batch Scheduling')
handcrafting = Transition(label='Handcrafting')
packaging = Transition(label='Packaging Design')
labeling = Transition(label='Custom Labeling')
sustainability = Transition(label='Sustainability Check')
inventory = Transition(label='Inventory Sync')
analysis = Transition(label='Market Analysis')
aggregation = Transition(label='Order Aggregation')
distribution = Transition(label='Distribution Plan')
feedback = Transition(label='Customer Feedback')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    sourcing, vetting, design, prototype, audit, scheduling, handcrafting, packaging, labeling, sustainability, inventory, analysis, aggregation, distribution, feedback
])

# Define the dependencies
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, design)
root.order.add_edge(design, prototype)
root.order.add_edge(prototype, audit)
root.order.add_edge(audit, scheduling)
root.order.add_edge(scheduling, handcrafting)
root.order.add_edge(handcrafting, packaging)
root.order.add_edge(packaging, labeling)
root.order.add_edge(labeling, sustainability)
root.order.add_edge(sustainability, inventory)
root.order.add_edge(inventory, analysis)
root.order.add_edge(analysis, aggregation)
root.order.add_edge(aggregation, distribution)
root.order.add_edge(distribution, feedback)

# Print the root POWL model
print(root)