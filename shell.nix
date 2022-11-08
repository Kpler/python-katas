# This nix config is not perfect and still under test
# To use it:
#   - Install nix with
#   - Configure pip as described there: https://github.com/Kpler/kp-deployment/blob/main/doc/source/installation.rst#kpler-python-package-index
#   - Use nix-shell to enter into a shell with all the requirements
#     or use direnv and echo 'use nix' >> .envrc to automatically
#     use nix-shell whenever you enter into the project
#
# Report issues on slack #tech-help-nix
let
  nixpkgs = builtins.fetchTarball {
    name   = "nixos-22.05-20221108";
    url    = "https://github.com/NixOS/nixpkgs/archive/987a9764e3b6.tar.gz";
    sha256 = "0bdnzkz5ka3bnjp33hb6zv9jcn44wylskdaqdrhjgc9znsbqqgjw";
  };
  pkgs = import nixpkgs { };

  python = pkgs.python310;

  poetry = pkgs.poetry.override {
    python = python;
  };

  poetryEnv = pkgs.poetry2nix.mkPoetryEnv {
    python = python;
    projectDir = ./.;
    preferWheels = true;
  };

in pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    poetry
    poetryEnv
    pkgs.pre-commit
  ];
}
