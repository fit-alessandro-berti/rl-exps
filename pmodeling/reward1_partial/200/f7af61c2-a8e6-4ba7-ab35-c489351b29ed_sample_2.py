from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
farm_design = Transition(label='Farm Design')
env_control = Transition(label='Env Control')
nutrient_prep = Transition(label='Nutrient Prep')
seed_selection = Transition(label='Seed Selection')
automated_plant = Transition(label='Automated Plant')
sensor_setup = Transition(label='Sensor Setup')
microclimate_mon = Transition(label='Microclimate Mon')
health_monitor = Transition(label='Health Monitor')
light_adjust = Transition(label='Light Adjust')
irrigation_mod = Transition(label='Irrigation Mod')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
quality_check = Transition(label='Quality Check')
crop_harvest = Transition(label='Crop Harvest')
distribution_plan = Transition(label='Distribution Plan')

skip = SilentTransition()

# Define the process model
site_analysis_to_structure_check = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structure_check])
structure_check_to_farm_design = OperatorPOWL(operator=Operator.LOOP, children=[structure_check, farm_design])
farm_design_to_env_control = OperatorPOWL(operator=Operator.LOOP, children=[farm_design, env_control])
env_control_to_nutrient_prep = OperatorPOWL(operator=Operator.LOOP, children=[env_control, nutrient_prep])
nutrient_prep_to_seed_selection = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep, seed_selection])
seed_selection_to_automated_plant = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, automated_plant])
automated_plant_to_sensor_setup = OperatorPOWL(operator=Operator.LOOP, children=[automated_plant, sensor_setup])
sensor_setup_to_microclimate_mon = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, microclimate_mon])
microclimate_mon_to_health_monitor = OperatorPOWL(operator=Operator.LOOP, children=[microclimate_mon, health_monitor])
health_monitor_to_light_adjust = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, light_adjust])
light_adjust_to_irrigation_mod = OperatorPOWL(operator=Operator.LOOP, children=[light_adjust, irrigation_mod])
irrigation_mod_to_waste_recycle = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_mod, waste_recycle])
waste_recycle_to_energy_optimize = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, energy_optimize])
energy_optimize_to_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[energy_optimize, quality_check])
quality_check_to_crop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, crop_harvest])
crop_harvest_to_distribution_plan = OperatorPOWL(operator=Operator.LOOP, children=[crop_harvest, distribution_plan])

# Define the order of execution
root = StrictPartialOrder(nodes=[
    site_analysis_to_structure_check,
    structure_check_to_farm_design,
    farm_design_to_env_control,
    env_control_to_nutrient_prep,
    nutrient_prep_to_seed_selection,
    seed_selection_to_automated_plant,
    automated_plant_to_sensor_setup,
    sensor_setup_to_microclimate_mon,
    microclimate_mon_to_health_monitor,
    health_monitor_to_light_adjust,
    light_adjust_to_irrigation_mod,
    irrigation_mod_to_waste_recycle,
    waste_recycle_to_energy_optimize,
    energy_optimize_to_quality_check,
    quality_check_to_crop_harvest,
    crop_harvest_to_distribution_plan
])

# Add the edges to the partial order
root.order.add_edge(site_analysis_to_structure_check, structure_check_to_farm_design)
root.order.add_edge(structure_check_to_farm_design, farm_design_to_env_control)
root.order.add_edge(farm_design_to_env_control, env_control_to_nutrient_prep)
root.order.add_edge(env_control_to_nutrient_prep, nutrient_prep_to_seed_selection)
root.order.add_edge(nutrient_prep_to_seed_selection, seed_selection_to_automated_plant)
root.order.add_edge(seed_selection_to_automated_plant, automated_plant_to_sensor_setup)
root.order.add_edge(automated_plant_to_sensor_setup, sensor_setup_to_microclimate_mon)
root.order.add_edge(sensor_setup_to_microclimate_mon, microclimate_mon_to_health_monitor)
root.order.add_edge(microclimate_mon_to_health_monitor, health_monitor_to_light_adjust)
root.order.add_edge(health_monitor_to_light_adjust, light_adjust_to_irrigation_mod)
root.order.add_edge(light_adjust_to_irrigation_mod, irrigation_mod_to_waste_recycle)
root.order.add_edge(irrigation_mod_to_waste_recycle, waste_recycle_to_energy_optimize)
root.order.add_edge(waste_recycle_to_energy_optimize, energy_optimize_to_quality_check)
root.order.add_edge(energy_optimize_to_quality_check, quality_check_to_crop_harvest)
root.order.add_edge(quality_check_to_crop_harvest, crop_harvest_to_distribution_plan)

print(root)