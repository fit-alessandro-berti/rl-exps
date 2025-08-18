import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Create the XOR operator for the seed selection and nutrient preparation
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_select, nutrient_prep])

# Create the loop for the sensor installation and AI integration
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, ai_integration])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, env_analysis, modular_build, hydroponic_setup,
    xor, climate_calibrate, loop, crop_monitor, growth_adjust,
    harvest_sort, packaging, distribution_plan, sustain_audit, energy_optimize
])

# Add edges to the partial order
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, modular_build)
root.order.add_edge(modular_build, hydroponic_setup)
root.order.add_edge(hydroponic_setup, xor)
root.order.add_edge(xor, climate_calibrate)
root.order.add_edge(climate_calibrate, loop)
root.order.add_edge(loop, crop_monitor)
root.order.add_edge(crop_monitor, growth_adjust)
root.order.add_edge(growth_adjust, harvest_sort)
root.order.add_edge(harvest_sort, packaging)
root.order.add_edge(packaging, distribution_plan)
root.order.add_edge(distribution_plan, sustain_audit)
root.order.add_edge(sustain_audit, energy_optimize)

# Print the root of the POWL model
print(root)