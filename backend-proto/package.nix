{ callPackage, lib, python3Packages }:

let
  inherit (python3Packages) buildPythonPackage fetchPypi pytest;
in
rec {
  simple-websocket = buildPythonPackage rec {
    pname = "simple-websocket";
    version = "0.8.1";
    src = fetchPypi {
      inherit pname version;
      hash = "sha256-Cr6HT2oMbd0Zfb1PDOVwi0dhCg0U+isHYuUVZZVz1Eo=";
    };
    propagatedBuildInputs = [
      python3Packages.wsproto
    ];
  };

  flask-sock = buildPythonPackage rec {
    pname = "flask-sock";
    version = "0.5.2";
    src = fetchPypi {
      inherit pname version;
      hash = "sha256-w26SgT6JejJaSMruZAUJ+IxGW432QuQBJsGyX8OKLDA=";
    };
    propagatedBuildInputs = [
      python3Packages.flask
      simple-websocket
    ];
  };

  flask-cors = buildPythonPackage rec {
    pname = "Flask-Cors";
    version = "1.10.3";
    src = fetchPypi {
      inherit pname version;
      hash = "sha256-nmknqgpG8xS8oOxj64cc7omKFirf3VtlIk23oAgodCM=";
    };
    propagatedBuildInputs = [
      python3Packages.flask
      python3Packages.six
    ];
    doCheck = false;
  };
}
