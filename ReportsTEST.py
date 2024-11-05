import calpads

from google.cloud import storage

from calpads.client import CALPADSClient


def handler(request):
    cc = CALPADSClient(username='data@cwclosangeles.org', password='CWCLA2425!')

    form_input = {

        'LEA': 'Citizens of the World Charter School East Valley',
        'SchoolName': {

            'Citizens of the World Charter School East Valley-0140749': True,
            'NPS School Group for Citizens of the World Charter School East Valley-0000001': True

        },
        'FromDate': '01/01/2022',
        'ThrouDate': '06/30/2025'
    }

    cc.download_report(

        lea_code='0140749',
        report_code='8.1a',
        dry_run=False,
        form_data=form_input,
        file_name='/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/EV - 8.1a.csv',
        download_format='csv'
    )

if __name__ == '__main__':
    handler(0)