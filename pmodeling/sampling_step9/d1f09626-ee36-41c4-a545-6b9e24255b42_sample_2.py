import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
climate_check = Transition(label='Climate Check')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
energy_setup = Transition(label='Energy Setup')
pest_control = Transition(label='Pest Control')
permit_obtain = Transition(label='Permit Obtain')
stakeholder_meet = Transition(label='Stakeholder Meet')
bed_construction = Transition(label='Bed Construction')
seed_planting = Transition(label='Seed Planting')
water_schedule = Transition(label='Water Schedule')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
yield_report = Transition(label='Yield Report')

# Define silent transitions
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[soil_sample, climate_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, irrigation_plan])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[energy_setup, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[permit_obtain, stakeholder_meet])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[bed_construction, seed_planting])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[water_schedule, growth_monitor])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, waste_recycle])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[yield_report, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop9)