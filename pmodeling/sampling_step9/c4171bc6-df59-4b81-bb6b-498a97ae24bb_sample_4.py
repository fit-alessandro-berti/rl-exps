import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the loop node for controlled aging
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])

# Define the exclusive choice for sensory check and feedback review
xor_sensory_review = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, feedback_review])

# Define the exclusive choice for packaging and logistics plan
xor_packaging_logistics = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, logistics_plan])

# Define the exclusive choice for retail delivery and demand forecast
xor_retail_demand = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, demand_forecast])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance_demand = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the exclusive choice for feedback review and demand forecast
xor_feedback_demand = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance_demand])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor_provenance])

# Define the exclusive choice for provenance track and demand forecast
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_track, demand_forecast])

# Define the loop node for demand forecast
loop_demand = OperatorPO