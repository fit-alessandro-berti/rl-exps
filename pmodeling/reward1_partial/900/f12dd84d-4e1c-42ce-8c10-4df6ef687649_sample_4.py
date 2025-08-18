import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Curd_Processing = Transition(label='Curd Processing')
Salt_Application = Transition(label='Salt Application')
Mold_Inoculation = Transition(label='Mold Inoculation')
Press_Molding = Transition(label='Press Molding')
Brine_Soaking = Transition(label='Brine Soaking')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Microbial_Check = Transition(label='Microbial Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Trace_Logging = Transition(label='Trace Logging')
Distribution_Plan = Transition(label='Distribution Plan')
Customer_Review = Transition(label='Customer Review')
Inventory_Audit = Transition(label='Inventory Audit')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Define silent transitions (if any)

# Define the process structure using POWL
root = StrictPartialOrder(
    nodes=[
        Milk_Sourcing,
        Quality_Testing,
        Curd_Processing,
        Salt_Application,
        Mold_Inoculation,
        Press_Molding,
        Brine_Soaking,
        Aging_Setup,
        Humidity_Control,
        Microbial_Check,
        Packaging_Design,
        Label_Printing,
        Trace_Logging,
        Distribution_Plan,
        Customer_Review,
        Inventory_Audit,
        Sustainability_Audit
    ],
    order=[
        (Milk_Sourcing, Quality_Testing),
        (Quality_Testing, Curd_Processing),
        (Curd_Processing, Salt_Application),
        (Salt_Application, Mold_Inoculation),
        (Mold_Inoculation, Press_Molding),
        (Press_Molding, Brine_Soaking),
        (Brine_Soaking, Aging_Setup),
        (Aging_Setup, Humidity_Control),
        (Humidity_Control, Microbial_Check),
        (Microbial_Check, Packaging_Design),
        (Packaging_Design, Label_Printing),
        (Label_Printing, Trace_Logging),
        (Trace_Logging, Distribution_Plan),
        (Distribution_Plan, Customer_Review),
        (Customer_Review, Inventory_Audit),
        (Inventory_Audit, Sustainability_Audit)
    ]
)

# You can add more dependencies or operators as needed