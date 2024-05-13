import calpads
import logging

from google.cloud import storage

def write_read(bucket_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)


from calpads.client import CALPADSClient

def handler():

    cc = CALPADSClient(username='data@cwclosangeles.org', password='123!')

    logging.getLogger().setLevel(logging.DEBUG)

    # report and school lists we will loop through
    report_list = ['8.1', '8.1a', '5.7']
    school_list = ['HW', 'MV', 'SL', 'EV', 'WV']

    # dictionary for schools and lea codes
    lea = {
        'HW': '0122556',
        'MV': '0126193',
        'SL': '0126177',
        'EV': '0140749',
        'WV': '0139832'
    }

    # loops through reports and schools, downloads reports for all
    for school in school_list:
        for report in report_list:
            # form_inputs for each school and report combo
            if school == 'HW':
                if report == '8.1':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School Hollywood',
                        'SchoolName': {

                            'Citizens of the World Charter School Hollywood-0122556': True,
                            'NPS School Group for Citizens of the World Charter School Hollywood-0000001': True
                        }
                    }
                elif report == '5.7':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School Hollywood',
                        'School': {

                            'Citizens of the World Charter School Hollywood-0122556': True,
                            'NPS School Group for Citizens of the World Charter School Hollywood-0000001': True
                        }
                    }
                elif report == '8.1a':
                    form_input = {

                        'FromDate': '01/01/2000',
                        'ThrouDate': '06/30/2024',
                        'SchoolName': {

                            'Citizens of the World Charter School Hollywood-0122556': True,
                            'NPS School Group for Citizens of the World Charter School Hollywood-0000001': True
                        }
                    }

            elif school == "MV":
                if report == '8.1':
                    form_input = {

                        'SchoolName': {

                            'Citizens of the World Charter School Mar Vista-0126193': True,
                            'NPS School Group for Citizens of the World Charter School Mar Vista-0000001': True
                        }
                    }
                elif report == '5.7':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School Mar Vista-0126193',
                        'School': {

                            'Citizens of the World Charter School Mar Vista-0126193': True,
                            'NPS School Group for Citizens of the World Charter School Mar Vista-0000001': True
                        }
                    }
                elif report == '8.1a':
                    form_input = {

                        'FromDate': '01/01/2000',
                        'ThrouDate': '06/30/2024',
                        'SchoolName': {

                            'Citizens of the World Charter School Mar Vista-0126193': True,
                            'NPS School Group for Citizens of the World Charter School Mar Vista-0000001': True
                        }
                    }

            elif school == 'SL':
                if report == '8.1':
                    form_input = {

                        'SchoolName': {

                            'Citizens of the World Charter School Silver Lake-0126177': True,
                            'NPS School Group for Citizens of the World Charter School Silver Lake-0000001': True
                        }
                    }
                elif report == '5.7':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School Silver Lake',
                        'School': {

                            'Citizens of the World Charter School Silver Lake-0126177': True,
                            'NPS School Group for Citizens of the World Charter School Silver Lake-0000001': True
                        }
                    }
                elif report == '8.1a':
                    form_input = {

                        'FromDate': '01/01/2000',
                        'ThrouDate': '06/30/2024',
                        'SchoolName': {

                            'Citizens of the World Charter School Silver Lake-0126177': True,
                            'NPS School Group for Citizens of the World Charter School Silver Lake-0000001': True
                        }
                    }

            elif school == 'EV':
                if report == '8.1':
                    form_input = {

                        'SchoolName': {

                            'Citizens of the World Charter School East Valley-0140749': True,
                            'NPS School Group for Citizens of the World Charter School East Valley-0000001': True
                        }
                    }
                elif report == '5.7':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School East Valley-0140749',
                        'School': {

                            'Citizens of the World Charter School East Valley-0140749': True,
                            'NPS School Group for Citizens of the World Charter School East Valley-0000001': True
                        }
                    }
                elif report == '8.1a':
                    form_input = {

                        'FromDate': '01/01/2000',
                        'ThrouDate': '06/30/2024',
                        'SchoolName': {

                            'Citizens of the World Charter School East Valley-0140749': True,
                            'NPS School Group for Citizens of the World Charter School East Valley-0000001': True
                        }
                    }

            elif school == 'WV':
                if report == '8.1':
                    form_input = {

                        'SchoolName': {

                            'Citizens of the World Charter School West Valley-0139832': True,
                            'NPS School Group for Citizens of the World Charter School West Valley-0000001': True
                        }
                    }
                elif report == '5.7':
                    form_input = {

                        'LEA': 'Citizens of the World Charter School Hollywood',
                        'School': {

                            'Citizens of the World Charter School Hollywood-0122556': True,
                            'NPS School Group for Citizens of the World Charter School Hollywood-0000001': True
                        }
                    }
                elif report == '8.1a':
                    form_input = {

                        'FromDate': '01/01/2000',
                        'ThrouDate': '06/30/2024',
                        'SchoolName': {

                            'Citizens of the World Charter School West Valley-0139832': True,
                            'NPS School Group for Citizens of the World Charter School West Valley-0000001': True
                        }
                    }

            cc.download_report(

                lea_code=lea[school],
                report_code=report,
                dry_run=False,
                form_data=form_input,
                file_name=f'/Users/cwcstaff/Library/CloudStorage/GoogleDrive-data@cwclosangeles.org/Shared drives/Data & Analytics/Source Docs/Exports and Downloads/CALPADS/For Tableau/{school} - {report}.csv',
                download_format='csv'

            )

if __name__ == '__main__':
    handler()