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

# Define exclusive choice for Quality Testing
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])

# Define loop for Milk Sourcing
loop_milk = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, xor_quality])

# Define loop for Milk Pasteurize
loop_milk_past = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, xor_quality])

# Define loop for Culture Inoculate
loop_culture = OperatorPOWL(operator=Operator.LOOP, children=[culture_inoculate, xor_quality])

# Define loop for Coagulation
loop_coag = OperatorPOWL(operator=Operator.LOOP, children=[coagulation, xor_quality])

# Define loop for Curd Cutting
loop_curd = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, xor_quality])

# Define loop for Whey Drain
loop_whey = OperatorPOWL(operator=Operator.LOOP, children=[whey_drain, xor_quality])

# Define loop for Pressing
loop_press = OperatorPOWL(operator=Operator.LOOP, children=[pressing, xor_quality])

# Define loop for Salting
loop_salt = OperatorPOWL(operator=Operator.LOOP, children=[salting, xor_quality])

# Define loop for Aging Control
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, xor_quality])

# Define loop for Sensory Audit
loop_sensory = OperatorPOWL(operator=Operator.LOOP, children=[sensory_audit, xor_quality])

# Define exclusive choice for Packaging Design
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define loop for Packaging Design
loop_packaging = OperatorPOWL(operator=Operator.LOOP, children=[xor_packaging, xor_quality])

# Define exclusive choice for Order Customization
xor_order = OperatorPOWL(operator=Operator.XOR, children=[order_customization, logistics_plan])

# Define loop for Order Customization
loop_order = OperatorPOWL(operator=Operator.LOOP, children=[xor_order, xor_quality])

# Define loop for Logistics Plan
loop_logistics = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, xor_quality])

# Define loop for Market Delivery
loop_market = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery, xor_quality])

# Define loop for Customer Feedback
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, xor_quality])

# Define loop for Regulatory Check
loop_regulatory = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, xor_quality])

# Define root Partial Order
root = StrictPartialOrder(nodes=[
    loop_milk,
    loop_milk_past,
    loop_culture,
    loop_coag,
    loop_curd,
    loop_whey,
    loop_press,
    loop_salt,
    loop_aging,
    loop_sensory,
    loop_packaging,
    loop_order,
    loop_logistics,
    loop_market,
    loop_feedback,
    loop_regulatory
])

# Add edges between nodes
root.order.add_edge(loop_milk, loop_milk_past)
root.order.add_edge(loop_milk_past, loop_culture)
root.order.add_edge(loop_culture, loop_coag)
root.order.add_edge(loop_coag, loop_curd)
root.order.add_edge(loop_curd, loop_whey)
root.order.add_edge(loop_whey, loop_press)
root.order.add_edge(loop_press, loop_salt)
root.order.add_edge(loop_salt, loop_aging)
root.order.add_edge(loop_aging, loop_sensory)
root.order.add_edge(loop_sensory, loop_packaging)
root.order.add_edge(loop_packaging, loop_order)
root.order.add_edge(loop_order, loop_logistics)
root.order.add_edge(loop_logistics, loop_market)
root.order.add_edge(loop_market, loop_feedback)
root.order.add_edge(loop_feedback, loop_regulatory)

# Print the root POWL model
print(root)