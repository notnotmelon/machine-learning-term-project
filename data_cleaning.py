import csv
import math
import subprocess

# Specify the path to the CSV file
csv_file_path = 'WFIGS_Incident_Locations_-835549102613066266.csv'

def find_fully_populated_cols(file):
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Get the header row
    header = next(csv_reader)

    # Get the total number of rows in the CSV file
    total_rows = sum(1 for row in csv_reader)

    # Iterate over each column index
    for col_index in range(len(header)):
        # Initialize a flag to track if the column has data populated on every row
        unpopulated = 0

        # Iterate over each row in the CSV file
        # Reset the file pointer to the beginning of the file
        file.seek(0)
        # Skip the header row
        next(csv_reader)
        for row in csv_reader:
            # Check if the current row has data populated in the column
            if not row[col_index]:
                unpopulated += 1

        population_percent = (1 - (unpopulated / total_rows)) * 100
        # Print the column name and the percentage of populated data
        print(f"{header[col_index]}: {population_percent:.2f}%")

'''
Columns with populated data on every row:
OBJECTID
SourceOID
ADSPermissionState
CreatedBySystem
FireDiscoveryDateTime
IncidentName
IncidentTypeCategory
IncidentTypeKind
IrwinID
IsFireCodeRequested
LocalIncidentIdentifier
POOProtectingUnit
POOState
UniqueFireIdentifier
CreatedOnDateTime_dt
ModifiedOnDateTime_dt
IsCpxChild
SourceGlobalID
GlobalID
x
y
'''

sparcity = '''
OBJECTID: 100.00%
SourceOID: 100.00%
ADSPermissionState: 100.00%
CreatedBySystem: 100.00%
FireDiscoveryDateTime: 100.00%
IncidentName: 100.00%
IncidentTypeCategory: 100.00%
IncidentTypeKind: 100.00%
IrwinID: 100.00%
IsFireCodeRequested: 100.00%
LocalIncidentIdentifier: 100.00%
POOProtectingUnit: 100.00%
POOState: 100.00%
UniqueFireIdentifier: 100.00%
CreatedOnDateTime_dt: 100.00%
ModifiedOnDateTime_dt: 100.00%
IsCpxChild: 100.00%
SourceGlobalID: 100.00%
GlobalID: 100.00%
x: 100.00%
y: 100.00%
GACC: 99.98%
POOCounty: 99.95%
POOFips: 99.94%
WFDSSDecisionStatus: 99.53%
POOPredictiveServiceAreaID: 90.24%
FireCause: 88.26%
DispatchCenterID: 87.55%
POOProtectingAgency: 83.69%
POOLandownerKind: 77.71%
POOLandownerCategory: 77.44%
DiscoveryAcres: 76.04%
InitialLatitude: 75.24%
InitialLongitude: 75.24%
POODispatchCenterID: 74.17%
IsFSAssisted: 73.44%
IncidentSize: 71.51%
IsReimbursable: 66.99%
IsTrespass: 66.88%
IsMultiJurisdictional: 65.58%
POOJurisdictionalUnit: 61.07%
ContainmentDateTime: 59.67%
FireOutDateTime: 55.14%
ControlDateTime: 53.26%
FireCode: 47.97%
POOJurisdictionalAgency: 43.11%
InitialResponseAcres: 30.41%
FSJobCode: 25.80%
FSOverrideCode: 25.62%
FireCauseGeneral: 20.34%
PredominantFuelModel: 12.14%
PredominantFuelGroup: 11.49%
FinalFireReportApprovedDate: 11.13%
InitialResponseDateTime: 10.50%
FireMgmtComplexity: 9.64%
PercentContained: 9.57%
FinalAcres: 8.91%
PrimaryFuelModel: 7.09%
FireBehaviorGeneral: 6.70%
FireCauseSpecific: 6.33%
IsUnifiedCommand: 5.91%
EstimatedCostToDate: 5.51%
ICS209ReportStatus: 5.18%
ABCDMisc: 5.00%
ICS209ReportDateTime: 4.97%
ICS209ReportForTimePeriodFrom: 4.82%
ICS209ReportForTimePeriodTo: 4.81%
IncidentManagementOrganization: 4.65%
TotalIncidentPersonnel: 4.25%
FireDepartmentID: 3.95%
IsFireCauseInvestigated: 3.92%
IncidentShortDescription: 3.76%
FireStrategyFullSuppPercent: 3.75%
PercentPerimeterToBeContained: 3.63%
FireStrategyMonitorPercent: 3.05%
FireStrategyConfinePercent: 3.01%
FireStrategyPointZonePercent: 2.93%
SecondaryFuelModel: 2.48%
FireBehaviorGeneral1: 2.46%
FireBehaviorGeneral2: 2.32%
POOCity: 2.24%
FireBehaviorGeneral3: 1.47%
FinalFireReportApprovedByUnit: 0.87%
POOLegalDescPrincipalMeridian: 0.83%
POOLegalDescRange: 0.81%
POOLegalDescSection: 0.81%
POOLegalDescTownship: 0.81%
OrganizationalAssessment: 0.79%
EstimatedFinalCost: 0.74%
StrategicDecisionPublishDate: 0.74%
POOLegalDescQtr: 0.36%
POOLegalDescQtrQtr: 0.33%
CpxName: 0.28%
CpxID: 0.28%
FinalFireReportApprovedByTitle: 0.00%
POOJurisdictionalUnitParentUnit: 0.00%
'''

