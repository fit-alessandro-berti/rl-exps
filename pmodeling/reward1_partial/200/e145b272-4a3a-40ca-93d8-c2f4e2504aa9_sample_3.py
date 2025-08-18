from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
permit_filing = Transition(label='Permit Filing')
modular_build = Transition(label='Modular Build')
sensor_install = Transition(label='Sensor Install')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
waste_setup = Transition(label='Waste Setup')
iot_deploy = Transition(label='IoT Deploy')
ai_scheduling = Transition(label='AI Scheduling')
energy_audit = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
crop_planting = Transition(label='Crop Planting')
yield_monitor = Transition(label='Yield Monitor')
data_analysis = Transition(label='Data Analysis')
system_upgrade = Transition(label='System Upgrade')

skip = SilentTransition()

site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])
system_design_xor = OperatorPOWL(operator=Operator.XOR, children=[modular_build, skip])
climate_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
nutrient_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
waste_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
iot_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_setup, skip])
ai_xor = OperatorPOWL(operator=Operator.XOR, children=[iot_deploy, skip])
energy_xor = OperatorPOWL(operator=Operator.XOR, children=[ai_scheduling, skip])
compliance_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
planting_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
yield_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])
analysis_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, skip])
upgrade_xor = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])

root = StrictPartialOrder(nodes=[
    site_survey_xor,
    system_design_xor,
    climate_xor,
    nutrient_xor,
    waste_xor,
    iot_xor,
    ai_xor,
    energy_xor,
    compliance_xor,
    planting_xor,
    yield_xor,
    analysis_xor,
    upgrade_xor
])

root.order.add_edge(site_survey_xor, system_design_xor)
root.order.add_edge(system_design_xor, climate_xor)
root.order.add_edge(climate_xor, nutrient_xor)
root.order.add_edge(nutrient_xor, waste_xor)
root.order.add_edge(waste_xor, iot_xor)
root.order.add_edge(iot_xor, ai_xor)
root.order.add_edge(ai_xor, energy_xor)
root.order.add_edge(energy_xor, compliance_xor)
root.order.add_edge(compliance_xor, planting_xor)
root.order.add_edge(planting_xor, yield_xor)
root.order.add_edge(yield_xor, analysis_xor)
root.order.add_edge(analysis_xor, upgrade_xor)

print(root)