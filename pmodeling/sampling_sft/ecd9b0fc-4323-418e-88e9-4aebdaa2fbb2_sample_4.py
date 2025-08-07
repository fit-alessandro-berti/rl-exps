import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
hydro_install   = Transition(label='Hydroponic Install')
lighting_setup  = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')
seed_selection  = Transition(label='Seed Selection')
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

# Build the main growth & harvest pipeline as a partial order
growth_pipeline = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    water_recycle,
    sensor_deploy,
    pest_control,
    growth_monitor,
    harvest_plan,
    packaging_prep,
    delivery_route
])
growth_pipeline.order.add_edge(seed_selection, nutrient_mix)
growth_pipeline.order.add_edge(nutrient_mix, water_recycle)
growth_pipeline.order.add_edge(water_recycle, sensor_deploy)
growth_pipeline.order.add_edge(sensor_deploy, pest_control)
growth_pipeline.order.add_edge(pest_control, growth_monitor)
growth_pipeline.order.add_edge(growth_monitor, harvest_plan)
growth_pipeline.order.add_edge(harvest_plan, packaging_prep)
growth_pipeline.order.add_edge(packaging_prep, delivery_route)

# Build the loop for continuous monitoring and data analysis
loop_body = growth_pipeline
skip = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_check,
    hydro_install,
    lighting_setup,
    climate_control,
    seed_selection,
    nutrient_mix,
    water_recycle,
    sensor_deploy,
    pest_control,
    growth_monitor,
    harvest_plan,
    packaging_prep,
    delivery_route,
    data_analysis,
    yield_forecast
])
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, hydro_install)
root.order.add_edge(hydro_install, lighting_setup)
root.order.add_edge(lighting_setup, climate_control)
root.order.add_edge(climate_control, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, water_recycle)
root.order.add_edge(water_recycle, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, delivery_route)
root.order.add_edge(harvest_plan, monitor_loop)
root.order.add_edge(monitor_loop, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)