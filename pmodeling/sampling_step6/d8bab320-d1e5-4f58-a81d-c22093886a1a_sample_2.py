import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the given activities
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

# Define the partial order
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

# Since there are no dependencies mentioned, we assume all activities are concurrent.
# Therefore, there are no edges in the order.

print(root)