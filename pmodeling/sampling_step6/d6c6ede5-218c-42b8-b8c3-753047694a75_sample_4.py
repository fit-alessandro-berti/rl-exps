from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
climate_study = Transition(label='Climate Study')
permit_check = Transition(label='Permit Check')
system_design = Transition(label='System Design')
equipment_buy = Transition(label='Equipment Buy')
sensor_setup = Transition(label='Sensor Setup')
irrigation_fit = Transition(label='Irrigation Fit')
solar_install = Transition(label='Solar Install')
staff_train = Transition(label='Staff Train')
pilot_plant = Transition(label='Pilot Plant')
data_monitor = Transition(label='Data Monitor')
crop_harvest = Transition(label='Crop Harvest')
maintenance_plan = Transition(label='Maintenance Plan')
community_meet = Transition(label='Community Meet')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    climate_study,
    permit_check,
    system_design,
    equipment_buy,
    sensor_setup,
    irrigation_fit,
    solar_install,
    staff_train,
    pilot_plant,
    data_monitor,
    crop_harvest,
    maintenance_plan,
    community_meet
])

# Add dependencies if any (in this case, no explicit dependencies are mentioned in the problem description)
# If there are dependencies, they would be added here like: root.order.add_edge(node1, node2)

# Now 'root' contains the POWL model for the process
print(root)