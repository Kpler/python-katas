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
    name   = "nixos-23.05-20230814";
    url    = "https://github.com/NixOS/nixpkgs/archive/720e61ed8de1.tar.gz";
    sha256 = "0ii10wmm8hqdp7bii7iza58rjaqs4z3ivv71qyix3qawwxx48hw9";
  };
  pkgs = import nixpkgs { };

  systemDependencies = [
    pkgs.python310
    pkgs.postgresql_12  # libpq is not available, see https://github.com/NixOS/nixpkgs/issues/61580
  ];

in pkgs.mkShell {
  buildInputs = [
      pkgs.python310
      pkgs.postgresql_12
      pkgs.openssl  # macOS default SSL libraries are binary incompatible
    ];

  shellHook = ''
    # nix should immediately halt when this setup hook fail
    set -eo pipefail

    KPLER_PROJECT_DIR="${builtins.toPath ./.}"

    # because nixpkgs may not always contain packages hosted on pypi,
    # we instead rely on a local virtualenv dir for python packages
    KPLER_VENV_DIR="$KPLER_PROJECT_DIR/.venv/py310"
    python -m venv $KPLER_VENV_DIR
    PATH="$KPLER_VENV_DIR/bin:$PATH"

    # install project dependencies
    echo -e "\033[1;33m\n>>> UPDATING PYTHON DEPENDENCIES\033[0m"
    pip install --quiet --no-cache-dir --upgrade pip setuptools wheel
    pip install --no-cache-dir --upgrade --requirement $KPLER_PROJECT_DIR/requirements_test.txt

    # user input should never cause nix to exit
    set +eo pipefail
  '';
}
