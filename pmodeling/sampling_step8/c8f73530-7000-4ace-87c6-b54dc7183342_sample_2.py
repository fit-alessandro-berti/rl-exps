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

# Define partial order and dependencies
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    culture_inoculate,
    coagulation,
    curd_cutting,
    whey_drain,
    pressing,
    salting,
    aging_control,
    sensory_audit,
    packaging_design,
    label_approval,
    order_customization,
    logistics_plan,
    market_delivery,
    customer_feedback,
    regulatory_check
])

# Define dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, aging_control)
root.order.add_edge(aging_control, sensory_audit)
root.order.add_edge(sensory_audit, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_customization)
root.order.add_edge(order_customization, logistics_plan)
root.order.add_edge(logistics_plan, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)
root.order.add_edge(customer_feedback, regulatory_check)

# Print the root model
print(root)