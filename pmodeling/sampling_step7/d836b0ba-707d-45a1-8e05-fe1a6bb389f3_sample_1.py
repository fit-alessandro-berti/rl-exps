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

# Define the partial order of activities
root = StrictPartialOrder(nodes=[site_select, design_layout, sensor_integrate, crop_choose, soil_prepare, irrigation_setup, pest_control, lighting_install, staff_train, compliance_check, market_analyze, package_design, logistics_plan, data_analyze, feedback_loop])

# Define dependencies between activities
root.order.add_edge(site_select, design_layout)
root.order.add_edge(design_layout, sensor_integrate)
root.order.add_edge(sensor_integrate, crop_choose)
root.order.add_edge(crop_choose, soil_prepare)
root.order.add_edge(soil_prepare, irrigation_setup)
root.order.add_edge(irrigation_setup, pest_control)
root.order.add_edge(pest_control, lighting_install)
root.order.add_edge(lighting_install, staff_train)
root.order.add_edge(staff_train, compliance_check)
root.order.add_edge(compliance_check, market_analyze)
root.order.add_edge(market_analyze, package_design)
root.order.add_edge(package_design, logistics_plan)
root.order.add_edge(logistics_plan, data_analyze)
root.order.add_edge(data_analyze, feedback_loop)

print(root)