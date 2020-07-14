from satsearch import Search
from felicette.utils.get_wrs import get_tiny_bbox
from felicette.utils.file_manager import save_to_file, data_file_exists

search = Search(
    bbox=get_tiny_bbox(85.8245, 20.2961),
    query={"eo:cloud_cover": {"lt": 10}, "collection": {"eq": "landsat-8-l1"}},
)
landsat_item = search.items()[0]


# save bands 2,3,4
band2_filename = landsat_item._data["id"] + "-b2.tiff"
if not data_file_exists(band2_filename):
    save_to_file(landsat_item.assets["B2"]["href"], band2_filename)
else:
    print("required data exists for {}".format(band2_filename))

band3_filename = landsat_item._data["id"] + "-b3.tiff"
if not data_file_exists(band3_filename):
    save_to_file(landsat_item.assets["B3"]["href"], band3_filename)
else:
    print("required data exists for {}".format(band3_filename))

band4_filename = landsat_item._data["id"] + "-b4.tiff"
if not data_file_exists(band4_filename):
    save_to_file(landsat_item.assets["B4"]["href"], band4_filename)
else:
    print("required data exists for {}".format(band4_filename))

