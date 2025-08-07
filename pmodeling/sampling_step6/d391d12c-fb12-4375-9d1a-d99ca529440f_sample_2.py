from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    climate_check,
    soil_testing,
    media_select,
    design_layout,
    hydro_setup,
    nutrient_mix,
    sensor_install,
    regulation_review,
    permit_apply,
    stakeholder_meet,
    community_train,
    plant_seed,
    monitor_growth,
    adjust_controls,
    harvest_plan,
    waste_recycle,
    feedback_loop
])

# Add dependencies between transitions if necessary
# For example, if 'climate_check' depends on 'site_survey':
root.order.add_edge(site_survey, climate_check)

# If you need to add more complex dependencies or choices, you can use the OperatorPOWL class.
# For instance, if there's an exclusive choice between 'soil_testing' and 'media_select':
# exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, media_select])
# root.nodes.append(exclusive_choice)
# root.order.add_edge(site_survey, exclusive_choice)

# Print the root to verify the model
print(root)