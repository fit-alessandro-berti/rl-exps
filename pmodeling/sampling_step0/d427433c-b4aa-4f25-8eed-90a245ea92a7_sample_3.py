import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_collection = Transition(label='Milk Collection')
quality_testing = Transition(label='Quality Testing')
milk_blending = Transition(label='Milk Blending')
starter_culture = Transition(label='Starter Culture')
fermentation_check = Transition(label='Fermentation Check')
curd_cutting = Transition(label='Curd Cutting')
whey_separation = Transition(label='Whey Separation')
molding_press = Transition(label='Molding Press')
salting_stage = Transition(label='Salting Stage')
aging_control = Transition(label='Aging Control')
packaging_design = Transition(label='Packaging Design')
cold_shipping = Transition(label='Cold Shipping')
compliance_audit = Transition(label='Compliance Audit')
blockchain_log = Transition(label='Blockchain Log')
market_pricing = Transition(label='Market Pricing')
order_fulfillment = Transition(label='Order Fulfillment')
feedback_review = Transition(label='Feedback Review')

# Define the silent transition for skip
skip = SilentTransition()

# Define the loop for aging control
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])

# Define the exclusive choice for packaging design
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])

# Define the loop for milk collection
loop_milk = OperatorPOWL(operator=Operator.LOOP, children=[milk_collection])

# Define the exclusive choice for milk blending
milk_blending_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_blending, skip])

# Define the exclusive choice for fermentation check
fermentation_check_choice = OperatorPOWL(operator=Operator.XOR, children=[fermentation_check, skip])

# Define the exclusive choice for curd cutting
curd_cutting_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])

# Define the exclusive choice for whey separation
whey_separation_choice = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, skip])

# Define the exclusive choice for molding press
molding_press_choice = OperatorPOWL(operator=Operator.XOR, children=[molding_press, skip])

# Define the exclusive choice for salting stage
salting_stage_choice = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, skip])

# Define the exclusive choice for cold shipping
cold_shipping_choice = OperatorPOWL(operator=Operator.XOR, children=[cold_shipping, skip])

# Define the exclusive choice for compliance audit
compliance_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])

# Define the exclusive choice for blockchain log
blockchain_log_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log, skip])

# Define the exclusive choice for market pricing
market_pricing_choice = OperatorPOWL(operator=Operator.XOR, children=[market_pricing, skip])

# Define the exclusive choice for order fulfillment
order_fulfillment_choice = OperatorPOWL(operator=Operator.XOR, children=[order_fulfillment, skip])

# Define the exclusive choice for feedback review
feedback_review_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_milk,
    milk_blending_choice,
    fermentation_check_choice,
    curd_cutting_choice,
    whey_separation_choice,
    molding_press_choice,
    salting_stage_choice,
    aging_control,
    loop_aging,
    packaging_choice,
    cold_shipping_choice,
    compliance_audit_choice,
    blockchain_log_choice,
    market_pricing_choice,
    order_fulfillment_choice,
    feedback_review_choice
])

# Add the dependencies between the nodes
root.order.add_edge(loop_milk, milk_blending_choice)
root.order.add_edge(milk_blending_choice, fermentation_check_choice)
root.order.add_edge(fermentation_check_choice, curd_cutting_choice)
root.order.add_edge(curd_cutting_choice, whey_separation_choice)
root.order.add_edge(whey_separation_choice, molding_press_choice)
root.order.add_edge(molding_press_choice, salting_stage_choice)
root.order.add_edge(salting_stage_choice, aging_control)
root.order.add_edge(aging_control, loop_aging)
root.order.add_edge(loop_aging, packaging_choice)
root.order.add_edge(packaging_choice, cold_shipping_choice)
root.order.add_edge(cold_shipping_choice, compliance_audit_choice)
root.order.add_edge(compliance_audit_choice, blockchain_log_choice)
root.order.add_edge(blockchain_log_choice, market_pricing_choice)
root.order.add_edge(market_pricing_choice, order_fulfillment_choice)
root.order.add_edge(order_fulfillment_choice, feedback_review_choice)

print(root)