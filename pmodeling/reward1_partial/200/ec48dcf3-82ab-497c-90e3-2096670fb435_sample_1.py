from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_germinate = Transition(label='Seed Germinate')
planting_phase = Transition(label='Planting Phase')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
water_monitor = Transition(label='Water Monitor')
data_analyze = Transition(label='Data Analyze')
staff_train = Transition(label='Staff Train')
yield_forecast = Transition(label='Yield Forecast')
community_meet = Transition(label='Community Meet')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        structure_build,
        system_install,
        climate_setup,
        nutrient_prep,
        seed_germinate,
        planting_phase,
        sensor_deploy,
        pest_control,
        water_monitor,
        data_analyze,
        staff_train,
        yield_forecast,
        community_meet
    ],
    order=[
        (site_survey, design_layout),
        (design_layout, structure_build),
        (structure_build, system_install),
        (system_install, climate_setup),
        (climate_setup, nutrient_prep),
        (nutrient_prep, seed_germinate),
        (seed_germinate, planting_phase),
        (planting_phase, sensor_deploy),
        (sensor_deploy, pest_control),
        (pest_control, water_monitor),
        (water_monitor, data_analyze),
        (data_analyze, staff_train),
        (staff_train, yield_forecast),
        (yield_forecast, community_meet)
    ]
)

# Add the partial order edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, planting_phase)
root.order.add_edge(planting_phase, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control)
root.order.add_edge(pest_control, water_monitor)
root.order.add_edge(water_monitor, data_analyze)
root.order.add_edge(data_analyze, staff_train)
root.order.add_edge(staff_train, yield_forecast)
root.order.add_edge(yield_forecast, community_meet)

print(root)