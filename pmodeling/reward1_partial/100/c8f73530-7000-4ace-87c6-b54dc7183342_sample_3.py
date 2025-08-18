import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, milk_sourcing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, culture_inoculate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[coagulation, curd_cutting])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, pressing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[salting, aging_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[sensory_audit, packaging_design])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[label_approval, order_customization])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, market_delivery])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, regulatory_check])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)