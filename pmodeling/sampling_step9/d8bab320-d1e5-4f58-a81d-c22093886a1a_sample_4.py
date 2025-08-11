import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasturize, curd_formation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[whey_separation, mold_inoculate])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[cheese_pressing, aging_setup])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, flavor_testing])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_approval])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[order_forecast, regulation_audit])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, market_delivery])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

# Define the root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop9)

print(root)