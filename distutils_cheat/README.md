# distutils

For each directory, do:

    # Fails because package not found, since the import
    # is on a different directory ("package").
    python test.py

    cd package
    python package/setup.py install --user

    # Works, using the installed version.
    cd ..
    python test.py

    # Cleanup
    # http://stackoverflow.com/questions/402359/how-do-you-uninstall-a-python-package-that-was-installed-using-distutils/43650802#43650802
    rm -rf files.txt
    sudo python setup.py install --record files.txt
    xargs sudo rm -rf < files.txt
    rm -rf files.txt

    # Fails again.
    python test.py

1. [min](min/)
1. [script](script/)
