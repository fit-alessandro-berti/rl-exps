import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, sensor_install, nutrient_mix, automation_code, crop_planning, pest_control, energy_audit, waste_sort])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[planting_tier, harvest_prep, logistics_plan, community_meet, data_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[system_upgrade, skip])
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)

# Print the root
print(root)