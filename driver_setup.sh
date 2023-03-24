#!/bin/bash

chvc=$(google-chrome --version)
chrome_version=$(echo $chvc | cut -d ' ' -f 3- | cut -d '.' -f 1-3)

pip3 install selenium


driver_file_url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version"

echo $chvc
echo $chrome_version
echo $driver_url

mkdir tmp-build
pushd tmp-build
    wget $driver_file_url
    filenm="LATEST_RELEASE_$chrome_version"
    vrsn=$(head -n 1 $filenm)
    driver_dl="https://chromedriver.storage.googleapis.com/$vrsn/chromedriver_linux64.zip"
    wget $driver_dl
    driver_pkg=$(basename $driver_dl)
    unzip $driver_pkg
    sudo cp chromedriver /usr/bin/chromedriver 
    sudo chown root:root /usr/bin/chromedriver 
    sudo chmod +x /usr/bin/chromedriver 

    sudo cp chromedriver /usr/local/bin/chromedriver 
    sudo chown root:root /usr/local/bin/chromedriver 
    sudo chmod +x /usr/local/bin/chromedriver 

    sudo cp chromedriver ../
    sudo chown root:root ../
    sudo chmod +x ../
popd

rm -rf tmp-build

export PATH=$PATH:/usr/local/bin/chromedriver

echo "Chromedriver successfully installed!"