import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_select = Transition(label='Site Select')
design_layout = Transition(label='Design Layout')
sensor_integrate = Transition(label='Sensor Integrate')
crop_choose = Transition(label='Crop Choose')
soil_prepare = Transition(label='Soil Prepare')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control = Transition(label='Pest Control')
lighting_install = Transition(label='Lighting Install')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
market_analyze = Transition(label='Market Analyze')
package_design = Transition(label='Package Design')
logistics_plan = Transition(label='Logistics Plan')
data_analyze = Transition(label='Data Analyze')
feedback_loop = Transition(label='Feedback Loop')

# Define silent transitions
skip = SilentTransition()

# Define loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_select, design_layout])

# Define XOR node
xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define root node
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root node
print(root)