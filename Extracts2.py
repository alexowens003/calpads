import calpads
import json

from google.cloud import storage

from calpads.client import CALPADSClient


def handler(request):
    cc = CALPADSClient(username='data@cwclosangeles.org', password='CWCLA2425!')

    schools = [
        {
             "School": {
            "0126177"
            , "0000001"
            , "0000002"
        }
            , "EnrollmentStartDate": "01/01/2000"
            , "EnrollmentEndDate": "06/30/2025"
            , "ActiveStudent": False
        }
    ]

    extracts = [
        {
            "extract_name": "SENR"
            , "parameters": ["School", "EnrollmentStartDate", "EnrollmentEndDate", "ActiveStudent"]
        }
    ]

    for extract in extracts:
        for school in schools:
            form_input = {}

            try:
                extract_name = extract["extract_name"]
                lea_code = school["lea_code"]
                school_abbr = school["abbr"]

                for parameter in extract["parameters"]:
                    form_input[parameter] = school[parameter]

            except Exception as error:
                print("Unable to build form input for following combination:")
                print("REPORT")
                print(json.dumps(extract, indent=2))
                print("SCHOOL")
                print(json.dumps(school, indent=2))

                print(repr(error))
                print("Skipping to next report...")
                continue

            print("Downloading", school_abbr + "-" + extract_name + "for lea_code", lea_code, "with input:")
            print(json.dumps(form_input, indent=2))

            try:
                cc.request_extract(lea_code=lea_code,
                                   extract_name=extract_name,
                                   by_date_range=True,
                                   form_data=form_input)

            except Exception as error:
                print("Failed to download", school_abbr + "-" + extract_name + ".csv!")

                print(repr(error))
                print("Skipping to next extract...")
                continue

    print("Done")


if __name__ == '__main__':
    handler(0)
