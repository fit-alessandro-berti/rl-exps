import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
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

# Build the aging sub‐process: Aging Set -> Flavor Check -> Texture Scan -> Quality Approve
aging = StrictPartialOrder(nodes=[aging_set, flavor_check, texture_scan, quality_approve])
aging.order.add_edge(aging_set, flavor_check)
aging.order.add_edge(flavor_check, texture_scan)
aging.order.add_edge(texture_scan, quality_approve)

# Build the distribution loop: Custom Pack -> Cold Ship (then optional Retail Train -> Feedback Log -> Batch Adjust)
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_pack, cold_ship])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    farm_select, milk_test, milk_pasteurize, curd_form, whey_drain, cheese_press,
    salt_rub, aging, distribution_loop, retail_train, feedback_log, batch_adjust
])

# Define the control‐flow dependencies
root.order.add_edge(farm_select, milk_test)
root.order.add_edge(milk_test, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_form)
root.order.add_edge(curd_form, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salt_rub)
root.order.add_edge(salt_rub, aging)
root.order.add_edge(aging, distribution_loop)

# The distribution loop can happen before or after the aging process
root.order.add_edge(aging, distribution_loop)
root.order.add_edge(aging, retail_train)

# After distribution, optional training and feedback can occur before the next batch adjustment
root.order.add_edge(distribution_loop, retail_train)
root.order.add_edge(retail_train, feedback_log)
root.order.add_edge(feedback_log, batch_adjust)