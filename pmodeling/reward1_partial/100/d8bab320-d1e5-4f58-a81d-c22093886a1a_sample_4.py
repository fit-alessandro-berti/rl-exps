from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the artisan cheese production process
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_forecast = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the workflow steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection, milk_pasteurize, curd_formation, whey_separation, mold_inoculate, cheese_pressing, aging_setup, humidity_control, flavor_testing])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[order_forecast, regulation_audit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, market_delivery])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)

print(root)