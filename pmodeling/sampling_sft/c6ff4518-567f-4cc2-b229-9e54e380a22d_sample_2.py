import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
milk_sourcing      = Transition(label='Milk Sourcing')
culture_prep       = Transition(label='Culture Prep')
milk_pasturize     = Transition(label='Milk Pasteurize')
coagulation        = Transition(label='Coagulation')
curd_cutting       = Transition(label='Curd Cutting')
whey_draining      = Transition(label='Whey Draining')
hand_molding       = Transition(label='Hand Molding')
pressing           = Transition(label='Pressing')
salting            = Transition(label='Salting')
rind_treatment     = Transition(label='Rind Treatment')
aging_setup        = Transition(label='Aging Setup')
microclimate_ctrl  = Transition(label='Microclimate Control')
flavor_profiling   = Transition(label='Flavor Profiling')
quality_check      = Transition(label='Quality Check')
sensory_review     = Transition(label='Sensory Review')
texture_inspect    = Transition(label='Texture Inspect')
eco_packaging      = Transition(label='Eco Packaging')
batch_labeling     = Transition(label='Batch Labeling')
blockchain_log     = Transition(label='Blockchain Log')
niche_shipping     = Transition(label='Niche Shipping')

# Define the loop for seasonal aging control
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_ctrl, aging_setup])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_prep, milk_pasturize,
    coagulation, curd_cutting, whey_draining,
    hand_molding, pressing, salting,
    rind_treatment, aging_loop,
    flavor_profiling, quality_check,
    sensory_review, texture_inspect,
    eco_packaging, batch_labeling,
    blockchain_log, niche_shipping
])

# Define the control-flow dependencies
# Milk Production
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(milk_sourcing, milk_pasturize)

# Cheese Production
root.order.add_edge(culture_prep, coagulation)
root.order.add_edge(milk_pasturize, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, hand_molding)
root.order.add_edge(hand_molding, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, rind_treatment)

# Aging Control
root.order.add_edge(aging_loop, flavor_profiling)

# Quality Control
root.order.add_edge(quality_check, sensory_review)
root.order.add_edge(quality_check, texture_inspect)

# Packaging & Distribution
root.order.add_edge(eco_packaging, batch_labeling)
root.order.add_edge(blockchain_log, batch_labeling)
root.order.add_edge(batch_labeling, niche_shipping)

# Finalize the loop body
root.order.add_edge(flavor_profiling, aging_loop)
root.order.add_edge(sensory_review, aging_loop)
root.order.add_edge(texture_inspect, aging_loop)