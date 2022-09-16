{ pkgs ? import <nixpkgs> {} }:

let
  myPython = pkgs.python3.withPackages (p: with p; [
    fastapi
  ]);
in
  myPython.env
