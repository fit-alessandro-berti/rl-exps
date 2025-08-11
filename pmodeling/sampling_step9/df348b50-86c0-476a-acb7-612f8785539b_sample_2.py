import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

material_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing])
botanical_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[botanical_harvest])
extraction_phase_loop = OperatorPOWL(operator=Operator.LOOP, children=[extraction_phase])
accord_blending_loop = OperatorPOWL(operator=Operator.LOOP, children=[accord_blending])
olfactory_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[olfactory_testing])
aging_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_process])
stability_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[stability_check])
sensory_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_panel])
label_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_design])
bottle_crafting_loop = OperatorPOWL(operator=Operator.LOOP, children=[bottle_crafting])
batch_mixing_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_mixing])
quality_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_review])
packaging_final_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_final])
inventory_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_final, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

root = StrictPartialOrder(nodes=[
    material_sourcing_loop,
    botanical_harvest_loop,
    extraction_phase_loop,
    accord_blending_loop,
    olfactory_testing_loop,
    aging_process_loop,
    stability_check_loop,
    sensory_panel_loop,
    label_design_loop,
    bottle_crafting_loop,
    xor1,
    xor2,
    xor3,
    xor4
])
root.order.add_edge(material_sourcing_loop, botanical_harvest_loop)
root.order.add_edge(botanical_harvest_loop, extraction_phase_loop)
root.order.add_edge(extraction_phase_loop, accord_blending_loop)
root.order.add_edge(accord_blending_loop, olfactory_testing_loop)
root.order.add_edge(olfactory_testing_loop, aging_process_loop)
root.order.add_edge(aging_process_loop, stability_check_loop)
root.order.add_edge(stability_check_loop, sensory_panel_loop)
root.order.add_edge(sensory_panel_loop, label_design_loop)
root.order.add_edge(label_design_loop, bottle_crafting_loop)
root.order.add_edge(bottle_crafting_loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)