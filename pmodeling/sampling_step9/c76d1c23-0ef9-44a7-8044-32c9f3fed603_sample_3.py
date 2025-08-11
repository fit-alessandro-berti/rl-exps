import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
design_layout = Transition(label='Design Layout')
system_order = Transition(label='System Order')
structure_build = Transition(label='Structure Build')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
package_produce = Transition(label='Package Produce')
local_delivery = Transition(label='Local Delivery')
analyze_data = Transition(label='Analyze Data')
skip = SilentTransition()

# Define loop for hydroponics installation and calibration
loop = OperatorPOWL(operator=Operator.LOOP, children=[install_hydroponics, calibrate_sensors])

# Define XOR for crop selection and skipping if no crops are selected
xor = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)