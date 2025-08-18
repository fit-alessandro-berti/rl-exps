import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control = Transition(label='Env Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
ai_setup = Transition(label='AI Setup')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
irrigation_plan = Transition(label='Irrigation Plan')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
market_setup = Transition(label='Market Setup')
logistics_plan = Transition(label='Logistics Plan')
waste_manage = Transition(label='Waste Manage')

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[
    env_control, nutrient_mix, crop_select, ai_setup, worker_train, pest_control, irrigation_plan, data_monitor, yield_forecast, energy_audit, market_setup, logistics_plan, waste_manage])

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_survey, structure_prep, system_install, xor])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor)

print(root)