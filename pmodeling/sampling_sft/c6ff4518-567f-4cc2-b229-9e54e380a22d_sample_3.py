import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_past = Transition(label='Milk Pasteurize')
coagulation = Transition(label='Coagulation')
curd_cut = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Draining')
hand_mold = Transition(label='Hand Molding')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
rind_treat = Transition(label='Rind Treatment')
aging_setup = Transition(label='Aging Setup')
microclimate_ctrl = Transition(label='Microclimate Control')
flavor_prof = Transition(label='Flavor Profiling')
quality_check = Transition(label='Quality Check')
sensory_review = Transition(label='Sensory Review')
texture_inspect = Transition(label='Texture Inspect')
eco_packaging = Transition(label='Eco Packaging')
batch_labeling = Transition(label='Batch Labeling')
blockchain_log = Transition(label='Blockchain Log')
niche_shipping = Transition(label='Niche Shipping')

# Loop for continuous aging
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_ctrl, flavor_prof, quality_check, sensory_review, texture_inspect])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_past,
    coagulation,
    curd_cut,
    whey_drain,
    hand_mold,
    pressing,
    salting,
    rind_treat,
    aging_loop,
    eco_packaging,
    batch_labeling,
    blockchain_log,
    niche_shipping
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_past)
root.order.add_edge(milk_past, coagulation)
root.order.add_edge(coagulation, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, hand_mold)
root.order.add_edge(hand_mold, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, rind_treat)
root.order.add_edge(rind_treat, aging_loop)
root.order.add_edge(aging_loop, eco_packaging)
root.order.add_edge(eco_packaging, batch_labeling)
root.order.add_edge(batch_labeling, blockchain_log)
root.order.add_edge(blockchain_log, niche_shipping)