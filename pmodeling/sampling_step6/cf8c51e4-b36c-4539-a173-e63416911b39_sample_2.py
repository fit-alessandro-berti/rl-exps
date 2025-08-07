import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
site_analysis = Transition(label='Site Analysis')
zoning_approval = Transition(label='Zoning Approval')
structural_check = Transition(label='Structural Check')
building_retrofit = Transition(label='Building Retrofit')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_control = Transition(label='Climate Control')
nutrient_design = Transition(label='Nutrient Design')
staff_hiring = Transition(label='Staff Hiring')
staff_training = Transition(label='Staff Training')
software_install = Transition(label='Software Install')
system_testing = Transition(label='System Testing')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[site_analysis, zoning_approval, structural_check, building_retrofit, hydroponic_setup, climate_control, nutrient_design, staff_hiring, staff_training, software_install, system_testing, crop_planting, growth_monitor, pest_control, harvest_plan])

# Optionally, you can add dependencies between activities if necessary
# For example, to ensure certain activities happen after others, you can add edges
# root.order.add_edge(site_analysis, zoning_approval)
# root.order.add_edge(site_analysis, structural_check)
# root.order.add_edge(site_analysis, building_retrofit)
# root.order.add_edge(site_analysis, hydroponic_setup)
# root.order.add_edge(site_analysis, climate_control)
# root.order.add_edge(site_analysis, nutrient_design)
# root.order.add_edge(site_analysis, staff_hiring)
# root.order.add_edge(site_analysis, staff_training)
# root.order.add_edge(site_analysis, software_install)
# root.order.add_edge(site_analysis, system_testing)
# root.order.add_edge(site_analysis, crop_planting)
# root.order.add_edge(site_analysis, growth_monitor)
# root.order.add_edge(site_analysis, pest_control)
# root.order.add_edge(site_analysis, harvest_plan)

# The 'root' variable now contains the POWL model for the urban vertical farm process.