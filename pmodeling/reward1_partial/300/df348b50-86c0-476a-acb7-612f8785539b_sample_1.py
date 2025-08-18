from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
material_sourcing = Transition(label='Material Sourcing')
botanical_harvest = Transition(label='Botanical Harvest')
extraction_phase = Transition(label='Extraction Phase')
accord_blending = Transition(label='Accord Blending')
olfactory_testing = Transition(label='Olfactory Testing')
aging_process = Transition(label='Aging Process')
stability_check = Transition(label='Stability Check')
sensory_panel = Transition(label='Sensory Panel')
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging_final = Transition(label='Packaging Final')
inventory_update = Transition(label='Inventory Update')
market_launch = Transition(label='Market Launch')

# Define the loop for the extraction phase
loop_extraction = OperatorPOWL(operator=Operator.LOOP, children=[extraction_phase])

# Define the xor for the sensory panel and market launch
xor_sensory_market = OperatorPOWL(operator=Operator.XOR, children=[sensory_panel, market_launch])

# Define the root POWL model
root = StrictPartialOrder(nodes=[material_sourcing, botanical_harvest, loop_extraction, accord_blending, olfactory_testing, aging_process, stability_check, xor_sensory_market, label_design, bottle_crafting, batch_mixing, quality_review, packaging_final, inventory_update])
root.order.add_edge(material_sourcing, botanical_harvest)
root.order.add_edge(botanical_harvest, loop_extraction)
root.order.add_edge(loop_extraction, accord_blending)
root.order.add_edge(accord_blending, olfactory_testing)
root.order.add_edge(olfactory_testing, aging_process)
root.order.add_edge(aging_process, stability_check)
root.order.add_edge(stability_check, xor_sensory_market)
root.order.add_edge(xor_sensory_market, label_design)
root.order.add_edge(label_design, bottle_crafting)
root.order.add_edge(bottle_crafting, batch_mixing)
root.order.add_edge(batch_mixing, quality_review)
root.order.add_edge(quality_review, packaging_final)
root.order.add_edge(packaging_final, inventory_update)