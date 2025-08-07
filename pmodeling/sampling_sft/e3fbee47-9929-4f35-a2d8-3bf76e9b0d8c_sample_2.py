import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
farm_sel      = Transition(label='Farm Selection')
milk_test     = Transition(label='Milk Testing')
pasteurize    = Transition(label='Batch Pasteurize')
culture_add   = Transition(label='Culture Add')
curd_cut      = Transition(label='Curd Cut')
whey_drain    = Transition(label='Whey Drain')
mold_inoc     = Transition(label='Mold Inoculate')
press_form    = Transition(label='Press Form')
salt_rub      = Transition(label='Salt Rub')
aging_mon     = Transition(label='Aging Monitor')
flavor_adj    = Transition(label='Flavor Adjust')
pack_design   = Transition(label='Packaging Design')
label_approval= Transition(label='Label Approval')
order_proc    = Transition(label='Order Processing')
cold_store    = Transition(label='Cold Storage')
delivery_sched= Transition(label='Delivery Schedule')
retail_setup  = Transition(label='Retail Setup')
feedback_col  = Transition(label='Feedback Collect')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: after aging, either adjust flavor or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_mon, flavor_adj])

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm_sel, milk_test, pasteurize, culture_add, curd_cut,
    whey_drain, mold_inoc, press_form, salt_rub,
    loop,
    pack_design, label_approval,
    order_proc, cold_store, delivery_sched,
    retail_setup, feedback_col
])

# Add control-flow edges
root.order.add_edge(farm_sel, milk_test)
root.order.add_edge(milk_test, pasteurize)
root.order.add_edge(pasteurize, culture_add)
root.order.add_edge(culture_add, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoc)
root.order.add_edge(mold_inoc, press_form)
root.order.add_edge(press_form, salt_rub)
root.order.add_edge(salt_rub, loop)
root.order.add_edge(loop, pack_design)
root.order.add_edge(loop, label_approval)
root.order.add_edge(pack_design, order_proc)
root.order.add_edge(label_approval, order_proc)
root.order.add_edge(order_proc, cold_store)
root.order.add_edge(cold_store, delivery_sched)
root.order.add_edge(delivery_sched, retail_setup)
root.order.add_edge(retail_setup, feedback_col)