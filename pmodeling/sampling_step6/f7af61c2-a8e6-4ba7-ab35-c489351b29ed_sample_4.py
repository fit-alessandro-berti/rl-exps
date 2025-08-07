import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    farm_design,
    env_control,
    nutrient_prep,
    seed_selection,
    automated_plant,
    sensor_setup,
    microclimate_mon,
    health_monitor,
    light_adjust,
    irrigation_mod,
    waste_recycle,
    energy_optimize,
    quality_check,
    crop_harvest,
    distribution_plan
])

# Add dependencies if needed
# For example, if the sensor setup must happen after the automated plant:
root.order.add_edge(automated_plant, sensor_setup)

# If the distribution plan must happen after the quality check:
root.order.add_edge(quality_check, distribution_plan)

# If there are no specific dependencies, you can leave the order empty or add them as needed.
# For simplicity, we assume there are no specific dependencies in this example.