# This nix config is not perfect and still under test
# To use it:
#   - Install nix with
#   - Configure pip as described there: https://github.com/Kpler/kp-deployment/blob/main/doc/source/installation.rst#kpler-python-package-index
#   - Use nix-shell to enter into a shell with all the requirements
#     or use direnv and echo 'use nix' >> .envrc to automatically
#     use nix-shell whenever you enter into the project
#
# Report issues on slack #tech-help-nixex
let
  nixpkgs = builtins.fetchTarball {
    name   = "nixos-24.11-20250513";
    url    = "https://github.com/NixOS/nixpkgs/archive/a39ed32a651f.tar.gz";
    sha256 = "16pw0f94nr3j91z0wm4ndjm44xfd238vcdkg07s2l74znkaavnwk";
  };
  pkgs = import nixpkgs { };

  systemDependencies = [
    pkgs.python312
  ];

in pkgs.mkShell {
  buildInputs = [
      pkgs.python312
      pkgs.openssl  # macOS default SSL libraries are binary incompatible
    ];

  shellHook = ''
    # nix should immediately halt when this setup hook fail
    set -eo pipefail

    KPLER_PROJECT_DIR="${builtins.toPath ./.}"

    # because nixpkgs may not always contain packages hosted on pypi,
    # we instead rely on a local virtualenv dir for python packages
    KPLER_VENV_DIR="$KPLER_PROJECT_DIR/.venv"
    python -m venv $KPLER_VENV_DIR
    PATH="$KPLER_VENV_DIR/bin:$PATH"
    # Add source root to python path
    export PYTHONPATH="$KPLER_PROJECT_DIR/src:$PYTHONPATH"

    # install project dependencies
    echo -e "\033[1;33m\n>>> UPDATING PYTHON DEPENDENCIES\033[0m"
    pip install --quiet --no-cache-dir --upgrade pip setuptools wheel
    pip install --no-cache-dir --upgrade --requirement $KPLER_PROJECT_DIR/requirements_test.txt

    # user input should never cause nix to exit
    set +eo pipefail
  '';
}
