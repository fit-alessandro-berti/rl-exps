import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_inoculate = Transition(label='Culture Inoculate')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
aging_control = Transition(label='Aging Control')
sensory_audit = Transition(label='Sensory Audit')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_customization = Transition(label='Order Customization')
logistics_plan = Transition(label='Logistics Plan')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')
regulatory_check = Transition(label='Regulatory Check')

# Define silent transitions
skip = SilentTransition()

# Define partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, regulatory_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[order_customization, logistics_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, customer_feedback])
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_inoculate, coagulation, curd_cutting, whey_drain, pressing, salting, loop, xor1, xor2, xor3])

# Define partial order dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)
root.order.add_edge(customer_feedback, regulatory_check)

# Print the final POWL model
print(root)