'''
# Split the sparsity string by newlines
sparsity_lines = sparcity.strip().split('\n')

# Split each line by colon to separate the column name and percentage
sparsity_data = [line.split(': ') for line in sparsity_lines]

# Sort the sparsity data by percentage in descending order
sorted_sparsity = sorted(sparsity_data, key=lambda x: float(x[1][:-1]), reverse=True)

# Print the sorted sparsity data
for column, percentage in sorted_sparsity:
    print(f"{column}: {percentage}")
'''

to_ingore = [
    "FireCode",
    "POOJurisdictionalAgency",
    "InitialResponseAcres",
    "FSJobCode",
    "FSOverrideCode",
    "FireCauseGeneral",
    "PredominantFuelModel",
    "PredominantFuelGroup",
    "FinalFireReportApprovedDate",
    "InitialResponseDateTime",
    "FireMgmtComplexity",
    "PercentContained",
    "FinalAcres",
    "PrimaryFuelModel",
    "FireBehaviorGeneral",
    "FireCauseSpecific",
    "IsUnifiedCommand",
    "EstimatedCostToDate",
    "ICS209ReportStatus",
    "ABCDMisc",
    "ICS209ReportDateTime",
    "ICS209ReportForTimePeriodFrom",
    "ICS209ReportForTimePeriodTo",
    "IncidentManagementOrganization",
    "TotalIncidentPersonnel",
    "FireDepartmentID",
    "IsFireCauseInvestigated",
    "IncidentShortDescription",
    "FireStrategyFullSuppPercent",
    "PercentPerimeterToBeContained",
    "FireStrategyMonitorPercent",
    "FireStrategyConfinePercent",
    "FireStrategyPointZonePercent",
    "SecondaryFuelModel",
    "FireBehaviorGeneral1",
    "FireBehaviorGeneral2",
    "POOCity",
    "FireBehaviorGeneral3",
    "FinalFireReportApprovedByUnit",
    "POOLegalDescPrincipalMeridian",
    "POOLegalDescRange",
    "POOLegalDescSection",
    "POOLegalDescTownship",
    "OrganizationalAssessment",
    "EstimatedFinalCost",
    "StrategicDecisionPublishDate",
    "POOLegalDescQtr",
    "POOLegalDescQtrQtr",
    "CpxName",
    "CpxID",
    "FinalFireReportApprovedByTitle",
    "POOJurisdictionalUnitParentUnit",
    #"OBJECTID",
    "SourceOID",
    "IrwinID",
    "SourceGlobalID",
    "GlobalID",
    "ADSPermissionState",
    "CreatedBySystem",
    "IncidentName",
    "GACC",
    "WFDSSDecisionStatus",
    "UniqueFireIdentifier",
    "x",
    "y",
    "IsCpxChild",
    "CreatedOnDateTime_dt",
    "ModifiedOnDateTime_dt",
    "POOProtectingAgency",
    "POOLandownerKind",
    "POOPredictiveServiceAreaID",
    "POOProtectingUnit",
    "LocalIncidentIdentifier",
    "IncidentTypeCategory",
    "IncidentTypeKind",
    "DispatchCenterID",
    "IsMultiJurisdictional",
    "IsTrespass",
    "IsReimbursable",
    "ContainmentDateTime",
    "ControlDateTime",
    "DiscoveryAcres",
    "POOJurisdictionalUnit",
    "POOFips",
    "IsFireCodeRequested",
    "FireOutDateTime",
    "POOCounty",
    "POODispatchCenterID",
    "IsFSAssisted",
    "POOLandownerCategory",
    "FireDiscoveryDateTime",
    "POOState"   
]

