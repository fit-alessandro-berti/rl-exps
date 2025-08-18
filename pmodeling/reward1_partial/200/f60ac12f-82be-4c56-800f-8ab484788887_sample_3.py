import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
milk_process = OperatorPOWL(operator=Operator.LOOP, children=[
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
    label_design
])

allocation_process = OperatorPOWL(operator=Operator.LOOP, children=[
    order_allocation,
    transport_arrange,
    retail_sync,
    customer_review,
    feedback_analyze
])

root = StrictPartialOrder(nodes=[milk_process, allocation_process])
root.order.add_edge(milk_process, allocation_process)

print(root)