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

# Define transitions for silent activities
skip = SilentTransition()

# Define partial order nodes
culture_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_prep])
milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip])
coagulation_choice = OperatorPOWL(operator=Operator.XOR, children=[coagulation, skip])
curd_cutting_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
whey_draining_choice = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, skip])
hand_molding_choice = OperatorPOWL(operator=Operator.XOR, children=[hand_molding, skip])
pressing_choice = OperatorPOWL(operator=Operator.XOR, children=[pressing, skip])
salting_choice = OperatorPOWL(operator=Operator.XOR, children=[salting, skip])
rind_treatment_choice = OperatorPOWL(operator=Operator.XOR, children=[rind_treatment, skip])
aging_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip])
microclimate_control_choice = OperatorPOWL(operator=Operator.XOR, children=[microclimate_control, skip])
flavor_profiling_choice = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip])
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
sensory_review_choice = OperatorPOWL(operator=Operator.XOR, children=[sensory_review, skip])
texture_inspect_choice = OperatorPOWL(operator=Operator.XOR, children=[texture_inspect, skip])
eco_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
batch_labeling_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, skip])
blockchain_log_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log, skip])
niche_shipping_choice = OperatorPOWL(operator=Operator.XOR, children=[niche_shipping, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    culture_prep_loop,
    milk_sourcing_choice,
    coagulation_choice,
    curd_cutting_choice,
    whey_draining_choice,
    hand_molding_choice,
    pressing_choice,
    salting_choice,
    rind_treatment_choice,
    aging_setup_choice,
    microclimate_control_choice,
    flavor_profiling_choice,
    quality_check_choice,
    sensory_review_choice,
    texture_inspect_choice,
    eco_packaging_choice,
    batch_labeling_choice,
    blockchain_log_choice,
    niche_shipping_choice
])

# Define the order between nodes
root.order.add_edge(culture_prep_loop, milk_sourcing_choice)
root.order.add_edge(milk_sourcing_choice, coagulation_choice)
root.order.add_edge(coagulation_choice, curd_cutting_choice)
root.order.add_edge(curd_cutting_choice, whey_draining_choice)
root.order.add_edge(whey_draining_choice, hand_molding_choice)
root.order.add_edge(hand_molding_choice, pressing_choice)
root.order.add_edge(pressing_choice, salting_choice)
root.order.add_edge(salting_choice, rind_treatment_choice)
root.order.add_edge(rind_treatment_choice, aging_setup_choice)
root.order.add_edge(aging_setup_choice, microclimate_control_choice)
root.order.add_edge(microclimate_control_choice, flavor_profiling_choice)
root.order.add_edge(flavor_profiling_choice, quality_check_choice)
root.order.add_edge(quality_check_choice, sensory_review_choice)
root.order.add_edge(sensory_review_choice, texture_inspect_choice)
root.order.add_edge(texture_inspect_choice, eco_packaging_choice)
root.order.add_edge(eco_packaging_choice, batch_labeling_choice)
root.order.add_edge(batch_labeling_choice, blockchain_log_choice)
root.order.add_edge(blockchain_log_choice, niche_shipping_choice)

# Print the root POWL model
print(root)