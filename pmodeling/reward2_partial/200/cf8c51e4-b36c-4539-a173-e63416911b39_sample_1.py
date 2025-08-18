import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[
    site_analysis,
    zoning_approval,
    structural_check,
    building_retrofit,
    hydroponic_setup,
    climate_control,
    nutrient_design,
    staff_hiring,
    staff_training,
    software_install,
    system_testing,
    crop_planting,
    growth_monitor,
    pest_control,
    harvest_plan
])

root.order.add_edge(site_analysis, zoning_approval)
root.order.add_edge(zoning_approval, structural_check)
root.order.add_edge(structural_check, building_retrofit)
root.order.add_edge(building_retrofit, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_control)
root.order.add_edge(climate_control, nutrient_design)
root.order.add_edge(nutrient_design, staff_hiring)
root.order.add_edge(staff_hiring, staff_training)
root.order.add_edge(staff_training, software_install)
root.order.add_edge(software_install, system_testing)
root.order.add_edge(system_testing, crop_planting)
root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvest_plan)