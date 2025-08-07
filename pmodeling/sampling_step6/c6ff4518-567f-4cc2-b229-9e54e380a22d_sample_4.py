import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the root of the process as a StrictPartialOrder
root = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, milk_pasteurize, coagulation, curd_cutting, whey_draining, hand_molding, pressing, salting, rind_treatment, aging_setup, microclimate_control, flavor_profiling, quality_check, sensory_review, texture_inspect, eco_packaging, batch_labeling, blockchain_log, niche_shipping])

# Optionally, you can define dependencies if needed. For example, if milk sourcing must be done before culture preparation:
# root.order.add_edge(milk_sourcing, culture_prep)

# This is the final POWL model for the process.
print(root)