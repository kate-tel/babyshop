## **babyshop.com End-to-end-testing**

### **Table of Contents**

* [About this Project](#about-this-project)
* [Test coverage](#test-coverage)
* [Prerequisites](#prerequisites)
* [Setup of testing environment](#setup-of-testing-environment)
* [Running the tests](#running-the-tests)
* [References](#references)

### **About this Project**

This test suite performs end-to-end functional testing for https://www.babyshop.com/.

### **Test coverage**

Functionality covered by this test suite:

* Website search;
* Menu navigation;
* Adding and manipulating items in cart;
* Changing region and language.

### **Prerequisites**

You should have the following installed:

* [Python 3](https://www.python.org/downloads/)
* [Chrome browser](https://www.google.com/chrome/)

### **Setup of testing environment**   

Please refer to [magento2.test project](https://github.com/kate-tel/magento2.test#setup-of-testing-environment) for instructions.

### **Running the tests**

1. To run the tests from the command line:

```bash
pytest test_babyshop.py
```

2. To select a specific test method to run, indicate class name and then method name:

```bash
pytest test_babyshop.py::BabyshopTestClass::test_menu
```
### **References**

1. For SeleniumBase CLI commands, log saving, configurations etc, please have a look at https://github.com/seleniumbase/SeleniumBase.

2. List of SeleniumBase methods:

https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/fixtures/base_case.py