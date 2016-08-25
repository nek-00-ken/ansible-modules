## check_network

### DOCUMENTATION

Refer to documentation in `check_network.py`  

Prerequisites :
 - vagrant
 - ansible

First, launch the VM:
 `vagrant up`

Then, create an ansible python development context:
`virtualenv venv; source venv/bin/activate; pip install ansible`


To test the module:  

`ansible server-1 -i inventory -M $(pwd) -m check_network -a "link=localhost:22" -vvvv`

To use the module in a playbook:  

`ansible-playbook -i inventory -M $(pwd) test.yml`
