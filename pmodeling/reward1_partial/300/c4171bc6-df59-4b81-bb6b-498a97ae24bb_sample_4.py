from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
pasteurize = Transition(label='Milk Pasteurize')
curdle = Transition(label='Curd Formation')
separate_whey = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
aged = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
package = Transition(label='Batch Packaging')
label_print = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
forecast = Transition(label='Demand Forecast')
provenance = Transition(label='Provenance Track')

# Define the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    pasteurize,
    curdle,
    separate_whey,
    press_cheese,
    salt_application,
    aged,
    sensory_check,
    package,
    label_print,
    cold_storage,
    logistics_plan,
    delivery,
    feedback_review,
    forecast,
    provenance
])

# Define the order
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, pasteurize)
root.order.add_edge(pasteurize, curdle)
root.order.add_edge(curdle, separate_whey)
root.order.add_edge(separate_whey, press_cheese)
root.order.add_edge(press_cheese, salt_application)
root.order.add_edge(salt_application, aged)
root.order.add_edge(aged, sensory_check)
root.order.add_edge(sensory_check, package)
root.order.add_edge(package, label_print)
root.order.add_edge(label_print, cold_storage)
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, delivery)
root.order.add_edge(delivery, feedback_review)
root.order.add_edge(feedback_review, forecast)
root.order.add_edge(forecast, provenance)

print(root)