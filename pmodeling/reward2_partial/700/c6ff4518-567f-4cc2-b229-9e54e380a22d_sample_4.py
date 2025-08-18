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

# Define the process structure
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_pasteurize,
    coagulation,
    curd_cutting,
    whey_draining,
    hand_molding,
    pressing,
    salting,
    rind_treatment,
    aging_setup,
    microclimate_control,
    flavor_profiling,
    quality_check,
    sensory_review,
    texture_inspect,
    eco_packaging,
    batch_labeling,
    blockchain_log,
    niche_shipping
])

# Define dependencies between activities
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, hand_molding)
root.order.add_edge(hand_molding, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, rind_treatment)
root.order.add_edge(rind_treatment, aging_setup)
root.order.add_edge(aging_setup, microclimate_control)
root.order.add_edge(microclimate_control, flavor_profiling)
root.order.add_edge(flavor_profiling, quality_check)
root.order.add_edge(quality_check, sensory_review)
root.order.add_edge(sensory_review, texture_inspect)
root.order.add_edge(texture_inspect, eco_packaging)
root.order.add_edge(eco_packaging, batch_labeling)
root.order.add_edge(batch_labeling, blockchain_log)
root.order.add_edge(blockchain_log, niche_shipping)

# Print the root model
print(root)