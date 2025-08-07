import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing    = Transition(label='Milk Sourcing')
culture_selection= Transition(label='Culture Selection')
milk_pasteurize  = Transition(label='Milk Pasteurize')
curd_formation   = Transition(label='Curd Formation')
whey_separation  = Transition(label='Whey Separation')
mold_inoculate   = Transition(label='Mold Inoculate')
cheese_pressing  = Transition(label='Cheese Pressing')
aging_setup      = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing   = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval   = Transition(label='Label Approval')
order_forecast   = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling  = Transition(label='Waste Recycling')
market_delivery  = Transition(label='Market Delivery')
customer_feedback= Transition(label='Customer Feedback')

# Build the aging sub‐process as a partial order
aging_po = StrictPartialOrder(nodes=[
    aging_setup, humidity_control, flavor_testing
])
# Concurrency between humidity control and flavor testing
aging_po.order.add_edge(aging_setup, humidity_control)
aging_po.order.add_edge(aging_setup, flavor_testing)

# Loop for continuous quality assurance & sustainability tracking
# Each iteration: Aging Setup -> Humidity Control -> Flavor Testing
# Then optionally do Waste Recycling before repeating
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_po, waste_recycling])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_pasteurize,
    curd_formation,
    whey_separation,
    mold_inoculate,
    cheese_pressing,
    aging_loop,
    packaging_design,
    label_approval,
    order_forecast,
    regulation_audit,
    market_delivery,
    customer_feedback
])

# Sequence of activities without loop
seq = [
    milk_sourcing,
    culture_selection,
    milk_pasteurize,
    curd_formation,
    whey_separation,
    mold_inoculate,
    cheese_pressing
]
for prev, next in zip(seq, seq[1:]):
    root.order.add_edge(prev, next)

# Sequentially add the aging loop after cheese pressing
root.order.add_edge(cheese_pressing, aging_loop)

# Parallelize packaging, labeling, forecasting, and auditing
for child in [packaging_design, label_approval, order_forecast, regulation_audit]:
    root.order.add_edge(aging_loop, child)

# Sequentially add market delivery and customer feedback
root.order.add_edge(aging_loop, market_delivery)
root.order.add_edge(market_delivery, customer_feedback)