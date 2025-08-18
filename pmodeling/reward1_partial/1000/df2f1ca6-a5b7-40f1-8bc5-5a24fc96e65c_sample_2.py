import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Artisan Vetting')
review = Transition(label='Sample Review')
finalize = Transition(label='Design Finalize')
scheduling = Transition(label='Batch Scheduling')
check = Transition(label='Quality Check')
packaging = Transition(label='Custom Packaging')
forecast = Transition(label='Demand Forecast')
adjust = Transition(label='Price Adjust')
inventory = Transition(label='Inventory Sync')
processing = Transition(label='Order Processing')
coordination = Transition(label='Craft Coordination')
shipment = Transition(label='Shipment Plan')
monitor = Transition(label='Market Analysis')
feedback = Transition(label='Feedback Loop')
trend = Transition(label='Trend Monitor')

# Define the partial order
root = StrictPartialOrder(nodes=[sourcing, vetting, review, finalize, scheduling, check, packaging, forecast, adjust, inventory, processing, coordination, shipment, monitor, feedback, trend])

# Define the dependencies
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, review)
root.order.add_edge(review, finalize)
root.order.add_edge(finalize, scheduling)
root.order.add_edge(scheduling, check)
root.order.add_edge(check, packaging)
root.order.add_edge(packaging, forecast)
root.order.add_edge(forecast, adjust)
root.order.add_edge(adjust, inventory)
root.order.add_edge(inventory, processing)
root.order.add_edge(processing, coordination)
root.order.add_edge(coordination, shipment)
root.order.add_edge(shipment, monitor)
root.order.add_edge(monitor, feedback)
root.order.add_edge(feedback, trend)

# Print the final result
print(root)