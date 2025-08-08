import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions and loops
quality_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, milk_pasturize])
curd_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_formation, whey_separation, press_cheese, salt_application, controlled_aging, sensory_check])
batch_production = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, label_printing])
storage_distribution = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, logistics_plan])
delivery_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, feedback_review])
provenance_check = OperatorPOWL(operator=Operator.XOR, children=[provenance_track])
demand_response = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, quality_control_loop])

# Define the root process
root = StrictPartialOrder(nodes=[quality_control_loop, curd_aging_loop, batch_production, storage_distribution, delivery_feedback, provenance_check, demand_response])
root.order.add_edge(quality_control_loop, curd_aging_loop)
root.order.add_edge(curd_aging_loop, batch_production)
root.order.add_edge(batch_production, storage_distribution)
root.order.add_edge(storage_distribution, delivery_feedback)
root.order.add_edge(delivery_feedback, provenance_check)
root.order.add_edge(provenance_check, demand_response)