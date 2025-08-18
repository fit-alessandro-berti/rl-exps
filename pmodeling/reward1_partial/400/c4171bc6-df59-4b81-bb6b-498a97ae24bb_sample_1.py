import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define operators (choices and loops)
# Milk Sourcing -> Quality Testing -> Milk Pasturize
milk_process = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
pasturize_process = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, milk_sourcing])
# Quality Testing -> Curd Formation -> Whey Separation
quality_process = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, curd_formation])
curd_process = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])
# Curd Formation -> Press Cheese -> Salt Application -> Controlled Aging
curd_aging = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, press_cheese])
aging_process = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])
# Salt Application -> Controlled Aging -> Sensory Check
salt_aging_process = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])
sensory_process = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, salt_aging_process])
# Sensory Check -> Batch Packaging -> Label Printing -> Cold Storage
sensory_packaging = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, batch_packaging])
packaging_process = OperatorPOWL(operator=Operator.XOR, children=[label_printing, cold_storage])
# Batch Packaging -> Label Printing -> Cold Storage -> Logistics Plan
batch_logistics = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, label_printing])
logistics_process = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, logistics_plan])
# Cold Storage -> Logistics Plan -> Retail Delivery
cold_delivery = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, logistics_plan])
delivery_process = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, cold_delivery])
# Retail Delivery -> Feedback Review -> Demand Forecast -> Provenance Track
delivery_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, feedback_review])
feedback_process = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, provenance_track])
# Demand Forecast -> Provenance Track
demand_provenance = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, provenance_track])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_process,
    pasturize_process,
    quality_process,
    curd_process,
    curd_aging,
    aging_process,
    sensory_process,
    sensory_packaging,
    packaging_process,
    batch_logistics,
    logistics_process,
    cold_delivery,
    delivery_process,
    delivery_feedback,
    feedback_process,
    demand_provenance
])

# Add edges to the root POWL model
root.order.add_edge(milk_process, pasturize_process)
root.order.add_edge(pasturize_process, quality_process)
root.order.add_edge(quality_process, curd_process)
root.order.add_edge(curd_process, curd_aging)
root.order.add_edge(curd_aging, aging_process)
root.order.add_edge(aging_process, sensory_process)
root.order.add_edge(sensory_process, sensory_packaging)
root.order.add_edge(sensory_packaging, packaging_process)
root.order.add_edge(packaging_process, batch_logistics)
root.order.add_edge(batch_logistics, logistics_process)
root.order.add_edge(logistics_process, cold_delivery)
root.order.add_edge(cold_delivery, delivery_process)
root.order.add_edge(delivery_process, delivery_feedback)
root.order.add_edge(delivery_feedback, feedback_process)
root.order.add_edge(feedback_process, demand_provenance)

print(root)