import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_analysis, structural_check, system_design, hydroponics_setup, lighting_install, sensor_install,
    climate_control, nutrient_monitor, seed_selection, germination_start, auto_planting, growth_monitoring,
    ai_analytics, robotic_harvest, packaging, trace_labeling, logistics_plan
])

# Add dependencies (assuming dependencies are not explicitly given in the problem description, we'll assume a simple linear flow for demonstration)
# In a real scenario, dependencies would be defined based on the actual process flow
# Here, we'll assume a simple linear flow for demonstration
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(site_analysis, system_design)
root.order.add_edge(site_analysis, hydroponics_setup)
root.order.add_edge(site_analysis, lighting_install)
root.order.add_edge(site_analysis, sensor_install)
root.order.add_edge(site_analysis, climate_control)
root.order.add_edge(site_analysis, nutrient_monitor)
root.order.add_edge(site_analysis, seed_selection)
root.order.add_edge(site_analysis, germination_start)
root.order.add_edge(site_analysis, auto_planting)
root.order.add_edge(site_analysis, growth_monitoring)
root.order.add_edge(site_analysis, ai_analytics)
root.order.add_edge(site_analysis, robotic_harvest)
root.order.add_edge(site_analysis, packaging)
root.order.add_edge(site_analysis, trace_labeling)
root.order.add_edge(site_analysis, logistics_plan)

print(root)