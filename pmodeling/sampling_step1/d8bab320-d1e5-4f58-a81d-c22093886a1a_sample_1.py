import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
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

# Define the dependencies
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

# Print the root model
print(root)