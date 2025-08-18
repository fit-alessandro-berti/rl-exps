import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
hand_molding = Transition(label='Hand Molding')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
rind_treatment = Transition(label='Rind Treatment')
aging_setup = Transition(label='Aging Setup')
microclimate_control = Transition(label='Microclimate Control')
flavor_profiling = Transition(label='Flavor Profiling')
quality_check = Transition(label='Quality Check')
sensory_review = Transition(label='Sensory Review')
texture_inspect = Transition(label='Texture Inspect')
eco_packaging = Transition(label='Eco Packaging')
batch_labeling = Transition(label='Batch Labeling')
blockchain_log = Transition(label='Blockchain Log')
niche_shipping = Transition(label='Niche Shipping')

# Define silent transitions
skip = SilentTransition()

# Define the process tree
loop_molding = OperatorPOWL(operator=Operator.LOOP, children=[hand_molding, pressing, salting])
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, microclimate_control])
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_check, sensory_review])
loop_flavor = OperatorPOWL(operator=Operator.LOOP, children=[flavor_profiling, texture_inspect])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, blockchain_log])
loop_shipping = OperatorPOWL(operator=Operator.LOOP, children=[niche_shipping])

# Construct the root node
root = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, milk_pasteurize, coagulation, curd_cutting, whey_draining, loop_molding, rind_treatment, loop_aging, flavor_profiling, loop_flavor, quality_check, sensory_review, texture_inspect, xor_packaging, eco_packaging, blockchain_log, niche_shipping])
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, loop_molding)
root.order.add_edge(loop_molding, rind_treatment)
root.order.add_edge(rind_treatment, loop_aging)
root.order.add_edge(loop_aging, flavor_profiling)
root.order.add_edge(flavor_profiling, loop_flavor)
root.order.add_edge(loop_flavor, quality_check)
root.order.add_edge(quality_check, sensory_review)
root.order.add_edge(sensory_review, texture_inspect)
root.order.add_edge(texture_inspect, xor_packaging)
root.order.add_edge(xor_packaging, eco_packaging)
root.order.add_edge(eco_packaging, blockchain_log)
root.order.add_edge(blockchain_log, niche_shipping)