import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_sourcing = Transition(label='Seed Sourcing')
germination_check = Transition(label='Germination Check')
nutrient_mix = Transition(label='Nutrient Mix')
automated_planting = Transition(label='Automated Planting')
climate_control = Transition(label='Climate Control')
crop_scanning = Transition(label='Crop Scanning')
pest_monitoring = Transition(label='Pest Monitoring')
growth_analysis = Transition(label='Growth Analysis')
robotic_harvest = Transition(label='Robotic Harvest')
quality_sort = Transition(label='Quality Sort')
eco_packaging = Transition(label='Eco Packaging')
blockchain_track = Transition(label='Blockchain Track')
route_planning = Transition(label='Route Planning')
feedback_collect = Transition(label='Feedback Collect')
waste_recycling = Transition(label='Waste Recycling')
data_analytics = Transition(label='Data Analytics')
demand_forecast = Transition(label='Demand Forecast')
maintenance_alert = Transition(label='Maintenance Alert')

# Define exclusive choice operators
supply_chain = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, germination_check])
nutrient_solution = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, automated_planting])
climate_adjustment = OperatorPOWL(operator=Operator.XOR, children=[climate_control, crop_scanning])
pest_management = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, growth_analysis])
harvesting = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_sort])
packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, blockchain_track])
distribution = OperatorPOWL(operator=Operator.XOR, children=[route_planning, feedback_collect])
waste_management = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, data_analytics])
demand_adaptation = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, maintenance_alert])

# Define the partial order
root = StrictPartialOrder(nodes=[
    supply_chain,
    nutrient_solution,
    climate_adjustment,
    pest_management,
    harvesting,
    packaging,
    distribution,
    waste_management,
    demand_adaptation
])

# Define the dependencies
root.order.add_edge(supply_chain, nutrient_solution)
root.order.add_edge(nutrient_solution, climate_adjustment)
root.order.add_edge(climate_adjustment, pest_management)
root.order.add_edge(pest_management, harvesting)
root.order.add_edge(harvesting, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, waste_management)
root.order.add_edge(waste_management, demand_adaptation)
root.order.add_edge(demand_adaptation, pest_management)

# Print the final root POWL model
print(root)