import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define loops and choices
coagulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[coagulation, whey_draining])
curd_cutting_loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, hand_molding])
pressing_loop = OperatorPOWL(operator=Operator.LOOP, children=[pressing, salting])
rind_treatment_loop = OperatorPOWL(operator=Operator.LOOP, children=[rind_treatment, microclimate_control])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, flavor_profiling])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, sensory_review, texture_inspect])

# Define XOR for Eco Packaging and Batch Labeling
eco_packaging_xor = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, batch_labeling])

# Define XOR for Blockchain Log and Niche Shipping
blockchain_log_xor = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log, niche_shipping])

# Define root Partial Order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_pasturize,
    coagulation_loop,
    curd_cutting_loop,
    pressing_loop,
    rind_treatment_loop,
    aging_loop,
    quality_loop,
    eco_packaging_xor,
    blockchain_log_xor
])

# Add edges to the Partial Order
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasturize)
root.order.add_edge(milk_pasturize, coagulation_loop)
root.order.add_edge(coagulation_loop, curd_cutting_loop)
root.order.add_edge(curd_cutting_loop, pressing_loop)
root.order.add_edge(pressing_loop, rind_treatment_loop)
root.order.add_edge(rind_treatment_loop, aging_loop)
root.order.add_edge(aging_loop, quality_loop)
root.order.add_edge(quality_loop, eco_packaging_xor)
root.order.add_edge(eco_packaging_xor, blockchain_log_xor)
root.order.add_edge(blockchain_log_xor, niche_shipping)

# Print the root Partial Order
print(root)