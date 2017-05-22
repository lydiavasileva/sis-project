# sis-project
The SIS (Simple Inventory System) project is a small scale inventory system for an item storage room, with a "library" style management (leasing out items to others).
### Motivation
This project was created and is being worked on by [Lidia Vasileva](https://github.com/lydiavasileva).
This project is being made as part of my job as a Student Helper at Lillebælt Academy, University of Applied Science and their IT Inventory, during my studies within the specialty of IT Technology with a focus on Networks.

This system is being created for Lillebælt Academy, University of Applied Science and their IT Inventory. This inventory includes only hardware pieces - Raspberry Pies, Monitors, Cables, etc.

This project was created due to a lack of known software solutions to be used in such a simple inventory.
Important reason is also the experience which a project like this could provide an IT student, including working with Databases, Coding languages, Security of Data and more.

## Aditional Documentation

[Project Plan](https://github.com/lydiavasileva/sis-project/blob/master/documentation/project-plan.md)

## Use Cases

![UseCaseDiagram](https://github.com/lydiavasileva/sis-project/blob/master/documentation/images/use-case-sis.png)

## Getting Started

TBA.

### Prerequisites

Required modules:

* `tinidb`

This is included in the `required.txt` which could be used to initialize the virtualenvironment

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r required.txt`

When done use `deactive` to leave the virtual environment.

### Installing

TBA.

## Running the tests

To run tests we use *nosetests*

Ensure that *nosetests* are installed, by either `apt-get install python-nosetests` or `pip install nosetests`

Run `nosetests` to run tests.

They are located in the subdirectory `tests`.


### Break down into end to end tests

TBA.

### And coding style tests

TBA.

## Deployment

TBA.

## Built With

* **Data Base** - [TinyDB](https://github.com/msiemens/tinydb)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning


## Authors

* **Lidia Vasileva** - *Initial work* - [lydiavasileva](https://github.com/lydiavasileva)

See also the list of [contributors](https://github.com/lydiavasileva/sis-project/blob/master/documentation/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

TBA.
