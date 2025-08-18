import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
choice_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
choice_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, silence])
choice_curd_formation = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, silence])
choice_whey_separation = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, silence])
choice_press_cheese = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, silence])
choice_salt_application = OperatorPOWL(operator=Operator.XOR, children=[salt_application, silence])
choice_controlled_aging = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, silence])
choice_sensory_check = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, silence])
choice_batch_packaging = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, silence])
choice_label_printing = OperatorPOWL(operator=Operator.XOR, children=[label_printing, silence])
choice_cold_storage = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, silence])
choice_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, silence])
choice_retail_delivery = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, silence])
choice_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, silence])
choice_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, silence])
choice_provenance_track = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, silence])

# Define the partial order
root = StrictPartialOrder(nodes=[
    choice_milk_sourcing,
    choice_milk_pasteurize,
    choice_curd_formation,
    choice_whey_separation,
    choice_press_cheese,
    choice_salt_application,
    choice_controlled_aging,
    choice_sensory_check,
    choice_batch_packaging,
    choice_label_printing,
    choice_cold_storage,
    choice_logistics_plan,
    choice_retail_delivery,
    choice_feedback_review,
    choice_demand_forecast,
    choice_provenance_track
])
root.order.add_edge(choice_milk_sourcing, choice_milk_pasteurize)
root.order.add_edge(choice_milk_pasteurize, choice_curd_formation)
root.order.add_edge(choice_curd_formation, choice_whey_separation)
root.order.add_edge(choice_whey_separation, choice_press_cheese)
root.order.add_edge(choice_press_cheese, choice_salt_application)
root.order.add_edge(choice_salt_application, choice_controlled_aging)
root.order.add_edge(choice_controlled_aging, choice_sensory_check)
root.order.add_edge(choice_sensory_check, choice_batch_packaging)
root.order.add_edge(choice_batch_packaging, choice_label_printing)
root.order.add_edge(choice_label_printing, choice_cold_storage)
root.order.add_edge(choice_cold_storage, choice_logistics_plan)
root.order.add_edge(choice_logistics_plan, choice_retail_delivery)
root.order.add_edge(choice_retail_delivery, choice_feedback_review)
root.order.add_edge(choice_feedback_review, choice_demand_forecast)
root.order.add_edge(choice_demand_forecast, choice_provenance_track)