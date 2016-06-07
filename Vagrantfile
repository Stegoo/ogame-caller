# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network :private_network, ip: "192.168.50.27"

    #config.vm.network "forwarded_port", guest: 8002, host: 8002

    # Provider-specific configuration so you can fine-tune various
    # backing providers for Vagrant. These expose provider-specific options.
    #
    config.vm.provider "virtualbox" do |vb|
        # Allow symbolic link inside shared directory (used for moving node_modules)
        #vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/path/to/guest/shared/directory", "1"]
        #   # Customize the amount of memory on the VM:
        vb.memory = "2048"
    end

    config.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y git python3 python3-pip build-essential libxml2-dev libncurses5-dev libsqlite3-dev libssl-dev
        sudo pip3 install virtualenv
        mkdir /tmp/asterisk
        cd /tmp/asterisk
        wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-11-current.tar.gz
        tar -xvzf asterisk-11-current.tar.gz
    SHELL

end
