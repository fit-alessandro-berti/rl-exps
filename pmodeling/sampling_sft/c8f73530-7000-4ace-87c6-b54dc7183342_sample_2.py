import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
milk_pasteurize    = Transition(label='Milk Pasteurize')
culture_inoculate  = Transition(label='Culture Inoculate')
coagulation        = Transition(label='Coagulation')
curd_cutting       = Transition(label='Curd Cutting')
whey_drain         = Transition(label='Whey Drain')
pressing           = Transition(label='Pressing')
salting            = Transition(label='Salting')
aging_control      = Transition(label='Aging Control')
sensory_audit      = Transition(label='Sensory Audit')
packaging_design   = Transition(label='Packaging Design')
label_approval     = Transition(label='Label Approval')
order_customization= Transition(label='Order Customization')
logistics_plan     = Transition(label='Logistics Plan')
market_delivery    = Transition(label='Market Delivery')
customer_feedback  = Transition(label='Customer Feedback')
regulatory_check   = Transition(label='Regulatory Check')

# Define the aging loop: control then audit, repeated until exit
aging_body = StrictPartialOrder(nodes=[aging_control, sensory_audit])
# no order edges => these two happen in parallel

# Loop operator: do aging_body, then choose to exit or do aging_body again
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_body, aging_body])

# Build the overall partial order
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
    aging_loop,
    packaging_design,
    label_approval,
    order_customization,
    logistics_plan,
    market_delivery,
    customer_feedback,
    regulatory_check
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing,   quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, aging_loop)

# Body of the aging loop
root.order.add_edge(aging_loop, sensory_audit)

# After aging, do packaging and approval
root.order.add_edge(aging_loop, packaging_design)
root.order.add_edge(packaging_design, label_approval)

# Then order customization, logistics plan, and market delivery
root.order.add_edge(label_approval, order_customization)
root.order.add_edge(order_customization, logistics_plan)
root.order.add_edge(logistics_plan, market_delivery)

# Finally, include customer feedback and regulatory check
root.order.add_edge(market_delivery, customer_feedback)
root.order.add_edge(customer_feedback, regulatory_check)