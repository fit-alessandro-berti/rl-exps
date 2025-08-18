from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
milk_inoculate = Transition(label='Milk Inoculate')
curd_form = Transition(label='Curd Formation')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
temp_monitor = Transition(label='Temperature Monitor')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
order_fulfill = Transition(label='Order Fulfill')
retail_deliver = Transition(label='Retail Deliver')
feedback_collect = Transition(label='Feedback Collect')

# Define the loop for aging process
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    aging_setup, humidity_control, temp_monitor, quality_test, packaging, order_fulfill
])

# Define the exclusive choice for milk sourcing
milk_source_choice = OperatorPOWL(operator=Operator.XOR, children=[
    milk_sourcing, feedback_collect
])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    milk_source_choice, aging_loop
])

# Add dependencies between nodes
root.order.add_edge(milk_source_choice, aging_loop)

print(root)