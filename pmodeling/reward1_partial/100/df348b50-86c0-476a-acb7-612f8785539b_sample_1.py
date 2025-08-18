import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for the process
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
review = Transition(label='Quality Review')
packaging = Transition(label='Packaging Final')
launch = Transition(label='Market Launch')

# Define the operators for the process
xor = OperatorPOWL(operator=Operator.XOR, children=[aging, stability])
loop = OperatorPOWL(operator=Operator.LOOP, children=[blending, testing])
partial_order = StrictPartialOrder(nodes=[sourcing, harvest, extraction, xor, loop, label_design, bottle_crafting, batch_mixing, review, packaging, launch])
partial_order.order.add_edge(sourcing, harvest)
partial_order.order.add_edge(harvest, extraction)
partial_order.order.add_edge(extraction, xor)
partial_order.order.add_edge(xor, loop)
partial_order.order.add_edge(loop, blending)
partial_order.order.add_edge(blending, testing)
partial_order.order.add_edge(testing, aging)
partial_order.order.add_edge(aging, stability)
partial_order.order.add_edge(stability, sensory)
partial_order.order.add_edge(sensory, label_design)
partial_order.order.add_edge(label_design, bottle_crafting)
partial_order.order.add_edge(bottle_crafting, batch_mixing)
partial_order.order.add_edge(batch_mixing, review)
partial_order.order.add_edge(review, packaging)
partial_order.order.add_edge(packaging, launch)

# Assign the generated POWL model to the variable 'root'
root = partial_order