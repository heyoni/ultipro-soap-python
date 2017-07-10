from zeep import Client as Zeep
from zeep import xsd

endpoint = '/EmployeePerson?wsdl'

def find_people(client, query):
    zeep_client = Zeep(client.base_url + endpoint)
    response = zeep_client.service.FindPeople(
        _soapheaders=[client.session_header],
        query=query)

    return response

def get_person_by_employee_identifier(client, employee_identifier):
    zeep_client = Zeep(client.base_url + endpoint)
    if 'EmployeeNumber' in employee_identifier:
        element = zeep_client.get_element('ns6:EmployeeNumberIdentifier')
        obj = element(**employee_identifier)
    elif 'EmailAddress' in employee_identifier:
        element = zeep_client.get_element('ns6:EmailAddressIdentifier')
        obj = element(**employee_identifier)

    response = zeep_client.service.GetPersonByEmployeeIdentifier(
        _soapheaders=[client.session_header],
        employeeIdentifier=obj)

    return response['Results']['Person'][0]
