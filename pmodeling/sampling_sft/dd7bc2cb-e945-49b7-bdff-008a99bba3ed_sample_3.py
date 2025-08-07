import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
farm_select     = Transition(label='Farm Select')
milk_test       = Transition(label='Milk Test')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_form       = Transition(label='Curd Form')
whey_drain      = Transition(label='Whey Drain')
cheese_press    = Transition(label='Cheese Press')
salt_rub        = Transition(label='Salt Rub')
aging_set       = Transition(label='Aging Set')
flavor_check    = Transition(label='Flavor Check')
texture_scan    = Transition(label='Texture Scan')
quality_approve = Transition(label='Quality Approve')
custom_pack     = Transition(label='Custom Pack')
cold_ship       = Transition(label='Cold Ship')
retail_train    = Transition(label='Retail Train')
feedback_log    = Transition(label='Feedback Log')
batch_adjust    = Transition(label='Batch Adjust')

# Loop for continuous aging and quality checks
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flavor_check, texture_scan]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    farm_select, milk_test, milk_pasteurize, curd_form, whey_drain, cheese_press, salt_rub,
    aging_set, aging_loop,
    quality_approve,
    custom_pack, cold_ship, retail_train, feedback_log, batch_adjust
])

# Sequence of milk processing before aging
root.order.add_edge(farm_select, milk_test)
root.order.add_edge(milk_test, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_form)
root.order.add_edge(curd_form, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salt_rub)

# Aging and quality control loop
root.order.add_edge(salt_rub, aging_set)
root.order.add_edge(aging_set, aging_loop)

# After aging, approve quality and proceed to packaging
root.order.add_edge(aging_loop, quality_approve)

# Packaging and distribution
root.order.add_edge(quality_approve, custom_pack)
root.order.add_edge(custom_pack, cold_ship)
root.order.add_edge(cold_ship, retail_train)

# Retail training and feedback loop
root.order.add_edge(retail_train, feedback_log)
root.order.add_edge(feedback_log, batch_adjust)