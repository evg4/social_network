# Social network database
## Description
This python project connects with a PostgreSQL database to allow users to create, read, update and delete posts/users. 

## How to use (mac)

### Requirements
- Python 3.10+
- PostgreSQL - ensure this is installed and running locally before creating the database

``` bash
# Clone the repo
git clone https://github.com/evg4/social_network.git

# Set up a venv and install the requirements
cd social_network
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create database
createdb social_network

# Run the app as is to see some example uses, or amend app.py to experiment. This file reseeds the database each time so changes are not saved. To change this, delete line 8.
python3 app.py

# To run the tests
pytest

```


## Areas for improvement
There is currently not full CRUD design for both data types, so this is the first thing I would add in the future.<br> I would also amend the model classes so that the id defaults to null; at the moment a user can enter any integer for id and this will be overwritten when added to the database, which I don't think is intuitive.

## Credits
Thanks to [Makers](https://github.com/makersacademy) for providing the starter code and guidance during the build.

## Licence
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
 