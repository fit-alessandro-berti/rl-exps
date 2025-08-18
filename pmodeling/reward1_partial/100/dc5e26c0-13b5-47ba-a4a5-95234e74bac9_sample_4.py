import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
nutrient_mix = Transition(label='Nutrient Mix')
automation_code = Transition(label='Automation Code')
crop_planning = Transition(label='Crop Planning')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_sort = Transition(label='Waste Sort')
planting_tier = Transition(label='Planting Tier')
harvest_prep = Transition(label='Harvest Prep')
logistics_plan = Transition(label='Logistics Plan')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
system_upgrade = Transition(label='System Upgrade')

# Define silent transitions
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, sensor_install])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[automation_code, crop_planning])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, energy_audit])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[waste_sort, planting_tier])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep, logistics_plan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, data_review])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[system_upgrade, skip])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor1, loop3])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor2, loop4])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor3, loop5])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor4, loop6])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor5, loop7])

root = StrictPartialOrder(nodes=[site_survey, design_layout, xor6])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, xor6)

print(root)