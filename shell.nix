let
  pkgs = import <nixpkgs> {};

in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      python-pkgs.requests
      python-pkgs.beautifulsoup4
      python-pkgs.certifi
      python-pkgs.charset-normalizer
      python-pkgs.idna
      python-pkgs.soupsieve
      python-pkgs.urllib3
      python-pkgs.cryptography
      python-pkgs.psutil
    ]))
  ];
}
