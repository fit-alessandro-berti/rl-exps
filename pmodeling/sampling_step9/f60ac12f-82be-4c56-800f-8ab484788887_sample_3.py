import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_blending = Transition(label='Culture Blending')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])
loop_culture_blending = OperatorPOWL(operator=Operator.LOOP, children=[culture_blending])
loop_milk_pasturize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasturize])
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

xor_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_sourcing, skip])
xor_culture_blending = OperatorPOWL(operator=Operator.XOR, children=[loop_culture_blending, skip])
xor_milk_pasturize = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_pasturize, skip])
xor_curd_cutting = OperatorPOWL(operator=Operator.XOR, children=[loop_curd_cutting, skip])
xor_whey_drain = OperatorPOWL(operator=Operator.XOR, children=[loop_whey_drain, skip])
xor_mold_inoculate = OperatorPOWL(operator=Operator.XOR, children=[loop_mold_inoculate, skip])
xor_press_cheese = OperatorPOWL(operator=Operator.XOR, children=[loop_press_cheese, skip])
xor_salt_brine = OperatorPOWL(operator=Operator.XOR, children=[loop_salt_brine, skip])
xor_age_monitor = OperatorPOWL(operator=Operator.XOR, children=[loop_age_monitor, skip])
xor_quality_test = OperatorPOWL(operator=Operator.XOR, children=[loop_quality_test, skip])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[loop_packaging_prep, skip])
xor_label_design = OperatorPOWL(operator=Operator.XOR, children=[loop_label_design, skip])
xor_order_allocation = OperatorPOWL(operator=Operator.XOR, children=[loop_order_allocation, skip])
xor_transport_arrange = OperatorPOWL(operator=Operator.XOR, children=[loop_transport_arrange, skip])
xor_retail_sync = OperatorPOWL(operator=Operator.XOR, children=[loop_retail_sync, skip])
xor_customer_review = OperatorPOWL(operator=Operator.XOR, children=[loop_customer_review, skip])
xor_feedback_analyze = OperatorPOWL(operator=Operator.XOR, children=[loop_feedback_analyze, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    xor_milk_sourcing,
    xor_culture_blending,
    xor_milk_pasturize,
    xor_curd_cutting,
    xor_whey_drain,
    xor_mold_inoculate,
    xor_press_cheese,
    xor_salt_brine,
    xor_age_monitor,
    xor_quality_test,
    xor_packaging_prep,
    xor_label_design,
    xor_order_allocation,
    xor_transport_arrange,
    xor_retail_sync,
    xor_customer_review,
    xor_feedback_analyze
])
root.order.add_edge(xor_milk_sourcing, xor_culture_blending)
root.order.add_edge(xor_culture_blending, xor_milk_pasturize)
root.order.add_edge(xor_milk_pasturize, xor_curd_cutting)
root.order.add_edge(xor_curd_cutting, xor_whey_drain)
root.order.add_edge(xor_whey_drain, xor_mold_inoculate)
root.order.add_edge(xor_mold_inoculate, xor_press_cheese)
root.order.add_edge(xor_press_cheese, xor_salt_brine)
root.order.add_edge(xor_salt_brine, xor_age_monitor)
root.order.add_edge(xor_age_monitor, xor_quality_test)
root.order.add_edge(xor_quality_test, xor_packaging_prep)
root.order.add_edge(xor_packaging_prep, xor_label_design)
root.order.add_edge(xor_label_design, xor_order_allocation)
root.order.add_edge(xor_order_allocation, xor_transport_arrange)
root.order.add_edge(xor_transport_arrange, xor_retail_sync)
root.order.add_edge(xor_retail_sync, xor_customer_review)
root.order.add_edge(xor_customer_review, xor_feedback_analyze)