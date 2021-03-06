{
  "targets": [
    {
      "target_name": "addon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "addon.cc",
        "timeseries.cpp",
        "timeseries.h",
        "SimpleAnomalyDetector.cpp",
        "SimpleAnomalyDetector.h",
        "HybridAnomalyDetector.cpp",
        "HybridAnomalyDetector.h",
        "minCircle.cpp",
        "minCircle.h",
        "AnomalyDetector.h",
        "anomaly_detection_util.cpp",
        "anomaly_detection_util.h"],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
