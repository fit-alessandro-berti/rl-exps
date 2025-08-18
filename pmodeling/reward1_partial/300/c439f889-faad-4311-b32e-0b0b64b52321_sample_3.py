from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_sourcing = Transition(label='Seed Sourcing')
farm_scheduling = Transition(label='Farm Scheduling')
sensor_monitoring = Transition(label='Sensor Monitoring')
nutrient_cycling = Transition(label='Nutrient Cycling')
crop_forecasting = Transition(label='Crop Forecasting')
pest_inspection = Transition(label='Pest Inspection')
harvest_timing = Transition(label='Harvest Timing')
quality_check = Transition(label='Quality Check')
eco_packaging = Transition(label='Eco Packaging')
storage_allocation = Transition(label='Storage Allocation')
order_processing = Transition(label='Order Processing')
route_planning = Transition(label='Route Planning')
vehicle_dispatch = Transition(label='Vehicle Dispatch')
customer_feedback = Transition(label='Customer Feedback')
demand_analysis = Transition(label='Demand Analysis')
waste_management = Transition(label='Waste Management')
community_outreach = Transition(label='Community Outreach')

# Define the POWL model
loop_seed_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing])
xor_farm_scheduling = OperatorPOWL(operator=Operator.XOR, children=[farm_scheduling])
loop_sensor_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring])
xor_nutrient_cycling = OperatorPOWL(operator=Operator.XOR, children=[nutrient_cycling])
xor_crop_forecasting = OperatorPOWL(operator=Operator.XOR, children=[crop_forecasting])
xor_pest_inspection = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection])
xor_harvest_timing = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing])
xor_quality_check = OperatorPOWL(operator=Operator.XOR, children=[quality_check])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging])
xor_storage_allocation = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation])
xor_order_processing = OperatorPOWL(operator=Operator.XOR, children=[order_processing])
xor_route_planning = OperatorPOWL(operator=Operator.XOR, children=[route_planning])
xor_vehicle_dispatch = OperatorPOWL(operator=Operator.XOR, children=[vehicle_dispatch])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback])
xor_demand_analysis = OperatorPOWL(operator=Operator.XOR, children=[demand_analysis])
xor_waste_management = OperatorPOWL(operator=Operator.XOR, children=[waste_management])
xor_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[community_outreach])

root = StrictPartialOrder(nodes=[
    loop_seed_sourcing, xor_farm_scheduling, loop_sensor_monitoring, xor_nutrient_cycling,
    xor_crop_forecasting, xor_pest_inspection, xor_harvest_timing, xor_quality_check,
    xor_eco_packaging, xor_storage_allocation, xor_order_processing, xor_route_planning,
    xor_vehicle_dispatch, xor_customer_feedback, xor_demand_analysis, xor_waste_management,
    xor_community_outreach
])
root.order.add_edge(loop_seed_sourcing, xor_farm_scheduling)
root.order.add_edge(loop_sensor_monitoring, xor_nutrient_cycling)
root.order.add_edge(xor_nutrient_cycling, xor_crop_forecasting)
root.order.add_edge(xor_crop_forecasting, xor_pest_inspection)
root.order.add_edge(xor_pest_inspection, xor_harvest_timing)
root.order.add_edge(xor_harvest_timing, xor_quality_check)
root.order.add_edge(xor_quality_check, xor_eco_packaging)
root.order.add_edge(xor_eco_packaging, xor_storage_allocation)
root.order.add_edge(xor_storage_allocation, xor_order_processing)
root.order.add_edge(xor_order_processing, xor_route_planning)
root.order.add_edge(xor_route_planning, xor_vehicle_dispatch)
root.order.add_edge(xor_vehicle_dispatch, xor_customer_feedback)
root.order.add_edge(xor_customer_feedback, xor_demand_analysis)
root.order.add_edge(xor_demand_analysis, xor_waste_management)
root.order.add_edge(xor_waste_management, xor_community_outreach)

print(root)