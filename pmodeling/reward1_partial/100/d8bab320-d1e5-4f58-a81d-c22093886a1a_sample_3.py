import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, market_delivery])

# Define XORs
sensory_analysis_xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_testing, customer_feedback])

# Define root
root = StrictPartialOrder(nodes=[milk_sourcing, culture_selection, milk_pasteurize, curd_formation, whey_separation, mold_inoculate, cheese_pressing, aging_loop, waste_recycling_loop, packaging_design, label_approval, order_forecast, regulation_audit, sensory_analysis_xor, market_delivery])
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, mold_inoculate)
root.order.add_edge(mold_inoculate, cheese_pressing)
root.order.add_edge(cheese_pressing, aging_loop)
root.order.add_edge(aging_loop, waste_recycling_loop)
root.order.add_edge(waste_recycling_loop, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_forecast)
root.order.add_edge(order_forecast, regulation_audit)
root.order.add_edge(regulation_audit, sensory_analysis_xor)
root.order.add_edge(sensory_analysis_xor, market_delivery)

print(root)