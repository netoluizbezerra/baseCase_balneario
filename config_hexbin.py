config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "t1iqcrb",
          "type": "hexagon",
          "config": {
            "dataId": "Balneario",
            "label": "Point",
            "color": [
              237,
              200,
              0
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "worldUnitSize": 0.3,
              "resolution": 8,
              "colorRange": {
                "name": "ColorBrewer YlOrRd-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffb2",
                  "#fed976",
                  "#feb24c",
                  "#fd8d3c",
                  "#f03b20",
                  "#bd0026"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                694.03
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 14.4,
              "colorAggregation": "average",
              "sizeAggregation": "average",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": []
          },
          "visualChannels": {
            "colorField": {
              "name": "preco_m2",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "preco_m2",
              "type": "real"
            },
            "sizeScale": "linear"
          }
        },
        {
          "id": "0mrmks",
          "type": "geojson",
          "config": {
            "dataId": "Boundaries",
            "label": "Boundaries",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.41,
              "thickness": 1,
              "strokeColor": [
                233,
                246,
                250
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Balneario": [
              {
                "name": "preco_m2",
                "type": "real",
                "format": "",
                "analyzerType": "INT",
                "id": "preco_m2",
                "tableFieldIndex": 57
              },
              {
                "name": "area_util",
                "type": "real",
                "format": "",
                "analyzerType": "INT",
                "id": "area_tot",
                "tableFieldIndex": 0
              },
              {
                "name": "preco",
                "type": "real",
                "format": "",
                "analyzerType": "INT",
                "id": "price",
                "tableFieldIndex": 56
              }
            ],
            "Boundaries": [
              {
                "name": "cd_mun",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -131.0625,
      "dragRotate": True,
      "latitude": -27.03341424997123,
      "longitude": -48.65418016287164,
      "pitch": 51.63704530953441,
      "zoom": 11.123636152054342,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}