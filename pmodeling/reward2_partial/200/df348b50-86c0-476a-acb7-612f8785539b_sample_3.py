import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
sourcing = Transition(label='Material Sourcing')
harvest = Transition(label='Botanical Harvest')
extraction = Transition(label='Extraction Phase')
blending = Transition(label='Accord Blending')
testing = Transition(label='Olfactory Testing')
aging = Transition(label='Aging Process')
stability = Transition(label='Stability Check')
sensory_panel = Transition(label='Sensory Panel')
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging_final = Transition(label='Packaging Final')
inventory_update = Transition(label='Inventory Update')
market_launch = Transition(label='Market Launch')

# Define the partial order (dependencies)
root = StrictPartialOrder(nodes=[sourcing, harvest, extraction, blending, testing, aging, stability, sensory_panel, label_design, bottle_crafting, batch_mixing, quality_review, packaging_final, inventory_update, market_launch])

# Define the dependencies between activities
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, aging)
root.order.add_edge(aging, stability)
root.order.add_edge(stability, sensory_panel)
root.order.add_edge(sensory_panel, label_design)
root.order.add_edge(label_design, bottle_crafting)
root.order.add_edge(bottle_crafting, batch_mixing)
root.order.add_edge(batch_mixing, quality_review)
root.order.add_edge(quality_review, packaging_final)
root.order.add_edge(packaging_final, inventory_update)
root.order.add_edge(inventory_update, market_launch)

# Print the root of the POWL model
print(root)