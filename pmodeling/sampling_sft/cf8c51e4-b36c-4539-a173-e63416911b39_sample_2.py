import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis     = Transition(label='Site Analysis')
zoning_approval   = Transition(label='Zoning Approval')
structural_check  = Transition(label='Structural Check')
building_retrofit = Transition(label='Building Retrofit')
hydroponic_setup  = Transition(label='Hydroponic Setup')
climate_control   = Transition(label='Climate Control')
nutrient_design   = Transition(label='Nutrient Design')
software_install  = Transition(label='Software Install')
system_testing    = Transition(label='System Testing')
staff_hiring      = Transition(label='Staff Hiring')
staff_training    = Transition(label='Staff Training')
crop_planting     = Transition(label='Crop Planting')
growth_monitor    = Transition(label='Growth Monitor')
pest_control      = Transition(label='Pest Control')
harvest_plan      = Transition(label='Harvest Plan')

# Define the monitoring & management loop: do Growth Monitor, then either exit or do Pest Control and Growth Monitor again
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_approval, structural_check, building_retrofit,
    hydroponic_setup, climate_control, nutrient_design, software_install,
    system_testing, staff_hiring, staff_training, crop_planting,
    monitor_loop, harvest_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis,   zoning_approval)
root.order.add_edge(zoning_approval, structural_check)
root.order.add_edge(structural_check, building_retrofit)
root.order.add_edge(building_retrofit, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_control)
root.order.add_edge(climate_control, nutrient_design)
root.order.add_edge(nutrient_design, software_install)
root.order.add_edge(software_install, system_testing)
root.order.add_edge(system_testing, staff_hiring)
root.order.add_edge(staff_hiring, staff_training)
root.order.add_edge(staff_training, crop_planting)
root.order.add_edge(crop_planting, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)