import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing   = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep    = Transition(label='Starter Prep')
curd_cutting    = Transition(label='Curd Cutting')
whey_draining   = Transition(label='Whey Draining')
molding_press   = Transition(label='Molding Press')
fermentation    = Transition(label='Fermentation Control')
aging_setup     = Transition(label='Aging Setup')
humidity_check  = Transition(label='Humidity Check')
packaging       = Transition(label='Packaging Design')
label_approval  = Transition(label='Label Approval')
inventory       = Transition(label='Inventory Audit')
order_sched     = Transition(label='Order Scheduling')
delivery        = Transition(label='Market Delivery')
feedback        = Transition(label='Feedback Review')
compliance      = Transition(label='Compliance Check')
marketing       = Transition(label='Marketing Sync')

# Loop for aging and humidity checks: do Aging Setup, then repeat Humidity Check until exit
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_check])

# Loop for marketing synchronization: do Marketing Sync, then repeat Marketing Sync until exit
marketing_loop = OperatorPOWL(operator=Operator.LOOP, children=[marketing, marketing])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_prep,
    curd_cutting,
    whey_draining,
    molding_press,
    fermentation,
    aging_loop,
    packaging,
    label_approval,
    inventory,
    order_sched,
    delivery,
    feedback,
    compliance,
    marketing_loop
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_press)
root.order.add_edge(molding_press, fermentation)
root.order.add_edge(fermentation, aging_loop)
root.order.add_edge(aging_loop, packaging)
root.order.add_edge(packaging, label_approval)
root.order.add_edge(label_approval, inventory)
root.order.add_edge(inventory, order_sched)
root.order.add_edge(order_sched, delivery)
root.order.add_edge(delivery, feedback)
root.order.add_edge(feedback, compliance)
root.order.add_edge(compliance, marketing_loop)
root.order.add_edge(marketing_loop, marketing_loop)  # repeat Marketing Sync until exit

# The final marketing loop will have no exit edge, so it will repeat indefinitely