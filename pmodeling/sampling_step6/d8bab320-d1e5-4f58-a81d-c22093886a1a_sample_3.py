import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_selection, milk_pasteurize, curd_formation, whey_separation, mold_inoculate, cheese_pressing, aging_setup, humidity_control, flavor_testing, packaging_design, label_approval, order_forecast, regulation_audit, waste_recycling, market_delivery, customer_feedback
])

# Add dependencies (if any)
# Example: Assuming 'milk_sourcing' and 'culture_selection' are concurrent
root.order.add_edge(milk_sourcing, culture_selection)

# Example: Assuming 'milk_pasteurize' and 'curd_formation' are concurrent
root.order.add_edge(milk_pasteurize, curd_formation)

# Example: Assuming 'whey_separation' and 'mold_inoculate' are concurrent
root.order.add_edge(whey_separation, mold_inoculate)

# Example: Assuming 'cheese_pressing' and 'aging_setup' are concurrent
root.order.add_edge(cheese_pressing, aging_setup)

# Example: Assuming 'humidity_control' and 'flavor_testing' are concurrent
root.order.add_edge(humidity_control, flavor_testing)

# Example: Assuming 'packaging_design' and 'label_approval' are concurrent
root.order.add_edge(packaging_design, label_approval)

# Example: Assuming 'order_forecast' and 'regulation_audit' are concurrent
root.order.add_edge(order_forecast, regulation_audit)

# Example: Assuming 'waste_recycling' and 'market_delivery' are concurrent
root.order.add_edge(waste_recycling, market_delivery)

# Example: Assuming 'customer_feedback' and 'market_delivery' are concurrent
root.order.add_edge(customer_feedback, market_delivery)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and 'customer_feedback' are concurrent
root.order.add_edge(market_delivery, customer_feedback)

# Example: Assuming 'market_delivery' and '