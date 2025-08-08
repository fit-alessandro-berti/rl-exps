import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')
skip = SilentTransition()

# Define the process tree
milk_process = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
pasteurize_process = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
curd_process = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip])
whey_process = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, skip])
press_process = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, skip])
salt_process = OperatorPOWL(operator=Operator.XOR, children=[salt_application, skip])
aging_process = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, skip])
sensory_process = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, skip])
packaging_process = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, skip])
label_printing_process = OperatorPOWL(operator=Operator.XOR, children=[label_printing, skip])
storage_process = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, skip])
logistics_process = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])
delivery_process = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, skip])
feedback_process = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
forecast_process = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])
provenance_process = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    milk_process,
    pasteurize_process,
    curd_process,
    whey_process,
    press_process,
    salt_process,
    aging_process,
    sensory_process,
    packaging_process,
    label_printing_process,
    storage_process,
    logistics_process,
    delivery_process,
    feedback_process,
    forecast_process,
    provenance_process
])

# Define the dependencies
root.order.add_edge(milk_process, pasteurize_process)
root.order.add_edge(pasteurize_process, curd_process)
root.order.add_edge(curd_process, whey_process)
root.order.add_edge(whey_process, press_process)
root.order.add_edge(press_process, salt_process)
root.order.add_edge(salt_process, aging_process)
root.order.add_edge(aging_process, sensory_process)
root.order.add_edge(sensory_process, packaging_process)
root.order.add_edge(packaging_process, label_printing_process)
root.order.add_edge(label_printing_process, storage_process)
root.order.add_edge(storage_process, logistics_process)
root.order.add_edge(logistics_process, delivery_process)
root.order.add_edge(delivery_process, feedback_process)
root.order.add_edge(feedback_process, forecast_process)
root.order.add_edge(forecast_process, provenance_process)

print(root)