import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, climate_study, system_design])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, unit_install, sensor_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, energy_audit, pest_control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[crop_plan, quality_check, yield_forecast])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, staff_train, data_review])

# Create the root of the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop1)