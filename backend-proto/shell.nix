{ pkgs ? import <nixpkgs> {} }:

let
  myPython = pkgs.python3.withPackages (p: with p; [
    flask
  ]);
in
  myPython.env
