import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the loop for aging and sensory evaluation
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, sensory_audit])

# Define the partial order for packaging and distribution
packaging_and_distribution = StrictPartialOrder(nodes=[packaging_design, label_approval, order_customization, logistics_plan, market_delivery])
packaging_and_distribution.order.add_edge(packaging_design, label_approval)
packaging_and_distribution.order.add_edge(label_approval, order_customization)
packaging_and_distribution.order.add_edge(order_customization, logistics_plan)
packaging_and_distribution.order.add_edge(logistics_plan, market_delivery)

# Build the overall root partial order
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
    regulatory_check,
    packaging_and_distribution,
    customer_feedback
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, aging_loop)
root.order.add_edge(aging_loop, regulatory_check)
root.order.add_edge(regulatory_check, packaging_and_distribution)
root.order.add_edge(packaging_and_distribution, customer_feedback)