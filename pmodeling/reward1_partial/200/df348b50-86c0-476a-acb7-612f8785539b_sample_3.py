from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
harvest = Transition(label='Botanical Harvest')
extraction = Transition(label='Extraction Phase')
blending = Transition(label='Accord Blending')
testing = Transition(label='Olfactory Testing')
aging = Transition(label='Aging Process')
stability_check = Transition(label='Stability Check')
sensory_panel = Transition(label='Sensory Panel')
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging_final = Transition(label='Packaging Final')
launch = Transition(label='Market Launch')
update_inventory = Transition(label='Inventory Update')

# Define control-flow operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[harvest, sourcing])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[extraction, blending])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[testing, aging])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[stability_check, sensory_panel])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[label_design, bottle_crafting])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, quality_review])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_final, update_inventory])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[launch, update_inventory])

# Define the root POWL model
root = StrictPartialOrder(nodes=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8])
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)