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

# Define silent transitions for skip
skip = SilentTransition()

# Define exclusive choice for culture preparation
xor_culture = OperatorPOWL(operator=Operator.XOR, children=[culture_prep, skip])

# Define loop for aging process
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, microclimate_control, flavor_profiling])

# Define exclusive choice for quality check
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[sensory_review, texture_inspect])

# Define loop for eco packaging
loop_packaging = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, batch_labeling, blockchain_log])

# Define root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing, milk_pasteurize, coagulation, curd_cutting, whey_draining, hand_molding, pressing,
    salting, rind_treatment, xor_culture, loop_aging, quality_check, xor_quality, eco_packaging, loop_packaging, niche_shipping
])

# Define dependencies between nodes
root.order.add_edge(milk_sourcing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, hand_molding)
root.order.add_edge(hand_molding, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, rind_treatment)
root.order.add_edge(rind_treatment, xor_culture)
root.order.add_edge(xor_culture, loop_aging)
root.order.add_edge(loop_aging, quality_check)
root.order.add_edge(quality_check, xor_quality)
root.order.add_edge(xor_quality, eco_packaging)
root.order.add_edge(eco_packaging, loop_packaging)
root.order.add_edge(loop_packaging, niche_shipping)