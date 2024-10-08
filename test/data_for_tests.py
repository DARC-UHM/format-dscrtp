"""
Sample data to use for tests. Do not alter this file unless you are prepared to rewrite all of the test cases :)
"""

annotations = [
    # annotations[0]
    {
        "observation_uuid": "0059f860-4799-485f-c06c-5830e5ddd31e",
        "concept": "Chaceon quinquedens",
        "observer": "NikkiCunanan",
        "observation_timestamp": "2022-11-17T21:26:14.245Z",
        "video_reference_uuid": "cd74c489-6336-4b97-89a6-f151872f282b",
        "imaged_moment_uuid": "aa7c743e-99ba-4b65-c16c-aeb3585dc91e",
        "elapsed_time_millis": 0,
        "recorded_timestamp": "2014-09-05T20:06:26Z",
        "group": "ROV",
        "associations": [
            {
                "uuid": "08f0563b-090e-417e-0e68-c314fb69d41e",
                "link_name": "s1",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "c4eaa100-4bee-46a9-0f65-6525fb69d41e",
                "link_name": "upon",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "b860c165-078e-4715-8bc3-491039679b67",
                "link_name": "bounding box",
                "to_concept": "self",
                "link_value": "{\"x\":504,\"y\":389,\"width\":109,\"height\":112,\"generator\":\"VARS Annotation\"}",
                "mime_type": "application/json"
            },
        ],
        "ancillary_data": {
            "altitude": 1.899999976158142,
            "depth_meters": 668.458984375,
            "latitude": 38.793148973388,
            "oxygen_ml_l": 7.3196001052856445,
            "salinity": 35.864898681640625,
            "temperature_celsius": 5.125999927520752,
            "uuid": "b5bdfa60-9b20-40c4-6462-9d4db9b3d41e"
        }
    },
    # annotations[1]
    {
        "observation_uuid": "0d9133d7-1d49-47d5-4b6d-6e4fb25dd41e",
        "concept": "Paralepididae",
        "observer": "MeaganPutts",
        "observation_timestamp": "2022-10-07T00:58:25.675Z",
        "video_reference_uuid": "9cb8f6cd-9720-4f51-aaac-4d7da1dec55a",
        "imaged_moment_uuid": "e602a14b-1a55-4451-4a6d-6e4fb25dd41e",
        "elapsed_time_millis": 6751855,
        "recorded_timestamp": "2014-09-05T14:37:57.855Z",
        "group": "ROV",
        "activity": "cruise",
        "associations": [
            {
                "uuid": "18bb6ed0-92b2-4f58-4c6d-6e4fb25dd41e",
                "link_name": "s1",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "a1c3990e-3566-4832-4d6d-6e4fb25dd41e",
                "link_name": "s2",
                "to_concept": "mantra",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d37d482e-5d56-4267-786b-0dfb525bd41e",
                "link_name": "occurrence-remark",
                "to_concept": "nil",
                "link_value": "in water column on descent",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d37d482e-5d56-4267-786b-0dfb525bd41e",
                "link_name": "occurrence-remark",
                "to_concept": "nil",
                "link_value": "another remark",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8c46c0fc-28d9-47e6-9a62-94e36b3adb1e",
                "link_name": "size",
                "to_concept": "50-100 cm",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "37c87be6-8b2c-436c-8b6a-fc0f42d2db1e",
                "link_name": "sampled-by",
                "to_concept": "manipulator",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "ae29252c-325d-43ce-b263-ce0d41c7d81e",
                "link_name": "habitat-comment",
                "to_concept": "nil",
                "link_value": "loose talus",
                "mime_type": "text/plain"
            },
        ],
        "image_references": [],
        "ancillary_data": {
            "altitude": 1.899999976158142,
            "depth_meters": 668.458984375,
            "latitude": 38.793148973388,
            "longitude": -72.992393976812,
            "oxygen_ml_l": 7.3196001052856445,
            "salinity": 35.864898681640625,
            "temperature_celsius": 5.125999927520752,
            "uuid": "b5bdfa60-9b20-40c4-6462-9d4db9b3d41e"
        }
    },
    # annotations[2]
    {
        "observation_uuid": "080118db-baa2-468a-d06a-144249c1d41e",
        "concept": "Etmopteridae",
        "observer": "MeaganPutts",
        "observation_timestamp": "2022-10-14T23:04:45.429Z",
        "video_reference_uuid": "88d0a6fa-0fac-48a7-a200-d50f0924c0c5",
        "imaged_moment_uuid": "67b21aab-9fcb-4342-0160-1c4249c1d41e",
        "elapsed_time_millis": 7028345,
        "recorded_timestamp": "2014-09-20T14:13:23.345Z",
        "group": "ROV",
        "activity": "cruise",
        "associations": [
            {
                "uuid": "1cc0aa4a-36e4-4eec-0261-b69749c1d41e",
                "link_name": "s1",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "204a46b5-8efa-47b9-a56d-22b149c1d41e",
                "link_name": "identity-certainty",
                "to_concept": "self",
                "link_value": "maybe",
                "mime_type": "text/plain"
            },
            {
                "uuid": "66f74ac5-12c5-4b50-9367-30a049c1d41e",
                "link_name": "s2",
                "to_concept": "bou",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "7dbddb7d-0442-470e-e46a-1ea549c1d41e",
                "link_name": "s2",
                "to_concept": "bed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "faf820ac-93fd-4d5a-486a-87775ec1d41e",
                "link_name": "s2",
                "to_concept": "bed",
                "link_value": "nil",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [],
        "ancillary_data": {
            "altitude": 2.299999952316284,
            "latitude": 39.023365743777,
            "longitude": -72.448741878402,
            "oxygen_ml_l": 8.13640022277832,
            "salinity": 34.951900482177734,
            "temperature_celsius": 3.8610000610351562,
            "uuid": "5b9fd45e-a771-4ae2-4c6c-8cd75f66d71e"
        }
    },
    # annotations[3]
    {
        "observation_uuid": "35aa2bb9-d067-419b-9a6e-09cdce8ed41e",
        "concept": "Demospongiae encrusting",
        "observer": "MeaganPutts",
        "observation_timestamp": "2022-10-10T22:43:14.208Z",
        "video_reference_uuid": "9888ccf0-22d7-40a1-9dc6-70e029c45155",
        "imaged_moment_uuid": "74c08709-b3ab-43d0-bb6c-0ecdce8ed41e",
        "elapsed_time_millis": 3995082,
        "recorded_timestamp": "2014-09-06T13:35:03.082Z",
        "group": "ROV",
        "activity": "cruise",
        "associations": [
            {
                "uuid": "297d23d7-5979-46e7-6f66-8f1fcf8ed41e",
                "link_name": "upon",
                "to_concept": "bed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "954b0835-ca6d-4180-1d6f-4ee4ce8ed41e",
                "link_name": "s2",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "cd581243-bdfb-469e-dc6a-b9dbce8ed41e",
                "link_name": "s1",
                "to_concept": "bed",
                "link_value": "nil",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [],
        "ancillary_data": {
            "altitude": 1.600000023841858,
            "depth_meters": 639.4940185546875,
            "latitude": 37.410213069179,
            "longitude": -74.464855305838,
            "oxygen_ml_l": 7.184100151062012,
            "salinity": 35.87260055541992,
            "temperature_celsius": 5.309000015258789,
            "uuid": "855dc798-961a-460f-886e-f53bbbb3d41e"
        }
    },
    # annotations[4]
    {
        "observation_uuid": "673754bb-81c7-4866-8362-1dfc4e5bd41e",
        "concept": "none",
        "observer": "MeaganPutts",
        "observation_timestamp": "2022-10-06T20:24:56.933Z",
        "video_reference_uuid": "9cb8f6cd-9720-4f51-aaac-4d7da1dec55a",
        "imaged_moment_uuid": "7cea8785-2b33-4c96-a460-22fc4e5bd41e",
        "elapsed_time_millis": 4017817,
        "recorded_timestamp": "2014-09-05T13:52:23.817Z",
        "group": "ROV",
        "activity": "descend",
        "associations": [
            {
                "uuid": "02dd535d-84fb-47a2-d56a-e674505bd41e",
                "link_name": "occurrence-remark",
                "to_concept": "nil",
                "link_value": "bottom in sight",
                "mime_type": "text/plain"
            },
            {
                "uuid": "aa6c0f9d-2794-4e0d-8d6d-389e545bd41e",
                "link_name": "s1",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "b503cd40-bfb5-4f35-076a-a1a7515bd41e",
                "link_name": "megahabitat",
                "to_concept": "continental shelf",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "e6b76818-4f08-4e43-166f-0e21515bd41e",
                "link_name": "habitat",
                "to_concept": "canyon",
                "link_value": "nil",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [],
        "ancillary_data": {
            "altitude": 3.299999952316284,
            "depth_meters": 669.0770263671875,
            "latitude": 38.793091602349,
            "longitude": -72.992535573368,
            "uuid": "173228c6-acad-4bd1-5d62-9d4db9b3d41e"
        }
    },
    # annotations[5]
    {
        "observation_uuid": "034e6380-f1d0-4e16-c86d-32c7e15dd41e",
        "concept": "Cyclothone sp",
        "observer": "MeaganPutts",
        "observation_timestamp": "2022-10-07T01:19:38.153Z",
        "video_reference_uuid": "9cb8f6cd-9720-4f51-aaac-4d7da1dec55a",
        "imaged_moment_uuid": "953c9cc7-d3a6-4182-c76d-32c7e15dd41e",
        "elapsed_time_millis": 8214963,
        "recorded_timestamp": "2014-09-05T15:02:20.963Z",
        "group": "ROV",
        "activity": "cruise",
        "associations": [
            {
                "uuid": "34f6e28b-d09c-42bb-3b66-a8cfe15dd41e",
                "link_name": "population-quantity",
                "to_concept": "self",
                "link_value": "2",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8b583938-0f2b-41a4-c96d-32c7e15dd41e",
                "link_name": "s1",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d2eb3cb2-b04b-4af9-ca6d-32c7e15dd41e",
                "link_name": "identity-certainty",
                "to_concept": "self",
                "link_value": "maybe",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [],
    },
    # annotations[6]
    {
        "observation_uuid": "eb288157-9e2c-4fcf-1863-3c2be5ddd31e",
        "concept": "Nemichthys scolopaceus cf",
        "observer": "NikkiCunanan",
        "observation_timestamp": "2022-11-17T21:26:14.245Z",
        "video_reference_uuid": "cd74c489-6336-4b97-89a6-f151872f282b",
        "imaged_moment_uuid": "cb776b90-8d21-4412-076c-7750ad58ca1e",
        "elapsed_time_millis": 0,
        "recorded_timestamp": "2014-09-05T13:50:40Z",
        "group": "ROV",
        "associations": [
            {
                "uuid": "46c6ec04-ed4c-4f16-496c-839f535bd41e",
                "link_name": "guide-photo",
                "to_concept": "1 best",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "5c5888ce-99e1-4125-0162-597a0bdfd31e",
                "link_name": "identity-certainty",
                "to_concept": "self",
                "link_value": "small head; long ribbon body",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d37d482e-5d56-4267-786b-0dfb525bd41e",
                "link_name": "occurrence-remark",
                "to_concept": "nil",
                "link_value": "in water column on descent",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [
            {
                "uuid": "7eaf9918-344f-4be0-486a-cf50ad58ca1e",
                "description": "imported image",
                "url": "http://hurlstor.soest.hawaii.edu/imagearchive/SupplementalPhotos/D2photos/EX1404photos/EX1404L2_DIVE01_20140905/EX1404L2_IMG_20140905T135040Z_ROVHD_NICE_EEL_BOTTOM.png"
            }
        ],
        "ancillary_data": {
            "altitude": 26.5,
            "depth_meters": 646.5650024414062,
            "latitude": 38.793034716155,
            "longitude": -72.99254911661,
            "oxygen_ml_l": 7.321300029754639,
            "salinity": 35.86949920654297,
            "temperature_celsius": 5.182499885559082,
            "uuid": "1533fda8-4180-478f-606a-a867b9b3d41e"
        }
    },
    # annotations[7]
    {
        "observation_uuid": "24e9a5d5-b65e-4926-ee65-30cad2bcda1e",
        "concept": "Trissopathes sp",
        "observer": "MeaganPutts",
        "observation_timestamp": "2023-02-24T01:20:58.388Z",
        "video_reference_uuid": "48229df3-0f41-43f8-8ec4-605c3314943d",
        "imaged_moment_uuid": "8cba8d06-bf4d-4580-ef65-30cad2bcda1e",
        "recorded_timestamp": "2021-11-30T09:07:25Z",
        "associations": [
            {
                "uuid": "2bcd2b8d-c5f2-4b99-b069-cc29183edb1e",
                "link_name": "upon",
                "to_concept": "bedbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "44c371ee-ba03-4c00-cf65-611cf4d4db1e",
                "link_name": "categorical-abundance",
                "to_concept": "self",
                "link_value": "\u003e100",
                "mime_type": "text/plain"
            },
            {
                "uuid": "b5f0ca93-4800-43cf-1f6f-da05183edb1e",
                "link_name": "s2",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "cc9f2172-03f1-4077-5e6e-06ff173edb1e",
                "link_name": "s2",
                "to_concept": "cobbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d8adca83-411c-4f31-5c62-6ef3173edb1e",
                "link_name": "s1",
                "to_concept": "bedbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "e1219ef3-36c2-4902-cd6a-72f9173edb1e",
                "link_name": "s2",
                "to_concept": "boubmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8c46c0fc-28d9-47e6-9a62-94e36b3adb1e",
                "link_name": "size",
                "to_concept": "51000000 cm",  # to fail
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "6cbe7784-92b5-414a-cd66-6c303b96db1e",
                "link_name": "condition-comment",
                "to_concept": "self",
                "link_value": "damaged",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [
            {
                "uuid": "be9e0179-5fbc-4309-c061-50cad2bcda1e",
                "description": "imported image",
                "url": "https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130090725.png"
            }
        ],
        "ancillary_data": {
            "depth_meters": 1861.291015625,
            "latitude": 23.83022078,
            "longitude": -172.817877,
            "oxygen_ml_l": 2.172351121902466,
            "salinity": 34.588722229003906,
            "temperature_celsius": 2.1976208686828613,
            "uuid": "0dc42ad6-ca57-44f7-7e69-e2adba9adc1e"
        }
    },
    # annotations[8]
    {
        "observation_uuid": "26d38322-b92b-4211-596d-24bed2bcda1e",
        "concept": "Trissopathes sp",
        "observer": "MeaganPutts",
        "observation_timestamp": "2023-02-23T18:29:34.133Z",
        "video_reference_uuid": "48229df3-0f41-43f8-8ec4-605c3314943d",
        "imaged_moment_uuid": "0fe852fe-3699-494a-5a6d-24bed2bcda1e",
        "recorded_timestamp": "2021-11-30T08:07:00Z",
        "activity": "stationary",
        "associations": [
            {
                "uuid": "24b22532-ed27-463e-966c-cac8c54ddd1e",
                "link_name": "population-density",
                "to_concept": "self",
                "link_value": "dense",
                "mime_type": "text/plain"
            },
            {
                "uuid": "2d51a65b-3fe0-46f1-586b-e3cb6b3adb1e",
                "link_name": "s2",
                "to_concept": "cobbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "604c3e40-1ac9-42ba-bb67-32f86b3adb1e",
                "link_name": "upon",
                "to_concept": "bedbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8c46c0fc-28d9-47e6-9a62-94e36b3adb1e",
                "link_name": "size",
                "to_concept": "50-100 cm",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8f0ad450-04b3-447a-0768-f5c66b3adb1e",
                "link_name": "s2",
                "to_concept": "boubmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8fd64fc9-c9f0-493d-7c6f-9f136c3adb1e",
                "link_name": "identity-reference",
                "to_concept": "self",
                "link_value": "20",
                "mime_type": "text/plain"
            },
            {
                "uuid": "9bca3c04-2ddf-4140-d662-0cc26b3adb1e",
                "link_name": "s1",
                "to_concept": "fail s1",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "f7de4fc4-6a42-450c-fd61-b5490cd5db1e",
                "link_name": "s2",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "6cbe7784-92b5-414a-cd66-6c303b96db1e",
                "link_name": "condition-comment",
                "to_concept": "self",
                "link_value": "dead",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [
            {
                "uuid": "5c5c759c-f71d-4ed0-1b62-42bed2bcda1e",
                "description": "imported image",
                "url": "https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130080700.png"
            }
        ],
        "ancillary_data": {
            "depth_meters": 1908.455322265625,
            "latitude": 23.8309845,
            "longitude": -172.8196795,
            "oxygen_ml_l": 2.2894139289855957,
            "salinity": 34.598243713378906,
            "temperature_celsius": 2.0848000049591064,
            "uuid": "5479105b-966c-4685-4162-e0adba9adc1e"
        }
    },
    # annotations[9]
    {
        "observation_uuid": "42c8308b-a92b-4105-c86a-9affd2bcda1e",
        "concept": "Narella sp",
        "observer": "MeaganPutts",
        "observation_timestamp": "2023-03-07T20:08:12.815Z",
        "video_reference_uuid": "48229df3-0f41-43f8-8ec4-605c3314943d",
        "imaged_moment_uuid": "a4a0e81b-d708-477d-c96a-9affd2bcda1e",
        "recorded_timestamp": "2021-11-30T14:57:09Z",
        "associations": [
            {
                "uuid": "0e92de19-a916-4dd0-ac60-b0c13cd2db1e",
                "link_name": "s2",
                "to_concept": "cobbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "2dd08980-c115-44b4-1e64-cce13cd2db1e",
                "link_name": "size",
                "to_concept": "30-50 cm",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "37c87be6-8b2c-436c-8b6a-fc0f42d2db1e",
                "link_name": "sampled-by",
                "to_concept": "manipulator",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "77f0d246-c814-4f4e-1768-44d740d2db1e",
                "link_name": "identity-reference",
                "to_concept": "self",
                "link_value": "51",
                "mime_type": "text/plain"
            },
            {
                "uuid": "7f46cf73-52e9-4899-eb63-78bb3cd2db1e",
                "link_name": "s2",
                "to_concept": "boubmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8e86307e-981b-4762-4063-c1f33ed2db1e",
                "link_name": "upon",
                "to_concept": "some creature",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "b364e693-a038-41a3-3a6d-1bb53cd2db1e",
                "link_name": "s1",
                "to_concept": "bedbmn",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "c3349bc4-3ff8-45ff-5d69-5ac83cd2db1e",
                "link_name": "s2",
                "to_concept": "sed",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "ff4c7d94-dc87-4454-0a62-e90f42d2db1e",
                "link_name": "sample-reference",
                "to_concept": "self",
                "link_value": "NA134-158-B-MCZ",
                "mime_type": "text/plain"
            }
        ],
        "image_references": [
            {
                "uuid": "a6b2a9d5-e305-48f0-9a66-baffd2bcda1e",
                "description": "imported image",
                "url": "https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130145709.png"
            },
            {
                "uuid": "a6b2a9d5-e305-48f0-9a66-baffd2bcda1e",
                "description": "imported image",
                "url": "https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130145709.jpg"
            }
        ],
        "ancillary_data": {
            "depth_meters": 1883.022705078125,
            "latitude": 23.83036,
            "longitude": -172.8159502,
            "oxygen_ml_l": 2.3752732276916504,
            "salinity": 34.60392379760742,
            "temperature_celsius": 2.0179998874664307,
            "uuid": "b26af95a-7dac-42a9-8e62-e0adba9adc1e"
        }
    },
    # annotations[10]
    {
        "observation_uuid": "b8e6c95b-3846-41f9-706e-f8c1b905c91e",
        "concept": "Plectranthias sp",
        "observer": "Virginia Moriwake",
        "observation_timestamp": "2016-03-12T00:03:32.963Z",
        "video_reference_uuid": "9d48bd89-6830-4482-abf3-7ab5acb2abe9",
        "imaged_moment_uuid": "8ef1c852-cf4b-4e7d-6f6e-f8c1b905c91e",
        "timecode": "01:31:49:16",
        "elapsed_time_millis": 0,
        "recorded_timestamp": "2005-07-21T00:18:02Z",
        "duration_millis": 0,
        "activity": "stationary",
        "associations": [
            {
                "uuid": "60f1afc8-65c3-4109-736e-f8c1b905c91e",
                "link_name": "identity-certainty",
                "to_concept": "self",
                "link_value": "maybe; banded",
                "mime_type": "text/plain"
            },
            {
                "uuid": "6fb829a8-7c89-421f-756e-f8c1b905c91e",
                "link_name": "slope",
                "to_concept": "slp2-3",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8c619257-b5c1-48a7-776e-f8c1b905c91e",
                "link_name": "observation notes",
                "to_concept": "self",
                "link_value": "363;;",
                "mime_type": "text/plain"
            },
            {
                "uuid": "985b9fc8-3001-4538-746e-f8c1b905c91e",
                "link_name": "photo-reference",
                "to_concept": "self",
                "link_value": "http://max5kn1.soest.hawaii.edu/imagearchive/SupplementalPhotos/P5photos/P5-653/P5-653-042.tif;P5-653-d3-13238a1.tif;P5-653-d3-13238a2.tif",
                "mime_type": "text/plain"
            },
            {
                "uuid": "d0c16531-488f-4e30-716e-f8c1b905c91e",
                "link_name": "s1",
                "to_concept": "bedl",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "dea99b18-9289-4ce5-766e-f8c1b905c91e",
                "link_name": "rugosity",
                "to_concept": "rs1-5",
                "link_value": "nil",
                "mime_type": "text/plain"
            },
            {
                "uuid": "fe1e3d9f-b4e3-4885-726e-f8c1b905c91e",
                "link_name": "habitat-comment",
                "to_concept": "nil",
                "link_value": "karstic",
                "mime_type": "text/plain"
            },
            {
                "uuid": "8fd64fc9-c9f0-493d-7c6f-9f136c3adb1e",
                "link_name": "identity-reference",
                "to_concept": "self",
                "link_value": "",  # this is a test (blank link val for id ref)
                "mime_type": "text/plain"
            }
        ],
        "image_references": [],
        "ancillary_data": {
            "depth_meters": 364.2099914550781,
            "latitude": -0.3766116666666666,
            "longitude": -160.0200645,
            "uuid": "f443328e-88a5-4b20-8762-c2c5b905c91e"
        }
    }
]

no_match = {"to_concept": "nomatch"}

list_data = [
    'Deep_Discoverer_14040203_00:33:49',
    'b4f72dce-847f-4c44-3d67-9c03dd01d41e',
    '',
    'NOAA Office of Ocean Exploration and Research | University of Hawaii Deep-sea Animal Research Center',
    'Brosme brosme',
    'NA',
    'NA',
    'Species',
    126447,
    'urn:lsid:marinespecies.org:taxname:126447',
    'Chordata',
    'Teleostei',
    'NA',
    'Gadiformes',
    'NA',
    'Lotidae',
    'NA',
    'Brosme',
    'NA',
    'Brosme brosme',
    'NA',
    '(Ascanius, 1772)',
    'NA',
    'Brosme brosme',
    'NA',
    'NA',
    'Cunanan, Nikki',
    '2022-11-17',
    'ID by expert from video',
    1, 'North Atlantic',
    'Northeast U.S. Continental Shelf',
    'USA',
    'New England',
    'U.S. Atlantic Continental Margin | Northeast Canyons | Norfolk Canyon',
    37.024100313941,
    -74.601851271556,
    496.522,
    'reported',
    496.522,
    496.522,
    'NA',
    '2014-09-08',
    '00:33:49',
    'EX1404L2',
    'Okeanos Explorer',
    'NA',
    'NA',
    'Deep Water Exploration of the Northeast U.S. Canyons and Seamounts to document biodiversisty and identify hot spots',
    'NA',
    'D2-EX1404L2-03',
    'D2-EX1404L2-03',
    'ROV',
    'Deep Discoverer',
    -999,
    'NA',
    'NA',
    '1',
    'NA',
    -999,
    -999,
    'NA',
    -999,
    -999,
    -999,
    'Live',
    'NA',
    'video not available',
    '',
    'USBL',
    'CTD',
    'NA',
    'bedrock',
    'continental shelf, canyon',
    6.3024,
    35.918,
    4.4171922249572875,
    'video observation',
    'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/D2photos/EX1404photos/EX1404L2_DIVE03_20140907/EX1404L2_IMG_20140908T003349Z_ROVHD_COR.png',
    'NA',
    'NOAA Office of Ocean Exploration and Research; University of Hawaiʻi',
    'Bingo, Sarah; sarahr6@hawaii.edu',
    '2023-03-07',
    'https://www.ncei.noaa.gov/waf/okeanos-rov-cruises/ex1404l2/ | https://www.ncei.noaa.gov/waf/okeanos-rov-cruises/ex1404l3/',
    'NA',
    'Bingo, Sarah',
    'sarahr6@hawaii.edu',
    'NA',
    'NA',
    -1,
    False,
    'NA',
]

taxon_rank_no_match = {
    'Superdomain': 'Biota',
    'Kingdom': 'Animalia',
    'Phylum': 'Chordata',
    'Subphylum': 'Vertebrata',
    'Infraphylum': 'Gnathostomata',
    'Parvphylum': 'Osteichthyes',
    'Gigaclass': 'Actinopterygii',
    'Superclass': 'Actinopteri',
    'Class': 'Teleostei',
    'Order': 'Anguilliformes',
    'Family': 'Nemichthyidae',
    'Genus': 'Nemichthys',
    'Species': 'cf. scolopaceus'
}

taxon_rank_match = {
    'Superdomain': 'Biota',
    'Kingdom': 'Animalia',
    'Phylum': 'Cnidaria',
    'Class': 'Anthozoa',
    'Subclass': 'Hexacorallia',
    'Order': 'Scleractinia',
    'Family': 'Caryophylliidae',
    'Genus': 'Desmophyllum',
    'Species': 'Desmophyllum dianthus'
}

sample_report_records = [
    ['Hercules_1341885_08:13:43', '5a0802e6-5010-4667-0f64-7898734fd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiuroidea', 'NA',
     'brittle stars | brittlestars', 'Class', 123084, 'urn:lsid:marinespecies.org:taxname:123084', 'Echinodermata',
     'Ophiuroidea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1840', 'NA', 'Ophiuroidea', 'NA', 'NA',
     'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260715, -172.7583542, 2991.719, 'reported', 2991.719, 2991.719, 'NA', '2021-11-20', '08:13:43', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5742, 34.6533, 2.3545, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'b44c0798-73e5-49c3-a42c-7470a06c6bf0',
     2, False, 'Ophiuroidea'],
    ['Hercules_1341885_08:13:43', '5a0802e6-5010-4667-0f64-7898734fd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiuroidea', 'NA',
     'brittle stars | brittlestars', 'Class', 123084, 'urn:lsid:marinespecies.org:taxname:123084', 'Echinodermata',
     'Ophiuroidea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1840', 'NA', 'Ophiuroidea', 'NA', 'NA',
     'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260715, -172.7583542, 2991.719, 'reported', 2991.719, 2991.719, 'NA', '2021-11-20', '08:13:43', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5742, 34.6533, 2.3545, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'b860c165-078e-4715-8bc3-491039679b67',
     2, False, 'Ophiuroidea'],
    ['Hercules_1341885_08:14:57', 'd4d9e963-57ce-411c-e869-fd5a744fd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Nematocarcinus sp.', 'NA', 'NA',
     'Genus', 107015, 'urn:lsid:marinespecies.org:taxname:107015', 'Arthropoda', 'Malacostraca', 'Eumalacostraca',
     'Decapoda', 'Pleocyemata', 'Nematocarcinidae', 'NA', 'Nematocarcinus', 'NA', 'NA', 'NA', 'A. Milne-Edwards, 1881',
     'NA', 'Nematocarcinus sp.', 'NA', 'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1,
     'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260865, -172.758366, 2991.558, 'reported', 2991.558, 2991.558, 'NA', '2021-11-20', '08:14:57', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5757, 34.6537, 2.3608, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA',  'NA', -1, False,
     'Nematocarcinus sp'],
    ['Hercules_1341885_08:22:13', 'a4365962-4930-41f1-db6d-1627cdf4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Brisingidae', 'NA', 'NA',
     'Family', 123119, 'urn:lsid:marinespecies.org:taxname:123119', 'Echinodermata', 'Asteroidea', 'Ambuloasteroidea',
     'Brisingida', 'NA', 'Brisingidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'G.O. Sars, 1875', 'NA', 'Brisingidae', 'NA',
     'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260955, -172.7584015, 2990.962, 'reported', 2990.962, 2990.962, 'NA', '2021-11-20', '08:22:13', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5829, 34.6536, 2.3548, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1885/cam1_20211120082213.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Brisingidae'],
    ['Hercules_1341885_08:32:51', '0ccceb1e-4fc7-4ec8-2e63-7127cdf4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Demospongiae', 'NA',
     'demosponges | horny sponges', 'Class', 164811, 'urn:lsid:marinespecies.org:taxname:164811', 'Porifera',
     'Demospongiae', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Sollas, 1885', 'NA', 'Demospongiae', 'NA',
     'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.52627407, -172.7585815, 2996.531, 'reported', 2996.531, 2996.531, 'NA', '2021-11-20', '08:32:51', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5941, 34.6484, 2.3612, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1885/cam1_20211120083251.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA',  1, False, 'Demospongiae']
]

sample_report_records_collapsed = [
    ['Hercules_1341885_08:13:43', '5a0802e6-5010-4667-0f64-7898734fd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiuroidea', 'NA',
     'brittle stars | brittlestars', 'Class', 123084, 'urn:lsid:marinespecies.org:taxname:123084', 'Echinodermata',
     'Ophiuroidea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1840', 'NA', 'Ophiuroidea', 'NA', 'NA',
     'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260715, -172.7583542, 2991.719, 'reported', 2991.719, 2991.719, 'NA', '2021-11-20', '08:13:43', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5742, 34.6533, 2.3545, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA',
     'b44c0798-73e5-49c3-a42c-7470a06c6bf0 | b860c165-078e-4715-8bc3-491039679b67', 2, False, 'Ophiuroidea'],
    ['Hercules_1341885_08:14:57', 'd4d9e963-57ce-411c-e869-fd5a744fd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Nematocarcinus sp.', 'NA', 'NA',
     'Genus', 107015, 'urn:lsid:marinespecies.org:taxname:107015', 'Arthropoda', 'Malacostraca', 'Eumalacostraca',
     'Decapoda', 'Pleocyemata', 'Nematocarcinidae', 'NA', 'Nematocarcinus', 'NA', 'NA', 'NA', 'A. Milne-Edwards, 1881',
     'NA', 'Nematocarcinus sp.', 'NA', 'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1,
     'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260865, -172.758366, 2991.558, 'reported', 2991.558, 2991.558, 'NA', '2021-11-20', '08:14:57', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5757, 34.6537, 2.3608, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False,
     'Nematocarcinus sp'],
    ['Hercules_1341885_08:22:13', 'a4365962-4930-41f1-db6d-1627cdf4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Brisingidae', 'NA', 'NA',
     'Family', 123119, 'urn:lsid:marinespecies.org:taxname:123119', 'Echinodermata', 'Asteroidea', 'Ambuloasteroidea',
     'Brisingida', 'NA', 'Brisingidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'G.O. Sars, 1875', 'NA', 'Brisingidae', 'NA',
     'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.5260955, -172.7584015, 2990.962, 'reported', 2990.962, 2990.962, 'NA', '2021-11-20', '08:22:13', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5829, 34.6536, 2.3548, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1885/cam1_20211120082213.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Brisingidae'],
    ['Hercules_1341885_08:32:51', '0ccceb1e-4fc7-4ec8-2e63-7127cdf4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Demospongiae', 'NA',
     'demosponges | horny sponges', 'Class', 164811, 'urn:lsid:marinespecies.org:taxname:164811', 'Porifera',
     'Demospongiae', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Sollas, 1885', 'NA', 'Demospongiae', 'NA',
     'NA', 'Putts, Meagan', '2022-12-05', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Ha_aheo Seamount | North Ridge',
     24.52627407, -172.7585815, 2996.531, 'reported', 2996.531, 2996.531, 'NA', '2021-11-20', '08:32:51', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1885', 'NA134-H1885', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt bedrock with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust; basalt boulder with manganese crust',
     'basalt bedrock with manganese crust', 'ridge seamount, ridge', 1.5941, 34.6484, 2.3612, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1885/cam1_20211120083251.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', 1, False, 'Demospongiae']
]

sample_concepts = {
    "Amphipoda": {},
    "Narella sp": {},
    "Ophiacanthidae": {},
    "Scleralcyonacea": {}
}

sample_records_for_associates = [
    ['Hercules_1341883_03:56:46', '4aac8d66-bbb7-478d-1f69-9ab7571cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Amphipoda', 'NA',
     'amphipods | beach hoppers | sand hoppers | scuds and relatives', 'Order', 1135,
     'urn:lsid:marinespecies.org:taxname:1135', 'Arthropoda', 'Malacostraca', 'Eumalacostraca', 'Amphipoda', 'NA', 'NA',
     'NA', 'NA', 'NA', 'NA', 'NA', 'Latreille, 1816', 'NA', 'Amphipoda', 'NA', 'NA', 'Putts, Meagan', '2022-12-01',
     'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.11069176, -171.5785041, 2703.834, 'reported', 2703.834, 2703.834, 'NA', '2021-11-19', '03:56:46', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'in water column', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'NA', 'conical seamount, ridge', 1.6275, 34.646, 2.2336, 'video observation', 'NA', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Amphipoda'],
    ['Hercules_1341884_04:01:47', '95b32fce-afd5-4f62-1a62-fcadc6f4d61e | NA134-001-01-C-GSO', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'NA', 'NA', 'NA', 'NA', -999,
     'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA',
     'Putts, Meagan', '2022-12-01', 'NA', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.11070311, -171.5785055, 2703.538, 'reported', 2703.538, 2703.538, 'NA', '2021-11-19', '04:01:47', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', -999, 'NA', -999, -999, 'NA', -999, -999,
     -999, 'NA', 'NA', 'Geology Sample - subangular cobble | sampled by manipulator', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Amphipoda', 'conical seamount, ridge', 1.6378, 34.6435, 2.2273, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119040147.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True, 'none'],
    ['Hercules_1341884_04:01:47', '974406ba-5336-4ceb-4361-26ca178fd91e | NA134-001-02-B-MCZ', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiuroidea', 'NA',
     'brittle stars | brittlestars', 'Class', 123084, 'urn:lsid:marinespecies.org:taxname:123084', 'Echinodermata',
     'Ophiuroidea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1840', 'NA', 'Ophiuroidea', 'NA', 'NA',
     'Putts, Meagan', '2023-01-20', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.11070311, -171.5785055, 2703.538, 'reported', 2703.538, 2703.538, 'NA', '2021-11-19', '04:01:47', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'sampled by manipulator', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Scleralcyonacea', 'conical seamount, ridge', 1.6378, 34.6435, 2.2273, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True, 'Ophiuroidea'],
    ['Hercules_1341884_04:05:40', '86caacc8-ce50-4e6c-d065-f17d9d1cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106945, -171.578504, 2702.89, 'reported', 2702.89, 2702.89, 'NA', '2021-11-19', '04:05:40', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt cobble with manganese crust', 'conical seamount, ridge', 1.641, 34.6535, 2.2319, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:06:00', 'abae04f3-0ad2-4480-0864-f9f69d1cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106885, -171.5784775, 2701.973, 'reported', 2701.973, 2701.973, 'NA', '2021-11-19', '04:06:00', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6967, 34.621, 2.2294, 'video observation', 'NA',
     'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True, 'Narella sp'],
    ['Hercules_1341884_04:07:31', '15efb9ce-d457-4f42-ff61-48049f1cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106675, -171.5784415, 2700.553, 'reported', 2700.553, 2700.553, 'NA', '2021-11-19', '04:07:31', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.635, 34.6452, 2.2324, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:07:31', 'd1212ee9-e22e-4f96-a760-946e9f1cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiacanthidae', 'NA', 'NA',
     'Family', 123204, 'urn:lsid:marinespecies.org:taxname:123204', 'Echinodermata', 'Ophiuroidea', 'Myophiuroida',
     'Ophiacanthida', 'Ophiacanthina', 'Ophiacanthidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Ljungman, 1867', 'NA',
     'Ophiacanthidae', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106675, -171.5784415, 2700.553, 'reported', 2700.553, 2700.553, 'NA', '2021-11-19', '04:07:31', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.635, 34.6452, 2.2324, 'video observation', 'NA', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Ophiacanthidae'],
    ['Hercules_1341884_04:08:09', 'f79d0381-c071-43cb-4f6b-6235a11cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110681, -171.578427, 2698.208, 'reported', 2698.208, 2698.208, 'NA', '2021-11-19', '04:08:09', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6695, 34.6474, 2.2316, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:08:15', '121d3699-783e-43c6-b760-b771a11cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Keratoisididae', 'NA', 'NA',
     'Family', 1544106, 'urn:lsid:marinespecies.org:taxname:1544106', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Keratoisididae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1870', 'unbranched',
     'Keratoisididae unbranched', 'Keratoisidinae unbranched | Isididae unbranched', 'NA', 'Putts, Meagan',
     '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110683, -171.5784185, 2699.244, 'reported', 2699.244, 2699.244, 'NA', '2021-11-19', '04:08:15', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6385, 34.6427, 2.2274, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Keratoisididae unbranched'],
    ['Hercules_1341884_04:08:20', 'fb0b899e-414c-4da1-ef61-1ce9a21cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Keratoisididae', 'NA', 'NA',
     'Family', 1544106, 'urn:lsid:marinespecies.org:taxname:1544106', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Keratoisididae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gray, 1870', 'unbranched',
     'Keratoisididae unbranched', 'Keratoisidinae unbranched | Isididae unbranched', 'NA', 'Putts, Meagan',
     '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.11065302, -171.5783953, 2696.336, 'reported', 2696.336, 2696.336, 'NA', '2021-11-19', '04:08:20', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt cobble with manganese crust', 'conical seamount, ridge', 1.6417, 34.6504, 2.2229, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False,
     'Keratoisididae unbranched'],
    ['Hercules_1341884_04:08:21', '821bc3a5-6139-466a-ed6e-42aec6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Alternatipathes cf. alternata',
     'NA', 'NA', 'Genus', 994317, 'urn:lsid:marinespecies.org:taxname:994317', 'Cnidaria', 'Anthozoa', 'Hexacorallia',
     'Antipatharia', 'NA', 'Schizopathidae', 'NA', 'Alternatipathes', 'NA', 'cf. alternata', 'NA',
     'Molodtsova & Opresko, 2017', 'NA', 'Alternatipathes cf. alternata', 'Bathypathes alternata ss cf', 'NA',
     'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110647, -171.578395, 2696.535, 'reported', 2696.535, 2696.535, 'NA', '2021-11-19', '04:08:21', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '10-30 cm', '10',
     '30', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6395, 34.6442, 2.2244, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041030.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Alternatipathes alternata cf'],
    ['Hercules_1341884_04:11:30', '6236622e-9ea9-41ff-4c6d-fe69c11cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Scleralcyonacea', 'NA', 'NA',
     'Order', 1609355, 'urn:lsid:marinespecies.org:taxname:1609355', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'McFadden, van Ofwegen & Quattrini, 2022', 'NA',
     'Scleralcyonacea', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110647, -171.5783833, 2695.662, 'reported', 2695.662, 2695.662, 'NA', '2021-11-19', '04:11:30', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6236, 34.6522, 2.2264, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Calcaxonia'],
    ['Hercules_1341884_04:12:56', 'c35ce176-70b2-43c7-1361-f81ec31cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Liparidae', 'NA', 'snailfishes',
     'Family', 234519, 'urn:lsid:marinespecies.org:taxname:234519', 'Chordata', 'Teleostei', 'NA', 'Perciformes',
     'Cottoidei', 'Liparidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Gill, 1861', 'NA', 'Liparidae', 'NA', 'NA',
     'Putts, Meagan', '2022-12-01', 'ID by expert from video | ID Uncertain', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106485, -171.5783262, 2691.73, 'reported', 2691.73, 2691.73, 'NA', '2021-11-19', '04:12:56', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'NA', 'conical seamount, ridge', 1.6215, 34.6458, 2.2368, 'video observation', 'NA', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Liparidae'],
    ['Hercules_1341884_04:14:01', '822f0c69-2cab-4efb-816b-660dd01cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiacanthidae', 'NA', 'NA',
     'Family', 123204, 'urn:lsid:marinespecies.org:taxname:123204', 'Echinodermata', 'Ophiuroidea', 'Myophiuroida',
     'Ophiacanthida', 'Ophiacanthina', 'Ophiacanthidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Ljungman, 1867', 'NA',
     'Ophiacanthidae', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106425, -171.578307, 2691.393, 'reported', 2691.393, 2691.393, 'NA', '2021-11-19', '04:14:01', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6258, 34.6468, 2.2439, 'video observation', 'NA', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Ophiacanthidae'],
    ['Hercules_1341884_04:14:01', '9eed2ec4-132f-469a-b064-87aec6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1106425, -171.578307, 2691.393, 'reported', 2691.393, 2691.393, 'NA', '2021-11-19', '04:14:01', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '10-30 cm', '10',
     '30', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6258, 34.6468, 2.2439, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041401.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:14:51', 'dbe6b4af-2fed-494b-6466-37c2c91cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Scleralcyonacea', 'NA', 'NA',
     'Order', 1609355, 'urn:lsid:marinespecies.org:taxname:1609355', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'McFadden, van Ofwegen & Quattrini, 2022', 'NA',
     'Scleralcyonacea', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110627, -171.578292, 2690.14, 'reported', 2690.14, 2690.14, 'NA', '2021-11-19', '04:14:51', 'NA134', 'Nautilus',
     'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, 'NA', -999, -999,
     -999, 'Live', 'NA', 'NA', '50m', 'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6335, 34.6452, 2.2415, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Calcaxonia'],
    ['Hercules_1341884_04:16:49', '2bc989bd-a1a1-40d1-ea6e-b08bd11cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110565, -171.5782816, 2689.041, 'reported', 2689.041, 2689.041, 'NA', '2021-11-19', '04:16:49', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '10-30 cm', '10',
     '30', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp.', 'conical seamount, ridge', 1.6516, 34.6459, 2.2364, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:16:54', '62dafadd-7cee-4c79-126b-5673d21cd71e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Alternatipathes cf. alternata',
     'NA', 'NA', 'Genus', 994317, 'urn:lsid:marinespecies.org:taxname:994317', 'Cnidaria', 'Anthozoa', 'Hexacorallia',
     'Antipatharia', 'NA', 'Schizopathidae', 'NA', 'Alternatipathes', 'NA', 'cf. alternata', 'NA',
     'Molodtsova & Opresko, 2017', 'NA', 'Alternatipathes cf. alternata', 'Bathypathes alternata ss cf', 'NA',
     'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian', 'USA',
     'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1105625, -171.5782855, 2688.22, 'reported', 2688.22, 2688.22, 'NA', '2021-11-19', '04:16:54', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '10-30 cm', '10',
     '30', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6399, 34.6444, 2.2349, 'video observation',
     'NA', 'NA', 'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False,
     'Alternatipathes alternata cf'],
    ['Hercules_1341884_04:17:34', 'b5b94690-8500-474b-336e-c1aec6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Narella sp.', 'NA', 'NA',
     'Genus', 125319, 'urn:lsid:marinespecies.org:taxname:125319', 'Cnidaria', 'Anthozoa', 'Octocorallia',
     'Scleralcyonacea', 'NA', 'Primnoidae', 'NA', 'Narella', 'NA', 'NA', 'NA', 'Gray, 1870', 'NA', 'Narella sp.', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1105475, -171.578265, 2688.352, 'reported', 2688.352, 2688.352, 'NA', '2021-11-19', '04:17:34', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, '10-30 cm', '10',
     '30', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'basalt boulder with manganese crust', 'conical seamount, ridge', 1.6695, 34.643, 2.2284, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041734.png',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041734.png',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, False, 'Narella sp'],
    ['Hercules_1341884_04:17:36', '9f44c993-fb45-474a-1663-32afc6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiacanthidae', 'NA', 'NA',
     'Family', 123204, 'urn:lsid:marinespecies.org:taxname:123204', 'Echinodermata', 'Ophiuroidea', 'Myophiuroida',
     'Ophiacanthida', 'Ophiacanthina', 'Ophiacanthidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Ljungman, 1867', 'NA',
     'Ophiacanthidae', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1105445, -171.578265, 2688.404, 'reported', 2688.404, 2688.404, 'NA', '2021-11-19', '04:17:36', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6704, 34.6368, 2.2281, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041736.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Ophiacanthidae'],
    ['Hercules_1341884_04:18:02', 'a7788cbd-07d4-4235-d968-76afc6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Scalpellidae', 'NA', 'NA',
     'Family', 106055, 'urn:lsid:marinespecies.org:taxname:106055', 'Arthropoda', 'Thecostraca', 'Cirripedia',
     'Scalpellomorpha', 'NA', 'Scalpellidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Pilsbry, 1907', 'NA', 'Scalpellidae', 'NA',
     'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific', 'Insular Pacific-Hawaiian',
     'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.110543, -171.5782645, 2688.97, 'reported', 2688.97, 2688.97, 'NA', '2021-11-19', '04:18:02', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '1', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'My Special Concept', 'conical seamount, ridge', 1.6504, 34.6448, 2.2253, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041802.png',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041802.png',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Scalpellidae'],
    ['Hercules_1341884_04:18:36', '9f44c993-fb45-474a-1663-32afc6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiacanthidae', 'NA', 'NA',
     'Family', 123204, 'urn:lsid:marinespecies.org:taxname:123204', 'Echinodermata', 'Ophiuroidea', 'Myophiuroida',
     'Ophiacanthida', 'Ophiacanthina', 'Ophiacanthidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Ljungman, 1867', 'NA',
     'Ophiacanthidae', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1105445, -171.578265, 2688.404, 'reported', 2688.404, 2688.404, 'NA', '2021-11-19', '04:18:36', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6704, 34.6368, 2.2281, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041736.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Ophiacanthidae'],
    ['Hercules_1341884_04:25:36', '9f44c993-fb45-474a-1663-32afc6f4d61e', '',
     'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center', 'Ophiacanthidae', 'NA', 'NA',
     'Family', 123204, 'urn:lsid:marinespecies.org:taxname:123204', 'Echinodermata', 'Ophiuroidea', 'Myophiuroida',
     'Ophiacanthida', 'Ophiacanthina', 'Ophiacanthidae', 'NA', 'NA', 'NA', 'NA', 'NA', 'Ljungman, 1867', 'NA',
     'Ophiacanthidae', 'NA', 'NA', 'Putts, Meagan', '2022-12-01', 'ID by expert from video', 1, 'North Pacific',
     'Insular Pacific-Hawaiian', 'USA', 'Western Pacific',
     'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A',
     22.1105445, -171.578265, 2688.404, 'reported', 2688.404, 2688.404, 'NA', '2021-11-19', '04:25:36', 'NA134',
     'Nautilus', 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil', 'NA',
     'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
     'NA', 'NA134-H1884', 'NA134-H1884', 'ROV', 'Hercules', -999, 'NA', 'NA', '2', 'NA', -999, -999, '0-10 cm', '0',
     '10', -999, 'Live', 'NA',
     'size is estimated greatest length of individual in cm. Size estimations placed into size category bins', '50m',
     'USBL', 'CTD',
     'primarily: basalt boulder with manganese crust / secondary: sediment; basalt pebble with manganese crust; basalt cobble with manganese crust',
     'Narella sp', 'conical seamount, ridge', 1.6704, 34.6368, 2.2281, 'video observation',
     'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1884/cam1_20211119041736.png', 'NA',
     'Ocean Exploration Trust; University of Hawaiʻi', 'Bingo, Sarah; sarahr6@hawaii.edu', '2023-04-06',
     'https://nautiluslive.org/cruise/na134', '', 'Bingo, Sarah', 'sarahr6@hawaii.edu', 'NA', 'NA', -1, True,
     'Ophiacanthidae'],
]

taxon_tree = {
    "AphiaID": 1,
    "rank": "Superdomain",
    "scientificname": "Biota",
    "child": {
        "AphiaID": 2,
        "rank": "Kingdom",
        "scientificname": "Animalia",
        "child": {
            "AphiaID": 1267,
            "rank": "Phylum",
            "scientificname": "Cnidaria",
            "child": {
                "AphiaID": 1292,
                "rank": "Class",
                "scientificname": "Anthozoa",
                "child": {
                    "AphiaID": 1340,
                    "rank": "Subclass",
                    "scientificname": "Hexacorallia",
                    "child": {
                        "AphiaID": 1360,
                        "rank": "Order",
                        "scientificname": "Actiniaria",
                        "child": {
                            "AphiaID": 888371,
                            "rank": "Suborder",
                            "scientificname": "Enthemonae",
                            "child": {
                                "AphiaID": 853973,
                                "rank": "Superfamily",
                                "scientificname": "Actinioidea",
                                "child": {
                                    "AphiaID": 100653,
                                    "rank": "Family",
                                    "scientificname": "Actiniidae",
                                    "child": {
                                        "AphiaID": 100698,
                                        "rank": "Genus",
                                        "scientificname": "Bolocera",
                                        "child": None
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

flattened_tree = {
    'Superdomain': 'Biota',
    'Kingdom': 'Animalia',
    'Phylum': 'Cnidaria',
    'Class': 'Anthozoa',
    'Subclass': 'Hexacorallia',
    'Order': 'Actiniaria',
    'Suborder': 'Enthemonae',
    'Superfamily': 'Actinioidea',
    'Family': 'Actiniidae',
    'Genus': 'Bolocera'
}

aphia_record = {
    "AphiaID": 140621,
    "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=140621",
    "scientificname": "Illex coindetii",
    "authority": "(Vérany, 1839)",
    "status": "accepted",
    "unacceptreason": None,
    "taxonRankID": 220,
    "rank": "Species",
    "valid_AphiaID": 140621,
    "valid_name": "Illex coindetii",
    "valid_authority": "(Vérany, 1839)",
    "parentNameUsageID": 138278,
    "kingdom": "Animalia",
    "phylum": "Mollusca",
    "class": "Cephalopoda",
    "order": "Oegopsida",
    "family": "Ommastrephidae",
    "genus": "Illex",
    "citation": "MolluscaBase eds. (2023). MolluscaBase. Illex coindetii (Vérany, 1839). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=140621 on 2023-03-31",
    "lsid": "urn:lsid:marinespecies.org:taxname:140621",
    "isMarine": 1,
    "isBrackish": None,
    "isFreshwater": 0,
    "isTerrestrial": 0,
    "isExtinct": None,
    "match_type": "like",
    "modified": "2016-06-11T23:30:29.807Z"
}

dive_dict = {
    'DIVENUMBER': 'Hercules 1341884',
    'Date': '11/19/21',
    'Expedition': '134',
    'Leg': 'NA',
    'Dive': '1884',
    'Site': 'Unnamed seamount A',
    'Ocean': 'North Pacific',
    'LargeMarineEcosystem': 'Insular Pacific-Hawaiian',
    'Country': 'USA',
    'FishCouncilRegion': 'Western Pacific',
    'Locality': 'Papah_naumoku_kea Marine National Monument (PMNM), Northwestern Hawaiian Islands, Unnamed Seamount A',
    'SurveyID': 'NA134',
    'Station': 'NA134-H1884',
    'PI': 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil',
    'PIAffiliation': 'NA',
    'Purpose': 'Document whether these underwater mountains support vibrant coral and sponge communities like others in the region',
    'CruiseComments': 'NA',
    'EventID': 'NA134-H1884',
    'SamplingEquipment': 'ROV',
    'VehicleName': 'Hercules',
    'DataProvider': 'Ocean Exploration Trust; University of Hawaiʻi',
    'DataContact': 'Bingo, Sarah; sarahr6@hawaii.edu',
    'Vessel': 'Nautilus',
    'LocationAccuracy': '50',
    'WebSite': 'https://nautiluslive.org/cruise/na134',
    'Citation': 'NA'
}

concepts = {
    "Paralepididae": {
        "scientific_name": "Paralepididae",
        "aphia_id": 125447,
        "authorship": "Bonaparte, 1835",
        "synonyms": [],
        "taxon_rank": "Family",
        "taxon_ranks": {
            'Superdomain': 'Biota',
            'Kingdom': 'Animalia',
            'Phylum': 'Chordata',
            'Subphylum': 'Vertebrata',
            'Infraphylum': 'Gnathostomata',
            'Parvphylum': 'Osteichthyes',
            'Gigaclass': 'Actinopterygii',
            'Superclass': 'Actinopteri',
            'Class': 'Teleostei',
            'Order': 'Aulopiformes',
            'Family': 'Paralepididae'
        },
        "descriptors": [],
        "vernacular_name": "barracudinas"
    },
    "Demospongiae encrusting": {
        "scientific_name": "Demospongiae",
        "aphia_id": 164811,
        "authorship": "Sollas, 1885",
        "synonyms": ["hehe", "test"],
        "taxon_rank": "Class",
        "taxon_ranks": {
            "Superdomain": "Biota",
            "Kingdom": "Animalia",
            "Phylum": "Porifera",
            "Class": "Demospongiae"},
        "descriptors": ["encrusting"],
        "vernacular_name": "demosponges | horny sponges"
    }
}

# json responses for request tests

vars_concept_base_url = 'http://hurlstor.soest.hawaii.edu:8083/v1/concept/'

vars_responses = {
    "Pennatulacea": {
        "name": "Pennatuloidea",
        "alternateNames": [
            "Pennatulacea",
            "pennatulacean",
            "sea-pen"
        ],
        "rank": "superfamily",
        "media": [],
        "descriptors": [],
        "author": "verrill, 1865"
    },
    "Demospongiae": {
        "name": "Demospongiae",
        "alternateNames": [],
        "rank": "class",
        "media": [],
        "descriptors": [],
        "author": "unknown"
    },
    "Actinopterygii": {
        "name": "Actinopterygii",
        "alternateNames": [
            "Actinopteri",
            "fish"
        ],
        "rank": "class",
        "media": [],
        "descriptors": [],
        "author": "unknown"
    },
    "Demospongiae phylogeny": {
        "name": "object",
        "alternativeNames": [
            "root"
        ],
        "children": [
            {
                "name": "physical-object",
                "alternativeNames": [
                    "physical object"
                ],
                "children": [
                    {
                        "name": "Biological",
                        "children": [
                            {
                                "name": "Organism",
                                "children": [
                                    {
                                        "name": "Animalia",
                                        "rank": "kingdom",
                                        "children": [
                                            {
                                                "name": "Porifera",
                                                "alternativeNames": [
                                                    "sponge"
                                                ],
                                                "rank": "phylum",
                                                "children": [
                                                    {
                                                        "name": "Demospongiae",
                                                        "rank": "class"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "Ptilella phylogeny": {
        "name": "object",
        "alternativeNames": [
            "root"
        ],
        "children": [
            {
                "name": "physical-object",
                "alternativeNames": [
                    "physical object"
                ],
                "children": [
                    {
                        "name": "Biological",
                        "children": [
                            {
                                "name": "Organism",
                                "children": [
                                    {
                                        "name": "Animalia",
                                        "rank": "kingdom",
                                        "children": [
                                            {
                                                "name": "Cnidaria",
                                                "alternativeNames": [
                                                    "coelenterate",
                                                    "cnidarian"
                                                ],
                                                "rank": "phylum",
                                                "children": [
                                                    {
                                                        "name": "Anthozoa",
                                                        "alternativeNames": [
                                                            "coral"
                                                        ],
                                                        "rank": "class",
                                                        "children": [
                                                            {
                                                                "name": "Octocorallia",
                                                                "alternativeNames": [
                                                                    "Alcyonaria"
                                                                ],
                                                                "rank": "subclass",
                                                                "children": [
                                                                    {
                                                                        "name": "Scleralcyonacea",
                                                                        "rank": "order",
                                                                        "children": [
                                                                            {
                                                                                "name": "Pennatuloidea",
                                                                                "alternativeNames": [
                                                                                    "sea-pen",
                                                                                    "pennatulacean",
                                                                                    "Pennatulacea"
                                                                                ],
                                                                                "rank": "superfamily",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Subselliflorae",
                                                                                        "alternativeNames": [
                                                                                            "Subsessiliflorae"
                                                                                        ],
                                                                                        "rank": "suborder",
                                                                                        "children": [
                                                                                            {
                                                                                                "name": "Pennatulidae",
                                                                                                "rank": "family",
                                                                                                "children": [
                                                                                                    {
                                                                                                        "name": "Ptilella",
                                                                                                        "rank": "genus"
                                                                                                    }
                                                                                                ]
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "Pennatula phylogeny": {
        "name": "object",
        "alternativeNames": [
            "root"
        ],
        "children": [
            {
                "name": "physical-object",
                "alternativeNames": [
                    "physical object"
                ],
                "children": [
                    {
                        "name": "Biological",
                        "children": [
                            {
                                "name": "Organism",
                                "children": [
                                    {
                                        "name": "Animalia",
                                        "rank": "kingdom",
                                        "children": [
                                            {
                                                "name": "Cnidaria",
                                                "alternativeNames": [
                                                    "coelenterate",
                                                    "cnidarian"
                                                ],
                                                "rank": "phylum",
                                                "children": [
                                                    {
                                                        "name": "Anthozoa",
                                                        "alternativeNames": [
                                                            "coral"
                                                        ],
                                                        "rank": "class",
                                                        "children": [
                                                            {
                                                                "name": "Octocorallia",
                                                                "alternativeNames": [
                                                                    "Alcyonaria"
                                                                ],
                                                                "rank": "subclass",
                                                                "children": [
                                                                    {
                                                                        "name": "Scleralcyonacea",
                                                                        "rank": "order",
                                                                        "children": [
                                                                            {
                                                                                "name": "Pennatuloidea",
                                                                                "alternativeNames": [
                                                                                    "sea-pen",
                                                                                    "pennatulacean",
                                                                                    "Pennatulacea"
                                                                                ],
                                                                                "rank": "superfamily",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Subselliflorae",
                                                                                        "alternativeNames": [
                                                                                            "Subsessiliflorae"
                                                                                        ],
                                                                                        "rank": "suborder",
                                                                                        "children": [
                                                                                            {
                                                                                                "name": "Pennatulidae",
                                                                                                "rank": "family",
                                                                                                "children": [
                                                                                                    {
                                                                                                        "name": "Pennatula",
                                                                                                        "rank": "genus"
                                                                                                    }
                                                                                                ]
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "Stolonifera phylogeny": {
        "name": "object",
        "alternativeNames": [
            "root"
        ],
        "children": [
            {
                "name": "physical-object",
                "alternativeNames": [
                    "physical object"
                ],
                "children": [
                    {
                        "name": "Biological",
                        "children": [
                            {
                                "name": "Organism",
                                "children": [
                                    {
                                        "name": "Animalia",
                                        "rank": "kingdom",
                                        "children": [
                                            {
                                                "name": "Cnidaria",
                                                "alternativeNames": [
                                                    "coelenterate",
                                                    "cnidarian"
                                                ],
                                                "rank": "phylum",
                                                "children": [
                                                    {
                                                        "name": "Anthozoa",
                                                        "alternativeNames": [
                                                            "coral"
                                                        ],
                                                        "rank": "class",
                                                        "children": [
                                                            {
                                                                "name": "Octocorallia",
                                                                "alternativeNames": [
                                                                    "Alcyonaria"
                                                                ],
                                                                "rank": "subclass",
                                                                "children": [
                                                                    {
                                                                        "name": "Malacalcyonacea",
                                                                        "rank": "order",
                                                                        "children": [
                                                                            {
                                                                                "name": "Stolonifera",
                                                                                "rank": "suborder"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "Plexauridae yellow": {
        "name": "Paramuriceidae yellow",
        "alternateNames": [
            "Plexauridae yellow"
        ],
        "media": [],
        "descriptors": [],
        "author": ""
    }
}

worms_responses = {
    "Antipatharia": [
        {"AphiaID": 22549,
         "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=22549",
         "scientificname": "Antipatharia",
         "authority": None,
         "status": "accepted",
         "unacceptreason": None,
         "taxonRankID": 100,
         "rank": "Order",
         "valid_AphiaID": 22549,
         "valid_name": "Antipatharia",
         "valid_authority": None,
         "parentNameUsageID": 1340,
         "kingdom": "Animalia",
         "phylum": "Cnidaria",
         "class": "Anthozoa",
         "order": "Antipatharia",
         "family": None,
         "genus": None,
         "citation": "Molodtsova, T.; Opresko, D. (2023). World List of Antipatharia. Antipatharia. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=22549 on 2023-05-04",
         "lsid": "urn:lsid:marinespecies.org:taxname:22549",
         "isMarine": 1,
         "isBrackish": 1,
         "isFreshwater": None,
         "isTerrestrial": None,
         "isExtinct": None,
         "match_type": "exact",
         "modified": "2008-09-09T22:16:15.703Z"
         }
    ],
    "Demospongiae": [
        {
            "AphiaID": 164811,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=164811",
            "scientificname": "Demospongiae",
            "authority": "Sollas, 1885",
            "status": "accepted",
            "unacceptreason": None,
            "taxonRankID": 60,
            "rank": "Class",
            "valid_AphiaID": 164811,
            "valid_name": "Demospongiae",
            "valid_authority": "Sollas, 1885",
            "parentNameUsageID": 558,
            "kingdom": "Animalia",
            "phylum": "Porifera",
            "class": "Demospongiae",
            "order": None,
            "family": None,
            "genus": None,
            "citation": "WoRMS (2023). Demospongiae. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=164811 on 2023-05-04",
            "lsid": "urn:lsid:marinespecies.org:taxname:164811",
            "isMarine": 1,
            "isBrackish": 1,
            "isFreshwater": 1,
            "isTerrestrial": 0,
            "isExtinct": 0,
            "match_type": "exact",
            "modified": "2020-10-22T11:37:08.657Z"
        }
    ],
    "Stolonifera": [
        {
            "AphiaID": 153683,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=153683",
            "scientificname": "Stolonifera",
            "authority": None,
            "status": "accepted",
            "unacceptreason": None,
            "taxonRankID": 110,
            "rank": "Suborder",
            "valid_AphiaID": 153683,
            "valid_name": "Stolonifera",
            "valid_authority": None,
            "parentNameUsageID": 110723,
            "kingdom": "Animalia",
            "phylum": "Bryozoa",
            "class": "Gymnolaemata",
            "order": "Ctenostomatida",
            "family": None,
            "genus": None,
            "citation": "Bock, P. (2023). World List of Bryozoa. Stolonifera. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=153683 on 2023-05-04",
            "lsid": "urn:lsid:marinespecies.org:taxname:153683",
            "isMarine": 1,
            "isBrackish": None,
            "isFreshwater": None,
            "isTerrestrial": None,
            "isExtinct": None,
            "match_type": "exact",
            "modified": "2005-04-15T10:25:19.903Z"
        },
        {
            "AphiaID": 1368,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=1368",
            "scientificname": "Stolonifera",
            "authority": "Thomson & Simpson, 1909",
            "status": "unaccepted",
            "unacceptreason": None,
            "taxonRankID": 110,
            "rank": "Suborder",
            "valid_AphiaID": 1609357,
            "valid_name": "Malacalcyonacea",
            "valid_authority": "McFadden, van Ofwegen & Quattrini, 2022",
            "parentNameUsageID": 1609357,
            "kingdom": "Animalia",
            "phylum": "Cnidaria",
            "class": "Anthozoa",
            "order": "Malacalcyonacea",
            "family": None,
            "genus": None,
            "citation": "McFadden, C.S.; Cordeiro, R.; Williams, G.; van Ofwegen, L. (2023). World List of Octocorallia. Stolonifera. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1368 on 2023-05-04",
            "lsid": "urn:lsid:marinespecies.org:taxname:1368",
            "isMarine": 1,
            "isBrackish": 1,
            "isFreshwater": 0,
            "isTerrestrial": 0,
            "isExtinct": None,
            "match_type": "exact",
            "modified": "2022-11-06T20:41:46.647Z"
        }
    ],
    "Malacalcyonacea": [
        {
            "AphiaID": 1609357,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=1609357",
            "scientificname": "Malacalcyonacea",
            "authority": "McFadden, van Ofwegen & Quattrini, 2022",
            "status": "accepted",
            "unacceptreason": None,
            "taxonRankID": 100,
            "rank": "Order",
            "valid_AphiaID": 1609357,
            "valid_name": "Malacalcyonacea",
            "valid_authority": "McFadden, van Ofwegen & Quattrini, 2022",
            "parentNameUsageID": 1341,
            "kingdom": "Animalia",
            "phylum": "Cnidaria",
            "class": "Anthozoa",
            "order": "Malacalcyonacea",
            "family": None,
            "genus": None,
            "citation": "WoRMS (2023). Malacalcyonacea. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1609357 on 2023-05-04",
            "lsid": "urn:lsid:marinespecies.org:taxname:1609357",
            "isMarine": 1,
            "isBrackish": None,
            "isFreshwater": 0,
            "isTerrestrial": 0,
            "isExtinct": None,
            "match_type": "exact",
            "modified": "2022-11-02T02:55:04.660Z"
        }
    ],
    "Demospongiae phylogeny": {
        "AphiaID": 1,
        "rank": "Superdomain",
        "scientificname": "Biota",
        "child": {
            "AphiaID": 2,
            "rank": "Kingdom",
            "scientificname": "Animalia",
            "child": {
                "AphiaID": 558,
                "rank": "Phylum",
                "scientificname": "Porifera",
                "child": {
                    "AphiaID": 164811,
                    "rank": "Class",
                    "scientificname": "Demospongiae",
                    "child": None
                }
            }
        }
    },
    "Demospongiae vernaculars": [
        {
            "vernacular": "demosponges",
            "language_code": "eng",
            "language": "English"
        },
        {
            "vernacular": "gewone sponzen",
            "language_code": "dut",
            "language": "Dutch"
        },
        {
            "vernacular": "horn- och kiselsvampar",
            "language_code": "swe",
            "language": "Swedish"
        },
        {
            "vernacular": "horny sponges",
            "language_code": "eng",
            "language": "English"
        },
    ],
    "Ophidiiformes vernaculars": [
        {
            "vernacular": "naaldvisachtigen",
            "language_code": "dut",
            "language": "Dutch"
        }
    ],
    "Plexauridae": [
        {
            "AphiaID": 125277,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=125277",
            "scientificname": "Plexauridae",
            "authority": "Gray, 1859",
            "status": "accepted",
            "unacceptreason": None,
            "taxonRankID": 140,
            "rank": "Family",
            "valid_AphiaID": 125277,
            "valid_name": "Plexauridae",
            "valid_authority": "Gray, 1859",
            "parentNameUsageID": 1609357,
            "kingdom": "Animalia",
            "phylum": "Cnidaria",
            "class": "Anthozoa",
            "order": "Malacalcyonacea",
            "family": "Plexauridae",
            "genus": None,
            "citation": "McFadden, C.S.; Cordeiro, R.; Williams, G.; van Ofwegen, L. (2023). World List of Octocorallia. Plexauridae Gray, 1859. Accessed through: World Register of Marine Species at: https:\\/\\/www.marinespecies.org\\/aphia.php?p=taxdetails&id=125277 on 2023-05-05",
            "lsid": "urn:lsid:marinespecies.org:taxname:125277",
            "isMarine": 1,
            "isBrackish": None,
            "isFreshwater": 0,
            "isTerrestrial": 0,
            "isExtinct": None,
            "match_type": "exact",
            "modified": "2022-11-06T01:15:04.990Z"
        }
    ],
    "Paramuriceidae": [
        {
            "AphiaID": 151540,
            "url": "https://www.marinespecies.org/aphia.php?p=taxdetails&id=151540",
            "scientificname": "Paramuriceidae",
            "authority": "Bayer, 1956",
            "status": "accepted",
            "unacceptreason": None,
            "taxonRankID": 140,
            "rank": "Family",
            "valid_AphiaID": 151540,
            "valid_name": "Paramuriceidae",
            "valid_authority": "Bayer, 1956",
            "parentNameUsageID": 1609357,
            "kingdom": "Animalia",
            "phylum": "Cnidaria",
            "class": "Anthozoa",
            "order": "Malacalcyonacea",
            "family": "Paramuriceidae",
            "genus": None,
            "citation": "McFadden, C.S.; Cordeiro, R.; Williams, G.; van Ofwegen, L. (2023). World List of Octocorallia. Paramuriceidae Bayer, 1956. Accessed through: World Register of Marine Species at: https:\\/\\/www.marinespecies.org\\/aphia.php?p=taxdetails&id=151540 on 2023-05-05",
            "lsid": "urn:lsid:marinespecies.org:taxname:151540",
            "isMarine": 1,
            "isBrackish": None,
            "isFreshwater": 0,
            "isTerrestrial": 0,
            "isExtinct": None,
            "match_type": "exact",
            "modified": "2022-11-05T21:48:31.350Z"
        }
    ],
    "Paramuriceidae phylogeny": {
        "AphiaID": 1,
        "rank": "Superdomain",
        "scientificname": "Biota",
        "child": {
            "AphiaID": 2,
            "rank": "Kingdom",
            "scientificname": "Animalia",
            "child": {
                "AphiaID": 1267,
                "rank": "Phylum",
                "scientificname": "Cnidaria",
                "child": {
                    "AphiaID": 1292,
                    "rank": "Class",
                    "scientificname": "Anthozoa",
                    "child": {
                        "AphiaID": 1341,
                        "rank": "Subclass",
                        "scientificname": "Octocorallia",
                        "child": {
                            "AphiaID": 1609357,
                            "rank": "Order",
                            "scientificname": "Malacalcyonacea",
                            "child": {
                                "AphiaID": 151540,
                                "rank": "Family",
                                "scientificname": "Paramuriceidae",
                                "child": None
                            }
                        }
                    }
                }
            }
        }
    }
}
