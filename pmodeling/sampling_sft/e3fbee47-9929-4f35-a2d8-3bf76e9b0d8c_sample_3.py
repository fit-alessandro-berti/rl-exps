import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm_selection     = Transition(label='Farm Selection')
milk_testing       = Transition(label='Milk Testing')
batch_pasteurize   = Transition(label='Batch Pasteurize')
culture_add        = Transition(label='Culture Add')
curd_cut           = Transition(label='Curd Cut')
whey_drain         = Transition(label='Whey Drain')
mold_inoculate     = Transition(label='Mold Inoculate')
press_form         = Transition(label='Press Form')
salt_rub           = Transition(label='Salt Rub')
aging_monitor      = Transition(label='Aging Monitor')
flavor_adjust      = Transition(label='Flavor Adjust')
packaging_design   = Transition(label='Packaging Design')
label_approval     = Transition(label='Label Approval')
order_processing   = Transition(label='Order Processing')
cold_storage       = Transition(label='Cold Storage')
delivery_schedule  = Transition(label='Delivery Schedule')
retail_setup       = Transition(label='Retail Setup')
feedback_collect   = Transition(label='Feedback Collect')

# Loop for seasonal flavor adjustment: repeat until exit
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[flavor_adjust, flavor_adjust])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    farm_selection, milk_testing, batch_pasteurize, culture_add,
    curd_cut, whey_drain, mold_inoculate, press_form, salt_rub,
    aging_monitor, seasonal_loop, packaging_design, label_approval,
    order_processing, cold_storage, delivery_schedule, retail_setup,
    feedback_collect
])

# Sequential edges
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, batch_pasteurize)
root.order.add_edge(batch_pasteurize, culture_add)
root.order.add_edge(culture_add, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_form)
root.order.add_edge(press_form, salt_rub)
root.order.add_edge(salt_rub, aging_monitor)
root.order.add_edge(aging_monitor, seasonal_loop)

# After seasonal loop, proceed with packaging, label approval, and order processing
root.order.add_edge(seasonal_loop, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_processing)

# After order processing, proceed to cold storage and delivery scheduling
root.order.add_edge(order_processing, cold_storage)
root.order.add_edge(cold_storage, delivery_schedule)

# After delivery, proceed to retail setup and feedback collection
root.order.add_edge(delivery_schedule, retail_setup)
root.order.add_edge(retail_setup, feedback_collect)