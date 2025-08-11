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
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_check, building_retrofit, hydroponic_setup, climate_control, nutrient_design])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, staff_hiring, staff_training, software_install, system_testing, crop_planting, growth_monitor, pest_control, harvest_plan])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)