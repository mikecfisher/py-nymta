"""Constants for MTA GTFS-RT library."""

# MTA GTFS-RT feed URLs for subway
FEED_URLS = {
    "1": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "A": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    "N": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
    "B": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
    "L": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l",
    "SI": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si",
    "G": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g",
    "J": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz",
}

# MTA Static GTFS feed URLs (https://www.mta.info/developers; S3 bucket since ~2025)
_STATIC_GTFS_BASE = "https://rrgtfsfeeds.s3.amazonaws.com"
STATIC_GTFS_URLS = {
    "subway": f"{_STATIC_GTFS_BASE}/gtfs_subway.zip",
    "bus_bronx": f"{_STATIC_GTFS_BASE}/gtfs_bx.zip",
    "bus_brooklyn": f"{_STATIC_GTFS_BASE}/gtfs_b.zip",
    "bus_manhattan": f"{_STATIC_GTFS_BASE}/gtfs_m.zip",
    "bus_queens": f"{_STATIC_GTFS_BASE}/gtfs_q.zip",
    "bus_staten_island": f"{_STATIC_GTFS_BASE}/gtfs_si.zip",
    # MTA Bus Company routes (e.g. Q18, Q52+, BxM1, QM2) are not in the NYCT borough feeds
    "bus_company": f"{_STATIC_GTFS_BASE}/gtfs_busco.zip",
}

# Static GTFS feeds searched for bus routes and stop names, as (feed_name, url) tuples
BUS_STATIC_GTFS_FEEDS = [
    (name, STATIC_GTFS_URLS[name])
    for name in (
        "bus_bronx",
        "bus_brooklyn",
        "bus_manhattan",
        "bus_queens",
        "bus_staten_island",
        "bus_company",
    )
]

# MTA GTFS-RT feed URLs for buses
# Note: These require an API key as a query parameter
BUS_FEED_URLS = {
    "trip_updates": "https://gtfsrt.prod.obanyc.com/tripUpdates",
    "vehicle_positions": "https://gtfsrt.prod.obanyc.com/vehiclePositions",
    "alerts": "https://gtfsrt.prod.obanyc.com/alerts",
}

# Mapping of subway lines to feed IDs
LINE_TO_FEED = {
    # Feed 1: 1, 2, 3, 4, 5, 6, 7, GS (Grand Central Shuttle)
    "1": "1",
    "2": "1",
    "3": "1",
    "4": "1",
    "5": "1",
    "6": "1",
    "7": "1",
    "GS": "1",
    # Feed A: A, C, E, H (Rockaway Shuttle)
    "A": "A",
    "C": "A",
    "E": "A",
    "H": "A",
    # Feed N: N, Q, R, W
    "N": "N",
    "Q": "N",
    "R": "N",
    "W": "N",
    # Feed B: B, D, F, M, FS (Franklin Av Shuttle)
    "B": "B",
    "D": "B",
    "F": "B",
    "M": "B",
    "FS": "B",
    # Feed L: L
    "L": "L",
    # Feed SI: SIR (Staten Island Railway)
    "SI": "SI",
    # Feed G: G
    "G": "G",
    # Feed J: J, Z
    "J": "J",
    "Z": "J",
}
