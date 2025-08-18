from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (site_analysis, structure_check),
        (structure_check, farm_design),
        (farm_design, env_control),
        (env_control, nutrient_prep),
        (nutrient_prep, seed_selection),
        (seed_selection, automated_plant),
        (automated_plant, sensor_setup),
        (sensor_setup, microclimate_mon),
        (microclimate_mon, health_monitor),
        (health_monitor, light_adjust),
        (light_adjust, irrigation_mod),
        (irrigation_mod, waste_recycle),
        (waste_recycle, energy_optimize),
        (energy_optimize, quality_check),
        (quality_check, crop_harvest),
        (crop_harvest, distribution_plan)
    ]
)