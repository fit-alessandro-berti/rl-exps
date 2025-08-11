import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Press_Cheese = Transition(label='Press Cheese')
Salt_Application = Transition(label='Salt Application')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Check = Transition(label='Sensory Check')
Batch_Packaging = Transition(label='Batch Packaging')
Label_Printing = Transition(label='Label Printing')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Feedback_Review = Transition(label='Feedback Review')
Demand_Forecast = Transition(label='Demand Forecast')
Provenance_Track = Transition(label='Provenance Track')

skip = SilentTransition()

# Milk Sourcing -> Quality Testing -> Milk Pasteurize -> Curd Formation -> Whey Separation -> Press Cheese -> Salt Application -> Controlled Aging
milk_sourcing_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[Milk_Sourcing, Quality_Testing])
milk_pasteurize_curd_formation = OperatorPOWL(operator=Operator.XOR, children=[Milk_Pasteurize, Curd_Formation])
whey_separation_press_cheese = OperatorPOWL(operator=Operator.XOR, children=[Whey_Separation, Press_Cheese])
salt_application_controlled_aging = OperatorPOWL(operator=Operator.XOR, children=[Salt_Application, Controlled_Aging])

# Controlled Aging -> Sensory Check -> Batch Packaging -> Label Printing -> Cold Storage -> Logistics Plan
controlled_aging_sensory_check = OperatorPOWL(operator=Operator.XOR, children=[Controlled_Aging, Sensory_Check])
batch_packaging_label_printing = OperatorPOWL(operator=Operator.XOR, children=[Batch_Packaging, Label_Printing])
cold_storage_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[Cold_Storage, Logistics_Plan])

# Retail Delivery -> Feedback Review -> Demand Forecast -> Provenance Track
retail_delivery_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[Retail_Delivery, Feedback_Review])
demand_forecast_provenance_track = OperatorPOWL(operator=Operator.XOR, children=[Demand_Forecast, Provenance_Track])

# Create the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing_quality_testing, milk_pasteurize_curd_formation, whey_separation_press_cheese, salt_application_controlled_aging,
                                 controlled_aging_sensory_check, batch_packaging_label_printing, cold_storage_logistics_plan,
                                 retail_delivery_feedback_review, demand_forecast_provenance_track])
root.order.add_edge(milk_sourcing_quality_testing, milk_pasteurize_curd_formation)
root.order.add_edge(milk_pasteurize_curd_formation, whey_separation_press_cheese)
root.order.add_edge(whey_separation_press_cheese, salt_application_controlled_aging)
root.order.add_edge(salt_application_controlled_aging, controlled_aging_sensory_check)
root.order.add_edge(controlled_aging_sensory_check, batch_packaging_label_printing)
root.order.add_edge(batch_packaging_label_printing, cold_storage_logistics_plan)
root.order.add_edge(cold_storage_logistics_plan, retail_delivery_feedback_review)
root.order.add_edge(retail_delivery_feedback_review, demand_forecast_provenance_track)