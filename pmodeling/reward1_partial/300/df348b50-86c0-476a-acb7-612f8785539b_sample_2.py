import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
harvest = Transition(label='Botanical Harvest')
extraction = Transition(label='Extraction Phase')
blending = Transition(label='Accord Blending')
testing = Transition(label='Olfactory Testing')
aging = Transition(label='Aging Process')
stability = Transition(label='Stability Check')
sensory = Transition(label='Sensory Panel')
labeling = Transition(label='Label Design')
bottling = Transition(label='Bottle Crafting')
mixing = Transition(label='Batch Mixing')
review = Transition(label='Quality Review')
packaging = Transition(label='Packaging Final')
inventory = Transition(label='Inventory Update')
launch = Transition(label='Market Launch')

# Define the partial order structure
root = StrictPartialOrder(nodes=[sourcing, harvest, extraction, blending, testing, aging, stability, sensory, labeling, bottling, mixing, review, packaging, inventory, launch])

# Define dependencies between activities
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, aging)
root.order.add_edge(aging, stability)
root.order.add_edge(stability, sensory)
root.order.add_edge(sensory, labeling)
root.order.add_edge(labeling, bottling)
root.order.add_edge(bottling, mixing)
root.order.add_edge(mixing, review)
root.order.add_edge(review, packaging)
root.order.add_edge(packaging, inventory)
root.order.add_edge(inventory, launch)

print(root)