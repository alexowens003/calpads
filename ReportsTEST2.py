import calpads
import json

from google.cloud import storage

from calpads.client import CALPADSClient


def handler(request):
    cc = CALPADSClient(username='data@cwclosangeles.org', password='CWCLA2425!')

    schools = [
        {
            "SchoolName": {
                "Citizens of the World Charter School Hollywood-0122556": True
                , "NPS School Group for Citizens of the World Charter School Hollywood-0000001": True
            }
            , "School": {
            "Citizens of the World Charter School Hollywood-0122556": True
            , "NPS School Group for Citizens of the World Charter School Hollywood-0000001": True
        }
            , "LEA": "Citizens of the World Charter School Hollywood"
            , "AcademicYear": "2024-2025"
            , "lea_code": "0122556"
            , "abbr": "HW"
        },
        {
            "SchoolName": {
                "Citizens of the World Charter School Hollywood-0122556": True
                , "NPS School Group for Citizens of the World Charter School Hollywood-0000001": True
            }
            , "School": {
            "Citizens of the World Charter School Hollywood-0122556": True
            , "NPS School Group for Citizens of the World Charter School Hollywood-0000001": True
        }
            , "LEA": "Citizens of the World Charter School Hollywood"
            , "AcademicYear": "2024-2025"
            , "lea_code": "0122556"
            , "abbr": "HW"
        }
    ]

    reports = [
        {
            "code": "8.1"
            , "parameters": ["SchoolName", "LEA"]
        }
    ]

    for report in reports:
        for school in schools:
            form_input = {}

            try:
                reports_code = report["code"]
                lea_code = school["lea_code"]
                school_abbr = school["abbr"]

                for parameter in report["parameters"]:
                    form_input[parameter] = school[parameter]

            except Exception as error:
                print("Unable to build form input for following combination:")
                print("REPORT")
                print(json.dumps(report, indent=2))
                print("SCHOOL")
                print(json.dumps(school, indent=2))

                print(repr(error))
                print("Skipping to next report...")
                continue

            print("Downloading", school_abbr + "-" + reports_code + ".csv for lea_code", lea_code, "with input:")
            print(json.dumps(form_input, indent=2))

            try:
                cc.download_report(lea_code=lea_code,
                                   report_code=reports_code,
                                   dry_run=False,
                                   form_data=form_input,
                                   file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/{school_abbr} - {reports_code}.csv',
                                   download_format='csv')
            except Exception as error:
                print("Failed to download", school_abbr + "-" + reports_code + ".csv!")

                print(repr(error))
                print("Skipping to next report...")
                continue

    print("Done")


if __name__ == '__main__':
    handler(0)
