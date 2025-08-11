import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])
xor_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
xor_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
xor_inoculate = OperatorPOWL(operator=Operator.XOR, children=[culture_inoculate, skip])
xor_coagulation = OperatorPOWL(operator=Operator.XOR, children=[coagulation, skip])
xor_cutting = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
xor_drain = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, skip])
xor_pressing = OperatorPOWL(operator=Operator.XOR, children=[pressing, skip])
xor_salting = OperatorPOWL(operator=Operator.XOR, children=[salting, skip])
xor_aging_control = OperatorPOWL(operator=Operator.XOR, children=[aging_control, skip])
xor_sensory_audit = OperatorPOWL(operator=Operator.XOR, children=[sensory_audit, skip])
xor_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
xor_label_approval = OperatorPOWL(operator=Operator.XOR, children=[label_approval, skip])
xor_order_customization = OperatorPOWL(operator=Operator.XOR, children=[order_customization, skip])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])
xor_market_delivery = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, skip])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
xor_regulatory_check = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, skip])

# Define the root node
root = StrictPartialOrder(nodes=[
    loop_milk_sourcing,
    xor_quality_testing,
    xor_pasteurize,
    xor_inoculate,
    xor_coagulation,
    xor_cutting,
    xor_drain,
    xor_pressing,
    xor_salting,
    xor_aging_control,
    xor_sensory_audit,
    xor_packaging_design,
    xor_label_approval,
    xor_order_customization,
    xor_logistics_plan,
    xor_market_delivery,
    xor_customer_feedback,
    xor_regulatory_check
])

# Define the dependencies between nodes
root.order.add_edge(loop_milk_sourcing, xor_quality_testing)
root.order.add_edge(xor_quality_testing, xor_pasteurize)
root.order.add_edge(xor_pasteurize, xor_inoculate)
root.order.add_edge(xor_inoculate, xor_coagulation)
root.order.add_edge(xor_coagulation, xor_cutting)
root.order.add_edge(xor_cutting, xor_drain)
root.order.add_edge(xor_drain, xor_pressing)
root.order.add_edge(xor_pressing, xor_salting)
root.order.add_edge(xor_salting, xor_aging_control)
root.order.add_edge(xor_aging_control, xor_sensory_audit)
root.order.add_edge(xor_sensory_audit, xor_packaging_design)
root.order.add_edge(xor_packaging_design, xor_label_approval)
root.order.add_edge(xor_label_approval, xor_order_customization)
root.order.add_edge(xor_order_customization, xor_logistics_plan)
root.order.add_edge(xor_logistics_plan, xor_market_delivery)
root.order.add_edge(xor_market_delivery, xor_customer_feedback)
root.order.add_edge(xor_customer_feedback, xor_regulatory_check)

# Print the root node
print(root)