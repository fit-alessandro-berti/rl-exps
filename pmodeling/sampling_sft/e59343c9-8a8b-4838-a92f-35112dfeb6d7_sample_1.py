import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
permit_approval = Transition(label='Permit Approval')
design_layout   = Transition(label='Design Layout')
system_procure  = Transition(label='System Procure')
nutrient_prep   = Transition(label='Nutrient Prep')
structure_build = Transition(label='Structure Build')
sensor_install  = Transition(label='Sensor Install')
climate_setup   = Transition(label='Climate Setup')
seed_select     = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
monitor_growth  = Transition(label='Monitor Growth')
data_analyze    = Transition(label='Data Analyze')
pest_control    = Transition(label='Pest Control')
harvest_crop    = Transition(label='Harvest Crop')
package_goods   = Transition(label='Package Goods')
ship_products   = Transition(label='Ship Products')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, permit_approval, design_layout, system_procure, nutrient_prep,
    structure_build, sensor_install, climate_setup, seed_select, germinate_seeds,
    monitor_growth, data_analyze, pest_control, harvest_crop, package_goods, ship_products
])

# Define the control‐flow dependencies
# 1. Initial setup
root.order.add_edge(site_survey, permit_approval)
root.order.add_edge(permit_approval, design_layout)
root.order.add_edge(design_layout, system_procure)
root.order.add_edge(system_procure, nutrient_prep)
root.order.add_edge(nutrient_prep, structure_build)

# 2. Installation and setup
root.order.add_edge(structure_build, sensor_install)
root.order.add_edge(structure_build, climate_setup)

# 3. Growth and maintenance
root.order.add_edge(sensor_install, monitor_growth)
root.order.add_edge(climate_setup, monitor_growth)
root.order.add_edge(monitor_growth, data_analyze)
root.order.add_edge(data_analyze, pest_control)

# 4. Harvesting and packaging
root.order.add_edge(pest_control, harvest_crop)
root.order.add_edge(harvest_crop, package_goods)

# 5. Shipping and completion
root.order.add_edge(package_goods, ship_products)