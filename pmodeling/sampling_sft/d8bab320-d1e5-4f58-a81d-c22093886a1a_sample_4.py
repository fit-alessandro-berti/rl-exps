import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label='Milk Sourcing')
culture_select  = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation  = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate  = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup     = Transition(label='Aging Setup')
humidity_ctrl   = Transition(label='Humidity Control')
flavor_test     = Transition(label='Flavor Testing')
pack_design     = Transition(label='Packaging Design')
label_approval  = Transition(label='Label Approval')
order_forecast  = Transition(label='Order Forecast')
reg_audit       = Transition(label='Regulation Audit')
waste_recycle   = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_fb     = Transition(label='Customer Feedback')

# Loop for seasonal demand forecasting & order fulfillment
demand_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[order_forecast, market_delivery]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_select, milk_pasteurize, curd_formation, whey_separation,
    mold_inoculate, cheese_pressing, aging_setup, humidity_ctrl, flavor_test,
    pack_design, label_approval, demand_loop, waste_recycle, customer_fb
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing,     culture_select)
root.order.add_edge(culture_select,    milk_pasteurize)
root.order.add_edge(milk_pasteurize,   curd_formation)
root.order.add_edge(curd_formation,    whey_separation)
root.order.add_edge(whey_separation,   mold_inoculate)
root.order.add_edge(mold_inoculate,    cheese_pressing)
root.order.add_edge(cheese_pressing,   aging_setup)
root.order.add_edge(aging_setup,       humidity_ctrl)
root.order.add_edge(humidity_ctrl,     flavor_test)
root.order.add_edge(flavor_test,       pack_design)
root.order.add_edge(pack_design,       label_approval)
root.order.add_edge(label_approval,    demand_loop)
root.order.add_edge(demand_loop,       waste_recycle)
root.order.add_edge(demand_loop,       customer_fb)