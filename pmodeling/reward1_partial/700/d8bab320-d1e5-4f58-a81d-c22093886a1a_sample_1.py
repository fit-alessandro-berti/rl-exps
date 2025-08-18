import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
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

# Define the partial order structure
root = StrictPartialOrder()

# Add activities to the root
root.nodes.append(milk_sourcing)
root.nodes.append(culture_selection)
root.nodes.append(milk_pasturize)
root.nodes.append(curd_formation)
root.nodes.append(whey_separation)
root.nodes.append(mold_inoculate)
root.nodes.append(cheese_pressing)
root.nodes.append(aging_setup)
root.nodes.append(humidity_control)
root.nodes.append(flavor_testing)
root.nodes.append(packaging_design)
root.nodes.append(label_approval)
root.nodes.append(order_forecast)
root.nodes.append(regulation_audit)
root.nodes.append(waste_recycling)
root.nodes.append(market_delivery)
root.nodes.append(customer_feedback)

# Define dependencies between activities
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, mold_inoculate)
root.order.add_edge(mold_inoculate, cheese_pressing)
root.order.add_edge(cheese_pressing, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, flavor_testing)
root.order.add_edge(flavor_testing, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_forecast)
root.order.add_edge(order_forecast, regulation_audit)
root.order.add_edge(regulation_audit, waste_recycling)
root.order.add_edge(waste_recycling, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)

print(root)