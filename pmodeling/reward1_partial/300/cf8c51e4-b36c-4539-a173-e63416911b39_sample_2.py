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

skip = SilentTransition()

site_analysis_zoning_approval = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, zoning_approval])
structural_check_retrofit = OperatorPOWL(operator=Operator.XOR, children=[structural_check, building_retrofit])
hydroponic_setup_climate_control = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, climate_control])
nutrient_design_install = OperatorPOWL(operator=Operator.XOR, children=[nutrient_design, software_install])
staff_hiring_training = OperatorPOWL(operator=Operator.XOR, children=[staff_hiring, staff_training])
system_testing_crop_planting = OperatorPOWL(operator=Operator.XOR, children=[system_testing, crop_planting])
growth_monitor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
harvest_plan_monitor = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, growth_monitor])

root = StrictPartialOrder(nodes=[site_analysis_zoning_approval, structural_check_retrofit, hydroponic_setup_climate_control, nutrient_design_install, staff_hiring_training, system_testing_crop_planting, growth_monitor_pest_control, harvest_plan_monitor])
root.order.add_edge(site_analysis_zoning_approval, structural_check_retrofit)
root.order.add_edge(structural_check_retrofit, hydroponic_setup_climate_control)
root.order.add_edge(hydroponic_setup_climate_control, nutrient_design_install)
root.order.add_edge(nutrient_design_install, staff_hiring_training)
root.order.add_edge(staff_hiring_training, system_testing_crop_planting)
root.order.add_edge(system_testing_crop_planting, growth_monitor_pest_control)
root.order.add_edge(growth_monitor_pest_control, harvest_plan_monitor)