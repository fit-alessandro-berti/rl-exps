import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop nodes for the aging and regulatory check processes
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, sensory_audit])
regulatory_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check])

# Define the exclusive choice for the packaging and logistics processes
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
logistics_choice = OperatorPOWL(operator=Operator.XOR, children=[order_customization, logistics_plan])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_inoculate, coagulation, curd_cutting, whey_drain, pressing, salting, aging_loop, sensory_audit, packaging_choice, label_approval, order_customization, logistics_choice, market_delivery, customer_feedback, regulatory_loop])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, aging_loop)
root.order.add_edge(aging_loop, sensory_audit)
root.order.add_edge(sensory_audit, packaging_choice)
root.order.add_edge(packaging_choice, label_approval)
root.order.add_edge(label_approval, order_customization)
root.order.add_edge(order_customization, logistics_choice)
root.order.add_edge(logistics_choice, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)
root.order.add_edge(customer_feedback, regulatory_loop)
root.order.add_edge(regulatory_loop, regulatory_check)