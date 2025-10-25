import React from 'react'
import DocsLayout from '../../layouts/DocsLayout'

export default function Geospatial() {
  return (
    <DocsLayout title="Phase: Geospatial">
      <p className="text-gray-700">We make maps and geospatial layers. Very simple English. Afghan survey examples.</p>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="plot-data">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>plot_data_on_map(df, lat_col, lon_col, popup_cols=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Plot points on an interactive map.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have locations (clinics, schools, camps) with lat/lon.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Quick view of where sites are.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>df</code>: Polars table with coordinates.</li>
          <li><code>lat_col</code>, <code>lon_col</code>: column names for latitude/longitude.</li>
          <li><code>popup_cols</code>: list of columns to show in popup bubble.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.plot_data_on_map import plot_data_on_map
import polars as pl

df = pl.DataFrame({"name":["Clinic A","Clinic B"], "lat":[34.5,34.3], "lon":[69.1,62.2]})
map_ = plot_data_on_map(df, lat_col="lat", lon_col="lon", popup_cols=["name"])  # returns a Folium map
map_.save("map_points.html")`}</code></pre>
        </div>
        <p className="text-gray-700 text-sm mt-2"><strong>Output:</strong> A Folium map object you can <code>save("file.html")</code>.</p>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="overlay-indicators">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>overlay_multiple_indicators_on_map(df, lat_col, lon_col, indicators, popup_cols=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Show multiple indicators as circle markers.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You want to compare values like in_need and reached at sites.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> See intensity by size/color on map.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>df</code>: Polars table with <code>lat_col</code>, <code>lon_col</code>.</li>
          <li><code>indicators</code>: list of numeric columns to overlay.</li>
          <li><code>popup_cols</code>: extra fields to show when clicked.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.overlay_multiple_indicators_on_map import overlay_multiple_indicators_on_map
import polars as pl

df = pl.DataFrame({
  "name":["Site1","Site2"], "lat":[34.5,34.7], "lon":[69.1,69.2],
  "in_need":[200,500], "reached":[120,300]
})
map_ = overlay_multiple_indicators_on_map(df, "lat", "lon", indicators=["in_need","reached"], popup_cols=["name"])
map_.save("map_indicators.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="choropleth">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>choropleth_maps_by_region(geojson_path, df, region_key, value_col)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Fill provinces/districts by color (value).</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have province values like severity rate or coverage %.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Understand spatial variation quickly.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>geojson_path</code>: GeoJSON file with region polygons.</li>
          <li><code>df</code>: table with a region column and a numeric value column.</li>
          <li><code>region_key</code>: column matching the GeoJSON property (like province name).</li>
          <li><code>value_col</code>: numeric column to color by.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.choropleth_maps_by_region import choropleth_maps_by_region
import polars as pl

df = pl.DataFrame({"province":["Kabul","Herat"], "rate":[20.5,15.0]})
map_ = choropleth_maps_by_region("data/afg_provinces.geojson", df, region_key="province", value_col="rate")
map_.save("map_choropleth.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="heatmap">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>heatmap_crisis_intensity(df, lat_col, lon_col, intensity_col)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Heatmap using intensity values.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Values are dense at hotspots (e.g., reports, cases).</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> See clusters and hotspots immediately.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>lat_col</code>, <code>lon_col</code>: coordinates columns.</li>
          <li><code>intensity_col</code>: numeric weight per point.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.heatmap_crisis_intensity import heatmap_crisis_intensity
import polars as pl

df = pl.DataFrame({"lat":[34.5,34.7], "lon":[69.1,69.2], "score":[5,10]})
map_ = heatmap_crisis_intensity(df, "lat", "lon", "score")
map_.save("map_heat.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="cluster-facilities">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>cluster_humanitarian_facilities(df, lat_col, lon_col, name_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Group nearby facilities into clusters.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Many sites are close; map gets crowded.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Clean map, better UX, expand clusters to see members.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>name_col</code>: optional label for popups.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.cluster_humanitarian_facilities import cluster_humanitarian_facilities
import polars as pl

df = pl.DataFrame({"name":["Clinic A","Clinic B"], "lat":[34.5,34.5005], "lon":[69.1,69.1005]})
map_ = cluster_humanitarian_facilities(df, "lat", "lon", name_col="name")
map_.save("map_facilities.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="buffers">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>generate_buffer_zones(df, lat_col, lon_col, distance_meters)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Draw circle buffers (e.g., 500m) around points.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You need coverage zones around facilities.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Visualize service radius or risk zones.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>distance_meters</code>: radius in meters (example: 500).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.generate_buffer_zones import generate_buffer_zones
import polars as pl

df = pl.DataFrame({"name":["Site1"], "lat":[34.5], "lon":[69.1]})
map_ = generate_buffer_zones(df, "lat", "lon", distance_meters=500)
map_.save("map_buffer.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="hazards">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>visualize_hazard_areas(geojson_or_df, hazard_type_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Show polygons representing hazard areas.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You have flood zones, landslide areas, etc.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Risk communication and planning.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>geojson_or_df</code>: GeoJSON path or compatible table.</li>
          <li><code>hazard_type_col</code>: optional column to style by type.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.visualize_hazard_areas import visualize_hazard_areas
# See module docstring for details; pass GeoJSON path or a table as supported.`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="camps">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>display_refugee_camp_locations(df, lat_col, lon_col, name_col=None)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Show refugee/IDP camp points.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Camp coordinates available from partners.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Planning and coordination.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>name_col</code>: optional column for camp name in popup.</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.display_refugee_camp_locations import display_refugee_camp_locations
import polars as pl

df = pl.DataFrame({"camp":["Camp A"], "lat":[34.4], "lon":[69.2]})
map_ = display_refugee_camp_locations(df, "lat", "lon", name_col="camp")
map_.save("map_camps.html")`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="conflict-zones">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>conflict_zones_polygons(geojson_or_df, level="district")</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Draw polygons to show conflict zones.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> Conflict extent is provided per district/province.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Situation awareness and analysis.</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>geojson_or_df</code>: polygons source.</li>
          <li><code>level</code>: area level (e.g., <code>"district"</code>).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.conflict_zones_polygons import conflict_zones_polygons
# See module docstring for usage based on your inputs.`}</code></pre>
        </div>
      </section>

      <section className="mt-8 rounded-lg border border-gray-200 bg-white p-5" id="osm">
        <div className="flex items-center gap-2 text-base font-semibold text-gray-900 mb-2">
          <span>connect_with_openstreetmap(bbox, tags)</span>
        </div>
        <p className="text-gray-700 text-sm"><strong>What:</strong> Fetch OSM features (roads, clinics, schools) by bounding box and tags.</p>
        <p className="text-gray-700 text-sm"><strong>When:</strong> You need base features to enrich your map.</p>
        <p className="text-gray-700 text-sm"><strong>Why:</strong> Free global data source (OpenStreetMap).</p>
        <h3 className="text-sm font-semibold mt-3">Parameters</h3>
        <ul className="text-sm text-gray-700 list-disc pl-6">
          <li><code>bbox</code>: (south, west, north, east) tuple.</li>
          <li><code>tags</code>: dict filter (example: <code>{`{"amenity": "clinic"}`}</code>).</li>
        </ul>
        <div className="relative mt-2">
          <pre className="rounded-md bg-gray-900 text-gray-100 p-3 overflow-auto"><code>{`# Python
from huda.geospatial.connect_with_openstreetmap import connect_with_openstreetmap

bbox = (34.2, 69.0, 34.8, 69.5)  # south, west, north, east for Kabul area
features = connect_with_openstreetmap(bbox=bbox, tags={"amenity": "clinic"})
print(features)`}</code></pre>
        </div>
      </section>
    </DocsLayout>
  )
}
