import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
modify_layout = Transition(label='Modify Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
deploy_sensors = Transition(label='Deploy Sensors')
pest_control = Transition(label='Pest Control')
optimize_energy = Transition(label='Optimize Energy')
recycle_water = Transition(label='Recycle Water')
automate_harvest = Transition(label='Automate Harvest')
package_crops = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data = Transition(label='Analyze Data')

# Define the partial order workflow
root = StrictPartialOrder(nodes=[site_analysis, structure_check, modify_layout, install_hvac, setup_hydroponics, prepare_nutrients, select_seeds, automate_planting, deploy_sensors, pest_control, optimize_energy, recycle_water, automate_harvest, package_crops, coordinate_delivery, analyze_data])