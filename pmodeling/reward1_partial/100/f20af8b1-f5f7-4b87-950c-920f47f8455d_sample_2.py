from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
modular_build = Transition(label='Modular Build')
hydroponic_setup = Transition(label='Hydroponic Setup')
seed_select = Transition(label='Seed Select')
nutrient_prep = Transition(label='Nutrient Prep')
climate_calibrate = Transition(label='Climate Calibrate')
sensor_install = Transition(label='Sensor Install')
ai_integration = Transition(label='AI Integration')
crop_monitor = Transition(label='Crop Monitor')
growth_adjust = Transition(label='Growth Adjust')
harvest_sort = Transition(label='Harvest Sort')
packaging = Transition(label='Packaging')
distribution_plan = Transition(label='Distribution Plan')
sustain_audit = Transition(label='Sustain Audit')
energy_optimize = Transition(label='Energy Optimize')

# Define exclusive choices for activities
modular_choice = OperatorPOWL(operator=Operator.XOR, children=[modular_build, hydroponic_setup])
sensor_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, ai_integration])
sustain_choice = OperatorPOWL(operator=Operator.XOR, children=[sustain_audit, energy_optimize])

# Define the root model
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    modular_choice,
    sensor_choice,
    sustain_choice,
    seed_select,
    nutrient_prep,
    climate_calibrate,
    crop_monitor,
    growth_adjust,
    harvest_sort,
    packaging,
    distribution_plan
])

# Define the partial order dependencies
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, modular_choice)
root.order.add_edge(modular_choice, sensor_choice)
root.order.add_edge(sensor_choice, sustain_choice)
root.order.add_edge(sustain_choice, seed_select)
root.order.add_edge(seed_select, nutrient_prep)
root.order.add_edge(nutrient_prep, climate_calibrate)
root.order.add_edge(climate_calibrate, crop_monitor)
root.order.add_edge(crop_monitor, growth_adjust)
root.order.add_edge(growth_adjust, harvest_sort)
root.order.add_edge(harvest_sort, packaging)
root.order.add_edge(packaging, distribution_plan)

print(root)