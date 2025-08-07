from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
supply_chain = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Define the loop for continuous optimization
optimization_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analyze, supply_chain])

# Define the partial order with concurrent activities
partial_order = StrictPartialOrder(
    nodes=[site_survey, climate_study, design_layout, system_install, crop_select, nutrient_plan, sensor_setup,
           automation_test, staff_train, compliance_check, marketing_sync, data_monitor, yield_analyze, supply_chain,
           customer_engage, optimization_loop],
    order={
        site_survey: [climate_study, design_layout],
        climate_study: [system_install],
        design_layout: [system_install],
        system_install: [crop_select, nutrient_plan],
        crop_select: [sensor_setup, automation_test],
        nutrient_plan: [automation_test],
        sensor_setup: [automation_test],
        automation_test: [staff_train, compliance_check],
        staff_train: [compliance_check],
        compliance_check: [marketing_sync, data_monitor],
        marketing_sync: [yield_analyze],
        data_monitor: [supply_chain],
        yield_analyze: [supply_chain],
        supply_chain: [customer_engage],
        customer_engage: [optimization_loop]
    }
)

# Define the root of the POWL model
root = partial_order