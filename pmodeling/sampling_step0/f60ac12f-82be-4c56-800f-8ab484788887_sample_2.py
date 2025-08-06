import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_blending = Transition(label='Culture Blending')
pasteurize = Transition(label='Milk Pasteurize')
cutting = Transition(label='Curd Cutting')
drain = Transition(label='Whey Drain')
inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
brine = Transition(label='Salt Brine')
age_monitor = Transition(label='Age Monitor')
quality_test = Transition(label='Quality Test')
packaging_prep = Transition(label='Packaging Prep')
label_design = Transition(label='Label Design')
order_allocation = Transition(label='Order Allocation')
transport_arrange = Transition(label='Transport Arrange')
retail_sync = Transition(label='Retail Sync')
customer_review = Transition(label='Customer Review')
feedback_analyze = Transition(label='Feedback Analyze')

# Define choices and loops
culture_blending_choice = OperatorPOWL(operator=Operator.XOR, children=[culture_blending, pasteurize])
pasteurize_choice = OperatorPOWL(operator=Operator.XOR, children=[cutting, drain])
drain_choice = OperatorPOWL(operator=Operator.XOR, children=[inoculate, press_cheese])
press_cheese_choice = OperatorPOWL(operator=Operator.XOR, children=[brine, age_monitor])
age_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_test, packaging_prep])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[label_design, order_allocation])
order_allocation_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_arrange, retail_sync])
retail_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_review, feedback_analyze])

# Define partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_blending_choice,
    pasteurize_choice,
    drain_choice,
    inoculate_choice,
    press_cheese_choice,
    age_monitor_choice,
    quality_test_choice,
    packaging_prep_choice,
    label_design_choice,
    order_allocation_choice,
    transport_arrange_choice,
    retail_sync_choice,
    customer_review_choice,
    feedback_analyze_choice
])

# Define edges in the partial order
root.order.add_edge(milk_sourcing, culture_blending_choice)
root.order.add_edge(culture_blending_choice, pasteurize_choice)
root.order.add_edge(pasteurize_choice, drain_choice)
root.order.add_edge(drain_choice, inoculate_choice)
root.order.add_edge(inoculate_choice, press_cheese_choice)
root.order.add_edge(press_cheese_choice, brine_choice)
root.order.add_edge(brine_choice, age_monitor_choice)
root.order.add_edge(age_monitor_choice, quality_test_choice)
root.order.add_edge(quality_test_choice, packaging_prep_choice)
root.order.add_edge(packaging_prep_choice, label_design_choice)
root.order.add_edge(label_design_choice, order_allocation_choice)
root.order.add_edge(order_allocation_choice, transport_arrange_choice)
root.order.add_edge(transport_arrange_choice, retail_sync_choice)
root.order.add_edge(retail_sync_choice, customer_review_choice)
root.order.add_edge(customer_review_choice, feedback_analyze_choice)

# Print the final root model
print(root)