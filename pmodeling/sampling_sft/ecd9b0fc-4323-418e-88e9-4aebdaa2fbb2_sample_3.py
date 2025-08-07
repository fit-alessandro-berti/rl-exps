import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
hydro_install   = Transition(label='Hydroponic Install')
light_setup     = Transition(label='Lighting Setup')
climate_ctrl    = Transition(label='Climate Control')
seed_sel        = Transition(label='Seed Selection')
nutrient_mix    = Transition(label='Nutrient Mix')
water_recycle   = Transition(label='Water Recycling')
sensor_deploy   = Transition(label='Sensor Deploy')
pest_control    = Transition(label='Pest Control')
growth_monitor  = Transition(label='Growth Monitor')
harvest_plan    = Transition(label='Harvest Plan')
packaging_prep  = Transition(label='Packaging Prep')
delivery_route  = Transition(label='Delivery Route')
data_analysis   = Transition(label='Data Analysis')
yield_forecast  = Transition(label='Yield Forecast')

# Loop for continuous growth monitoring and pest control
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_check,
    hydro_install,
    light_setup,
    climate_ctrl,
    seed_sel,
    nutrient_mix,
    water_recycle,
    sensor_deploy,
    monitor_loop,
    harvest_plan,
    packaging_prep,
    delivery_route,
    data_analysis,
    yield_forecast
])

# Sequence of setup activities
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, hydro_install)
root.order.add_edge(hydro_install, light_setup)
root.order.add_edge(light_setup, climate_ctrl)

# Nutrient and water recycling after setup
root.order.add_edge(climate_ctrl, nutrient_mix)
root.order.add_edge(climate_ctrl, water_recycle)

# Sensors deployed after climate control
root.order.add_edge(climate_ctrl, sensor_deploy)

# Continuous monitoring and pest control loop after sensor deployment
root.order.add_edge(sensor_deploy, monitor_loop)

# Harvest planning after monitoring loop
root.order.add_edge(monitor_loop, harvest_plan)

# Packaging and delivery after harvest plan
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, delivery_route)

# Data analysis and yield forecast at the end
root.order.add_edge(delivery_route, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)