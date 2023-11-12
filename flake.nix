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
    in rec {
        devShell = (pkgs.buildFHSUserEnv {
          name = "pipzone";
          targetPkgs = pkgs: (with pkgs; [
            (python39.withPackages(ps: with ps; [
                pip
                numpy
            ]))
          ]);
          profile = ''
            export TEST="test"
          '';
          runScript = "bash";
        }).env;
    });
}
