import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_sourcing      = Transition(label='Seed Sourcing')
farm_scheduling    = Transition(label='Farm Scheduling')
sensor_monitoring  = Transition(label='Sensor Monitoring')
nutrient_cycling   = Transition(label='Nutrient Cycling')
pest_inspection    = Transition(label='Pest Inspection')
crop_forecasting   = Transition(label='Crop Forecasting')
harvest_timing     = Transition(label='Harvest Timing')
quality_check      = Transition(label='Quality Check')
eco_packaging      = Transition(label='Eco Packaging')
storage_allocation = Transition(label='Storage Allocation')
demand_analysis    = Transition(label='Demand Analysis')
customer_feedback  = Transition(label='Customer Feedback')
order_processing   = Transition(label='Order Processing')
route_planning     = Transition(label='Route Planning')
vehicle_dispatch   = Transition(label='Vehicle Dispatch')
waste_management   = Transition(label='Waste Management')
community_outreach = Transition(label='Community Outreach')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    farm_scheduling,
    sensor_monitoring,
    nutrient_cycling,
    pest_inspection,
    crop_forecasting,
    harvest_timing,
    quality_check,
    eco_packaging,
    storage_allocation,
    demand_analysis,
    customer_feedback,
    order_processing,
    route_planning,
    vehicle_dispatch,
    waste_management,
    community_outreach
])

# Sequence: Seed Sourcing -> Farm Scheduling
root.order.add_edge(seed_sourcing, farm_scheduling)

# Parallel: Nutrient Cycling, Pest Inspection, Crop Forecasting run in parallel
root.order.add_edge(farm_scheduling, nutrient_cycling)
root.order.add_edge(farm_scheduling, pest_inspection)
root.order.add_edge(farm_scheduling, crop_forecasting)

# After nutrient cycling, we can either harvest or inspect pests
harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing, pest_inspection])
root.order.add_edge(nutrient_cycling, harvest_choice)

# Harvest timing leads to quality check and packaging
root.order.add_edge(harvest_choice, quality_check)
root.order.add_edge(harvest_choice, eco_packaging)

# Quality check and packaging both lead to storage allocation
root.order.add_edge(quality_check, storage_allocation)
root.order.add_edge(eco_packaging, storage_allocation)

# Demand analysis triggers order processing
root.order.add_edge(demand_analysis, order_processing)

# Order processing triggers route planning and vehicle dispatch
root.order.add_edge(order_processing, route_planning)
root.order.add_edge(order_processing, vehicle_dispatch)

# After delivery, we can either waste management or community outreach
delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])
root.order.add_edge(route_planning, delivery_choice)
root.order.add_edge(vehicle_dispatch, delivery_choice)

# Waste management and community outreach both finish the process
root.order.add_edge(delivery_choice, waste_management)
root.order.add_edge(delivery_choice, community_outreach)