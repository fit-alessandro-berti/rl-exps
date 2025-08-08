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

# Define the POWL model
loop_milk_pasteurize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, culture_blending])
loop_curd_cutting = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, mold_inoculate])
loop_whey_drain = OperatorPOWL(operator=Operator.LOOP, children=[whey_drain, press_cheese])
loop_salt_brine = OperatorPOWL(operator=Operator.LOOP, children=[salt_brine, age_monitor])
loop_quality_test = OperatorPOWL(operator=Operator.LOOP, children=[quality_test, packaging_prep])
loop_label_design = OperatorPOWL(operator=Operator.LOOP, children=[label_design, order_allocation])
loop_transport_arrange = OperatorPOWL(operator=Operator.LOOP, children=[transport_arrange, retail_sync])
loop_customer_review = OperatorPOWL(operator=Operator.LOOP, children=[customer_review, feedback_analyze])

root = StrictPartialOrder(nodes=[milk_sourcing, loop_milk_pasteurize, loop_curd_cutting, loop_whey_drain, loop_salt_brine, loop_quality_test, loop_label_design, loop_transport_arrange, loop_customer_review])
root.order.add_edge(milk_sourcing, loop_milk_pasteurize)
root.order.add_edge(loop_milk_pasteurize, loop_curd_cutting)
root.order.add_edge(loop_curd_cutting, loop_whey_drain)
root.order.add_edge(loop_whey_drain, loop_salt_brine)
root.order.add_edge(loop_salt_brine, loop_quality_test)
root.order.add_edge(loop_quality_test, loop_label_design)
root.order.add_edge(loop_label_design, loop_transport_arrange)
root.order.add_edge(loop_transport_arrange, loop_customer_review)