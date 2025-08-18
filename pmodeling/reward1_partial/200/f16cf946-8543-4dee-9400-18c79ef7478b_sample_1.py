import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
system_design = Transition(label='System Design')
seed_selection = Transition(label='Seed Selection')
unit_install = Transition(label='Unit Install')
sensor_setup = Transition(label='Sensor Setup')
nutrient_mix = Transition(label='Nutrient Mix')
energy_audit = Transition(label='Energy Audit')
pest_control = Transition(label='Pest Control')
crop_plan = Transition(label='Crop Plan')
quality_check = Transition(label='Quality Check')
yield_forecast = Transition(label='Yield Forecast')
supply_sync = Transition(label='Supply Sync')
staff_train = Transition(label='Staff Train')
data_review = Transition(label='Data Review')

# Define loop for site survey and climate study
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, climate_study])

# Define XOR for seed selection and unit install
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, unit_install])

# Define XOR for sensor setup and nutrient mix
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, nutrient_mix])

# Define XOR for energy audit and pest control
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, pest_control])

# Define XOR for crop plan and quality check
xor4 = OperatorPOWL(operator=Operator.XOR, children=[crop_plan, quality_check])

# Define XOR for yield forecast and supply sync
xor5 = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, supply_sync])

# Define XOR for staff train and data review
xor6 = OperatorPOWL(operator=Operator.XOR, children=[staff_train, data_review])

# Define partial order
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

print(root)