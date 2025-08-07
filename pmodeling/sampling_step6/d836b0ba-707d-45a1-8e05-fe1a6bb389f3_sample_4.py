import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root as a strict partial order with the defined activities
root = StrictPartialOrder(nodes=[site_select, design_layout, sensor_integrate, crop_choose, soil_prepare, irrigation_setup, pest_control, lighting_install, staff_train, compliance_check, market_analyze, package_design, logistics_plan, data_analyze, feedback_loop])

# Define the dependencies (if any) between activities
# For this example, we assume no dependencies are defined
# If there were dependencies, they would be added here using root.order.add_edge() method

print(root)