from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
system_design = Transition(label='System Design')
hydroponics_setup = Transition(label='Hydroponics Setup')
lighting_install = Transition(label='Lighting Install')
sensor_install = Transition(label='Sensor Install')
climate_control = Transition(label='Climate Control')
nutrient_monitor = Transition(label='Nutrient Monitor')
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
auto_planting = Transition(label='Auto Planting')
growth_monitoring = Transition(label='Growth Monitoring')
ai_analytics = Transition(label='AI Analytics')
robotic_harvest = Transition(label='Robotic Harvest')
packaging = Transition(label='Packaging')
trace_labeling = Transition(label='Trace Labeling')
logistics_plan = Transition(label='Logistics Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structural_check,
    system_design,
    hydroponics_setup,
    lighting_install,
    sensor_install,
    climate_control,
    nutrient_monitor,
    seed_selection,
    germination_start,
    auto_planting,
    growth_monitoring,
    ai_analytics,
    robotic_harvest,
    packaging,
    trace_labeling,
    logistics_plan
])

# Define the order dependencies
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, hydroponics_setup)
root.order.add_edge(hydroponics_setup, lighting_install)
root.order.add_edge(lighting_install, sensor_install)
root.order.add_edge(sensor_install, climate_control)
root.order.add_edge(climate_control, nutrient_monitor)
root.order.add_edge(nutrient_monitor, seed_selection)
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, auto_planting)
root.order.add_edge(auto_planting, growth_monitoring)
root.order.add_edge(growth_monitoring, ai_analytics)
root.order.add_edge(ai_analytics, robotic_harvest)
root.order.add_edge(robotic_harvest, packaging)
root.order.add_edge(packaging, trace_labeling)
root.order.add_edge(trace_labeling, logistics_plan)

print(root)