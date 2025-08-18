import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sourcing = Transition(label='Material Sourcing')
harvest = Transition(label='Botanical Harvest')
extraction = Transition(label='Extraction Phase')
blending = Transition(label='Accord Blending')
testing = Transition(label='Olfactory Testing')
aging = Transition(label='Aging Process')
stability = Transition(label='Stability Check')
panel = Transition(label='Sensory Panel')
label = Transition(label='Label Design')
bottle = Transition(label='Bottle Crafting')
mixing = Transition(label='Batch Mixing')
review = Transition(label='Quality Review')
packaging = Transition(label='Packaging Final')
inventory = Transition(label='Inventory Update')
launch = Transition(label='Market Launch')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    sourcing, harvest, extraction, blending, testing, aging, stability, panel, label, bottle, mixing, review, packaging, inventory, launch
])

# Define the partial order dependencies
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, aging)
root.order.add_edge(aging, stability)
root.order.add_edge(stability, panel)
root.order.add_edge(panel, label)
root.order.add_edge(label, bottle)
root.order.add_edge(bottle, mixing)
root.order.add_edge(mixing, review)
root.order.add_edge(review, packaging)
root.order.add_edge(packaging, inventory)
root.order.add_edge(inventory, launch)

print(root)