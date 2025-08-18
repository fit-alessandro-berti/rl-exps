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
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging_final = Transition(label='Packaging Final')
inventory_update = Transition(label='Inventory Update')
market_launch = Transition(label='Market Launch')

# Define the partial order model
root = StrictPartialOrder(nodes=[sourcing, harvest, extraction, blending, testing, aging, stability, sensory, label_design, bottle_crafting, batch_mixing, quality_review, packaging_final, inventory_update, market_launch])

# Define the partial order dependencies
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, aging)
root.order.add_edge(aging, stability)
root.order.add_edge(stability, sensory)
root.order.add_edge(sensory, label_design)
root.order.add_edge(label_design, bottle_crafting)
root.order.add_edge(bottle_crafting, batch_mixing)
root.order.add_edge(batch_mixing, quality_review)
root.order.add_edge(quality_review, packaging_final)
root.order.add_edge(packaging_final, inventory_update)
root.order.add_edge(inventory_update, market_launch)

# Print the root model
print(root)