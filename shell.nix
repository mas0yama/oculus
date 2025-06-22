{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {

  

    nativeBuildInputs = with pkgs.buildPackages; [ 

      python312
      git
      qt5.full];

packages = [
  (pkgs.python312.withPackages(p: with p; [
  numpy
  matplotlib
  networkx
  pyvis
  splinter
  ]))];


      env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc.lib
        pkgs.glib
        pkgs.glibc
        pkgs.gmime
      pkgs.libz
      pkgs.libglvnd
    ];

}
