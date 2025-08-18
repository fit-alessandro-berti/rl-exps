from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_assess = Transition(label='Site Assess')
env_analysis = Transition(label='Env Analysis')
modular_install = Transition(label='Modular Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_selection = Transition(label='Crop Selection')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_calibrate = Transition(label='Lighting Calibrate')
pest_monitor = Transition(label='Pest Monitor')
staff_training = Transition(label='Staff Training')
energy_integrate = Transition(label='Energy Integrate')
data_analytics = Transition(label='Data Analytics')
waste_recycle = Transition(label='Waste Recycle')
market_develop = Transition(label='Market Develop')
yield_optimize = Transition(label='Yield Optimize')
climate_simulate = Transition(label='Climate Simulate')

# Define partial order model
root = StrictPartialOrder(
    nodes=[site_assess, env_analysis, modular_install, irrigation_setup,
           crop_selection, nutrient_mix, lighting_calibrate, pest_monitor,
           staff_training, energy_integrate, data_analytics, waste_recycle,
           market_develop, yield_optimize, climate_simulate],
    order=[
        (site_assess, env_analysis),
        (env_analysis, modular_install),
        (modular_install, irrigation_setup),
        (irrigation_setup, crop_selection),
        (crop_selection, nutrient_mix),
        (nutrient_mix, lighting_calibrate),
        (lighting_calibrate, pest_monitor),
        (pest_monitor, staff_training),
        (staff_training, energy_integrate),
        (energy_integrate, data_analytics),
        (data_analytics, waste_recycle),
        (waste_recycle, market_develop),
        (market_develop, yield_optimize),
        (yield_optimize, climate_simulate)
    ]
)