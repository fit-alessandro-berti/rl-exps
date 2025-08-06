import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix = Transition(label='Nutrient Mix')
water_delivery = Transition(label='Water Delivery')
light_adjustment = Transition(label='Light Adjustment')
climate_control = Transition(label='Climate Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
harvest_planning = Transition(label='Harvest Planning')
crop_harvest = Transition(label='Crop Harvest')
waste_sorting = Transition(label='Waste Sorting')
biomass_process = Transition(label='Biomass Process')
energy_recycling = Transition(label='Energy Recycling')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

skip = SilentTransition()

# Process starts with seed selection and germination
start = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, germination_start])

# Germination starts with seedling transplant
germination = OperatorPOWL(operator=Operator.XOR, children=[seedling_transplant, skip])

# Seedling transplant leads to nutrient mix and water delivery
transplant = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_delivery])

# Nutrient mix and water delivery lead to light adjustment and climate control
mix = OperatorPOWL(operator=Operator.XOR, children=[light_adjustment, climate_control])

# Light adjustment and climate control lead to sensor monitoring
adjustment = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitoring, skip])

# Sensor monitoring leads to health check
monitoring = OperatorPOWL(operator=Operator.XOR, children=[health_check, skip])

# Health check leads to pest control and harvest planning
check = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_planning])

# Pest control and harvest planning lead to crop harvest
control = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, skip])

# Crop harvest leads to waste sorting
harvest = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, skip])

# Waste sorting leads to biomass process
sorting = OperatorPOWL(operator=Operator.XOR, children=[biomass_process, skip])

# Biomass process leads to energy recycling
process = OperatorPOWL(operator=Operator.XOR, children=[energy_recycling, skip])

# Energy recycling leads to data analysis
recycling = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])

# Data analysis leads to yield forecast
analysis = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])

# Yield forecast leads back to seed selection and germination
forecast = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, germination_start])

# Connect the processes
root = StrictPartialOrder(nodes=[start, germination, transplant, mix, adjustment, monitoring, check, control, harvest, sorting, process, recycling, analysis, forecast])
root.order.add_edge(start, germination)
root.order.add_edge(germination, transplant)
root.order.add_edge(transplant, mix)
root.order.add_edge(mix, adjustment)
root.order.add_edge(adjustment, monitoring)
root.order.add_edge(monitoring, check)
root.order.add_edge(check, control)
root.order.add_edge(control, harvest)
root.order.add_edge(harvest, sorting)
root.order.add_edge(sorting, process)
root.order.add_edge(process, recycling)
root.order.add_edge(recycling, analysis)
root.order.add_edge(analysis, forecast)
root.order.add_edge(forecast, start)

print(root)