{ pkgs ? import <nixpkgs> {} }:

let
  extraPythonDeps = pkgs.callPackage ./package.nix {};

  myPython = pkgs.python3.withPackages (p: with p; [
    flask
    extraPythonDeps.flask-cors
    extraPythonDeps.flask-sock
    httpx
    websockets
  ]);
in
  myPython.env
