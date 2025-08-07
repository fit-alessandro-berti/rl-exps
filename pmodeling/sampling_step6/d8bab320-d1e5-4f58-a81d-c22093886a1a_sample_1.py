import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
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

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_pasteurize,
    curd_formation,
    whey_separation,
    mold_inoculate,
    cheese_pressing,
    aging_setup,
    humidity_control,
    flavor_testing,
    packaging_design,
    label_approval,
    order_forecast,
    regulation_audit,
    waste_recycling,
    market_delivery,
    customer_feedback
])

# Define dependencies between activities (POWL model)
# For example, let's assume the following dependencies:
# - Milk Sourcing must occur before Culture Selection
# - Culture Selection must occur before Milk Pasteurize
# - Milk Pasteurize must occur before Curd Formation
# - Curd Formation must occur before Whey Separation
# - Whey Separation must occur before Mold Inoculate
# - Mold Inoculate must occur before Cheese Pressing
# - Cheese Pressing must occur before Aging Setup
# - Aging Setup must occur before Humidity Control
# - Humidity Control must occur before Flavor Testing
# - Flavor Testing must occur before Packaging Design
# - Packaging Design must occur before Label Approval
# - Label Approval must occur before Order Forecast
# - Order Forecast must occur before Regulation Audit
# - Regulation Audit must occur before Waste Recycling
# - Waste Recycling must occur before Market Delivery
# - Market Delivery must occur before Customer Feedback

# Add the dependencies to the partial order
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
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

# The final result is stored in the variable 'root'