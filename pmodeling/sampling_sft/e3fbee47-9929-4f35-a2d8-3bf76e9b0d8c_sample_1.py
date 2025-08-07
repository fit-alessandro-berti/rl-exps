import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
farm_selection       = Transition(label='Farm Selection')
milk_testing         = Transition(label='Milk Testing')
batch_pasteurize     = Transition(label='Batch Pasteurize')
culture_add          = Transition(label='Culture Add')
curd_cut             = Transition(label='Curd Cut')
whey_drain           = Transition(label='Whey Drain')
mold_inoculate       = Transition(label='Mold Inoculate')
press_form           = Transition(label='Press Form')
salt_rub             = Transition(label='Salt Rub')
aging_monitor        = Transition(label='Aging Monitor')
flavor_adjust        = Transition(label='Flavor Adjust')
packaging_design     = Transition(label='Packaging Design')
label_approval       = Transition(label='Label Approval')
order_processing     = Transition(label='Order Processing')
cold_storage         = Transition(label='Cold Storage')
delivery_schedule    = Transition(label='Delivery Schedule')
retail_setup         = Transition(label='Retail Setup')
feedback_collect     = Transition(label='Feedback Collect')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    farm_selection, milk_testing,
    batch_pasteurize, culture_add,
    curd_cut, whey_drain, mold_inoculate,
    press_form, salt_rub,
    aging_monitor, flavor_adjust,
    packaging_design, label_approval,
    order_processing, cold_storage,
    delivery_schedule, retail_setup,
    feedback_collect
])

# Define the control‐flow dependencies
# 1. After farm selection, proceed to milk testing
root.order.add_edge(farm_selection, milk_testing)

# 2. Milk testing → batch pasteurize
root.order.add_edge(milk_testing, batch_pasteurize)

# 3. Batch pasteurize → culture add
root.order.add_edge(batch_pasteurize, culture_add)

# 4. Culture add → curd cut
root.order.add_edge(culture_add, curd_cut)

# 5. Curd cut → whey drain
root.order.add_edge(curd_cut, whey_drain)

# 6. Whey drain → mold inoculate
root.order.add_edge(whey_drain, mold_inoculate)

# 7. Mold inoculate → press form
root.order.add_edge(mold_inoculate, press_form)

# 8. Press form → salt rub
root.order.add_edge(press_form, salt_rub)

# 9. Salt rub → aging monitor
root.order.add_edge(salt_rub, aging_monitor)

# 10. Aging monitor → flavor adjust
root.order.add_edge(aging_monitor, flavor_adjust)

# 11. Flavor adjust → packaging design
root.order.add_edge(flavor_adjust, packaging_design)

# 12. Packaging design → label approval
root.order.add_edge(packaging_design, label_approval)

# 13. Label approval → order processing
root.order.add_edge(label_approval, order_processing)

# 14. Order processing → cold storage
root.order.add_edge(order_processing, cold_storage)

# 15. Cold storage → delivery schedule
root.order.add_edge(cold_storage, delivery_schedule)

# 16. Delivery schedule → retail setup
root.order.add_edge(delivery_schedule, retail_setup)

# 17. Retail setup → feedback collect
root.order.add_edge(retail_setup, feedback_collect)

# The sequence of activities is now fully defined