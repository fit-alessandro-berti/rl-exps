import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for aging control
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, sensory_audit])

# Define the XOR for packaging design and label approval
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define the root model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_inoculate, coagulation, curd_cutting, whey_drain, pressing, salting, loop, xor, order_customization, logistics_plan, market_delivery, customer_feedback, regulatory_check])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, loop)
root.order.add_edge(loop, sensory_audit)
root.order.add_edge(sensory_audit, xor)
root.order.add_edge(xor, packaging_design)
root.order.add_edge(xor, label_approval)
root.order.add_edge(packaging_design, order_customization)
root.order.add_edge(order_customization, logistics_plan)
root.order.add_edge(logistics_plan, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)
root.order.add_edge(customer_feedback, regulatory_check)