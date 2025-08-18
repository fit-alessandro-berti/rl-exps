import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the process structure
site_survey_to_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_structure = OperatorPOWL(operator=Operator.XOR, children=[structure_build, skip])
structure_build_to_system = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])
system_install_to_climate = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
climate_setup_to_nutrient = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
nutrient_prep_to_seed = OperatorPOWL(operator=Operator.XOR, children=[seed_germinate, skip])
seed_germinate_to_planting = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, skip])
planting_phase_to_sensor = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip])
sensor_deploy_to_pest = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_to_water = OperatorPOWL(operator=Operator.XOR, children=[water_monitor, skip])
water_monitor_to_data = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])
data_analyze_to_staff = OperatorPOWL(operator=Operator.XOR, children=[staff_train, skip])
staff_train_to_yield = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
yield_forecast_to_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])

# Construct the Partial Order
root = StrictPartialOrder(nodes=[
    site_survey_to_design,
    design_layout_to_structure,
    structure_build_to_system,
    system_install_to_climate,
    climate_setup_to_nutrient,
    nutrient_prep_to_seed,
    seed_germinate_to_planting,
    planting_phase_to_sensor,
    sensor_deploy_to_pest,
    pest_control_to_water,
    water_monitor_to_data,
    data_analyze_to_staff,
    staff_train_to_yield,
    yield_forecast_to_meet
])

# Add dependencies
root.order.add_edge(site_survey_to_design, design_layout_to_structure)
root.order.add_edge(design_layout_to_structure, structure_build_to_system)
root.order.add_edge(structure_build_to_system, system_install_to_climate)
root.order.add_edge(system_install_to_climate, climate_setup_to_nutrient)
root.order.add_edge(climate_setup_to_nutrient, nutrient_prep_to_seed)
root.order.add_edge(nutrient_prep_to_seed, seed_germinate_to_planting)
root.order.add_edge(seed_germinate_to_planting, planting_phase_to_sensor)
root.order.add_edge(planting_phase_to_sensor, sensor_deploy_to_pest)
root.order.add_edge(sensor_deploy_to_pest, pest_control_to_water)
root.order.add_edge(pest_control_to_water, water_monitor_to_data)
root.order.add_edge(water_monitor_to_data, data_analyze_to_staff)
root.order.add_edge(data_analyze_to_staff, staff_train_to_yield)
root.order.add_edge(staff_train_to_yield, yield_forecast_to_meet)

# Print the POWL model
print(root)