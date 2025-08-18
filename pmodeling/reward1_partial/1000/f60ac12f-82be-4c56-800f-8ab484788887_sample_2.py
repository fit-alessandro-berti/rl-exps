import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop nodes
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])
loop_culture_blending = OperatorPOWL(operator=Operator.LOOP, children=[culture_blending])
loop_milk_pasteurize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize])
loop_curd_cutting = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting])
loop_whey_drain = OperatorPOWL(operator=Operator.LOOP, children=[whey_drain])
loop_mold_inoculate = OperatorPOWL(operator=Operator.LOOP, children=[mold_inoculate])
loop_press_cheese = OperatorPOWL(operator=Operator.LOOP, children=[press_cheese])
loop_salt_brine = OperatorPOWL(operator=Operator.LOOP, children=[salt_brine])
loop_age_monitor = OperatorPOWL(operator=Operator.LOOP, children=[age_monitor])
loop_quality_test = OperatorPOWL(operator=Operator.LOOP, children=[quality_test])
loop_packaging_prep = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
loop_label_design = OperatorPOWL(operator=Operator.LOOP, children=[label_design])
loop_order_allocation = OperatorPOWL(operator=Operator.LOOP, children=[order_allocation])
loop_transport_arrange = OperatorPOWL(operator=Operator.LOOP, children=[transport_arrange])
loop_retail_sync = OperatorPOWL(operator=Operator.LOOP, children=[retail_sync])
loop_customer_review = OperatorPOWL(operator=Operator.LOOP, children=[customer_review])
loop_feedback_analyze = OperatorPOWL(operator=Operator.LOOP, children=[feedback_analyze])

# Define the exclusive choice nodes
exclusive_choice_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_sourcing, loop_culture_blending])
exclusive_choice_culture_blending = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_pasteurize, loop_curd_cutting])
exclusive_choice_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[loop_whey_drain, loop_mold_inoculate])
exclusive_choice_whey_drain = OperatorPOWL(operator=Operator.XOR, children=[loop_press_cheese, loop_salt_brine])
exclusive_choice_press_cheese = OperatorPOWL(operator=Operator.XOR, children=[loop_age_monitor, loop_quality_test])
exclusive_choice_age_monitor = OperatorPOWL(operator=Operator.XOR, children=[loop_packaging_prep, loop_label_design])
exclusive_choice_label_design = OperatorPOWL(operator=Operator.XOR, children=[loop_order_allocation, loop_transport_arrange])
exclusive_choice_order_allocation = OperatorPOWL(operator=Operator.XOR, children=[loop_retail_sync, loop_customer_review])
exclusive_choice_retail_sync = OperatorPOWL(operator=Operator.XOR, children=[loop_feedback_analyze, loop_customer_review])

# Define the root node
root = StrictPartialOrder(nodes=[exclusive_choice_milk_sourcing, exclusive_choice_culture_blending, exclusive_choice_milk_pasteurize, exclusive_choice_whey_drain, exclusive_choice_press_cheese, exclusive_choice_age_monitor, exclusive_choice_label_design, exclusive_choice_order_allocation, exclusive_choice_retail_sync, exclusive_choice_customer_review, exclusive_choice_feedback_analyze])
root.order.add_edge(exclusive_choice_milk_sourcing, exclusive_choice_culture_blending)
root.order.add_edge(exclusive_choice_culture_blending, exclusive_choice_milk_pasteurize)
root.order.add_edge(exclusive_choice_milk_pasteurize, exclusive_choice_whey_drain)
root.order.add_edge(exclusive_choice_whey_drain, exclusive_choice_press_cheese)
root.order.add_edge(exclusive_choice_press_cheese, exclusive_choice_age_monitor)
root.order.add_edge(exclusive_choice_age_monitor, exclusive_choice_label_design)
root.order.add_edge(exclusive_choice_label_design, exclusive_choice_order_allocation)
root.order.add_edge(exclusive_choice_order_allocation, exclusive_choice_retail_sync)
root.order.add_edge(exclusive_choice_retail_sync, exclusive_choice_customer_review)
root.order.add_edge(exclusive_choice_customer_review, exclusive_choice_feedback_analyze)

# Print the root node
print(root)