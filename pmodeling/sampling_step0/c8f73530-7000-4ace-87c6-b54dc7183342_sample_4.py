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

# Define the loop for aging control
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, sensory_audit])

# Define the XOR for packaging design and label approval
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define the XOR for logistics plan and market delivery
xor2 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, market_delivery])

# Define the XOR for order customization and customer feedback
xor3 = OperatorPOWL(operator=Operator.XOR, children=[order_customization, customer_feedback])

# Define the XOR for regulatory check and customer feedback
xor4 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, customer_feedback])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_inoculate, coagulation, curd_cutting, whey_drain, pressing, salting, loop, xor, xor2, xor3, xor4])
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
root.order.add_edge(sensory_audit, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, regulatory_check)