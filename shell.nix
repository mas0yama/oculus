{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {

    nativeBuildInputs = with pkgs.buildPackages; [

      python312
      git
      chromedriver
      pkgs.google-chrome

    (pkgs.writeShellScriptBin "google-chrome" "exec -a $0 ${pkgs.google-chrome}/bin/google-chrome-stable $@")
    ];
packages = [
  (pkgs.python312.withPackages(p: with p; [
    numpy
    pandas
    scipy
    splinter
    selenium
    beautifulsoup4
    aiohttp
    termcolor
    requests
  ]))];  



  env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc.lib
        pkgs.glib
        pkgs.glibc
        pkgs.gmime
      pkgs.libz
      pkgs.libglvnd
  
    ];


shellHook = ''
    SOURCE_DATE_EPOCH=$(date +%s)
    VENV=.venv

    if test ! -d $VENV; then
      python3.12 -m venv $VENV
    fi
    source ./$VENV/bin/activate
    export PYTHONPATH=`pwd`/$VENV/${pkgs.python312.sitePackages}/:$PYTHONPATH
  '';

  postShellHook = ''
    ln -sf ${pkgs.python312.sitePackages}/* ./.venv/lib/python3.12/site-packages
  '';
}
