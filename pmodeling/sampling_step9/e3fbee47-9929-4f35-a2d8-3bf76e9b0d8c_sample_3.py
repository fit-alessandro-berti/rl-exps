import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
farm_selection = Transition(label='Farm Selection')
milk_testing = Transition(label='Milk Testing')
batch_pasturize = Transition(label='Batch Pasteurize')
culture_add = Transition(label='Culture Add')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_form = Transition(label='Press Form')
salt_rub = Transition(label='Salt Rub')
aging_monitor = Transition(label='Aging Monitor')
flavor_adjust = Transition(label='Flavor Adjust')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_processing = Transition(label='Order Processing')
cold_storage = Transition(label='Cold Storage')
delivery_schedule = Transition(label='Delivery Schedule')
retail_setup = Transition(label='Retail Setup')
feedback_collect = Transition(label='Feedback Collect')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for milk testing
xor_milk_testing = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])

# Define the exclusive choice for aging monitoring
xor_aging_monitor = OperatorPOWL(operator=Operator.XOR, children=[aging_monitor, skip])

# Define the exclusive choice for flavor adjustment
xor_flavor_adjust = OperatorPOWL(operator=Operator.XOR, children=[flavor_adjust, skip])

# Define the exclusive choice for packaging design
xor_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])

# Define the exclusive choice for label approval
xor_label_approval = OperatorPOWL(operator=Operator.XOR, children=[label_approval, skip])

# Define the exclusive choice for order processing
xor_order_processing = OperatorPOWL(operator=Operator.XOR, children=[order_processing, skip])

# Define the exclusive choice for cold storage
xor_cold_storage = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, skip])

# Define the exclusive choice for delivery schedule
xor_delivery_schedule = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, skip])

# Define the exclusive choice for retail setup
xor_retail_setup = OperatorPOWL(operator=Operator.XOR, children=[retail_setup, skip])

# Define the exclusive choice for feedback collection
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

# Define the loop for aging monitoring
loop_aging_monitor = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitor, xor_flavor_adjust])

# Define the loop for packaging design
loop_packaging_design = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, xor_label_approval])

# Define the loop for order processing
loop_order_processing = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, xor_cold_storage])

# Define the loop for cold storage
loop_cold_storage = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, xor_delivery_schedule])

# Define the loop for delivery schedule
loop_delivery_schedule = OperatorPOWL(operator=Operator.LOOP, children=[delivery_schedule, xor_retail_setup])

# Define the loop for retail setup
loop_retail_setup = OperatorPOWL(operator=Operator.LOOP, children=[retail_setup, xor_feedback_collect])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    xor_milk_testing,
    loop_aging_monitor,
    loop_packaging_design,
    loop_order_processing,
    loop_cold_storage,
    loop_delivery_schedule,
    loop_retail_setup
])
root.order.add_edge(xor_milk_testing, loop_aging_monitor)
root.order.add_edge(loop_aging_monitor, loop_packaging_design)
root.order.add_edge(loop_packaging_design, loop_order_processing)
root.order.add_edge(loop_order_processing, loop_cold_storage)
root.order.add_edge(loop_cold_storage, loop_delivery_schedule)
root.order.add_edge(loop_delivery_schedule, loop_retail_setup)

# Print the root POWL model
print(root)