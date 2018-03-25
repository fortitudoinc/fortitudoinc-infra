Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|
    
    config.vm.box = "ubuntu/trusty64"
    config.vm.define "openmrs-test-server"
    config.ssh.insert_key = false
    
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
        ansible.groups = {
            "openmrs-servers" => ["openmrs-test-server"]
        }
    end
end