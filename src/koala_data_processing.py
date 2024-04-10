"""
Processing data from Koala Sighting API.
"""
import requests
from typing import Dict, List
from src.schemas import KoalaData


def query_koala_endpoint(where_query: str) -> Dict:
    """
    Queries the KoalaSighting endpoint using where_query and returns a raw result.
    :param where_query: defines the date range when a koala has been sighted.
    :return: data about different koala sightings
    """

    address = f"https://spatial-gis.information.qld.gov.au/arcgis/rest/services/QWise/CrocodileSightingsPublicView/FeatureServer/30/query?where={where_query}&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=%7B+%22wkid%22%3A4326+%7D&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=geojson"  # noqa E501
    res = requests.get(address)
    print(res.json())
    return res.json()


def flatten_koala_response(koala_response: Dict) -> List[KoalaData]:
    """
    Preprocessing of a koala sighting response data.
    :param koala_response: raw response from the koala sighting API.
    :return: flattening some nested dictionaries.
    """
    koala_array: List[KoalaData] = []
    for koala_point in koala_response["features"]:
        _properties = koala_point["properties"]
        _properties.pop("has_attachment", None)
        koala_array.append(
            {
                **_properties,
                "gis_x": koala_point["geometry"]["coordinates"][0],
                "gis_y": koala_point["geometry"]["coordinates"][1],
            }
        )
    return koala_array
