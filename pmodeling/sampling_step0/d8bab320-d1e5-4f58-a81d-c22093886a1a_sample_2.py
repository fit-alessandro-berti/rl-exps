import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define POWL model
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])
loop_flavor = OperatorPOWL(operator=Operator.LOOP, children=[flavor_testing, customer_feedback])
loop_recycle = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, regulation_audit])

xor_sourcing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, regulation_audit])
xor_culture = OperatorPOWL(operator=Operator.XOR, children=[culture_selection, market_delivery])
xor_pasturize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, label_approval])
xor_curd = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, order_forecast])
xor_whey = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, market_delivery])
xor_mold = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, market_delivery])
xor_pressing = OperatorPOWL(operator=Operator.XOR, children=[cheese_pressing, market_delivery])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, market_delivery])
xor_approval = OperatorPOWL(operator=Operator.XOR, children=[label_approval, market_delivery])

xor_setup = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, flavor_testing])
xor_control = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, customer_feedback])

xor_recycle = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, market_delivery])

xor_audit = OperatorPOWL(operator=Operator.XOR, children=[regulation_audit, market_delivery])

root = StrictPartialOrder(nodes=[loop_aging, loop_flavor, loop_recycle, xor_sourcing, xor_culture, xor_pasturize, xor_curd, xor_whey, xor_mold, xor_pressing, xor_packaging, xor_approval, xor_setup, xor_control, xor_recycle, xor_audit])
root.order.add_edge(loop_aging, xor_setup)
root.order.add_edge(loop_flavor, xor_control)
root.order.add_edge(loop_recycle, xor_audit)
root.order.add_edge(xor_sourcing, xor_culture)
root.order.add_edge(xor_culture, xor_pasturize)
root.order.add_edge(xor_pasturize, xor_curd)
root.order.add_edge(xor_curd, xor_whey)
root.order.add_edge(xor_whey, xor_mold)
root.order.add_edge(xor_mold, xor_pressing)
root.order.add_edge(xor_pressing, xor_packaging)
root.order.add_edge(xor_packaging, xor_approval)
root.order.add_edge(xor_approval, xor_recycle)
root.order.add_edge(xor_recycle, xor_audit)

return root