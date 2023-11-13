{
    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = {nixpkgs, flake-utils, ... }: 
    flake-utils.lib.eachDefaultSystem (system:
    let
        pkgs = import nixpkgs {
            inherit system;
        };
        auto-all = pkgs.python3Packages.buildPythonPackage rec {
            pname = "auto-all";
            version = "1.4.1";
            src = pkgs.fetchPypi {
                inherit pname version;
                sha256 = "";
            };
            doCheck = false;
            propagatedBuildInputs = with pkgs.python3Packages; [
                # Specify dependencies
                numpy
            ];
        };

        abqpy = pkgs.python3Packages.buildPythonPackage rec {
            pname = "abqpy";
            version = "2023.6.1";
            src = pkgs.fetchPypi {
                inherit pname version;
                sha256 = "";
            };
            doCheck = false;
            propagatedBuildInputs = with pkgs.python3Packages; [
                # Specify dependencies
                numpy
                auto-all
                fire
                pydantic
                typeguard
                typing-extensions
            ];
        };
    in rec {
        devShell = (pkgs.buildFHSUserEnv {
          name = "py_env";
          targetPkgs = pkgs: (with pkgs; [
            (python310.withPackages(ps: with ps; [
                pip
                numpy
                abqpy
            ]))
          ]);
          runScript = "bash";
        }).env;
    });
}
