Vagrant.configure("2") do |config|
    config.vm.define "db" do |db|
        db.vm.box = "ubuntu/trusty64"
        db.vm.hostname = "db"
        db.vm.network "private_network", ip: "192.168.50.11"
    end
    
    config.vm.define "web" do |web|
        web.vm.box = "ubuntu/xenial64"
        web.vm.hostname = "web"
        web.vm.network "private_network", ip: "192.168.50.10"
    end
    
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
        ansible.groups = {
            "openmrs-databases" => ["db"],
            "openmrs-servers" => ["web"],
            "openmrs-servers:vars" => {"ansible_python_interpreter" => "/usr/bin/python3"}
        }
    end
    
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end
end