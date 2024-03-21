import requests
from typing import Dict, Optional, List
from dataclasses import dataclass


address = "https://spatial-gis.information.qld.gov.au/arcgis/rest/services/QWise/CrocodileSightingsPublicView/FeatureServer/30/query?where=sighttime+%3E+CURRENT_TIMESTAMP+-+INTERVAL+%271%27+DAY&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=%7B+%22wkid%22%3A4326+%7D&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=geojson"


@dataclass
class KoalaData:
    objectid: int
    globalid: str
    sighttime: int
    joeypresent: Optional[str]
    numberofkoala: Optional[int]
    koalacondifinal: Optional[str]
    locality: Optional[str]
    near_koala_habitat: Optional[str]
    attachment_cc_lic_check: Optional[str]
    lga: Optional[str]
    sighting_lat_wgs84: Optional[float]
    sighting_long_wgs84: Optional[float]
    vetting_code: Optional[str]
    gis_x: float
    gis_y: float


def query_koala_endpoint() -> Dict:
    res = requests.get(address)
    print(res.json())
    return res.json()


def flatten_koala_response(koala_response: Dict) -> List[KoalaData]:
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


if __name__ == "__main__":
    res = query_koala_endpoint()
    print(flatten_koala_response(res))
