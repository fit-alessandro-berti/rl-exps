import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_blending = Transition(label='Culture Blending')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
salt_brine = Transition(label='Salt Brine')
age_monitor = Transition(label='Age Monitor')
quality_test = Transition(label='Quality Test')
packaging_prep = Transition(label='Packaging Prep')
label_design = Transition(label='Label Design')
order_allocation = Transition(label='Order Allocation')
transport_arrange = Transition(label='Transport Arrange')
retail_sync = Transition(label='Retail Sync')
customer_review = Transition(label='Customer Review')
feedback_analyze = Transition(label='Feedback Analyze')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_blending,
    milk_pasteurize,
    curd_cutting,
    whey_drain,
    mold_inoculate,
    press_cheese,
    salt_brine,
    age_monitor,
    quality_test,
    packaging_prep,
    label_design,
    order_allocation,
    transport_arrange,
    retail_sync,
    customer_review,
    feedback_analyze
])

# Define the partial order edges
root.order.add_edge(milk_sourcing, culture_blending)
root.order.add_edge(culture_blending, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, salt_brine)
root.order.add_edge(salt_brine, age_monitor)
root.order.add_edge(age_monitor, quality_test)
root.order.add_edge(quality_test, packaging_prep)
root.order.add_edge(packaging_prep, label_design)
root.order.add_edge(label_design, order_allocation)
root.order.add_edge(order_allocation, transport_arrange)
root.order.add_edge(transport_arrange, retail_sync)
root.order.add_edge(retail_sync, customer_review)
root.order.add_edge(customer_review, feedback_analyze)

print(root)