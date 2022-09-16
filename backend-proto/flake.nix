{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";

    flake-utils.url = "github:numtide/flake-utils";
    flake-utils.inputs.nixpkgs.follows = "nixpkgs";

    # Current as of: Fri Sep 16 20:28:10 UTC 2022
    pypi-deps-db.url = "github:DavHau/pypi-deps-db/90b371109a9283cd8a5c11874a9a1a37e8e789f2";
    pypi-deps-db.flake = false;

    mach-nix.url = "mach-nix/3.5.0";
    mach-nix.inputs.nixpkgs.follows = "nixpkgs";
    mach-nix.inputs.flake-utils.follows = "flake-utils";
    mach-nix.inputs.pypi-deps-db.follows = "pypi-deps-db";
  };
  outputs = { self, nixpkgs, flake-utils, pypi-deps-db, mach-nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonEnv = mach-nix.lib."${system}".mkPython {
          requirements = builtins.readFile ../hackzurich22-backend/requirements.txt + ''
            # additional dependencies for local work
            ipython
          '';
        };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [ pythonEnv ];
        };
      });
}
