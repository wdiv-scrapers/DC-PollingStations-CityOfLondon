from gml_scraper import scrape


stations_url = "http://www.mapping2.cityoflondon.gov.uk/arcgis/services/INSPIRE/MapServer/WFSServer?request=GetFeature&version=1.1.0&service=wfs&typeNames=INSPIRE:UK_Parliamentary_General_Election_Polling_Places&srsName=EPSG%3A4326"
stations_fields = {
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}Address': 'Address',
}

districts_url = "http://www.mapping2.cityoflondon.gov.uk/arcgis/services/INSPIRE/MapServer/WFSServer?request=GetFeature&version=1.1.0&service=wfs&typeNames=INSPIRE:UK_Parliamentary_General_Election_Polling_Districts&srsName=EPSG%3A4326"
districts_fields = {
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}POLLING_DISTRICT': 'POLLING_DISTRICT',
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}GLA_CONSTITUENCY': 'GLA_CONSTITUENCY',
    '{http://localhost:6080/arcgis/services/INSPIRE/MapServer/WFSServer}UK_PARLIAMENTARY_CONSTITUENCY': 'UK_PARLIAMENTARY_CONSTITUENCY',
}

council_id = 'E09000001'


scrape(stations_url, council_id, 'stations', stations_fields, 'OBJECTID')
scrape(districts_url, council_id, 'districts', districts_fields, 'OBJECTID')
