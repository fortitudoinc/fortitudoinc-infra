Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|
    
    config.vm.box = "ubuntu/trusty64"
    
    config.ssh.insert_key = false
    
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
    end
end