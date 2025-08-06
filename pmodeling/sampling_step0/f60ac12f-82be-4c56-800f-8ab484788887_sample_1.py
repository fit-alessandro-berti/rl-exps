import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loop nodes
loop_milk_pasteurize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, culture_blending])
loop_milk_pasteurize.order.add_edge(milk_pasteurize, culture_blending)

loop_curd_cutting = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, whey_drain])
loop_curd_cutting.order.add_edge(curd_cutting, whey_drain)

loop_mold_inoculate = OperatorPOWL(operator=Operator.LOOP, children=[mold_inoculate, press_cheese])
loop_mold_inoculate.order.add_edge(mold_inoculate, press_cheese)

loop_salt_brine = OperatorPOWL(operator=Operator.LOOP, children=[salt_brine, age_monitor])
loop_salt_brine.order.add_edge(salt_brine, age_monitor)

loop_age_monitor = OperatorPOWL(operator=Operator.LOOP, children=[age_monitor, quality_test])
loop_age_monitor.order.add_edge(age_monitor, quality_test)

loop_quality_test = OperatorPOWL(operator=Operator.LOOP, children=[quality_test, packaging_prep])
loop_quality_test.order.add_edge(quality_test, packaging_prep)

loop_packaging_prep = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, label_design])
loop_packaging_prep.order.add_edge(packaging_prep, label_design)

loop_label_design = OperatorPOWL(operator=Operator.LOOP, children=[label_design, order_allocation])
loop_label_design.order.add_edge(label_design, order_allocation)

loop_order_allocation = OperatorPOWL(operator=Operator.LOOP, children=[order_allocation, transport_arrange])
loop_order_allocation.order.add_edge(order_allocation, transport_arrange)

loop_transport_arrange = OperatorPOWL(operator=Operator.LOOP, children=[transport_arrange, retail_sync])
loop_transport_arrange.order.add_edge(transport_arrange, retail_sync)

loop_retail_sync = OperatorPOWL(operator=Operator.LOOP, children=[retail_sync, customer_review])
loop_retail_sync.order.add_edge(retail_sync, customer_review)

loop_customer_review = OperatorPOWL(operator=Operator.LOOP, children=[customer_review, feedback_analyze])
loop_customer_review.order.add_edge(customer_review, feedback_analyze)

# Define XOR nodes
xor_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
xor_curd_cutting = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
xor_mold_inoculate = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, skip])
xor_salt_brine = OperatorPOWL(operator=Operator.XOR, children=[salt_brine, skip])
xor_age_monitor = OperatorPOWL(operator=Operator.XOR, children=[age_monitor, skip])
xor_quality_test = OperatorPOWL(operator=Operator.XOR, children=[quality_test, skip])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor_label_design = OperatorPOWL(operator=Operator.XOR, children=[label_design, skip])
xor_order_allocation = OperatorPOWL(operator=Operator.XOR, children=[order_allocation, skip])
xor_transport_arrange = OperatorPOWL(operator=Operator.XOR, children=[transport_arrange, skip])
xor_retail_sync = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip])
xor_customer_review = OperatorPOWL(operator=Operator.XOR, children=[customer_review, skip])
xor_feedback_analyze = OperatorPOWL(operator=Operator.XOR, children=[feedback_analyze, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_milk_pasteurize, loop_curd_cutting, loop_mold_inoculate, loop_salt_brine, loop_age_monitor, loop_quality_test, loop_packaging_prep, loop_label_design, loop_order_allocation, loop_transport_arrange, loop_retail_sync, loop_customer_review, xor_milk_pasteurize, xor_curd_cutting, xor_mold_inoculate, xor_salt_brine, xor_age_monitor, xor_quality_test, xor_packaging_prep, xor_label_design, xor_order_allocation, xor_transport_arrange, xor_retail_sync, xor_customer_review, xor_feedback_analyze])
root.order.add_edge(loop_milk_pasteurize, xor_milk_pasteurize)
root.order.add_edge(loop_curd_cutting, xor_curd_cutting)
root.order.add_edge(loop_mold_inoculate, xor_mold_inoculate)
root.order.add_edge(loop_salt_brine, xor_salt_brine)
root.order.add_edge(loop_age_monitor, xor_age_monitor)
root.order.add_edge(loop_quality_test, xor_quality_test)
root.order.add_edge(loop_packaging_prep, xor_packaging_prep)
root.order.add_edge(loop_label_design, xor_label_design)
root.order.add_edge(loop_order_allocation, xor_order_allocation)
root.order.add_edge(loop_transport_arrange, xor_transport_arrange)
root.order.add_edge(loop_retail_sync, xor_retail_sync)
root.order.add_edge(loop_customer_review, xor_customer_review)
root.order.add_edge(loop_feedback_analyze, xor_feedback_analyze)

# Print the root POWL model
print(root)