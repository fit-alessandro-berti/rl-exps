import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions (if any)

# Define exclusive choice for extraction methods
enfleurage = Transition(label='Enfleurage')
steam_distillation = Transition(label='Steam Distillation')
choice_extraction = OperatorPOWL(operator=Operator.XOR, children=[enfleurage, steam_distillation])

# Define loop for aging process
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging])

# Define strict partial order for the process
root = StrictPartialOrder(nodes=[sourcing, harvest, choice_extraction, blending, testing, loop_aging, stability, sensory, labeling, bottling, mixing, review, packaging, inventory, launch])

# Define dependencies between nodes
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, choice_extraction)
root.order.add_edge(choice_extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, loop_aging)
root.order.add_edge(loop_aging, stability)
root.order.add_edge(stability, sensory)
root.order.add_edge(sensory, labeling)
root.order.add_edge(labeling, bottling)
root.order.add_edge(bottling, mixing)
root.order.add_edge(mixing, review)
root.order.add_edge(review, packaging)
root.order.add_edge(packaging, inventory)
root.order.add_edge(inventory, launch)

print(root)