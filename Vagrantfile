# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.network "private_network", type: "dhcp"

  config.vm.define "web" do |web|
    web.vm.hostname = "webapp"
    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.

    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://vagrantcloud.com/search.
    # config.vm.box = "hashicorp/precise64"
    web.vm.box = "ubuntu/trusty64"

    # Disable automatic box update checking. If you disable this, then
    # boxes will only be checked for updates when the user runs
    # `vagrant box outdated`. This is not recommended.
    # config.vm.box_check_update = false

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8080" will access port 80 on the guest machine.
    # NOTE: This will enable public access to the opened port
    # config.vm.network "forwarded_port", guest: 80, host: 8080

    web.vm.network "forwarded_port", guest: 5000, host: 5000

    # (49000..49900).each do |port|
    #   config.vm.network :forwarded_port, :host => port, :guest => port
    # end

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine and only allow access
    # via 127.0.0.1 to disable public access
    # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    # config.vm.network "private_network", ip: "192.168.33.10"

    # Create a public network, which generally matched to bridged network.
    # Bridged networks make the machine appear as another physical device on
    # your network.
    # config.vm.network "public_network"

    # Share an additional folder to the guest VM. The first argument is
    # the path on the host to the actual folder. The second argument is
    # the path on the guest to mount the folder. And the optional third
    # argument is a set of non-required options.
    # config.vm.synced_folder ".", "/vagrant_app"

    # Provider-specific configuration so you can fine-tune various
    # backing providers for Vagrant. These expose provider-specific options.
    # Example for VirtualBox:
    #
    # config.vm.provider "virtualbox" do |vb|
    #   # Display the VirtualBox GUI when booting the machine
    #   vb.gui = true
    # 
    #   # Customize the amount of memory on the VM:
    #   # vb.memory = "1024"
    # end

    # View the documentation for the provider you are using for more
    # information on available options.

    # Enable provisioning with a shell script. Additional provisioners such as
    # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
    # documentation for more information about their specific syntax and use.
    # config.vm.provision "shell", inline: <<-SHELL
    #   apt-get update
    #   apt-get install -y apache2
    # SHELL

    web.vm.provision "shell", inline: <<-SHELL
      apt-get update 2> /dev/null
      apt-get install -y python-pip 2> /dev/null

      # remove any previously installed docker and install newest
      apt-get remove docker docker-engine docker.io 2> /dev/null
      apt-get install -y apt-transport-https ca-certificates curl software-properties-common 2> /dev/null
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get update
      apt-get install -y docker-ce
      pip install docker-compose 2> /dev/null
      cd /vagrant/web
      docker-compose up --build -d
    SHELL
  end
  config.vm.define "locust_master" do |master|
    master.vm.box = "ubuntu/trusty64"
    master.vm.hostname = "locust-master"
    master.vm.provision "shell", inline: <<-SHELL
      apt-get update 2> /dev/null
      apt-get install -y python-pip 2> /dev/null

      # remove any previously installed docker and install newest
      apt-get remove docker docker-engine docker.io 2> /dev/null
      apt-get install -y apt-transport-https ca-certificates curl software-properties-common 2> /dev/null
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get update
      apt-get install -y docker-ce
      pip install docker-compose 2> /dev/null
    SHELL
  end
  config.vm.define "locust_slave" do |slave|
    slave.vm.box = "ubuntu/trusty64"
    slave.vm.hostname = "locust-slave"
    slave.vm.provision "shell", inline: <<-SHELL
      apt-get update 2> /dev/null
      apt-get install -y python-pip 2> /dev/null

      # remove any previously installed docker and install newest
      apt-get remove docker docker-engine docker.io 2> /dev/null
      apt-get install -y apt-transport-https ca-certificates curl software-properties-common 2> /dev/null
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get update
      apt-get install -y docker-ce
      pip install docker-compose 2> /dev/null
    SHELL
  end
end
