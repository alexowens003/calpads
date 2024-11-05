import time
import calpads
from calpads.client import CALPADSClient
from google.cloud import storage

cc = CALPADSClient(username='data@cwclosangeles.org', password='CWCLA2526!')

extract = 'SELA'
extract_filename = 'DirectCert' if extract == 'DIRECTCERTIFICATION' else extract

extract_input = [
    ('School', '0126177'),
    ('School', '0000001'),
    ('School', '0000002'),
    ('StartDate', '01/01/2000'),
    ('EnrollmentStartDate', '01/01/2000'),
    ('EndDate', '06/30/2025'),
    ('EnrollmentEndDate', '06/30/2025'),
    ('SpecialEducationStatus', '1'),
    ('SpecialEducationStatus', '2'),
    ('SpecialEducationStatus', '3'),
    ('SpecialEducationStatus', '4'),
    ('ActiveStudent', False),
    ('CertificationStatusCode', 'All'),
    ('EducationProgramCode', 'All'),
    ('RecordHistory', 'Y')
]

cc.request_extract(lea_code='0126177',
                   extract_name=extract,
                   by_date_range=True,
                   form_data=extract_input)

extract_input = [
    ('School', '0126193'),
    ('School', '0000001'),
    ('School', '0000002'),
    ('StartDate', '01/01/2000'),
    ('EnrollmentStartDate', '01/01/2000'),
    ('EndDate', '06/30/2025'),
    ('EnrollmentEndDate', '06/30/2025'),
    ('SpecialEducationStatus', '1'),
    ('SpecialEducationStatus', '2'),
    ('SpecialEducationStatus', '3'),
    ('SpecialEducationStatus', '4'),
    ('ActiveStudent', False),
    ('CertificationStatusCode', 'All'),
    ('EducationProgramCode', 'All'),
    ('RecordHistory', 'Y')
]

cc.request_extract(lea_code='0126193',
                   extract_name=extract,
                   by_date_range=True,
                   form_data=extract_input)

extract_input = [
    ('School', '0122556'),
    ('School', '0000001'),
    ('School', '0000002'),
    ('StartDate', '01/01/2000'),
    ('EnrollmentStartDate', '01/01/2000'),
    ('EndDate', '06/30/2025'),
    ('EnrollmentEndDate', '06/30/2025'),
    ('SpecialEducationStatus', '1'),
    ('SpecialEducationStatus', '2'),
    ('SpecialEducationStatus', '3'),
    ('SpecialEducationStatus', '4'),
    ('ActiveStudent', False),
    ('CertificationStatusCode', 'All'),
    ('EducationProgramCode', 'All'),
    ('RecordHistory', 'Y')
]

cc.request_extract(lea_code='0122556',
                   extract_name=extract,
                   by_date_range=True,
                   form_data=extract_input)

extract_input = [
    ('School', '0140749'),
    ('School', '0000001'),
    ('School', '0000002'),
    ('StartDate', '01/01/2000'),
    ('EnrollmentStartDate', '01/01/2000'),
    ('EndDate', '06/30/2025'),
    ('EnrollmentEndDate', '06/30/2025'),
    ('SpecialEducationStatus', '1'),
    ('SpecialEducationStatus', '2'),
    ('SpecialEducationStatus', '3'),
    ('SpecialEducationStatus', '4'),
    ('ActiveStudent', False),
    ('CertificationStatusCode', 'All'),
    ('EducationProgramCode', 'All'),
    ('RecordHistory', 'Y')
]

cc.request_extract(lea_code='0140749',
                   extract_name=extract,
                   by_date_range=True,
                   form_data=extract_input)

extract_input = [
    ('School', '0139832'),
    ('School', '0000001'),
    ('School', '0000002'),
    ('StartDate', '01/01/2000'),
    ('EnrollmentStartDate', '01/01/2000'),
    ('EndDate', '06/30/2025'),
    ('EnrollmentEndDate', '06/30/2025'),
    ('SpecialEducationStatus', '1'),
    ('SpecialEducationStatus', '2'),
    ('SpecialEducationStatus', '3'),
    ('SpecialEducationStatus', '4'),
    ('ActiveStudent', False),
    ('CertificationStatusCode', 'All'),
    ('EducationProgramCode', 'All'),
    ('RecordHistory', 'Y')
]

cc.request_extract(lea_code='0139832',
                   extract_name=extract,
                   by_date_range=True,
                   form_data=extract_input)

time.sleep(30)

cc.download_extract(lea_code='0126177',
                    file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/SL - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )
'''
cc.download_extract(lea_code='0126177',
                    file_name=f'/tmp/SL - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )

storage_client = storage.Client('lofty-hearth-422200-e9')
bucket = storage_client.bucket('calpads')
blob = bucket.blob(f'Extracts/SL - {extract_filename}.txt')

blob.upload_from_filename(f'/tmp/SL - {extract_filename}.txt')
'''

cc.download_extract(lea_code='0126193',
                    file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/MV - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )

cc.download_extract(lea_code='0122556',
                    file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/HW - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )

cc.download_extract(lea_code='0140749',
                    file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/EV - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )

cc.download_extract(lea_code='0139832',
                    file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/WV - {extract_filename}.txt',
                    timeout=600,
                    poll=10
                    )