fire_cause_map = {
    'human': 1,
    'undetermined': 0,
    'unknown': 0,
    'natural': -1
}

# Open the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as file:
    # Create a list to store the filtered rows
    filtered_rows = []

    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Get the header row
    header = next(csv_reader)

    # Get the column indices to ignore
    ignore_indices = [header.index(col) for col in to_ingore]
    ignore_indices.append(0)
    ignore_indices = set(ignore_indices)

    incident_size_index = header.index('IncidentSize')
    fire_cause_index = header.index('FireCause')
    longitude_index = header.index('InitialLongitude')
    latitude_index = header.index('InitialLatitude')
    date_index = header.index('FireDiscoveryDateTime')
    state_index = header.index('POOState')

    # Iterate over each row in the CSV file
    for row in csv_reader:
        if row[incident_size_index] and row[longitude_index] and row[latitude_index] and row[incident_size_index] != '0' and row[state_index] == 'US-CA':
            # Remove the columns to ignore from the row
            row[fire_cause_index] = fire_cause_map.get(row[fire_cause_index].lower(), 0)
            row[state_index] = row[state_index][3:] # Remove 'US-' from the state code
            row[incident_size_index] = math.log(float(row[incident_size_index]))
            filtered_row = [row[i] for i in range(len(row)) if i not in ignore_indices]

            month, day, year = row[date_index].split(' ')[0].split('/')
            filtered_row.append(month)

            # Add the filtered row to the list
            filtered_rows.append(filtered_row)

    # Specify the path to the new CSV file
    new_csv_file_path = 'filtered_data.csv'

    new_header = [header[i] for i in range(len(header)) if i not in ignore_indices]
    new_header.append('Month')

    filtered_rows.sort(key=lambda x: float(x[0]))

    # Open the new CSV file in write mode
    with open(new_csv_file_path, 'w', newline='', encoding='utf-8') as new_file:
        # Create a CSV writer object
        csv_writer = csv.writer(new_file)
        # Write the header row to the new CSV file
        csv_writer.writerow(new_header)
        # Write the filtered rows to the new CSV file
        csv_writer.writerows(filtered_rows)

    # Print a message indicating the new CSV file has been created
    print(f"Filtered data has been saved to {new_csv_file_path}")

    '''
    incidents_per_state = {}
    total_area_per_state = {}
    for row in filtered_rows:
        state = row[new_header.index('POOState')]
        if state in incidents_per_state:
            incidents_per_state[state] += 1
        else:
            incidents_per_state[state] = 1
        incident_size = float(row[new_header.index('IncidentSize')])
        if state in total_area_per_state:
            total_area_per_state[state] += incident_size
        else:
            total_area_per_state[state] = incident_size

    incidents_per_state = sorted(incidents_per_state.items(), key=lambda x: x[1], reverse=True)
    for state, count in incidents_per_state:
        print(f"{state}: {count}. Total affected area: {total_area_per_state[state]:.2f} acres")
    '''